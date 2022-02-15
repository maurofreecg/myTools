#######################################################################
#
#
#                            UTILITIES
#
#
#######################################################################

import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm
from maya import cmds, OpenMaya
import controls
import hierarchyJntTempletes
import importlib
importlib.reload(controls)
myCtrl = controls.myControls()
importlib.reload(hierarchyJntTempletes)
myHJntTemp = hierarchyJntTempletes.myHierarchyJntTempletes()

#################################################### color ##############################################################################
def itemColor(s, c):  # yellow 17, red 13, blue 6, light blue 18
    mc.setAttr(s + '.overrideEnabled', 1)
    mc.setAttr(s + '.overrideColor', c)

#######################################################################
#
#
#                           Matrix Constraints
#
#
#######################################################################

################################################ translate / rotate / scale - Matrix Constraint #######################################
def tranRotScl_const():
    selO = mc.ls(sl=True)
    for i in (selO):
        masterGrp = mc.group(n= i + '_ctrlSpaceMaster', em=True)
        grp = mc.group(n= i + '_ctrlSpace', em=True)
        crv = mc.circle( n= i + '_ctrl', ch=False, radius = 3, nr=(1, 0, 0))
        mc.parent(crv, grp), mc.parent(grp, masterGrp)
        mc.delete(mc.parentConstraint(i, masterGrp, mo=False))
        mc.connectAttr(('%s.rx'%crv[0]), ('%s.rx'%i))
        mc.connectAttr(('%s.ry'%crv[0]), ('%s.ry'%i))
        mc.connectAttr(('%s.rz'%crv[0]), ('%s.rz'%i))
        mc.connectAttr(('%s.sx'%crv[0]), ('%s.sx'%i))
        mc.connectAttr(('%s.sy'%crv[0]), ('%s.sy'%i))
        mc.connectAttr(('%s.sz'%crv[0]), ('%s.sz'%i))
        multM = mc.createNode('multMatrix', n= i + '_MM')
        decM = mc.createNode('decomposeMatrix', n= i + '_DM')
        mc.connectAttr(multM + '.matrixSum', decM + '.inputMatrix')
        mc.connectAttr(('%s.worldMatrix[0]'%crv[0]), ('%s.matrixIn[0]'%multM), f=True)
        mc.connectAttr(str(i) + '.parentInverseMatrix[0]', multM + '.matrixIn[1]', f=True)
        mc.connectAttr(decM + '.outputTranslate', i + '.t')

################################################ Point Matrix constraint ##############################################################

#######################################################################
#
#
#                          FK System
#
#
#######################################################################

################################################# neck head fk transform ###################################################################
def neck_FK_transform(*args):
    neckHead_jnt_list = ['neck', 'head']

    for neckHead in (neckHead_jnt_list):
        mc.makeIdentity(neckHead, apply=True, t=True, r=True, s=True)
        mc.select(d=True)

    mc.select(neckHead_jnt_list)
    tranRotScl_const()
    itemColor('neck_ctrl', 17)
    mc.parent('head_ctrlSpaceMaster', 'neck_ctrl')
    neckCtrl = mc.group(n= 'neck_controls', em=True)
    mc.parent('neck_ctrlSpaceMaster', neckCtrl)

    ### neck twist
    neckTwist = mc.joint('neck', n= 'neck_twist', rad=2)
    mc.delete(mc.pointConstraint('neck', 'head', neckTwist, mo=False))
    neck_PB = mc.createNode('pairBlend', n= 'neck_twist_PB')
    mc.setAttr(neck_PB + '.weight', 0.5)
    mc.connectAttr('head_ctrl.rotateX', neck_PB + '.inRotateX2')
    mc.connectAttr(neck_PB + '.outRotateX', neckTwist + '.rx')

    mc.select(d=True)
    print('neckHead_FK_completed')

################################################## spine FK transform ################################################################
def spine_FK_transfomr(*args):
    spine_jnt_list = ['pelvis', 'spine_01', 'spine_02', 'spine_03']

    for spine_jnt in (spine_jnt_list):
        mc.makeIdentity(spine_jnt, apply=True, t=True, r=True, s=True)
        mc.select(d=True)

    mc.select(spine_jnt_list)
    tranRotScl_const()
    mc.parent('spine_03_ctrlSpaceMaster', 'spine_02_ctrl'), mc.parent('spine_02_ctrlSpaceMaster', 'spine_01_ctrl')
    mc.parent('spine_01_ctrlSpaceMaster', 'pelvis_ctrl')
    itemColor('pelvis_ctrl', 17)
    spineCtrlGrp = mc.group(n = 'spine_controls', em=True)
    mc.parent('pelvis_ctrlSpaceMaster', spineCtrlGrp)

    mc.select(d=True)
    print('spine_FK_completed')

################################################# arm finger FK transform ######################################################
def arm_fingers_FK_transform(*args):

    arm_fingers_l_jnt_list = ['clavicle_l', 'upperarm_l', 'lowerarm_l', 'hand_l', 'pinky_00_l', 'pinky_01_l', 'pinky_02_l', 'pinky_03_l',
                              'ring_00_l', 'ring_01_l', 'ring_02_l', 'ring_03_l', 'middle_00_l', 'middle_01_l', 'middle_02_l', 'middle_03_l',
                              'index_00_l', 'index_01_l', 'index_02_l', 'index_03_l', 'thumb_01_l', 'thumb_02_l', 'thumb_03_l']

    for arm_fingers_jnt in (arm_fingers_l_jnt_list):
         mc.makeIdentity(arm_fingers_jnt, apply=True, t=True, r=True, s=True)
         mc.select(d=True)

    ### twist arm
    upperarmTwist_01_l = mc.joint('upperarm_l', n='upperarm_twist_fk_01_l', rad=2)
    upperarmTConst_01_l = mc.pointConstraint('upperarm_l', 'lowerarm_l', upperarmTwist_01_l ,mo=False), mc.setAttr('upperarm_twist_fk_01_l_pointConstraint1.upperarm_lW0', 2)
    upperarmTwist_02_l = mc.joint('upperarm_l', n='upperarm_twist_fk_02_l', rad=2)
    upperarmTConst_02_l = mc.pointConstraint('upperarm_l', 'lowerarm_l', upperarmTwist_02_l ,mo=False), mc.setAttr('upperarm_twist_fk_02_l_pointConstraint1.lowerarm_lW1', 2)
    mc.delete('upperarm_twist_fk_01_l_pointConstraint1', 'upperarm_twist_fk_02_l_pointConstraint1')

    lowerarmTwist_01_l = mc.joint('lowerarm_l', n='lowerarm_twist_fk_01_l', rad=2)
    lowerarmTConst_01_l = mc.pointConstraint('lowerarm_l', 'hand_l', lowerarmTwist_01_l ,mo=False), mc.setAttr('lowerarm_twist_fk_01_l_pointConstraint1.lowerarm_lW0', 1.5)
    lowerarmTwist_02_l = mc.joint('lowerarm_l', n='lowerarm_twist_fk_02_l', rad=2)
    lowerarmTConst_02_l = mc.pointConstraint('lowerarm_l', 'hand_l', lowerarmTwist_02_l ,mo=False), mc.setAttr('lowerarm_twist_fk_02_l_pointConstraint1.hand_lW1', 3)
    mc.delete('lowerarm_twist_fk_01_l_pointConstraint1', 'lowerarm_twist_fk_02_l_pointConstraint1')
    mc.select(d=True)

    mc.mirrorJoint('clavicle_l', mirrorYZ=True, mirrorBehavior=True, searchReplace=('_l', '_r')), mc.select(d=True)

    arm_fingers_r_jnt_list = ['clavicle_r', 'upperarm_r', 'lowerarm_r', 'hand_r', 'pinky_00_r', 'pinky_01_r', 'pinky_02_r', 'pinky_03_r',
                              'ring_00_r', 'ring_01_r', 'ring_02_r', 'ring_03_r', 'middle_00_r', 'middle_01_r', 'middle_02_r', 'middle_03_r',
                              'index_00_r', 'index_01_r', 'index_02_r', 'index_03_r', 'thumb_01_r', 'thumb_02_r', 'thumb_03_r']

    mc.select(arm_fingers_l_jnt_list, arm_fingers_r_jnt_list)
    tranRotScl_const()

    ### controls
    arm_fingers_l_ctrl_list = ['clavicle_l_ctrl', 'upperarm_l_ctrl', 'lowerarm_l_ctrl', 'hand_l_ctrl', 'pinky_00_l_ctrl', 'pinky_01_l_ctrl', 'pinky_02_l_ctrl', 'pinky_03_l_ctrl',
                                'ring_00_l_ctrl', 'ring_01_l_ctrl', 'ring_02_l_ctrl', 'ring_03_l_ctrl', 'middle_00_l_ctrl', 'middle_01_l_ctrl', 'middle_02_l_ctrl', 'middle_03_l_ctrl',
                                'index_00_l_ctrl', 'index_01_l_ctrl', 'index_02_l_ctrl', 'index_03_l_ctrl', 'thumb_01_l_ctrl', 'thumb_02_l_ctrl', 'thumb_03_l_ctrl']

    arm_fingers_r_ctrl_list = ['clavicle_r_ctrl', 'upperarm_r_ctrl', 'lowerarm_r_ctrl', 'hand_r_ctrl', 'pinky_00_r_ctrl', 'pinky_01_r_ctrl', 'pinky_02_r_ctrl', 'pinky_03_r_ctrl',
                               'ring_00_r_ctrl', 'ring_01_r_ctrl', 'ring_02_r_ctrl', 'ring_03_r_ctrl', 'middle_00_r_ctrl', 'middle_01_r_ctrl', 'middle_02_r_ctrl', 'middle_03_r_ctrl',
                               'index_00_r_ctrl', 'index_01_r_ctrl', 'index_02_r_ctrl', 'index_03_r_ctrl', 'thumb_01_r_ctrl', 'thumb_02_r_ctrl', 'thumb_03_r_ctrl']

    for armF_l in arm_fingers_l_ctrl_list:
        itemColor(armF_l, 6)

    for armF_r in arm_fingers_r_ctrl_list:
        itemColor(armF_r, 13)

    ### parent controls
    mc.parent('upperarm_l_ctrlSpaceMaster', 'clavicle_l_ctrl'), mc.parent('lowerarm_l_ctrlSpaceMaster', 'upperarm_l_ctrl'), mc.parent('hand_l_ctrlSpaceMaster', 'lowerarm_l_ctrl')
    mc.parent('pinky_03_l_ctrlSpaceMaster', 'pinky_02_l_ctrl'), mc.parent('pinky_02_l_ctrlSpaceMaster', 'pinky_01_l_ctrl'), mc.parent('pinky_01_l_ctrlSpaceMaster', 'pinky_00_l_ctrl')
    mc.parent('ring_03_l_ctrlSpaceMaster', 'ring_02_l_ctrl'), mc.parent('ring_02_l_ctrlSpaceMaster', 'ring_01_l_ctrl'), mc.parent('ring_01_l_ctrlSpaceMaster', 'ring_00_l_ctrl')
    mc.parent('middle_03_l_ctrlSpaceMaster', 'middle_02_l_ctrl'), mc.parent('middle_02_l_ctrlSpaceMaster', 'middle_01_l_ctrl'), mc.parent('middle_01_l_ctrlSpaceMaster', 'middle_00_l_ctrl')
    mc.parent('index_03_l_ctrlSpaceMaster', 'index_02_l_ctrl'), mc.parent('index_02_l_ctrlSpaceMaster', 'index_01_l_ctrl'), mc.parent('index_01_l_ctrlSpaceMaster', 'index_00_l_ctrl')
    mc.parent('thumb_03_l_ctrlSpaceMaster', 'thumb_02_l_ctrl'), mc.parent('thumb_02_l_ctrlSpaceMaster', 'thumb_01_l_ctrl')
    mc.parent('pinky_00_l_ctrlSpaceMaster', 'ring_00_l_ctrlSpaceMaster', 'middle_00_l_ctrlSpaceMaster', 'index_00_l_ctrlSpaceMaster', 'thumb_01_l_ctrlSpaceMaster', 'hand_l_ctrl')

    mc.parent('upperarm_r_ctrlSpaceMaster', 'clavicle_r_ctrl'), mc.parent('lowerarm_r_ctrlSpaceMaster', 'upperarm_r_ctrl'), mc.parent('hand_r_ctrlSpaceMaster', 'lowerarm_r_ctrl')
    mc.parent('pinky_03_r_ctrlSpaceMaster', 'pinky_02_r_ctrl'), mc.parent('pinky_02_r_ctrlSpaceMaster', 'pinky_01_r_ctrl'), mc.parent('pinky_01_r_ctrlSpaceMaster', 'pinky_00_r_ctrl')
    mc.parent('ring_03_r_ctrlSpaceMaster', 'ring_02_r_ctrl'), mc.parent('ring_02_r_ctrlSpaceMaster', 'ring_01_r_ctrl'), mc.parent('ring_01_r_ctrlSpaceMaster', 'ring_00_r_ctrl')
    mc.parent('middle_03_r_ctrlSpaceMaster', 'middle_02_r_ctrl'), mc.parent('middle_02_r_ctrlSpaceMaster', 'middle_01_r_ctrl'), mc.parent('middle_01_r_ctrlSpaceMaster', 'middle_00_r_ctrl')
    mc.parent('index_03_r_ctrlSpaceMaster', 'index_02_r_ctrl'), mc.parent('index_02_r_ctrlSpaceMaster', 'index_01_r_ctrl'), mc.parent('index_01_r_ctrlSpaceMaster', 'index_00_r_ctrl')
    mc.parent('thumb_03_r_ctrlSpaceMaster', 'thumb_02_r_ctrl'), mc.parent('thumb_02_r_ctrlSpaceMaster', 'thumb_01_r_ctrl')
    mc.parent('pinky_00_r_ctrlSpaceMaster', 'ring_00_r_ctrlSpaceMaster', 'middle_00_r_ctrlSpaceMaster', 'index_00_r_ctrlSpaceMaster', 'thumb_01_r_ctrlSpaceMaster', 'hand_r_ctrl')

    armsGrp = mc.group(n = 'arms_ctrls', em=True)
    mc.parent('clavicle_r_ctrlSpaceMaster', 'clavicle_l_ctrlSpaceMaster', armsGrp), mc.select(d=True)

    ######################## twist l_transform
    upperarmTwist_l_jnt_list = ['upperarm_twist_fk_01_l', 'upperarm_twist_fk_02_l', 'lowerarm_twist_fk_01_l', 'lowerarm_twist_fk_02_l']
    mc.select(upperarmTwist_l_jnt_list)
    tranRotScl_const()

    upperarmTwist_l_ctrl_list = ['upperarm_twist_01_l_ctrl', 'upperarm_twist_02_l_ctrl', 'lowerarm_twist_01_l_ctrl', 'lowerarm_twist_02_l_ctrl']
    upperarmTwist_l_masterGrp_list = ['upperarm_twist_fk_01_l_ctrlSpaceMaster', 'upperarm_twist_fk_02_l_ctrlSpaceMaster']
    lowerarmTwist_l_masterGrp_list = ['lowerarm_twist_fk_01_l_ctrlSpaceMaster', 'lowerarm_twist_fk_02_l_ctrlSpaceMaster']
    mc.parent(upperarmTwist_l_masterGrp_list, 'upperarm_l_ctrl'), mc.parent(lowerarmTwist_l_masterGrp_list, 'lowerarm_l_ctrl')
    mc.select(d=True)

    mc.disconnectAttr('upperarm_l_ctrl.rx', 'upperarm_l.rx')
    mc.disconnectAttr('upperarm_twist_fk_01_l_ctrl.rx', 'upperarm_twist_fk_01_l.rx')
    mc.disconnectAttr('upperarm_twist_fk_02_l_ctrl.rx', 'upperarm_twist_fk_02_l.rx')
    mc.disconnectAttr('lowerarm_twist_fk_01_l_ctrl.rx', 'lowerarm_twist_fk_01_l.rx')
    mc.disconnectAttr('lowerarm_twist_fk_02_l_ctrl.rx', 'lowerarm_twist_fk_02_l.rx')

    #### armTwist PB connection
    mc.select(upperarmTwist_l_jnt_list)

    upperarmT_l_01_PB = mc.createNode('pairBlend', n= 'upperarm_twist_fk_01_l_PB')
    mc.setAttr(upperarmT_l_01_PB + '.weight', 0.2)
    mc.connectAttr('upperarm_l_ctrl.rx', upperarmT_l_01_PB + '.inRotateX2')
    mc.connectAttr(upperarmT_l_01_PB + '.outRotateX', 'upperarm_twist_fk_01_l.rx', f=True)

    upperarmT_l_02_PB = mc.createNode('pairBlend', n= 'upperarm_twist_fk_02_l_PB')
    mc.setAttr(upperarmT_l_02_PB + '.weight', 0.8)
    mc.connectAttr('upperarm_l_ctrl.rx', upperarmT_l_02_PB + '.inRotateX2')
    mc.connectAttr(upperarmT_l_02_PB + '.outRotateX', 'upperarm_twist_fk_02_l.rx', f=True)

    lowerarmT_l_01_PB = mc.createNode('pairBlend', n= 'lowerarm_twist_fk_01_l_PB')
    mc.setAttr(lowerarmT_l_01_PB + '.weight', 0.4)
    mc.connectAttr('hand_l_ctrl.rx', lowerarmT_l_01_PB + '.inRotateX2')
    mc.connectAttr(lowerarmT_l_01_PB + '.outRotateX', 'lowerarm_twist_fk_01_l.rx', f=True)

    lowerarmT_l_02_PB = mc.createNode('pairBlend', n= 'lowerarm_twist_02_fk_l_PB')
    mc.setAttr(lowerarmT_l_02_PB + '.weight', 0.8)
    mc.connectAttr('hand_l_ctrl.rx', lowerarmT_l_02_PB + '.inRotateX2')
    mc.connectAttr(lowerarmT_l_02_PB + '.outRotateX', 'lowerarm_twist_fk_02_l.rx', f=True)

    ######################## twist r_transform
    upperarmTwist_fk_r_jnt_list = ['upperarm_twist_fk_01_r', 'upperarm_twist_fk_02_r', 'lowerarm_twist_fk_01_r', 'lowerarm_twist_fk_02_r']
    mc.select(upperarmTwist_fk_r_jnt_list)
    tranRotScl_const()

    upperarmTwist_fk_r_ctrl_list = ['upperarm_twist_fk_01_r_ctrl', 'upperarm_twist_fk_02_r', 'lowerarm_twist_fk_01_r', 'lowerarm_twist_fk_02_r']
    upperarmTwist_fk_r_masterGrp_list = ['upperarm_twist_fk_01_r_ctrlSpaceMaster', 'upperarm_twist_fk_02_r_ctrlSpaceMaster']
    lowerarmTwist_fk_r_masterGrp_list = ['lowerarm_twist_fk_01_r_ctrlSpaceMaster', 'lowerarm_twist_fk_02_r_ctrlSpaceMaster']
    mc.parent(upperarmTwist_fk_r_masterGrp_list, 'upperarm_r_ctrl'), mc.parent(lowerarmTwist_fk_r_masterGrp_list, 'lowerarm_r_ctrl')
    mc.select(d=True)

    mc.disconnectAttr('upperarm_r_ctrl.rx', 'upperarm_r.rx')
    mc.disconnectAttr('upperarm_twist_fk_01_r_ctrl.rx', 'upperarm_twist_fk_01_r.rx')
    mc.disconnectAttr('upperarm_twist_fk_02_r_ctrl.rx', 'upperarm_twist_fk_02_r.rx')
    mc.disconnectAttr('lowerarm_twist_fk_01_r_ctrl.rx', 'lowerarm_twist_fk_01_r.rx')
    mc.disconnectAttr('lowerarm_twist_fk_02_r_ctrl.rx', 'lowerarm_twist_fk_02_r.rx')

    #### armTwist PB connection
    mc.select(upperarmTwist_fk_r_jnt_list)

    upperarmT_r_01_PB = mc.createNode('pairBlend', n= 'upperarm_twist_fk_01_r_PB')
    mc.setAttr(upperarmT_r_01_PB + '.weight', 0.2)
    mc.connectAttr('upperarm_r_ctrl.rx', upperarmT_r_01_PB + '.inRotateX2')
    mc.connectAttr(upperarmT_r_01_PB + '.outRotateX', 'upperarm_twist_fk_01_r.rx', f=True)

    upperarmT_r_02_PB = mc.createNode('pairBlend', n= 'upperarm_twist_fk_02_r_PB')
    mc.setAttr(upperarmT_r_02_PB + '.weight', 0.8)
    mc.connectAttr('upperarm_r_ctrl.rx', upperarmT_r_02_PB + '.inRotateX2')
    mc.connectAttr(upperarmT_r_02_PB + '.outRotateX', 'upperarm_twist_fk_02_r.rx', f=True)

    lowerarmT_r_01_PB = mc.createNode('pairBlend', n= 'lowerarm_twist_fk_01_r_PB')
    mc.setAttr(lowerarmT_r_01_PB + '.weight', 0.4)
    mc.connectAttr('hand_r_ctrl.rx', lowerarmT_r_01_PB + '.inRotateX2')
    mc.connectAttr(lowerarmT_r_01_PB + '.outRotateX', 'lowerarm_twist_fk_01_r.rx', f=True)

    lowerarmT_r_02_PB = mc.createNode('pairBlend', n= 'lowerarm_twist_fk_02_r_PB')
    mc.setAttr(lowerarmT_r_02_PB + '.weight', 0.8)
    mc.connectAttr('hand_r_ctrl.rx', lowerarmT_r_02_PB + '.inRotateX2')
    mc.connectAttr(lowerarmT_r_02_PB + '.outRotateX', 'lowerarm_twist_fk_02_r.rx', f=True)

    mc.select(d=True)
    print('armFinger_FK_completed')

##################################################### leg FK transform ##############################################################
def leg_FK_Transform(*args):

    leg_l_jnt_list = ['thigh_l', 'calf_l', 'foot_l', 'ball_l', 'toe_l']

    for leg_l_jnt in (leg_l_jnt_list):
        mc.makeIdentity(leg_l_jnt, apply=True, t=True, r=True, s=True)
        mc.select(d=True)

    ### twist leg
    thighTwist_01_l = mc.joint('thigh_l', n='thigh_twist_fk_01_l', rad=2)
    thighTConst_01_l = mc.pointConstraint('thigh_l', 'calf_l', thighTwist_01_l ,mo=False), mc.setAttr('thigh_twist_fk_01_l_pointConstraint1.thigh_lW0', 2)
    thighTwist_02_l = mc.joint('thigh_l', n='thigh_twist_fk_02_l', rad=2)
    thighTConst_02_l = mc.pointConstraint('thigh_l', 'calf_l', thighTwist_02_l ,mo=False), mc.setAttr('thigh_twist_fk_02_l_pointConstraint1.calf_lW1', 2)
    mc.delete('thigh_twist_fk_01_l_pointConstraint1', 'thigh_twist_fk_02_l_pointConstraint1')

    calfTwist_01_l = mc.joint('calf_l', n='calf_twist_fk_01_l', rad=2)
    calfTConst_01_l = mc.pointConstraint('calf_l', 'foot_l', calfTwist_01_l ,mo=False), mc.setAttr('calf_twist_fk_01_l_pointConstraint1.calf_lW0', 2)
    calfTwist_02_l = mc.joint('calf_l', n='calf_twist_fk_02_l', rad=2)
    calfTConst_02_l = mc.pointConstraint('calf_l', 'foot_l', calfTwist_02_l ,mo=False), mc.setAttr('calf_twist_fk_02_l_pointConstraint1.foot_lW1', 2)
    mc.delete('calf_twist_fk_01_l_pointConstraint1', 'calf_twist_fk_02_l_pointConstraint1')
    mc.select(d=True)

    mc.mirrorJoint('thigh_l', mirrorYZ=True, mirrorBehavior=True, searchReplace=('_l', '_r')), mc.select(d=True)

    leg_r_jnt_list = ['thigh_r', 'calf_r', 'foot_r', 'ball_r', 'toe_r']

    mc.select(leg_r_jnt_list, leg_l_jnt_list)
    tranRotScl_const()

    ##### controls
    leg_l_ctrl_list = ['thigh_l_ctrl', 'calf_l_ctrl', 'foot_l_ctrl', 'ball_l_ctrl', 'toe_l_ctrl']
    leg_r_ctrl_list = ['thigh_r_ctrl', 'calf_r_ctrl', 'foot_r_ctrl', 'ball_r_ctrl', 'toe_r_ctrl']

    for leg_l_color in leg_l_ctrl_list:
        itemColor(leg_l_color, 6)

    for leg_r_color in leg_r_ctrl_list:
        itemColor(leg_r_color, 13)

    mc.parent('toe_l_ctrlSpaceMaster', 'ball_l_ctrl'), mc.parent('ball_l_ctrlSpaceMaster', 'foot_l_ctrl'), mc.parent('foot_l_ctrlSpaceMaster', 'calf_l_ctrl'), mc.parent('calf_l_ctrlSpaceMaster', 'thigh_l_ctrl')
    mc.parent('toe_r_ctrlSpaceMaster', 'ball_r_ctrl'), mc.parent('ball_r_ctrlSpaceMaster', 'foot_r_ctrl'), mc.parent('foot_r_ctrlSpaceMaster', 'calf_r_ctrl'), mc.parent('calf_r_ctrlSpaceMaster', 'thigh_r_ctrl')
    legGrp = mc.group(n= 'leg_controls', em=True)
    mc.parent('thigh_r_ctrlSpaceMaster', 'thigh_l_ctrlSpaceMaster', legGrp), mc.select(d=True)

    ######################## twist l_transform
    legTwist_l_jnt_list = ['thigh_twist_fk_01_l', 'thigh_twist_fk_02_l', 'calf_twist_fk_01_l', 'calf_twist_fk_02_l']
    mc.select(legTwist_l_jnt_list)
    tranRotScl_const()

    thighTwist_l_ctrl_list = ['thigh_twist_fk_01_l_ctrl', 'thigh_twist_fk_02_l_ctrl', 'calf_twist_fk_01_l_ctrl', 'calf_twist_fk_02_l_ctrl']
    thighTwist_l_masterGrp_list = ['thigh_twist_fk_01_l_ctrlSpaceMaster', 'thigh_twist_fk_02_l_ctrlSpaceMaster']
    calfTwist_l_masterGrp_list = ['calf_twist_fk_01_l_ctrlSpaceMaster', 'calf_twist_fk_02_l_ctrlSpaceMaster']
    mc.parent(thighTwist_l_masterGrp_list, 'thigh_l_ctrl'), mc.parent(calfTwist_l_masterGrp_list, 'calf_l_ctrl')
    mc.select(d=True)

    mc.disconnectAttr('thigh_l_ctrl.rx', 'thigh_l.rx')
    mc.disconnectAttr('thigh_twist_fk_01_l_ctrl.rx', 'thigh_twist_fk_01_l.rx')
    mc.disconnectAttr('thigh_twist_fk_02_l_ctrl.rx', 'thigh_twist_fk_02_l.rx')
    mc.disconnectAttr('calf_twist_fk_01_l_ctrl.rx', 'calf_twist_fk_01_l.rx')
    mc.disconnectAttr('calf_twist_fk_02_l_ctrl.rx', 'calf_twist_fk_02_l.rx')

    ####### legTwist PB transform

    mc.select(legTwist_l_jnt_list)
    thighT_l_01_PB = mc.createNode('pairBlend', n='thigh_twist_fk_01_l_PB')
    mc.setAttr(thighT_l_01_PB + '.weight', 0.4)
    mc.connectAttr('thigh_l_ctrl.rx', thighT_l_01_PB + '.inRotateX2')
    mc.connectAttr(thighT_l_01_PB + '.outRotateX', 'thigh_twist_fk_01_l.rx', f=True)

    thighT_l_02_PB = mc.createNode('pairBlend', n='thigh_twist_fk_02_l_PB')
    mc.setAttr(thighT_l_02_PB + '.weight', 0.8)
    mc.connectAttr('thigh_l_ctrl.rx', thighT_l_02_PB + '.inRotateX2')
    mc.connectAttr(thighT_l_02_PB + '.outRotateX', 'thigh_twist_fk_02_l.rx', f=True)

    calfT_l_01_PB = mc.createNode('pairBlend', n='calf_twist_fk_01_l_PB')
    mc.setAttr(calfT_l_01_PB + '.weight', -0.4)
    mc.connectAttr('foot_l_ctrl.rz', calfT_l_01_PB + '.inRotateX2')
    mc.connectAttr(calfT_l_01_PB + '.outRotateX', 'calf_twist_fk_01_l.rx', f=True)

    calfT_l_02_PB = mc.createNode('pairBlend', n='calf_twist_fk_02_l_PB')
    mc.setAttr(calfT_l_02_PB + '.weight', -0.8)
    mc.connectAttr('foot_l_ctrl.rz', calfT_l_02_PB + '.inRotateX2')
    mc.connectAttr(calfT_l_02_PB + '.outRotateX', 'calf_twist_fk_02_l.rx', f=True)

    ######################## twist r_transform
    legTwist_r_jnt_rist = ['thigh_twist_fk_01_r', 'thigh_twist_fk_02_r', 'calf_twist_fk_01_r', 'calf_twist_fk_02_r']
    mc.select(legTwist_r_jnt_rist)
    tranRotScl_const()

    thighTwist_r_ctrl_rist = ['thigh_twist_fk_01_r_ctrl', 'thigh_twist_fk_02_r_ctrl', 'calf_twist_fk_01_r_ctrl', 'calf_twist_fk_02_r_ctrl']
    thighTwist_r_masterGrp_rist = ['thigh_twist_fk_01_r_ctrlSpaceMaster', 'thigh_twist_fk_02_r_ctrlSpaceMaster']
    calfTwist_r_masterGrp_rist = ['calf_twist_fk_01_r_ctrlSpaceMaster', 'calf_twist_fk_02_r_ctrlSpaceMaster']
    mc.parent(thighTwist_r_masterGrp_rist, 'thigh_r_ctrl'), mc.parent(calfTwist_r_masterGrp_rist, 'calf_r_ctrl')
    mc.select(d=True)

    mc.disconnectAttr('thigh_r_ctrl.rx', 'thigh_r.rx')
    mc.disconnectAttr('thigh_twist_fk_01_r_ctrl.rx', 'thigh_twist_fk_01_r.rx')
    mc.disconnectAttr('thigh_twist_fk_02_r_ctrl.rx', 'thigh_twist_fk_02_r.rx')
    mc.disconnectAttr('calf_twist_fk_01_r_ctrl.rx', 'calf_twist_fk_01_r.rx')
    mc.disconnectAttr('calf_twist_fk_02_r_ctrl.rx', 'calf_twist_fk_02_r.rx')

    ####### legTwist PB transform

    mc.select(legTwist_r_jnt_rist)
    thighT_r_01_PB = mc.createNode('pairBlend', n='thigh_twist_fk_01_r_PB')
    mc.setAttr(thighT_r_01_PB + '.weight', 0.4)
    mc.connectAttr('thigh_r_ctrl.rx', thighT_r_01_PB + '.inRotateX2')
    mc.connectAttr(thighT_r_01_PB + '.outRotateX', 'thigh_twist_fk_01_r.rx', f=True)

    thighT_r_02_PB = mc.createNode('pairBlend', n='thigh_twist_fk_02_r_PB')
    mc.setAttr(thighT_r_02_PB + '.weight', 0.8)
    mc.connectAttr('thigh_r_ctrl.rx', thighT_r_02_PB + '.inRotateX2')
    mc.connectAttr(thighT_r_02_PB + '.outRotateX', 'thigh_twist_fk_02_r.rx', f=True)

    calfT_r_01_PB = mc.createNode('pairBlend', n='calf_twist_fk_01_r_PB')
    mc.setAttr(calfT_r_01_PB + '.weight', -0.4)
    mc.connectAttr('foot_r_ctrl.rz', calfT_r_01_PB + '.inRotateX2')
    mc.connectAttr(calfT_r_01_PB + '.outRotateX', 'calf_twist_fk_01_r.rx', f=True)

    calfT_r_02_PB = mc.createNode('pairBlend', n='calf_twist_fk_02_r_PB')
    mc.setAttr(calfT_r_02_PB + '.weight', -0.8)
    mc.connectAttr('foot_r_ctrl.rz', calfT_r_02_PB + '.inRotateX2')
    mc.connectAttr(calfT_r_02_PB + '.outRotateX', 'calf_twist_fk_02_r.rx', f=True)

    mc.select(d=True)
    print('leg_FK_Completed')

##################################################### biped FK transform #########################################################

def biped_FK_transform(*args):

    ##################################### FK bones

    spine_jnt_list = ['pelvis', 'spine_01', 'spine_02', 'spine_03']

    for spine_jnt in (spine_jnt_list):
            mc.makeIdentity(spine_jnt, apply=True, t=True, r=True, s=True)
            mc.select(d=True)

    neckHead_jnt_list = ['neck', 'head']

    for neckHead in (neckHead_jnt_list):
            mc.makeIdentity(neckHead, apply=True, t=True, r=True, s=True)
            mc.select(d=True)

    arm_fingers_l_jnt_list = ['clavicle_l', 'upperarm_l', 'lowerarm_l', 'hand_l', 'pinky_00_l', 'pinky_01_l', 'pinky_02_l','pinky_03_l',
                              'ring_00_l', 'ring_01_l', 'ring_02_l', 'ring_03_l', 'middle_00_l', 'middle_01_l',
                              'middle_02_l', 'middle_03_l','index_00_l', 'index_01_l', 'index_02_l', 'index_03_l', 'thumb_01_l', 'thumb_02_l','thumb_03_l']

    for arm_fingers_jnt in (arm_fingers_l_jnt_list):
            mc.makeIdentity(arm_fingers_jnt, apply=True, t=True, r=True, s=True)
            mc.select(d=True)

    ### twist arm
    upperarmTwist_01_l = mc.joint('upperarm_l', n='upperarm_twist_01_l', rad=2)
    upperarmTConst_01_l = mc.pointConstraint('upperarm_l', 'lowerarm_l', upperarmTwist_01_l, mo=False), mc.setAttr('upperarm_twist_01_l_pointConstraint1.upperarm_lW0', 2)
    upperarmTwist_02_l = mc.joint('upperarm_l', n='upperarm_twist_02_l', rad=2)
    upperarmTConst_02_l = mc.pointConstraint('upperarm_l', 'lowerarm_l', upperarmTwist_02_l, mo=False), mc.setAttr('upperarm_twist_02_l_pointConstraint1.lowerarm_lW1', 2)
    mc.delete('upperarm_twist_01_l_pointConstraint1', 'upperarm_twist_02_l_pointConstraint1')

    lowerarmTwist_01_l = mc.joint('lowerarm_l', n='lowerarm_twist_01_l', rad=2)
    lowerarmTConst_01_l = mc.pointConstraint('lowerarm_l', 'hand_l', lowerarmTwist_01_l, mo=False), mc.setAttr('lowerarm_twist_01_l_pointConstraint1.lowerarm_lW0', 1.5)
    lowerarmTwist_02_l = mc.joint('lowerarm_l', n='lowerarm_twist_02_l', rad=2)
    lowerarmTConst_02_l = mc.pointConstraint('lowerarm_l', 'hand_l', lowerarmTwist_02_l, mo=False), mc.setAttr('lowerarm_twist_02_l_pointConstraint1.hand_lW1', 3)
    mc.delete('lowerarm_twist_01_l_pointConstraint1', 'lowerarm_twist_02_l_pointConstraint1')
    mc.select(d=True)

    leg_l_jnt_list = ['thigh_l', 'calf_l', 'foot_l', 'ball_l', 'toe_l']

    for leg_l_jnt in (leg_l_jnt_list):
            mc.makeIdentity(leg_l_jnt, apply=True, t=True, r=True, s=True)
            mc.select(d=True)

    ### twist leg
    thighTwist_01_l = mc.joint('thigh_l', n='thigh_twist_01_l', rad=2)
    thighTConst_01_l = mc.pointConstraint('thigh_l', 'calf_l', thighTwist_01_l, mo=False), mc.setAttr('thigh_twist_01_l_pointConstraint1.thigh_lW0', 2)
    thighTwist_02_l = mc.joint('thigh_l', n='thigh_twist_02_l', rad=2)
    thighTConst_02_l = mc.pointConstraint('thigh_l', 'calf_l', thighTwist_02_l, mo=False), mc.setAttr('thigh_twist_02_l_pointConstraint1.calf_lW1', 2)
    mc.delete('thigh_twist_01_l_pointConstraint1', 'thigh_twist_02_l_pointConstraint1')

    calfTwist_01_l = mc.joint('calf_l', n='calf_twist_01_l', rad=2)
    calfTConst_01_l = mc.pointConstraint('calf_l', 'foot_l', calfTwist_01_l, mo=False), mc.setAttr('calf_twist_01_l_pointConstraint1.calf_lW0', 2)
    calfTwist_02_l = mc.joint('calf_l', n='calf_twist_02_l', rad=2)
    calfTConst_02_l = mc.pointConstraint('calf_l', 'foot_l', calfTwist_02_l, mo=False), mc.setAttr('calf_twist_02_l_pointConstraint1.foot_lW1', 2)
    mc.delete('calf_twist_01_l_pointConstraint1', 'calf_twist_02_l_pointConstraint1')
    mc.select(d=True)

    mc.mirrorJoint('clavicle_l', mirrorYZ=True, mirrorBehavior=True, searchReplace=('_l', '_r')), mc.select(d=True)
    mc.mirrorJoint('thigh_l', mirrorYZ=True, mirrorBehavior=True, searchReplace=('_l', '_r')), mc.select(d=True)

    ###################################################################### spine FK

    mc.select(spine_jnt_list)
    tranRotScl_const()
    mc.parent('spine_03_ctrlSpaceMaster', 'spine_02_ctrl'), mc.parent('spine_02_ctrlSpaceMaster', 'spine_01_ctrl')
    mc.parent('spine_01_ctrlSpaceMaster', 'pelvis_ctrl')
    itemColor('pelvis_ctrl', 17)
    spineGrp = mc.group(n='spine_controls', em=True)
    mc.parent('pelvis_ctrlSpaceMaster', spineGrp)

    mc.select(d=True)

    ################################################################## neck FK

    mc.select(neckHead_jnt_list)
    tranRotScl_const()
    itemColor('neck_ctrl', 17)
    mc.parent('head_ctrlSpaceMaster', 'neck_ctrl')
    neckHeadGrp = mc.group(n= 'neck_controls', em=True)
    mc.parent('neck_ctrlSpaceMaster', neckHeadGrp)

    ### neck twist
    neckTwist = mc.joint('neck', n= 'neck_twist', rad=2)
    mc.delete(mc.pointConstraint('neck', 'head', neckTwist, mo=False))
    neck_PB = mc.createNode('pairBlend', n= 'neck_twist_PB')
    mc.setAttr(neck_PB + '.weight', 0.5)
    mc.connectAttr('head_ctrl.rotateX', neck_PB + '.inRotateX2')
    mc.connectAttr(neck_PB + '.outRotateX', neckTwist + '.rx')

    mc.select(d=True)

    ############################################################################# arm FK


    arm_fingers_r_jnt_list = ['clavicle_r', 'upperarm_r', 'lowerarm_r', 'hand_r', 'pinky_00_r', 'pinky_01_r', 'pinky_02_r',
                              'pinky_03_r','ring_00_r', 'ring_01_r', 'ring_02_r', 'ring_03_r', 'middle_00_r', 'middle_01_r',
                              'middle_02_r', 'middle_03_r','index_00_r', 'index_01_r', 'index_02_r', 'index_03_r', 'thumb_01_r', 'thumb_02_r','thumb_03_r']

    mc.select(arm_fingers_l_jnt_list, arm_fingers_r_jnt_list)
    tranRotScl_const()

    ### controls
    arm_fingers_l_ctrl_list = ['clavicle_l_ctrl', 'upperarm_l_ctrl', 'lowerarm_l_ctrl', 'hand_l_ctrl', 'pinky_00_l_ctrl',
                               'pinky_01_l_ctrl', 'pinky_02_l_ctrl', 'pinky_03_l_ctrl','ring_00_l_ctrl', 'ring_01_l_ctrl', 'ring_02_l_ctrl', 'ring_03_l_ctrl', 'middle_00_l_ctrl',
                               'middle_01_l_ctrl', 'middle_02_l_ctrl', 'middle_03_l_ctrl','index_00_l_ctrl', 'index_01_l_ctrl', 'index_02_l_ctrl', 'index_03_l_ctrl',
                               'thumb_01_l_ctrl', 'thumb_02_l_ctrl', 'thumb_03_l_ctrl']

    arm_fingers_r_ctrl_list = ['clavicle_r_ctrl', 'upperarm_r_ctrl', 'lowerarm_r_ctrl', 'hand_r_ctrl', 'pinky_00_r_ctrl','pinky_01_r_ctrl', 'pinky_02_r_ctrl', 'pinky_03_r_ctrl',
                               'ring_00_r_ctrl', 'ring_01_r_ctrl', 'ring_02_r_ctrl', 'ring_03_r_ctrl', 'middle_00_r_ctrl',
                               'middle_01_r_ctrl', 'middle_02_r_ctrl', 'middle_03_r_ctrl','index_00_r_ctrl', 'index_01_r_ctrl', 'index_02_r_ctrl', 'index_03_r_ctrl',
                               'thumb_01_r_ctrl', 'thumb_02_r_ctrl', 'thumb_03_r_ctrl']

    for armF_l in arm_fingers_l_ctrl_list:
            itemColor(armF_l, 6)

    for armF_r in arm_fingers_r_ctrl_list:
            itemColor(armF_r, 13)

    ### parent controls
    mc.parent('upperarm_l_ctrlSpaceMaster', 'clavicle_l_ctrl'), mc.parent('lowerarm_l_ctrlSpaceMaster','upperarm_l_ctrl'), mc.parent('hand_l_ctrlSpaceMaster', 'lowerarm_l_ctrl')
    mc.parent('pinky_03_l_ctrlSpaceMaster', 'pinky_02_l_ctrl'), mc.parent('pinky_02_l_ctrlSpaceMaster','pinky_01_l_ctrl'), mc.parent('pinky_01_l_ctrlSpaceMaster', 'pinky_00_l_ctrl')
    mc.parent('ring_03_l_ctrlSpaceMaster', 'ring_02_l_ctrl'), mc.parent('ring_02_l_ctrlSpaceMaster','ring_01_l_ctrl'), mc.parent('ring_01_l_ctrlSpaceMaster', 'ring_00_l_ctrl')
    mc.parent('middle_03_l_ctrlSpaceMaster', 'middle_02_l_ctrl'), mc.parent('middle_02_l_ctrlSpaceMaster','middle_01_l_ctrl'), mc.parent('middle_01_l_ctrlSpaceMaster', 'middle_00_l_ctrl')
    mc.parent('index_03_l_ctrlSpaceMaster', 'index_02_l_ctrl'), mc.parent('index_02_l_ctrlSpaceMaster','index_01_l_ctrl'), mc.parent('index_01_l_ctrlSpaceMaster', 'index_00_l_ctrl')
    mc.parent('thumb_03_l_ctrlSpaceMaster', 'thumb_02_l_ctrl'), mc.parent('thumb_02_l_ctrlSpaceMaster', 'thumb_01_l_ctrl')
    mc.parent('pinky_00_l_ctrlSpaceMaster', 'ring_00_l_ctrlSpaceMaster', 'middle_00_l_ctrlSpaceMaster', 'index_00_l_ctrlSpaceMaster', 'thumb_01_l_ctrlSpaceMaster', 'hand_l_ctrl')

    mc.parent('upperarm_r_ctrlSpaceMaster', 'clavicle_r_ctrl'), mc.parent('lowerarm_r_ctrlSpaceMaster','upperarm_r_ctrl'), mc.parent('hand_r_ctrlSpaceMaster', 'lowerarm_r_ctrl')
    mc.parent('pinky_03_r_ctrlSpaceMaster', 'pinky_02_r_ctrl'), mc.parent('pinky_02_r_ctrlSpaceMaster','pinky_01_r_ctrl'), mc.parent('pinky_01_r_ctrlSpaceMaster', 'pinky_00_r_ctrl')
    mc.parent('ring_03_r_ctrlSpaceMaster', 'ring_02_r_ctrl'), mc.parent('ring_02_r_ctrlSpaceMaster','ring_01_r_ctrl'), mc.parent('ring_01_r_ctrlSpaceMaster', 'ring_00_r_ctrl')
    mc.parent('middle_03_r_ctrlSpaceMaster', 'middle_02_r_ctrl'), mc.parent('middle_02_r_ctrlSpaceMaster','middle_01_r_ctrl'), mc.parent('middle_01_r_ctrlSpaceMaster', 'middle_00_r_ctrl')
    mc.parent('index_03_r_ctrlSpaceMaster', 'index_02_r_ctrl'), mc.parent('index_02_r_ctrlSpaceMaster','index_01_r_ctrl'), mc.parent('index_01_r_ctrlSpaceMaster', 'index_00_r_ctrl')
    mc.parent('thumb_03_r_ctrlSpaceMaster', 'thumb_02_r_ctrl'), mc.parent('thumb_02_r_ctrlSpaceMaster', 'thumb_01_r_ctrl')
    mc.parent('pinky_00_r_ctrlSpaceMaster', 'ring_00_r_ctrlSpaceMaster', 'middle_00_r_ctrlSpaceMaster','index_00_r_ctrlSpaceMaster', 'thumb_01_r_ctrlSpaceMaster', 'hand_r_ctrl')

    armsGrp = mc.group(n='arms_ctrls', em=True)
    mc.parent('clavicle_r_ctrlSpaceMaster', 'clavicle_l_ctrlSpaceMaster', armsGrp), mc.select(d=True)

    ######################## twist l_transform
    upperarmTwist_l_jnt_list = ['upperarm_twist_01_l', 'upperarm_twist_02_l', 'lowerarm_twist_01_l', 'lowerarm_twist_02_l']
    mc.select(upperarmTwist_l_jnt_list)
    tranRotScl_const()

    upperarmTwist_l_ctrl_list = ['upperarm_twist_01_l_ctrl', 'upperarm_twist_02_l_ctrl', 'lowerarm_twist_01_l_ctrl','lowerarm_twist_02_l_ctrl']
    upperarmTwist_l_masterGrp_list = ['upperarm_twist_01_l_ctrlSpaceMaster', 'upperarm_twist_02_l_ctrlSpaceMaster']
    lowerarmTwist_l_masterGrp_list = ['lowerarm_twist_01_l_ctrlSpaceMaster', 'lowerarm_twist_02_l_ctrlSpaceMaster']
    mc.parent(upperarmTwist_l_masterGrp_list, 'upperarm_l_ctrl'), mc.parent(lowerarmTwist_l_masterGrp_list,'lowerarm_l_ctrl')
    mc.select(d=True)

    mc.disconnectAttr('upperarm_l_ctrl.rx', 'upperarm_l.rx')
    mc.disconnectAttr('upperarm_twist_01_l_ctrl.rx', 'upperarm_twist_01_l.rx')
    mc.disconnectAttr('upperarm_twist_02_l_ctrl.rx', 'upperarm_twist_02_l.rx')
    mc.disconnectAttr('lowerarm_twist_01_l_ctrl.rx', 'lowerarm_twist_01_l.rx')
    mc.disconnectAttr('lowerarm_twist_02_l_ctrl.rx', 'lowerarm_twist_02_l.rx')

    #### armTwist PB connection
    mc.select(upperarmTwist_l_jnt_list)

    upperarmT_l_01_PB = mc.createNode('pairBlend', n='upperarm_twist_01_l_PB')
    mc.setAttr(upperarmT_l_01_PB + '.weight', 0.2)
    mc.connectAttr('upperarm_l_ctrl.rx', upperarmT_l_01_PB + '.inRotateX2')
    mc.connectAttr(upperarmT_l_01_PB + '.outRotateX', 'upperarm_twist_01_l.rx', f=True)

    upperarmT_l_02_PB = mc.createNode('pairBlend', n='upperarm_twist_02_l_PB')
    mc.setAttr(upperarmT_l_02_PB + '.weight', 0.8)
    mc.connectAttr('upperarm_l_ctrl.rx', upperarmT_l_02_PB + '.inRotateX2')
    mc.connectAttr(upperarmT_l_02_PB + '.outRotateX', 'upperarm_twist_02_l.rx', f=True)

    lowerarmT_l_01_PB = mc.createNode('pairBlend', n='lowerarm_twist_01_l_PB')
    mc.setAttr(lowerarmT_l_01_PB + '.weight', 0.4)
    mc.connectAttr('hand_l_ctrl.rx', lowerarmT_l_01_PB + '.inRotateX2')
    mc.connectAttr(lowerarmT_l_01_PB + '.outRotateX', 'lowerarm_twist_01_l.rx', f=True)

    lowerarmT_l_02_PB = mc.createNode('pairBlend', n='lowerarm_twist_02_l_PB')
    mc.setAttr(lowerarmT_l_02_PB + '.weight', 0.8)
    mc.connectAttr('hand_l_ctrl.rx', lowerarmT_l_02_PB + '.inRotateX2')
    mc.connectAttr(lowerarmT_l_02_PB + '.outRotateX', 'lowerarm_twist_02_l.rx', f=True)

    ######################## twist r_transform
    upperarmTwist_r_jnt_list = ['upperarm_twist_01_r', 'upperarm_twist_02_r', 'lowerarm_twist_01_r', 'lowerarm_twist_02_r']
    mc.select(upperarmTwist_r_jnt_list)
    tranRotScl_const()

    upperarmTwist_r_ctrl_list = ['upperarm_twist_01_r_ctrl', 'upperarm_twist_02_r_ctrl', 'lowerarm_twist_01_r_ctrl','lowerarm_twist_02_r_ctrl']
    upperarmTwist_r_masterGrp_list = ['upperarm_twist_01_r_ctrlSpaceMaster', 'upperarm_twist_02_r_ctrlSpaceMaster']
    lowerarmTwist_r_masterGrp_list = ['lowerarm_twist_01_r_ctrlSpaceMaster', 'lowerarm_twist_02_r_ctrlSpaceMaster']
    mc.parent(upperarmTwist_r_masterGrp_list, 'upperarm_r_ctrl'), mc.parent(lowerarmTwist_r_masterGrp_list, 'lowerarm_r_ctrl')
    mc.select(d=True)

    mc.disconnectAttr('upperarm_r_ctrl.rx', 'upperarm_r.rx')
    mc.disconnectAttr('upperarm_twist_01_r_ctrl.rx', 'upperarm_twist_01_r.rx')
    mc.disconnectAttr('upperarm_twist_02_r_ctrl.rx', 'upperarm_twist_02_r.rx')
    mc.disconnectAttr('lowerarm_twist_01_r_ctrl.rx', 'lowerarm_twist_01_r.rx')
    mc.disconnectAttr('lowerarm_twist_02_r_ctrl.rx', 'lowerarm_twist_02_r.rx')

    #### armTwist PB connection
    mc.select(upperarmTwist_r_jnt_list)

    upperarmT_r_01_PB = mc.createNode('pairBlend', n='upperarm_twist_01_r_PB')
    mc.setAttr(upperarmT_r_01_PB + '.weight', 0.2)
    mc.connectAttr('upperarm_r_ctrl.rx', upperarmT_r_01_PB + '.inRotateX2')
    mc.connectAttr(upperarmT_r_01_PB + '.outRotateX', 'upperarm_twist_01_r.rx', f=True)

    upperarmT_r_02_PB = mc.createNode('pairBlend', n='upperarm_twist_02_r_PB')
    mc.setAttr(upperarmT_r_02_PB + '.weight', 0.8)
    mc.connectAttr('upperarm_r_ctrl.rx', upperarmT_r_02_PB + '.inRotateX2')
    mc.connectAttr(upperarmT_r_02_PB + '.outRotateX', 'upperarm_twist_02_r.rx', f=True)

    lowerarmT_r_01_PB = mc.createNode('pairBlend', n='lowerarm_twist_01_r_PB')
    mc.setAttr(lowerarmT_r_01_PB + '.weight', 0.4)
    mc.connectAttr('hand_r_ctrl.rx', lowerarmT_r_01_PB + '.inRotateX2')
    mc.connectAttr(lowerarmT_r_01_PB + '.outRotateX', 'lowerarm_twist_01_r.rx', f=True)

    lowerarmT_r_02_PB = mc.createNode('pairBlend', n='lowerarm_twist_02_r_PB')
    mc.setAttr(lowerarmT_r_02_PB + '.weight', 0.8)
    mc.connectAttr('hand_r_ctrl.rx', lowerarmT_r_02_PB + '.inRotateX2')
    mc.connectAttr(lowerarmT_r_02_PB + '.outRotateX', 'lowerarm_twist_02_r.rx', f=True)

    mc.select(d=True)

    ##################################################################################### leg FK

    leg_r_jnt_list = ['thigh_r', 'calf_r', 'foot_r', 'ball_r', 'toe_r']

    mc.select(leg_r_jnt_list, leg_l_jnt_list)
    tranRotScl_const()

    ##### controls
    leg_l_ctrl_list = ['thigh_l_ctrl', 'calf_l_ctrl', 'foot_l_ctrl', 'ball_l_ctrl', 'toe_l_ctrl']
    leg_r_ctrl_list = ['thigh_r_ctrl', 'calf_r_ctrl', 'foot_r_ctrl', 'ball_r_ctrl', 'toe_r_ctrl']

    for leg_l_color in leg_l_ctrl_list:
            itemColor(leg_l_color, 6)

    for leg_r_color in leg_r_ctrl_list:
            itemColor(leg_r_color, 13)

    mc.parent('toe_l_ctrlSpaceMaster', 'ball_l_ctrl'), mc.parent('ball_l_ctrlSpaceMaster', 'foot_l_ctrl'), mc.parent('foot_l_ctrlSpaceMaster', 'calf_l_ctrl'), mc.parent('calf_l_ctrlSpaceMaster', 'thigh_l_ctrl')
    mc.parent('toe_r_ctrlSpaceMaster', 'ball_r_ctrl'), mc.parent('ball_r_ctrlSpaceMaster', 'foot_r_ctrl'), mc.parent('foot_r_ctrlSpaceMaster', 'calf_r_ctrl'), mc.parent('calf_r_ctrlSpaceMaster', 'thigh_r_ctrl')
    legGrp = mc.group(n='leg_controls', em=True)
    mc.parent('thigh_r_ctrlSpaceMaster', 'thigh_l_ctrlSpaceMaster', legGrp), mc.select(d=True)

    ######################## twist l_transform
    legTwist_l_jnt_list = ['thigh_twist_01_l', 'thigh_twist_02_l', 'calf_twist_01_l', 'calf_twist_02_l']
    mc.select(legTwist_l_jnt_list)
    tranRotScl_const()

    thighTwist_l_ctrl_list = ['thigh_twist_01_l_ctrl', 'thigh_twist_02_l_ctrl', 'calf_twist_01_l_ctrl','calf_twist_02_l_ctrl']
    thighTwist_l_masterGrp_list = ['thigh_twist_01_l_ctrlSpaceMaster', 'thigh_twist_02_l_ctrlSpaceMaster']
    calfTwist_l_masterGrp_list = ['calf_twist_01_l_ctrlSpaceMaster', 'calf_twist_02_l_ctrlSpaceMaster']
    mc.parent(thighTwist_l_masterGrp_list, 'thigh_l_ctrl'), mc.parent(calfTwist_l_masterGrp_list, 'calf_l_ctrl')
    mc.select(d=True)

    mc.disconnectAttr('thigh_l_ctrl.rx', 'thigh_l.rx')
    mc.disconnectAttr('thigh_twist_01_l_ctrl.rx', 'thigh_twist_01_l.rx')
    mc.disconnectAttr('thigh_twist_02_l_ctrl.rx', 'thigh_twist_02_l.rx')
    mc.disconnectAttr('calf_twist_01_l_ctrl.rx', 'calf_twist_01_l.rx')
    mc.disconnectAttr('calf_twist_02_l_ctrl.rx', 'calf_twist_02_l.rx')

    ####### legTwist PB transform

    mc.select(legTwist_l_jnt_list)
    thighT_l_01_PB = mc.createNode('pairBlend', n='thigh_twist_01_l_PB')
    mc.setAttr(thighT_l_01_PB + '.weight', 0.4)
    mc.connectAttr('thigh_l_ctrl.rx', thighT_l_01_PB + '.inRotateX2')
    mc.connectAttr(thighT_l_01_PB + '.outRotateX', 'thigh_twist_01_l.rx', f=True)

    thighT_l_02_PB = mc.createNode('pairBlend', n='thigh_twist_02_l_PB')
    mc.setAttr(thighT_l_02_PB + '.weight', 0.8)
    mc.connectAttr('thigh_l_ctrl.rx', thighT_l_02_PB + '.inRotateX2')
    mc.connectAttr(thighT_l_02_PB + '.outRotateX', 'thigh_twist_02_l.rx', f=True)

    calfT_l_01_PB = mc.createNode('pairBlend', n='calf_twist_01_l_PB')
    mc.setAttr(calfT_l_01_PB + '.weight', -0.4)
    mc.connectAttr('foot_l_ctrl.rz', calfT_l_01_PB + '.inRotateX2')
    mc.connectAttr(calfT_l_01_PB + '.outRotateX', 'calf_twist_01_l.rx', f=True)

    calfT_l_02_PB = mc.createNode('pairBlend', n='calf_twist_02_l_PB')
    mc.setAttr(calfT_l_02_PB + '.weight', -0.8)
    mc.connectAttr('foot_l_ctrl.rz', calfT_l_02_PB + '.inRotateX2')
    mc.connectAttr(calfT_l_02_PB + '.outRotateX', 'calf_twist_02_l.rx', f=True)

    ######################## twist r_transform
    legTwist_r_jnt_rist = ['thigh_twist_01_r', 'thigh_twist_02_r', 'calf_twist_01_r', 'calf_twist_02_r']
    mc.select(legTwist_r_jnt_rist)
    tranRotScl_const()

    thighTwist_r_ctrl_rist = ['thigh_twist_01_r_ctrl', 'thigh_twist_02_r_ctrl', 'calf_twist_01_r_ctrl','calf_twist_02_r_ctrl']
    thighTwist_r_masterGrp_rist = ['thigh_twist_01_r_ctrlSpaceMaster', 'thigh_twist_02_r_ctrlSpaceMaster']
    calfTwist_r_masterGrp_rist = ['calf_twist_01_r_ctrlSpaceMaster', 'calf_twist_02_r_ctrlSpaceMaster']
    mc.parent(thighTwist_r_masterGrp_rist, 'thigh_r_ctrl'), mc.parent(calfTwist_r_masterGrp_rist, 'calf_r_ctrl')
    mc.select(d=True)

    mc.disconnectAttr('thigh_r_ctrl.rx', 'thigh_r.rx')
    mc.disconnectAttr('thigh_twist_01_r_ctrl.rx', 'thigh_twist_01_r.rx')
    mc.disconnectAttr('thigh_twist_02_r_ctrl.rx', 'thigh_twist_02_r.rx')
    mc.disconnectAttr('calf_twist_01_r_ctrl.rx', 'calf_twist_01_r.rx')
    mc.disconnectAttr('calf_twist_02_r_ctrl.rx', 'calf_twist_02_r.rx')

    ####### legTwist PB transform

    mc.select(legTwist_r_jnt_rist)
    thighT_r_01_PB = mc.createNode('pairBlend', n='thigh_twist_01_r_PB')
    mc.setAttr(thighT_r_01_PB + '.weight', 0.4)
    mc.connectAttr('thigh_r_ctrl.rx', thighT_r_01_PB + '.inRotateX2')
    mc.connectAttr(thighT_r_01_PB + '.outRotateX', 'thigh_twist_01_r.rx', f=True)

    thighT_r_02_PB = mc.createNode('pairBlend', n='thigh_twist_02_r_PB')
    mc.setAttr(thighT_r_02_PB + '.weight', 0.8)
    mc.connectAttr('thigh_r_ctrl.rx', thighT_r_02_PB + '.inRotateX2')
    mc.connectAttr(thighT_r_02_PB + '.outRotateX', 'thigh_twist_02_r.rx', f=True)

    calfT_r_01_PB = mc.createNode('pairBlend', n='calf_twist_01_r_PB')
    mc.setAttr(calfT_r_01_PB + '.weight', -0.4)
    mc.connectAttr('foot_r_ctrl.rz', calfT_r_01_PB + '.inRotateX2')
    mc.connectAttr(calfT_r_01_PB + '.outRotateX', 'calf_twist_01_r.rx', f=True)

    calfT_r_02_PB = mc.createNode('pairBlend', n='calf_twist_02_r_PB')
    mc.setAttr(calfT_r_02_PB + '.weight', -0.8)
    mc.connectAttr('foot_r_ctrl.rz', calfT_r_02_PB + '.inRotateX2')
    mc.connectAttr(calfT_r_02_PB + '.outRotateX', 'calf_twist_02_r.rx', f=True)

    mc.select(d=True)

    bipedGrp = mc.group(n='biped_controls', em=True)
    mc.parent(armsGrp, legGrp, neckHeadGrp, spineGrp, bipedGrp), mc.select(d=True)
    mc.parent(armsGrp, neckHeadGrp, 'spine_03_ctrl'), mc.parent(legGrp, 'pelvis_ctrl')
    mc.parent('thigh_r', 'thigh_l', 'pelvis'), mc.parent('neck', 'clavicle_l', 'clavicle_r', 'spine_03'), mc.select(d=True)
    print('Biped_FK_completed')

#######################################################################
#
#
#                           IK System
#
#
#######################################################################

######################################################### spine IK transform #############################################################

def spine_IK_transform(*args):

    mc.ikHandle(n='spine_ik', sj='pelvis', ee='spine_03', sol='ikSplineSolver')

    spine_jnt_list = ['pelvis', 'spine_01', 'spine_02', 'spine_03']

    cv_list = ['curve1.cv[0]', 'curve1.cv[1:2]', 'curve1.cv[3]']
    for each in cv_list:
        mc.cluster(each)
    mc.select(d=True)

    clusters = ['cluster1Handle', 'cluster2Handle', 'cluster3Handle']
    for each in clusters:
        mc.rename(each, 'spine_cl')

    clustersNodes = ['spine_cl', 'spine_cl1', 'spine_cl2']
    for each in clustersNodes:
        cluster_ctrl = mc.circle(nr=(0, 1, 0), c=(0, 0, 0), r=5, n=each + '_ctrl', ch=False)
        cluster_grp = mc.group(n= each + '_ctrlSpace', em=True)
        cluster_masterGrp = mc.group(n= each + '_master_ctrSpace', em=True)
        mc.parent(cluster_ctrl, cluster_grp)
        mc.parent(cluster_grp, cluster_masterGrp)
        mc.delete(mc.parentConstraint(each, cluster_masterGrp, mo=False))
    mc.select(d=True)

    spine_ctrl_list = ['spine_cl_ctrl', 'spine_cl1_ctrl', 'spine_cl2_ctrl']
    for item in spine_ctrl_list:
        itemColor(item, 17)

    # parent the cluster under the controllers
    mc.parent('spine_cl', 'spine_cl_ctrl'), mc.parent('spine_cl1', 'spine_cl1_ctrl'), mc.parent('spine_cl2', 'spine_cl2_ctrl')
    mc.select(d=True)

    # advance twist controls setup
    mc.setAttr("spine_ik.dTwistControlEnable", 1)
    mc.setAttr("spine_ik.dWorldUpType", 4)
    mc.setAttr("spine_ik.dForwardAxis", 0)
    mc.setAttr("spine_ik.dWorldUpAxis", 3)
    mc.setAttr("spine_ik.dTwistValueType", 1)
    mc.setAttr('spine_ik.dWorldUpVectorZ', 1)
    mc.setAttr('spine_ik.dWorldUpVectorEndZ', 1)
    mc.setAttr('spine_ik.dWorldUpVectorY', 0)
    mc.setAttr('spine_ik.dWorldUpVectorEndY', 0)
    mc.connectAttr('spine_cl2_ctrl.worldMatrix', 'spine_ik.dWorldUpMatrixEnd')
    mc.connectAttr('spine_cl_ctrl.worldMatrix', 'spine_ik.dWorldUpMatrix')

    # S&S
    spine_arcLength_MD = mc.createNode('multiplyDivide', n='spine_arcLength_MD')
    mc.setAttr(spine_arcLength_MD + '.operation', 2)
    spine_arcLength_div_MD = mc.createNode('multiplyDivide', n='spine_arcLength_div_MD')
    mc.setAttr(spine_arcLength_div_MD + '.operation', 2)
    crvInfo = mc.createNode('curveInfo', n='spine_crvInfo')
    mc.connectAttr('curveShape1.worldSpace', crvInfo + '.inputCurve', f=True)
    arcLengh_data = mc.getAttr(crvInfo + '.arcLength')
    mc.setAttr(spine_arcLength_MD + '.input2X', arcLengh_data)
    mc.connectAttr(crvInfo + '.arcLength', spine_arcLength_MD + '.input1X', f=True)
    mc.connectAttr(spine_arcLength_MD + '.outputX', spine_arcLength_div_MD + '.input1X', f=True)

    for spineJnt in (spine_jnt_list):
        mc.connectAttr(spine_arcLength_div_MD + '.outputX', spineJnt + '.sx')

    # COG control
    cog_ctrl = mc.circle(nr=(0, 1, 0), r=20, n='cog_ctrl', ch=False)
    cog_ctrlSpace = mc.group(cog_ctrl, n='cog_ctrlSpace')
    cog_ctrlSpaceMaster = mc.group(cog_ctrlSpace, n='cog_masterSpace')
    mc.delete(mc.parentConstraint('pelvis', cog_ctrlSpaceMaster))
    mc.setAttr(cog_ctrlSpaceMaster + '.rx', 0), mc.setAttr(cog_ctrlSpaceMaster + '.ry', 0), mc.setAttr(cog_ctrlSpaceMaster + '.rz', 0)

    # clean
    spineIK_grp = mc.group(n='spine_IK_controls', em=True)
    mc.parent('spine_cl_master_ctrSpace', 'spine_cl1_master_ctrSpace', 'spine_cl2_master_ctrSpace', cog_ctrl), mc.parent(cog_ctrlSpaceMaster, spineIK_grp)
    mc.select(d=True)
    for i in clustersNodes:
        mc.setAttr(i + '.v', 0)
    mc.setAttr('spine_ik.v', 0)

######################################################### arm IK transform ################################################################
'''
################################# call arm templete ############################################################
myHJntTemp.armT()
'''
def arm_fingers_IK_transform(*args):

    ############################### freeze transformation of bones rotation #####################################
    arm_fingers_l_jnt_list = ['clavicle_l', 'upperarm_l', 'lowerarm_l', 'hand_l', 'pinky_00_l', 'pinky_01_l', 'pinky_02_l', 'pinky_03_l', 'ring_00_l', 'ring_01_l',
                              'ring_02_l', 'ring_03_l', 'index_00_l', 'index_01_l', 'index_02_l', 'index_03_l', 'middle_00_l', 'middle_01_l', 'middle_02_l', 'middle_03_l',
                              'thumb_03_l', 'upperarm_twist_01_l', 'upperarm_twist_02_l', 'lowerarm_twist_01_l', 'lowerarm_twist_02_l']

    # twist arm
    upperarmTwist_01_l = mc.joint('upperarm_l', n='upperarm_twist_01_l', rad=2)
    upperarmTConst_01_l = mc.pointConstraint('upperarm_l', 'lowerarm_l', upperarmTwist_01_l, mo=False), mc.setAttr('upperarm_twist_01_l_pointConstraint1.upperarm_lW0', 2)
    upperarmTwist_02_l = mc.joint('upperarm_l', n='upperarm_twist_02_l', rad=2)
    upperarmTConst_02_l = mc.pointConstraint('upperarm_l', 'lowerarm_l', upperarmTwist_02_l, mo=False), mc.setAttr('upperarm_twist_02_l_pointConstraint1.lowerarm_lW1', 2)
    mc.delete('upperarm_twist_01_l_pointConstraint1', 'upperarm_twist_02_l_pointConstraint1')

    lowerarmTwist_01_l = mc.joint('lowerarm_l', n='lowerarm_twist_01_l', rad=2)
    lowerarmTConst_01_l = mc.pointConstraint('lowerarm_l', 'hand_l', lowerarmTwist_01_l, mo=False), mc.setAttr('lowerarm_twist_01_l_pointConstraint1.lowerarm_lW0', 1.5)
    lowerarmTwist_02_l = mc.joint('lowerarm_l', n='lowerarm_twist_02_l', rad=2)
    lowerarmTConst_02_l = mc.pointConstraint('lowerarm_l', 'hand_l', lowerarmTwist_02_l, mo=False), mc.setAttr('lowerarm_twist_02_l_pointConstraint1.hand_lW1', 3)
    mc.delete('lowerarm_twist_01_l_pointConstraint1', 'lowerarm_twist_02_l_pointConstraint1')
    mc.select(d=True)

    for arm_jnt in arm_fingers_l_jnt_list:
        mc.makeIdentity(arm_jnt, apply=True, t=True, r=True, s=True)
        mc.select(d=True)

    # mirror base arm skeleton
    mc.mirrorJoint('clavicle_l', mirrorYZ=True, mirrorBehavior=True, searchReplace=('_l', '_r'))
    mc.select(d=True)

    ###################################################### IK SYSTEM ############################################################
    mc.duplicate('upperarm_l')
    mc.select('upperarm_l1')
    mel.eval('searchReplaceNames "_l" "_l2" "hierarchy"')
    mc.rename('upperarm_l21', 'upperarm_l2')
    mc.select('upperarm_l2', hi=True)
    ikJnt = mc.ls(sl=True)

    for i in ikJnt:
        name = i.replace('l2', 'l_ik')
        mc.rename(i, name)
    mc.parent('upperarm_l_ik', w=True), mc.select(d=True)

    ################################################################### pole vector templete
    mc.select('upperarm_l_ik', 'lowerarm_l_ik', 'hand_l_ik')
    selO = mc.ls(sl=True)

    upperarmIK = mc.xform(selO[0], q=True, ws=True, t=True)
    lowerarmIK = mc.xform(selO[1], q=True, ws=True, t=True)
    handIK = mc.xform(selO[2], q=True, ws=True, t=True)

    upperarmIKV = OpenMaya.MVector(upperarmIK[0], upperarmIK[1], upperarmIK[2])
    lowerarmIKV = OpenMaya.MVector(lowerarmIK[0], lowerarmIK[1], lowerarmIK[2])
    handIKV = OpenMaya.MVector(handIK[0], handIK[1], handIK[2])

    startEnd = handIKV - upperarmIKV
    startMid = lowerarmIKV - upperarmIKV

    dotP = startMid * startEnd
    proj = float(dotP) / float(startEnd.length())
    startEndN = startEnd.normal()
    projV = startEndN * proj

    arrowV = startMid - projV
    arrowV*=5
    finalV = arrowV + lowerarmIKV

    loc_PV = mc.spaceLocator(n='arm_PV_l')
    loc_PVSpace = mc.group(loc_PV, n='PV_locSpace'), mc.select(d=True)
    mc.xform(loc_PVSpace, ws=True, t=(finalV.x, finalV.y, finalV.z))
    mc.parent(loc_PVSpace, 'lowerarm_l_ik')

    ################################################################################## mirror ik chain
    mc.mirrorJoint('upperarm_l_ik', mirrorYZ=True, mirrorBehavior=True, searchReplace=('_l', '_r'))
    mc.rename('arm_PV_l1', 'arm_PV_r')

    ########################################################## create ikhandle rotate plane solver, PV & controls
    ikArm_l = mc.ikHandle(n='ikArm_l', sj='upperarm_l_ik', ee='hand_l_ik', sol='ikRPsolver')
    ikArm_r = mc.ikHandle(n='ikArm_r', sj='upperarm_r_ik', ee='hand_r_ik', sol='ikRPsolver')
    ikArms_list = [ikArm_r, ikArm_r]
    mc.select(d=True)

    ikHand_jnt_list = ['hand_l_ik', 'hand_r_ik']
    for ikH in ikHand_jnt_list:
        myCtrl.square_ctrl(ikH)

    ikHand_ctrl_list = ['hand_l_ik_ctrl', 'hand_r_ik_ctrl']
    for ikHand_ctrl in ikHand_ctrl_list:
        mc.setAttr(ikHand_ctrl + '.sx', l=True, k=False, ch=False)
        mc.setAttr(ikHand_ctrl + '.sy', l=True, k=False, ch=False)
        mc.setAttr(ikHand_ctrl + '.sz', l=True, k=False, ch=False)
        mc.setAttr(ikHand_ctrl + '.v', l=True, k=False, ch=False)

    ikHand_gimbalCtrl_list = ['hand_l_ik', 'hand_r_ik']
    for ikHGimbal in ikHand_gimbalCtrl_list:
        myCtrl.diamondLow_ctrl(ikHGimbal)
    mc.select('hand_l_ik_ctrlSpaceMaster1', 'hand_r_ik_ctrlSpaceMaster1', hi=True)
    ikHGimbalCtrlSpaceMaster = mc.ls(sl=True)

    ########################################################################## ik gimbal control setup
    for gimbal in ikHGimbalCtrlSpaceMaster:
        mel.eval('searchReplaceNames "ik_ctrl" "ik_gimbal_ctrl" "hierarchy"')
    mc.rename('hand_l_ik_gimbal_ctrlSpaceMaster1', 'hand_l_ik_gimbal_ctrlSpaceMaster'), mc.rename('hand_r_ik_gimbal_ctrlSpaceMaster1', 'hand_r_ik_gimbal_ctrlSpaceMaster')
    mc.select(d=True)

    mc.parent('hand_l_ik_gimbal_ctrlSpaceMaster', 'hand_l_ik_ctrl'), mc.parent('hand_r_ik_gimbal_ctrlSpaceMaster', 'hand_r_ik_ctrl'), mc.select(d=True)

    mc.delete(mc.parentConstraint('hand_r_ik', 'hand_r_ik_ctrlSpaceMaster'))
    mc.delete(mc.parentConstraint('hand_l_ik', 'hand_l_ik_ctrlSpaceMaster'))

    mc.select('hand_l_ik_gimbal_ctrl.cv[0:18]', 'hand_r_ik_gimbal_ctrl.cv[0:18]')
    mc.rotate(0,90,0, fo=True), mc.select(d=True)

    ikHRotCtrl_list = ['hand_l_ik_gimbal_ctrl', 'hand_r_ik_gimbal_ctrl']
    for ikRot in ikHRotCtrl_list:
        mc.setAttr(ikRot + '.tx', l=True, k=False, ch=False)
        mc.setAttr(ikRot + '.ty', l=True, k=False, ch=False)
        mc.setAttr(ikRot + '.tz', l=True, k=False, ch=False)
        mc.setAttr(ikRot + '.sx', l=True, k=False, ch=False)
        mc.setAttr(ikRot + '.sy', l=True, k=False, ch=False)
        mc.setAttr(ikRot + '.sz', l=True, k=False, ch=False)
        mc.setAttr(ikRot + '.v', l=True, k=False, ch=False)

    ###################################################################################################
    #
    #                                                   ik twist setup
    #
    ###################################################################################################
    ############################# lef side ik twist setup
    leftUpperarmT_ikJnt_list = ['upperarm_twist_01_l_ik', 'upperarm_twist_02_l_ik']
    for leftUpperT_ik in leftUpperarmT_ikJnt_list:
        upperarmPB = mc.createNode('pairBlend', n= leftUpperT_ik + '_PB')
        mc.connectAttr('upperarm_l_ik.rx', upperarmPB + '.inRotateX2', f=True)
        mc.connectAttr(upperarmPB + '.outRotateX', leftUpperT_ik + '.rx', f=True)
    mc.setAttr('upperarm_twist_01_l_ik_PB.weight', 0.2), mc.setAttr('upperarm_twist_02_l_ik_PB.weight', 0.8)

    leftLowerarmT_ikJnt_list = ['lowerarm_twist_01_l_ik', 'lowerarm_twist_02_l_ik']
    for leftLowerT_ik in leftLowerarmT_ikJnt_list:
        lowerarmPB = mc.createNode('pairBlend', n= leftLowerT_ik + '_PB')
        mc.connectAttr('hand_l_ik.rx', lowerarmPB + '.inRotateX2', f=True)
        mc.connectAttr(lowerarmPB + '.outRotateX', leftLowerT_ik + '.rx', f=True)
    mc.setAttr('lowerarm_twist_01_l_ik_PB.weight', 0.4), mc.setAttr('lowerarm_twist_02_l_ik_PB.weight', 0.8)

    ############################# right side ik twist setup
    rightUpperarmT_ikJnt_list = ['upperarm_twist_01_r_ik', 'upperarm_twist_02_r_ik']
    for rightUpperT_ik in rightUpperarmT_ikJnt_list:
        upperarmPB = mc.createNode('pairBlend', n= rightUpperT_ik + '_PB')
        mc.connectAttr('upperarm_r_ik.rx', upperarmPB + '.inRotateX2', f=True)
        mc.connectAttr(upperarmPB + '.outRotateX', rightUpperT_ik + '.rx', f=True)
    mc.setAttr('upperarm_twist_01_r_ik_PB.weight', 0.2), mc.setAttr('upperarm_twist_02_r_ik_PB.weight', 0.8)

    rightLowerarmT_ikJnt_list = ['lowerarm_twist_01_r_ik', 'lowerarm_twist_02_r_ik']
    for rightLowerT_ik in rightLowerarmT_ikJnt_list:
        lowerarmPB = mc.createNode('pairBlend', n= rightLowerT_ik + '_PB')
        mc.connectAttr('hand_r_ik.rx', lowerarmPB + '.inRotateX2', f=True)
        mc.connectAttr(lowerarmPB + '.outRotateX', rightLowerT_ik + '.rx', f=True)
    mc.setAttr('lowerarm_twist_01_r_ik_PB.weight', 0.4), mc.setAttr('lowerarm_twist_02_r_ik_PB.weight', 0.8)


    ########################################################################## pole vector ctrl setup
    PV_arm_loc_list = ['arm_PV_l', 'arm_PV_r']
    for armPV in PV_arm_loc_list:
        myCtrl.cone_ctrl(armPV)

    mc.delete(mc.parentConstraint('arm_PV_l', 'arm_PV_l_ctrlSpaceMaster'))
    mc.delete(mc.parentConstraint('arm_PV_r', 'arm_PV_r_ctrlSpaceMaster'))

    mc.setAttr('arm_PV_l_ctrlSpaceMaster.rx', -90)
    mc.setAttr('arm_PV_r_ctrlSpaceMaster.rx', 270)
    mc.setAttr('arm_PV_r_ctrlSpaceMaster.sx', -1)
    mc.delete('PV_locSpace1', 'PV_locSpace')

    ######################################################################### lock PV attrs
    armPV_ctrl_list = ['arm_PV_l_ctrl', 'arm_PV_r_ctrl']
    for armPV_lockAt in armPV_ctrl_list:
        mc.setAttr(armPV_lockAt + '.rx', l=True, k=False, ch=False)
        mc.setAttr(armPV_lockAt + '.ry', l=True, k=False, ch=False)
        mc.setAttr(armPV_lockAt + '.rz', l=True, k=False, ch=False)
        mc.setAttr(armPV_lockAt + '.sx', l=True, k=False, ch=False)
        mc.setAttr(armPV_lockAt + '.sy', l=True, k=False, ch=False)
        mc.setAttr(armPV_lockAt + '.sz', l=True, k=False, ch=False)
        mc.setAttr(armPV_lockAt + '.v', l=True, k=False, ch=False)

    ################################################################## PV / point / orient constraint
    mc.poleVectorConstraint('arm_PV_l_ctrl', 'ikArm_l', w=1), mc.poleVectorConstraint('arm_PV_r_ctrl', 'ikArm_r', w=1)
    mc.pointConstraint('hand_l_ik_ctrl', 'ikArm_l', mo=True), mc.pointConstraint('hand_r_ik_ctrl', 'ikArm_r', mo=True)
    mc.orientConstraint('hand_l_ik_gimbal_ctrl', 'hand_l_ik', mo=True), mc.orientConstraint('hand_r_ik_gimbal_ctrl', 'hand_r_ik', mo=True)

    ######################################################### IK fingers system ###############################

    ########################## fingers 00
    finger00_list = ['pinky_00_l_ik', 'ring_00_l_ik', 'middle_00_l_ik', 'index_00_l_ik', 'pinky_00_r_ik', 'ring_00_r_ik', 'middle_00_r_ik', 'index_00_r_ik']
    mc.select(finger00_list)
    tranRotScl_const()
    mc.select('ring_00_l_ik_ctrl.cv[0:7]', 'index_00_l_ik_ctrl.cv[0:7]', 'middle_00_l_ik_ctrl.cv[0:7]', 'pinky_00_l_ik_ctrl.cv[0:7]',
              'ring_00_r_ik_ctrl.cv[0:7]', 'index_00_r_ik_ctrl.cv[0:7]', 'middle_00_r_ik_ctrl.cv[0:7]', 'pinky_00_r_ik_ctrl.cv[0:7]')
    mc.scale(1, 1, 0.27, ocp=True), mc.select(d=True)

    ### lock scale att
    finger00_ctrl_list = ['pinky_00_l_ik_ctrl', 'ring_00_l_ik_ctrl', 'middle_00_l_ik_ctrl', 'index_00_l_ik_ctrl', 'pinky_00_r_ik_ctrl', 'ring_00_r_ik_ctrl', 'middle_00_r_ik_ctrl', 'index_00_r_ik_ctrl']
    for f00_ctrl in finger00_ctrl_list:
        mc.setAttr(f00_ctrl + '.sx', l=True, k=False, ch=False)
        mc.setAttr(f00_ctrl + '.sy', l=True, k=False, ch=False)
        mc.setAttr(f00_ctrl + '.sz', l=True, k=False, ch=False)
        mc.setAttr(f00_ctrl + '.v', l=True, k=False, ch=False)
    ########################################################################################################
    #
    #                                      finger IK system setup
    #
    ######################################################################################################

    # delete right fingers to make mirror with correct pole vector on each left finger
    mc.delete('pinky_01_r_ik', 'ring_01_r_ik', 'middle_01_r_ik', 'index_01_r_ik', 'thumb_01_r_ik')

    # un parent left fingers to make mirror finger with correct pole vector position
    mc.parent('pinky_01_l_ik', 'ring_01_l_ik', 'middle_01_l_ik', 'index_01_l_ik', 'thumb_01_l_ik', w=True), mc.select(d=True)

    ########################## pinky l ik setup
    mc.select('pinky_01_l_ik', 'pinky_02_l_ik', 'pinky_03_l_ik')
    fingersPSel = mc.ls(sl=True)

    fingPSel01_IK = mc.xform(fingersPSel[0], q=True, ws=True, t=True)
    fingPSel02_IK = mc.xform(fingersPSel[1], q=True, ws=True, t=True)
    fingPSel03_IK = mc.xform(fingersPSel[2], q=True, ws=True, t=True)

    fingP01_IKV = OpenMaya.MVector(fingPSel01_IK[0], fingPSel01_IK[1], fingPSel01_IK[2])
    fingP02_IKV = OpenMaya.MVector(fingPSel02_IK[0], fingPSel02_IK[1], fingPSel02_IK[2])
    fingP03_IKV = OpenMaya.MVector(fingPSel03_IK[0], fingPSel03_IK[1], fingPSel03_IK[2])

    startEndP = fingP03_IKV - fingP01_IKV
    startMidP = fingP02_IKV - fingP01_IKV

    dotPP = startMidP * startEndP
    projP = float(dotPP) / float(startEndP.length())
    startEndPN = startEndP.normal()
    projPV = startEndPN * projP

    arrowPV = startMidP - projPV
    arrowPV *= 5
    finalPV = arrowPV + fingP02_IKV

    locP_PV = mc.spaceLocator(n='pinky_l_PV')
    locP_PVSpace = mc.group(locP_PV, n='pinky_l_ik_locSpace'), mc.select(d=True)
    mc.xform(locP_PVSpace, ws=True, t=(finalPV.x, finalPV.y, finalPV.z))
    mc.parent(locP_PVSpace, 'pinky_02_l_ik')
    mc.orientConstraint('pinky_02_l_ik', 'pinky_l_ik_locSpace', mo=False)

    mc.mirrorJoint('pinky_01_l_ik', mirrorYZ=True, mirrorBehavior=True, searchReplace=('_l', '_r')), mc.rename('pinky_l_PV1', 'pinky_r_PV')
    mc.parent('pinky_01_r_ik', 'pinky_00_r_ik'), mc.parent('pinky_01_l_ik', 'pinky_00_l_ik')
    mc.orientConstraint('pinky_02_r_ik', 'pinky_l_ik_locSpace1', mo=False), mc.select(d=True)

    ############################################# ring l ik setup
    mc.select('ring_01_l_ik', 'ring_02_l_ik', 'ring_03_l_ik')
    fingersRSel = mc.ls(sl=True)

    fingRSel01_IK = mc.xform(fingersRSel[0], q=True, ws=True, t=True)
    fingRSel02_IK = mc.xform(fingersRSel[1], q=True, ws=True, t=True)
    fingRSel03_IK = mc.xform(fingersRSel[2], q=True, ws=True, t=True)

    fingR01_IKV = OpenMaya.MVector(fingRSel01_IK[0], fingRSel01_IK[1], fingRSel01_IK[2])
    fingR02_IKV = OpenMaya.MVector(fingRSel02_IK[0], fingRSel02_IK[1], fingRSel02_IK[2])
    fingR03_IKV = OpenMaya.MVector(fingRSel03_IK[0], fingRSel03_IK[1], fingRSel03_IK[2])

    startEndR = fingR03_IKV - fingR01_IKV
    startMidR = fingR02_IKV - fingR01_IKV

    dotRR = startMidR * startEndR
    projR = float(dotRR) / float(startEndR.length())
    startEndRN = startEndR.normal()
    projRV = startEndRN * projR

    arrowRV = startMidR - projRV
    arrowRV *= 4
    finalRV = arrowRV + fingR02_IKV

    locR_PV = mc.spaceLocator(n='ring_l_PV')
    locR_PVSpace = mc.group(locR_PV, n='ring_l_ik_locSpace'), mc.select(d=True)
    mc.xform(locR_PVSpace, ws=True, t=(finalRV.x, finalRV.y, finalRV.z))
    mc.parent(locR_PVSpace, 'ring_02_l_ik')
    mc.orientConstraint('ring_02_l_ik', 'ring_l_ik_locSpace', mo=False)

    mc.mirrorJoint('ring_01_l_ik', mirrorYZ=True, mirrorBehavior=True, searchReplace=('_l', '_r')), mc.rename('ring_l_PV1', 'ring_r_PV')
    mc.parent('ring_01_r_ik', 'ring_00_r_ik'), mc.parent('ring_01_l_ik', 'ring_00_l_ik')
    mc.orientConstraint('ring_02_r_ik', 'ring_l_ik_locSpace1', mo=False), mc.select(d=True)

    ###################################################### middle l ik setup
    mc.select('middle_01_l_ik', 'middle_02_l_ik', 'middle_03_l_ik')
    fingersMSel = mc.ls(sl=True)

    fingMSel01_IK = mc.xform(fingersMSel[0], q=True, ws=True, t=True)
    fingMSel02_IK = mc.xform(fingersMSel[1], q=True, ws=True, t=True)
    fingMSel03_IK = mc.xform(fingersMSel[2], q=True, ws=True, t=True)

    fingM01_IKV = OpenMaya.MVector(fingMSel01_IK[0], fingMSel01_IK[1], fingMSel01_IK[2])
    fingM02_IKV = OpenMaya.MVector(fingMSel02_IK[0], fingMSel02_IK[1], fingMSel02_IK[2])
    fingM03_IKV = OpenMaya.MVector(fingMSel03_IK[0], fingMSel03_IK[1], fingMSel03_IK[2])

    startEndM = fingM03_IKV - fingM01_IKV
    startMidM = fingM02_IKV - fingM01_IKV

    dotMP = startMidM * startEndM
    projM = float(dotMP) / float(startEndM.length())
    startEndMN = startEndM.normal()
    projMV = startEndMN * projM

    arrowMV = startMidM - projMV
    arrowMV *= 4
    finalMV = arrowMV + fingM02_IKV

    locM_PV = mc.spaceLocator(n='middle_l_PV')
    locM_PVSpace = mc.group(locM_PV, n='middle_l_ik_locSpace'), mc.select(d=True)
    mc.xform(locM_PVSpace, ws=True, t=(finalMV.x, finalMV.y, finalMV.z))
    mc.parent(locM_PVSpace, 'middle_02_l_ik')
    mc.orientConstraint('middle_02_l_ik', 'middle_l_ik_locSpace', mo=False)

    mc.mirrorJoint('middle_01_l_ik', mirrorYZ=True, mirrorBehavior=True, searchReplace=('_l', '_r')), mc.rename('middle_l_PV1', 'middle_r_PV')
    mc.parent('middle_01_r_ik', 'middle_00_r_ik'), mc.parent('middle_01_l_ik', 'middle_00_l_ik')
    mc.orientConstraint('middle_02_r_ik', 'middle_l_ik_locSpace1', mo=False), mc.select(d=True)

    ############################################################ index l ik setup
    mc.select('index_01_l_ik', 'index_02_l_ik', 'index_03_l_ik')
    fingersISel = mc.ls(sl=True)

    fingISel01_IK = mc.xform(fingersISel[0], q=True, ws=True, t=True)
    fingISel02_IK = mc.xform(fingersISel[1], q=True, ws=True, t=True)
    fingISel03_IK = mc.xform(fingersISel[2], q=True, ws=True, t=True)

    fingI01_IKV = OpenMaya.MVector(fingISel01_IK[0], fingISel01_IK[1], fingISel01_IK[2])
    fingI02_IKV = OpenMaya.MVector(fingISel02_IK[0], fingISel02_IK[1], fingISel02_IK[2])
    fingI03_IKV = OpenMaya.MVector(fingISel03_IK[0], fingISel03_IK[1], fingISel03_IK[2])

    startEndI = fingI03_IKV - fingI01_IKV
    startMidI = fingI02_IKV - fingI01_IKV

    dotIP = startMidI * startEndI
    projI = float(dotIP) / float(startEndI.length())
    startEndIN = startEndI.normal()
    projIV = startEndIN * projI

    arrowIV = startMidI - projIV
    arrowIV *= 8
    finalIV = arrowIV + fingI02_IKV

    locI_PV = mc.spaceLocator(n='index_l_PV')
    locI_PVSpace = mc.group(locI_PV, n='index_l_ik_locSpace'), mc.select(d=True)
    mc.xform(locI_PVSpace, ws=True, t=(finalIV.x, finalIV.y, finalIV.z))
    mc.parent(locI_PVSpace, 'index_02_l_ik')
    mc.orientConstraint('index_02_l_ik', 'index_l_ik_locSpace', mo=False)

    mc.mirrorJoint('index_01_l_ik', mirrorYZ=True, mirrorBehavior=True, searchReplace=('_l', '_r')), mc.rename('index_l_PV1', 'index_r_PV')
    mc.parent('index_01_r_ik', 'index_00_r_ik'), mc.parent('index_01_l_ik', 'index_00_l_ik')
    mc.orientConstraint('index_02_r_ik', 'index_l_ik_locSpace1', mo=False), mc.select(d=True)

    ########################################################## thumb l ik setup
    mc.select('thumb_01_l_ik', 'thumb_02_l_ik', 'thumb_03_l_ik')
    fingersTSel = mc.ls(sl=True)

    fingTSel01_IK = mc.xform(fingersTSel[0], q=True, ws=True, t=True)
    fingTSel02_IK = mc.xform(fingersTSel[1], q=True, ws=True, t=True)
    fingTSel03_IK = mc.xform(fingersTSel[2], q=True, ws=True, t=True)

    fingT01_IKV = OpenMaya.MVector(fingTSel01_IK[0], fingTSel01_IK[1], fingTSel01_IK[2])
    fingT02_IKV = OpenMaya.MVector(fingTSel02_IK[0], fingTSel02_IK[1], fingTSel02_IK[2])
    fingT03_IKV = OpenMaya.MVector(fingTSel03_IK[0], fingTSel03_IK[1], fingTSel03_IK[2])

    startEndT = fingT03_IKV - fingT01_IKV
    startMidT = fingT02_IKV - fingT01_IKV

    dotTP = startMidT * startEndT
    projT = float(dotTP) / float(startEndT.length())
    startEndTN = startEndT.normal()
    projTV = startEndTN * projT

    arrowTV = startMidT - projTV
    arrowTV *= 8
    finalTV = arrowTV + fingT02_IKV

    locT_PV = mc.spaceLocator(n='thumb_l_PV')
    locT_PVSpace = mc.group(locT_PV, n='thumb_l_ik_locSpace'), mc.select(d=True)
    mc.xform(locT_PVSpace, ws=True, t=(finalTV.x, finalTV.y, finalTV.z))
    mc.parent(locT_PVSpace, 'thumb_02_l_ik')
    mc.orientConstraint('thumb_02_l_ik', 'thumb_l_ik_locSpace', mo=False)

    mc.mirrorJoint('thumb_01_l_ik', mirrorYZ=True, mirrorBehavior=True, searchReplace=('_l', '_r')), mc.rename('thumb_l_PV1', 'thumb_r_PV')
    mc.parent('thumb_01_r_ik', 'hand_r_ik'), mc.parent('thumb_01_l_ik', 'hand_l_ik')
    mc.orientConstraint('thumb_02_r_ik', 'thumb_l_ik_locSpace1', mo=False), mc.select(d=True)

    ######################################## fingers IK handle setup - Left side

    ikPinky_l = mc.ikHandle(n='pinky_l_ik', sj='pinky_01_l_ik', ee='pinky_03_l_ik', sol='ikRPsolver')
    ikRing_l = mc.ikHandle(n='ring_l_ik', sj='ring_01_l_ik', ee='ring_03_l_ik', sol='ikRPsolver')
    ikMiddle_l = mc.ikHandle(n='middle_l_ik', sj='middle_01_l_ik', ee='middle_03_l_ik', sol='ikRPsolver')
    ikIndex_l = mc.ikHandle(n='index_l_ik', sj='index_01_l_ik', ee='index_03_l_ik', sol='ikRPsolver')
    ikThumb_l = mc.ikHandle(n='thumb_l_ik', sj='thumb_01_l_ik', ee='thumb_03_l_ik', sol='ikRPsolver')

    ######################################## fingers IK handle setup - Right side

    ikPinky_r = mc.ikHandle(n='pinky_r_ik', sj='pinky_01_r_ik', ee='pinky_03_r_ik', sol='ikRPsolver')
    ikRing_r = mc.ikHandle(n='ring_r_ik', sj='ring_01_r_ik', ee='ring_03_r_ik', sol='ikRPsolver')
    ikMiddle_r = mc.ikHandle(n='middle_r_ik', sj='middle_01_r_ik', ee='middle_03_r_ik', sol='ikRPsolver')
    ikIndex_r = mc.ikHandle(n='index_r_ik', sj='index_01_r_ik', ee='index_03_r_ik', sol='ikRPsolver')
    ikThumb_r = mc.ikHandle(n='thumb_r_ik', sj='thumb_01_r_ik', ee='thumb_03_r_ik', sol='ikRPsolver')

    mc.select(d=True)

    ########################################### fingers ik handle & PV setup - Controls

    fingerIK_list = ['pinky_l_ik', 'ring_l_ik', 'middle_l_ik', 'index_l_ik', 'thumb_l_ik', 'pinky_r_ik', 'ring_r_ik', 'middle_r_ik', 'index_r_ik', 'thumb_r_ik']
    for finIkH in fingerIK_list:
        myCtrl.diamondMid_ctrl(finIkH)

    mc.delete(mc.parentConstraint('pinky_03_l_ik', 'pinky_l_ik_ctrlSpaceMaster', mo=False)), mc.delete(mc.parentConstraint('ring_03_l_ik', 'ring_l_ik_ctrlSpaceMaster', mo=False))
    mc.delete(mc.parentConstraint('middle_03_l_ik', 'middle_l_ik_ctrlSpaceMaster', mo=False)), mc.delete(mc.parentConstraint('index_03_l_ik', 'index_l_ik_ctrlSpaceMaster', mo=False))
    mc.delete(mc.parentConstraint('thumb_03_l_ik', 'thumb_l_ik_ctrlSpaceMaster', mo=False))

    mc.delete(mc.parentConstraint('pinky_03_r_ik', 'pinky_r_ik_ctrlSpaceMaster', mo=False)), mc.delete(mc.parentConstraint('ring_03_r_ik', 'ring_r_ik_ctrlSpaceMaster', mo=False))
    mc.delete(mc.parentConstraint('middle_03_r_ik', 'middle_r_ik_ctrlSpaceMaster', mo=False)), mc.delete(mc.parentConstraint('index_03_r_ik', 'index_r_ik_ctrlSpaceMaster', mo=False))
    mc.delete(mc.parentConstraint('thumb_03_r_ik', 'thumb_r_ik_ctrlSpaceMaster', mo=False))

    fingerPV_list = ['pinky_l_PV', 'ring_l_PV', 'middle_l_PV', 'index_l_PV', 'thumb_l_PV', 'pinky_r_PV', 'ring_r_PV', 'middle_r_PV', 'index_r_PV', 'thumb_r_PV']
    for finPV in fingerPV_list:
        myCtrl.lineCross_ctrl(finPV)

    mc.delete(mc.parentConstraint('pinky_l_PV', 'pinky_l_PV_ctrlSpaceMaster', mo=False)), mc.delete(mc.parentConstraint('ring_l_PV', 'ring_l_PV_ctrlSpaceMaster', mo=False))
    mc.delete(mc.parentConstraint('middle_l_PV', 'middle_l_PV_ctrlSpaceMaster', mo=False)), mc.delete(mc.parentConstraint('index_l_PV', 'index_l_PV_ctrlSpaceMaster', mo=False))
    mc.delete(mc.parentConstraint('thumb_l_PV', 'thumb_l_PV_ctrlSpaceMaster', mo=False))

    mc.delete(mc.parentConstraint('pinky_r_PV', 'pinky_r_PV_ctrlSpaceMaster', mo=False)), mc.delete(mc.parentConstraint('ring_r_PV', 'ring_r_PV_ctrlSpaceMaster', mo=False))
    mc.delete(mc.parentConstraint('middle_r_PV', 'middle_r_PV_ctrlSpaceMaster', mo=False)), mc.delete(mc.parentConstraint('index_r_PV', 'index_r_PV_ctrlSpaceMaster', mo=False))
    mc.delete(mc.parentConstraint('thumb_r_PV', 'thumb_r_PV_ctrlSpaceMaster', mo=False))

    mc.select(d=True)

    ### finger IK scale CV's
    mc.select('pinky_l_ik_ctrl.cv[0:20]', 'ring_l_ik_ctrl.cv[0:20]', 'middle_l_ik_ctrl.cv[0:20]', 'index_l_ik_ctrl.cv[0:20]', 'thumb_l_ik_ctrl.cv[0:20]', 'pinky_r_ik_ctrl.cv[0:20]',
              'ring_r_ik_ctrl.cv[0:20]', 'middle_r_ik_ctrl.cv[0:20]', 'index_r_ik_ctrl.cv[0:20]', 'thumb_r_ik_ctrl.cv[0:20]')
    mc.scale(0.188324, 0.188324, 0.188324, ocp=True), mc.select(d=True)

    mc.select('pinky_l_PV_ctrl.cv[0:7]', 'ring_l_PV_ctrl.cv[0:7]', 'middle_l_PV_ctrl.cv[0:7]', 'index_l_PV_ctrl.cv[0:7]', 'thumb_l_PV_ctrl.cv[0:7]', 'pinky_r_PV_ctrl.cv[0:7]', 'ring_r_PV_ctrl.cv[0:7]',
              'middle_r_PV_ctrl.cv[0:7]', 'index_r_PV_ctrl.cv[0:7]', 'thumb_r_PV_ctrl.cv[0:7]')
    mc.scale(0.156885, 0.156885, 0.156885, ocp=True), mc.select(d=True)

    ### fingers setup - Point / PV constraint
    mc.pointConstraint('pinky_l_ik_ctrl', 'pinky_l_ik', mo=True), mc.pointConstraint('ring_l_ik_ctrl', 'ring_l_ik', mo=True), mc.pointConstraint('middle_l_ik_ctrl', 'middle_l_ik', mo=True)
    mc.pointConstraint('index_l_ik_ctrl', 'index_l_ik', mo=True), mc.pointConstraint('thumb_l_ik_ctrl', 'thumb_l_ik', mo=True)

    mc.pointConstraint('pinky_r_ik_ctrl', 'pinky_r_ik', mo=True), mc.pointConstraint('ring_r_ik_ctrl', 'ring_r_ik', mo=True), mc.pointConstraint('middle_r_ik_ctrl', 'middle_r_ik', mo=True)
    mc.pointConstraint('index_r_ik_ctrl', 'index_r_ik', mo=True), mc.pointConstraint('thumb_r_ik_ctrl', 'thumb_r_ik', mo=True)

    mc.poleVectorConstraint('pinky_l_PV_ctrl', 'pinky_l_ik', w=1), mc.poleVectorConstraint('ring_l_PV_ctrl', 'ring_l_ik', w=1), mc.poleVectorConstraint('middle_l_PV_ctrl', 'middle_l_ik', w=1)
    mc.poleVectorConstraint('index_l_PV_ctrl', 'index_l_ik', w=1), mc.poleVectorConstraint('thumb_l_PV_ctrl', 'thumb_l_ik', w=1)

    mc.poleVectorConstraint('pinky_r_PV_ctrl', 'pinky_r_ik', w=1), mc.poleVectorConstraint('ring_r_PV_ctrl', 'ring_r_ik', w=1), mc.poleVectorConstraint('middle_r_PV_ctrl', 'middle_r_ik', w=1)
    mc.poleVectorConstraint('index_r_PV_ctrl', 'index_r_ik', w=1), mc.poleVectorConstraint('thumb_r_PV_ctrl', 'thumb_r_ik', w=1)

    mc.delete('pinky_l_ik_locSpace', 'ring_l_ik_locSpace', 'middle_l_ik_locSpace', 'index_l_ik_locSpace', 'thumb_l_ik_locSpace', 'pinky_l_ik_locSpace1', 'ring_l_ik_locSpace1', 'middle_l_ik_locSpace1',
              'index_l_ik_locSpace1', 'thumb_l_ik_locSpace1')

    ########################################################### ik fingers control orient constraint

    fingerIK_ctrl_list = ['pinky_l_ik_ctrl', 'ring_l_ik_ctrl', 'middle_l_ik_ctrl', 'index_l_ik_ctrl', 'thumb_l_ik_ctrl', 'pinky_r_ik_ctrl', 'ring_r_ik_ctrl', 'middle_r_ik_ctrl', 'index_r_ik_ctrl', 'thumb_r_ik_ctrl']
    ### finger IK lock scale attrs
    for finIK_ctrl in fingerIK_ctrl_list:
        mc.setAttr(finIK_ctrl + '.sx', l=True, k=False, ch=False)
        mc.setAttr(finIK_ctrl + '.sy', l=True, k=False, ch=False)
        mc.setAttr(finIK_ctrl + '.sz', l=True, k=False, ch=False)
        mc.setAttr(finIK_ctrl + '.v', l=True, k=False, ch=False)

    finger03_ik_list = ['pinky_03_l_ik', 'ring_03_l_ik', 'middle_03_l_ik', 'index_03_l_ik', 'thumb_03_l_ik', 'pinky_03_r_ik', 'ring_03_r_ik', 'middle_03_r_ik', 'index_03_r_ik', 'thumb_03_r_ik']

    for i, item in enumerate(fingerIK_ctrl_list):
        pm.orientConstraint(item, finger03_ik_list[i])

    ###################################################### control colors and cleanup

    ### colors
    leftSideIK_ctrl_list =['pinky_l_ik_ctrl', 'ring_l_ik_ctrl', 'middle_l_ik_ctrl', 'index_l_ik_ctrl', 'thumb_l_ik_ctrl', 'pinky_l_PV_ctrl', 'ring_l_PV_ctrl', 'middle_l_PV_ctrl', 'index_l_PV_ctrl',
                           'thumb_l_PV_ctrl', 'pinky_00_l_ik_ctrl', 'ring_00_l_ik_ctrl', 'middle_00_l_ik_ctrl', 'index_00_l_ik_ctrl', 'hand_l_ik_ctrl', 'hand_l_ik_gimbal_ctrl', 'arm_PV_l_ctrl']
    for lIK_ctrl in leftSideIK_ctrl_list:
        itemColor(lIK_ctrl, 6)

    rightSideIK_ctrl_list =['pinky_r_ik_ctrl', 'ring_r_ik_ctrl', 'middle_r_ik_ctrl', 'index_r_ik_ctrl', 'thumb_r_ik_ctrl', 'pinky_r_PV_ctrl', 'ring_r_PV_ctrl', 'middle_r_PV_ctrl', 'index_r_PV_ctrl',
                           'thumb_r_PV_ctrl', 'pinky_00_r_ik_ctrl', 'ring_00_r_ik_ctrl', 'middle_00_r_ik_ctrl', 'index_00_r_ik_ctrl', 'hand_r_ik_ctrl', 'hand_r_ik_gimbal_ctrl', 'arm_PV_r_ctrl']
    for rIK_ctrl in rightSideIK_ctrl_list:
        itemColor(rIK_ctrl, 13)

    ######################### cleanup
    #### ik's
    ikHandle_arm_grp = mc.group(em=True, n= 'ikHandle_arms_grp')
    ikHandle_arm_list = ['ikArm_l', 'ikArm_r', 'pinky_l_ik', 'ring_l_ik', 'middle_l_ik', 'index_l_ik', 'thumb_l_ik', 'pinky_r_ik', 'ring_r_ik', 'middle_r_ik', 'index_r_ik', 'thumb_r_ik']
    mc.parent(ikHandle_arm_list, ikHandle_arm_grp), mc.select(d=True)
    mc.setAttr(ikHandle_arm_grp + '.v', 0)

    ### left ik controls
    leftIKFinger_ctrlMaster_list = ['pinky_00_l_ik_ctrlSpaceMaster', 'ring_00_l_ik_ctrlSpaceMaster', 'middle_00_l_ik_ctrlSpaceMaster', 'index_00_l_ik_ctrlSpaceMaster', 'pinky_00_r_ik_ctrlSpaceMaster',
                                    'pinky_l_ik_ctrlSpaceMaster', 'ring_l_ik_ctrlSpaceMaster', 'middle_l_ik_ctrlSpaceMaster', 'index_l_ik_ctrlSpaceMaster', 'thumb_l_ik_ctrlSpaceMaster',
                                    'pinky_l_PV_ctrlSpaceMaster', 'ring_l_PV_ctrlSpaceMaster', 'middle_l_PV_ctrlSpaceMaster', 'index_l_PV_ctrlSpaceMaster', 'thumb_l_PV_ctrlSpaceMaster']
    left_fingerIK_ctrl_grp = mc.group(em=True, n= 'left_finger_ik_ctrl_grp')
    mc.parent(leftIKFinger_ctrlMaster_list, left_fingerIK_ctrl_grp)

    ### parent ik / PV fionger to phalange 00 -> just for presentation -> need think the best rig via
    mc.parent('pinky_l_ik_ctrlSpaceMaster', 'pinky_l_PV_ctrlSpaceMaster', 'pinky_00_l_ik_ctrl'), mc.parent('ring_l_ik_ctrlSpaceMaster', 'ring_l_PV_ctrlSpaceMaster', 'ring_00_l_ik_ctrl')
    mc.parent('middle_l_ik_ctrlSpaceMaster', 'middle_l_PV_ctrlSpaceMaster', 'middle_00_l_ik_ctrl'), mc.parent('index_l_ik_ctrlSpaceMaster', 'index_l_PV_ctrlSpaceMaster', 'index_00_l_ik_ctrl'), mc.select(d=True)

    ### right ik controls
    rightIKFinger_ctrlMaster_list = ['pinky_00_r_ik_ctrlSpaceMaster', 'ring_00_r_ik_ctrlSpaceMaster', 'middle_00_r_ik_ctrlSpaceMaster', 'index_00_r_ik_ctrlSpaceMaster', 'pinky_00_r_ik_ctrlSpaceMaster',
                                    'pinky_r_ik_ctrlSpaceMaster', 'ring_r_ik_ctrlSpaceMaster', 'middle_r_ik_ctrlSpaceMaster', 'index_r_ik_ctrlSpaceMaster', 'thumb_r_ik_ctrlSpaceMaster',
                                    'pinky_r_PV_ctrlSpaceMaster', 'ring_r_PV_ctrlSpaceMaster', 'middle_r_PV_ctrlSpaceMaster', 'index_r_PV_ctrlSpaceMaster', 'thumb_r_PV_ctrlSpaceMaster']
    right_fingerIK_ctrl_grp = mc.group(em=True, n= 'right_finger_ik_ctrl_grp')
    mc.parent(rightIKFinger_ctrlMaster_list, right_fingerIK_ctrl_grp), mc.select(d=True)

    mc.parent(left_fingerIK_ctrl_grp, 'hand_l_ik_gimbal_ctrl'), mc.parent(right_fingerIK_ctrl_grp, 'hand_r_ik_gimbal_ctrl'), mc.select(d=True)

    ### parent ik / PV fionger to phalange 00 -> just for presentation -> need think the best rig via
    mc.parent('pinky_r_ik_ctrlSpaceMaster', 'pinky_r_PV_ctrlSpaceMaster', 'pinky_00_r_ik_ctrl'), mc.parent('ring_r_ik_ctrlSpaceMaster', 'ring_r_PV_ctrlSpaceMaster', 'ring_00_r_ik_ctrl')
    mc.parent('middle_r_ik_ctrlSpaceMaster', 'middle_r_PV_ctrlSpaceMaster', 'middle_00_r_ik_ctrl'), mc.parent('index_r_ik_ctrlSpaceMaster', 'index_r_PV_ctrlSpaceMaster', 'index_00_r_ik_ctrl'), mc.select(d=True)

    ### arm master group
    ik_arm_grp = mc.group(em=True, n='arms_ik_grp')
    mc.parent(ikHandle_arm_grp, 'arm_PV_r_ctrlSpaceMaster', 'arm_PV_l_ctrlSpaceMaster', 'hand_r_ik_ctrlSpaceMaster', 'hand_l_ik_ctrlSpaceMaster', ik_arm_grp), mc.select(d=True)
