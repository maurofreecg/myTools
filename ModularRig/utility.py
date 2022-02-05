#######################################################################
#
#
#                            UTILITIES
#
#
#######################################################################

import maya.cmds as mc
import maya.mel as mel
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
def neck_FK_transform():
    neckHead_jnt_list = ['neck', 'head']

    for neckHead in (neckHead_jnt_list):
        mc.makeIdentity(neckHead, apply=True, t=True, r=True, s=True)
        mc.select(d=True)

    mc.select(neckHead_jnt_list)
    tranRotScl_const()
    itemColor('neck_ctrl', 17)
    mc.parent('head_masterCtrlSpace', 'neck_ctrl')
    neckCtrl = mc.group(n= 'neck_controls', em=True)
    mc.parent('neck_masterCtrlSpace', neckCtrl)

    ### neck twist
    neckTwist = mc.joint('neck', n= 'neck_twist', rad=2)
    mc.delete(mc.pointConstraint('neck', 'head', neckTwist, mo=False))
    neck_PB = mc.createNode('pairBlend', n= 'neck_twist_PB')
    mc.setAttr(neck_PB + '.weight', 0.5)
    mc.connectAttr('head_ctrl.rotateX', neck_PB + '.inRotateX2')
    mc.connectAttr(neck_PB + '.outRotateX', neckTwist + '.rx')

    mc.select(d=True)

################################################## spine FK transform ################################################################
def spine_FK_transfomr():
    spine_jnt_list = ['pelvis', 'spine_01', 'spine_02', 'spine_03']

    for spine_jnt in (spine_jnt_list):
        mc.makeIdentity(spine_jnt, apply=True, t=True, r=True, s=True)
        mc.select(d=True)

    mc.select(spine_jnt_list)
    tranRotScl_const()
    mc.parent('spine_03_masterCtrlSpace', 'spine_02_ctrl'), mc.parent('spine_02_masterCtrlSpace', 'spine_01_ctrl')
    mc.parent('spine_01_masterCtrlSpace', 'pelvis_ctrl')
    itemColor('pelvis_ctrl', 17)
    spineCtrlGrp = mc.group(n = 'spine_controls', em=True)
    mc.parent('pelvis_masterCtrlSpace', spineCtrlGrp)

    mc.select(d=True)

################################################# arm finger FK transform ######################################################
def arm_fingers_FK_transform():

    arm_fingers_l_jnt_list = ['clavicle_l', 'upperarm_l', 'lowerarm_l', 'hand_l', 'pinky_00_l', 'pinky_01_l', 'pinky_02_l', 'pinky_03_l',
                              'ring_00_l', 'ring_01_l', 'ring_02_l', 'ring_03_l', 'middle_00_l', 'middle_01_l', 'middle_02_l', 'middle_03_l',
                              'index_00_l', 'index_01_l', 'index_02_l', 'index_03_l', 'thumb_01_l', 'thumb_02_l', 'thumb_03_l']

    for arm_fingers_jnt in (arm_fingers_l_jnt_list):
         mc.makeIdentity(arm_fingers_jnt, apply=True, t=True, r=True, s=True)
         mc.select(d=True)

    ### twist arm
    upperarmTwist_01_l = mc.joint('upperarm_l', n='upperarm_twist_01_l', rad=2)
    upperarmTConst_01_l = mc.pointConstraint('upperarm_l', 'lowerarm_l', upperarmTwist_01_l ,mo=False), mc.setAttr('upperarm_twist_01_l_pointConstraint1.upperarm_lW0', 2)
    upperarmTwist_02_l = mc.joint('upperarm_l', n='upperarm_twist_02_l', rad=2)
    upperarmTConst_02_l = mc.pointConstraint('upperarm_l', 'lowerarm_l', upperarmTwist_02_l ,mo=False), mc.setAttr('upperarm_twist_02_l_pointConstraint1.lowerarm_lW1', 2)
    mc.delete('upperarm_twist_01_l_pointConstraint1', 'upperarm_twist_02_l_pointConstraint1')

    lowerarmTwist_01_l = mc.joint('lowerarm_l', n='lowerarm_twist_01_l', rad=2)
    lowerarmTConst_01_l = mc.pointConstraint('lowerarm_l', 'hand_l', lowerarmTwist_01_l ,mo=False), mc.setAttr('lowerarm_twist_01_l_pointConstraint1.lowerarm_lW0', 1.5)
    lowerarmTwist_02_l = mc.joint('lowerarm_l', n='lowerarm_twist_02_l', rad=2)
    lowerarmTConst_02_l = mc.pointConstraint('lowerarm_l', 'hand_l', lowerarmTwist_02_l ,mo=False), mc.setAttr('lowerarm_twist_02_l_pointConstraint1.hand_lW1', 3)
    mc.delete('lowerarm_twist_01_l_pointConstraint1', 'lowerarm_twist_02_l_pointConstraint1')
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
    mc.parent('upperarm_l_masterCtrlSpace', 'clavicle_l_ctrl'), mc.parent('lowerarm_l_masterCtrlSpace', 'upperarm_l_ctrl'), mc.parent('hand_l_masterCtrlSpace', 'lowerarm_l_ctrl')
    mc.parent('pinky_03_l_masterCtrlSpace', 'pinky_02_l_ctrl'), mc.parent('pinky_02_l_masterCtrlSpace', 'pinky_01_l_ctrl'), mc.parent('pinky_01_l_masterCtrlSpace', 'pinky_00_l_ctrl')
    mc.parent('ring_03_l_masterCtrlSpace', 'ring_02_l_ctrl'), mc.parent('ring_02_l_masterCtrlSpace', 'ring_01_l_ctrl'), mc.parent('ring_01_l_masterCtrlSpace', 'ring_00_l_ctrl')
    mc.parent('middle_03_l_masterCtrlSpace', 'middle_02_l_ctrl'), mc.parent('middle_02_l_masterCtrlSpace', 'middle_01_l_ctrl'), mc.parent('middle_01_l_masterCtrlSpace', 'middle_00_l_ctrl')
    mc.parent('index_03_l_masterCtrlSpace', 'index_02_l_ctrl'), mc.parent('index_02_l_masterCtrlSpace', 'index_01_l_ctrl'), mc.parent('index_01_l_masterCtrlSpace', 'index_00_l_ctrl')
    mc.parent('thumb_03_l_masterCtrlSpace', 'thumb_02_l_ctrl'), mc.parent('thumb_02_l_masterCtrlSpace', 'thumb_01_l_ctrl')
    mc.parent('pinky_00_l_masterCtrlSpace', 'ring_00_l_masterCtrlSpace', 'middle_00_l_masterCtrlSpace', 'index_00_l_masterCtrlSpace', 'thumb_01_l_masterCtrlSpace', 'hand_l_ctrl')

    mc.parent('upperarm_r_masterCtrlSpace', 'clavicle_r_ctrl'), mc.parent('lowerarm_r_masterCtrlSpace', 'upperarm_r_ctrl'), mc.parent('hand_r_masterCtrlSpace', 'lowerarm_r_ctrl')
    mc.parent('pinky_03_r_masterCtrlSpace', 'pinky_02_r_ctrl'), mc.parent('pinky_02_r_masterCtrlSpace', 'pinky_01_r_ctrl'), mc.parent('pinky_01_r_masterCtrlSpace', 'pinky_00_r_ctrl')
    mc.parent('ring_03_r_masterCtrlSpace', 'ring_02_r_ctrl'), mc.parent('ring_02_r_masterCtrlSpace', 'ring_01_r_ctrl'), mc.parent('ring_01_r_masterCtrlSpace', 'ring_00_r_ctrl')
    mc.parent('middle_03_r_masterCtrlSpace', 'middle_02_r_ctrl'), mc.parent('middle_02_r_masterCtrlSpace', 'middle_01_r_ctrl'), mc.parent('middle_01_r_masterCtrlSpace', 'middle_00_r_ctrl')
    mc.parent('index_03_r_masterCtrlSpace', 'index_02_r_ctrl'), mc.parent('index_02_r_masterCtrlSpace', 'index_01_r_ctrl'), mc.parent('index_01_r_masterCtrlSpace', 'index_00_r_ctrl')
    mc.parent('thumb_03_r_masterCtrlSpace', 'thumb_02_r_ctrl'), mc.parent('thumb_02_r_masterCtrlSpace', 'thumb_01_r_ctrl')
    mc.parent('pinky_00_r_masterCtrlSpace', 'ring_00_r_masterCtrlSpace', 'middle_00_r_masterCtrlSpace', 'index_00_r_masterCtrlSpace', 'thumb_01_r_masterCtrlSpace', 'hand_r_ctrl')

    armsGrp = mc.group(n = 'arms_ctrls', em=True)
    mc.parent('clavicle_r_masterCtrlSpace', 'clavicle_l_masterCtrlSpace', armsGrp), mc.select(d=True)

    ######################## twist l_transform
    upperarmTwist_l_jnt_list = ['upperarm_twist_01_l', 'upperarm_twist_02_l', 'lowerarm_twist_01_l', 'lowerarm_twist_02_l']
    mc.select(upperarmTwist_l_jnt_list)
    tranRotScl_const()

    upperarmTwist_l_ctrl_list = ['upperarm_twist_01_l_ctrl', 'upperarm_twist_02_l_ctrl', 'lowerarm_twist_01_l_ctrl', 'lowerarm_twist_02_l_ctrl']
    upperarmTwist_l_masterGrp_list = ['upperarm_twist_01_l_masterCtrlSpace', 'upperarm_twist_02_l_masterCtrlSpace']
    lowerarmTwist_l_masterGrp_list = ['lowerarm_twist_01_l_masterCtrlSpace', 'lowerarm_twist_02_l_masterCtrlSpace']
    mc.parent(upperarmTwist_l_masterGrp_list, 'upperarm_l_ctrl'), mc.parent(lowerarmTwist_l_masterGrp_list, 'lowerarm_l_ctrl')
    mc.select(d=True)

    mc.disconnectAttr('upperarm_l_ctrl.rx', 'upperarm_l.rx')
    mc.disconnectAttr('upperarm_twist_01_l_ctrl.rx', 'upperarm_twist_01_l.rx')
    mc.disconnectAttr('upperarm_twist_02_l_ctrl.rx', 'upperarm_twist_02_l.rx')
    mc.disconnectAttr('lowerarm_twist_01_l_ctrl.rx', 'lowerarm_twist_01_l.rx')
    mc.disconnectAttr('lowerarm_twist_02_l_ctrl.rx', 'lowerarm_twist_02_l.rx')

    #### armTwist PB connection
    mc.select(upperarmTwist_l_jnt_list)

    upperarmT_l_01_PB = mc.createNode('pairBlend', n= 'upperarm_twist_01_l_PB')
    mc.setAttr(upperarmT_l_01_PB + '.weight', 0.2)
    mc.connectAttr('upperarm_l_ctrl.rx', upperarmT_l_01_PB + '.inRotateX2')
    mc.connectAttr(upperarmT_l_01_PB + '.outRotateX', 'upperarm_twist_01_l.rx', f=True)

    upperarmT_l_02_PB = mc.createNode('pairBlend', n= 'upperarm_twist_02_l_PB')
    mc.setAttr(upperarmT_l_02_PB + '.weight', 0.8)
    mc.connectAttr('upperarm_l_ctrl.rx', upperarmT_l_02_PB + '.inRotateX2')
    mc.connectAttr(upperarmT_l_02_PB + '.outRotateX', 'upperarm_twist_02_l.rx', f=True)

    lowerarmT_l_01_PB = mc.createNode('pairBlend', n= 'lowerarm_twist_01_l_PB')
    mc.setAttr(lowerarmT_l_01_PB + '.weight', 0.4)
    mc.connectAttr('hand_l_ctrl.rx', lowerarmT_l_01_PB + '.inRotateX2')
    mc.connectAttr(lowerarmT_l_01_PB + '.outRotateX', 'lowerarm_twist_01_l.rx', f=True)

    lowerarmT_l_02_PB = mc.createNode('pairBlend', n= 'lowerarm_twist_02_l_PB')
    mc.setAttr(lowerarmT_l_02_PB + '.weight', 0.8)
    mc.connectAttr('hand_l_ctrl.rx', lowerarmT_l_02_PB + '.inRotateX2')
    mc.connectAttr(lowerarmT_l_02_PB + '.outRotateX', 'lowerarm_twist_02_l.rx', f=True)

    ######################## twist r_transform
    upperarmTwist_r_jnt_list = ['upperarm_twist_01_r', 'upperarm_twist_02_r', 'lowerarm_twist_01_r', 'lowerarm_twist_02_r']
    mc.select(upperarmTwist_r_jnt_list)
    tranRotScl_const()

    upperarmTwist_r_ctrl_list = ['upperarm_twist_01_r_ctrl', 'upperarm_twist_02_r_ctrl', 'lowerarm_twist_01_r_ctrl', 'lowerarm_twist_02_r_ctrl']
    upperarmTwist_r_masterGrp_list = ['upperarm_twist_01_r_masterCtrlSpace', 'upperarm_twist_02_r_masterCtrlSpace']
    lowerarmTwist_r_masterGrp_list = ['lowerarm_twist_01_r_masterCtrlSpace', 'lowerarm_twist_02_r_masterCtrlSpace']
    mc.parent(upperarmTwist_r_masterGrp_list, 'upperarm_r_ctrl'), mc.parent(lowerarmTwist_r_masterGrp_list, 'lowerarm_r_ctrl')
    mc.select(d=True)

    mc.disconnectAttr('upperarm_r_ctrl.rx', 'upperarm_r.rx')
    mc.disconnectAttr('upperarm_twist_01_r_ctrl.rx', 'upperarm_twist_01_r.rx')
    mc.disconnectAttr('upperarm_twist_02_r_ctrl.rx', 'upperarm_twist_02_r.rx')
    mc.disconnectAttr('lowerarm_twist_01_r_ctrl.rx', 'lowerarm_twist_01_r.rx')
    mc.disconnectAttr('lowerarm_twist_02_r_ctrl.rx', 'lowerarm_twist_02_r.rx')

    #### armTwist PB connection
    mc.select(upperarmTwist_r_jnt_list)

    upperarmT_r_01_PB = mc.createNode('pairBlend', n= 'upperarm_twist_01_r_PB')
    mc.setAttr(upperarmT_r_01_PB + '.weight', 0.2)
    mc.connectAttr('upperarm_r_ctrl.rx', upperarmT_r_01_PB + '.inRotateX2')
    mc.connectAttr(upperarmT_r_01_PB + '.outRotateX', 'upperarm_twist_01_r.rx', f=True)

    upperarmT_r_02_PB = mc.createNode('pairBlend', n= 'upperarm_twist_02_r_PB')
    mc.setAttr(upperarmT_r_02_PB + '.weight', 0.8)
    mc.connectAttr('upperarm_r_ctrl.rx', upperarmT_r_02_PB + '.inRotateX2')
    mc.connectAttr(upperarmT_r_02_PB + '.outRotateX', 'upperarm_twist_02_r.rx', f=True)

    lowerarmT_r_01_PB = mc.createNode('pairBlend', n= 'lowerarm_twist_01_r_PB')
    mc.setAttr(lowerarmT_r_01_PB + '.weight', 0.4)
    mc.connectAttr('hand_r_ctrl.rx', lowerarmT_r_01_PB + '.inRotateX2')
    mc.connectAttr(lowerarmT_r_01_PB + '.outRotateX', 'lowerarm_twist_01_r.rx', f=True)

    lowerarmT_r_02_PB = mc.createNode('pairBlend', n= 'lowerarm_twist_02_r_PB')
    mc.setAttr(lowerarmT_r_02_PB + '.weight', 0.8)
    mc.connectAttr('hand_r_ctrl.rx', lowerarmT_r_02_PB + '.inRotateX2')
    mc.connectAttr(lowerarmT_r_02_PB + '.outRotateX', 'lowerarm_twist_02_r.rx', f=True)

    mc.select(d=True)

##################################################### leg FK transform ##############################################################
def leg_FK_Transform():

    leg_l_jnt_list = ['thigh_l', 'calf_l', 'foot_l', 'ball_l', 'toe_l']

    for leg_l_jnt in (leg_l_jnt_list):
        mc.makeIdentity(leg_l_jnt, apply=True, t=True, r=True, s=True)
        mc.select(d=True)

    ### twist leg
    thighTwist_01_l = mc.joint('thigh_l', n='thigh_twist_01_l', rad=2)
    thighTConst_01_l = mc.pointConstraint('thigh_l', 'calf_l', thighTwist_01_l ,mo=False), mc.setAttr('thigh_twist_01_l_pointConstraint1.thigh_lW0', 2)
    thighTwist_02_l = mc.joint('thigh_l', n='thigh_twist_02_l', rad=2)
    thighTConst_02_l = mc.pointConstraint('thigh_l', 'calf_l', thighTwist_02_l ,mo=False), mc.setAttr('thigh_twist_02_l_pointConstraint1.calf_lW1', 2)
    mc.delete('thigh_twist_01_l_pointConstraint1', 'thigh_twist_02_l_pointConstraint1')

    calfTwist_01_l = mc.joint('calf_l', n='calf_twist_01_l', rad=2)
    calfTConst_01_l = mc.pointConstraint('calf_l', 'foot_l', calfTwist_01_l ,mo=False), mc.setAttr('calf_twist_01_l_pointConstraint1.calf_lW0', 2)
    calfTwist_02_l = mc.joint('calf_l', n='calf_twist_02_l', rad=2)
    calfTConst_02_l = mc.pointConstraint('calf_l', 'foot_l', calfTwist_02_l ,mo=False), mc.setAttr('calf_twist_02_l_pointConstraint1.foot_lW1', 2)
    mc.delete('calf_twist_01_l_pointConstraint1', 'calf_twist_02_l_pointConstraint1')
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

    mc.parent('toe_l_masterCtrlSpace', 'ball_l_ctrl'), mc.parent('ball_l_masterCtrlSpace', 'foot_l_ctrl'), mc.parent('foot_l_masterCtrlSpace', 'calf_l_ctrl'), mc.parent('calf_l_masterCtrlSpace', 'thigh_l_ctrl')
    mc.parent('toe_r_masterCtrlSpace', 'ball_r_ctrl'), mc.parent('ball_r_masterCtrlSpace', 'foot_r_ctrl'), mc.parent('foot_r_masterCtrlSpace', 'calf_r_ctrl'), mc.parent('calf_r_masterCtrlSpace', 'thigh_r_ctrl')
    legGrp = mc.group(n= 'leg_controls', em=True)
    mc.parent('thigh_r_masterCtrlSpace', 'thigh_l_masterCtrlSpace', legGrp), mc.select(d=True)

    ######################## twist l_transform
    legTwist_l_jnt_list = ['thigh_twist_01_l', 'thigh_twist_02_l', 'calf_twist_01_l', 'calf_twist_02_l']
    mc.select(legTwist_l_jnt_list)
    tranRotScl_const()

    thighTwist_l_ctrl_list = ['thigh_twist_01_l_ctrl', 'thigh_twist_02_l_ctrl', 'calf_twist_01_l_ctrl', 'calf_twist_02_l_ctrl']
    thighTwist_l_masterGrp_list = ['thigh_twist_01_l_masterCtrlSpace', 'thigh_twist_02_l_masterCtrlSpace']
    calfTwist_l_masterGrp_list = ['calf_twist_01_l_masterCtrlSpace', 'calf_twist_02_l_masterCtrlSpace']
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

    thighTwist_r_ctrl_rist = ['thigh_twist_01_r_ctrl', 'thigh_twist_02_r_ctrl', 'calf_twist_01_r_ctrl', 'calf_twist_02_r_ctrl']
    thighTwist_r_masterGrp_rist = ['thigh_twist_01_r_masterCtrlSpace', 'thigh_twist_02_r_masterCtrlSpace']
    calfTwist_r_masterGrp_rist = ['calf_twist_01_r_masterCtrlSpace', 'calf_twist_02_r_masterCtrlSpace']
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

##################################################### biped FK transform #########################################################

def biped_FK_transform():

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
    mc.parent('spine_03_masterCtrlSpace', 'spine_02_ctrl'), mc.parent('spine_02_masterCtrlSpace', 'spine_01_ctrl')
    mc.parent('spine_01_masterCtrlSpace', 'pelvis_ctrl')
    itemColor('pelvis_ctrl', 17)
    spineGrp = mc.group(n='spine_controls', em=True)
    mc.parent('pelvis_masterCtrlSpace', spineGrp)

    mc.select(d=True)

    ################################################################## neck FK

    mc.select(neckHead_jnt_list)
    tranRotScl_const()
    itemColor('neck_ctrl', 17)
    mc.parent('head_masterCtrlSpace', 'neck_ctrl')
    neckHeadGrp = mc.group(n= 'neck_controls', em=True)
    mc.parent('neck_masterCtrlSpace', neckHeadGrp)

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
    mc.parent('upperarm_l_masterCtrlSpace', 'clavicle_l_ctrl'), mc.parent('lowerarm_l_masterCtrlSpace','upperarm_l_ctrl'), mc.parent('hand_l_masterCtrlSpace', 'lowerarm_l_ctrl')
    mc.parent('pinky_03_l_masterCtrlSpace', 'pinky_02_l_ctrl'), mc.parent('pinky_02_l_masterCtrlSpace','pinky_01_l_ctrl'), mc.parent('pinky_01_l_masterCtrlSpace', 'pinky_00_l_ctrl')
    mc.parent('ring_03_l_masterCtrlSpace', 'ring_02_l_ctrl'), mc.parent('ring_02_l_masterCtrlSpace','ring_01_l_ctrl'), mc.parent('ring_01_l_masterCtrlSpace', 'ring_00_l_ctrl')
    mc.parent('middle_03_l_masterCtrlSpace', 'middle_02_l_ctrl'), mc.parent('middle_02_l_masterCtrlSpace','middle_01_l_ctrl'), mc.parent('middle_01_l_masterCtrlSpace', 'middle_00_l_ctrl')
    mc.parent('index_03_l_masterCtrlSpace', 'index_02_l_ctrl'), mc.parent('index_02_l_masterCtrlSpace','index_01_l_ctrl'), mc.parent('index_01_l_masterCtrlSpace', 'index_00_l_ctrl')
    mc.parent('thumb_03_l_masterCtrlSpace', 'thumb_02_l_ctrl'), mc.parent('thumb_02_l_masterCtrlSpace', 'thumb_01_l_ctrl')
    mc.parent('pinky_00_l_masterCtrlSpace', 'ring_00_l_masterCtrlSpace', 'middle_00_l_masterCtrlSpace', 'index_00_l_masterCtrlSpace', 'thumb_01_l_masterCtrlSpace', 'hand_l_ctrl')

    mc.parent('upperarm_r_masterCtrlSpace', 'clavicle_r_ctrl'), mc.parent('lowerarm_r_masterCtrlSpace','upperarm_r_ctrl'), mc.parent('hand_r_masterCtrlSpace', 'lowerarm_r_ctrl')
    mc.parent('pinky_03_r_masterCtrlSpace', 'pinky_02_r_ctrl'), mc.parent('pinky_02_r_masterCtrlSpace','pinky_01_r_ctrl'), mc.parent('pinky_01_r_masterCtrlSpace', 'pinky_00_r_ctrl')
    mc.parent('ring_03_r_masterCtrlSpace', 'ring_02_r_ctrl'), mc.parent('ring_02_r_masterCtrlSpace','ring_01_r_ctrl'), mc.parent('ring_01_r_masterCtrlSpace', 'ring_00_r_ctrl')
    mc.parent('middle_03_r_masterCtrlSpace', 'middle_02_r_ctrl'), mc.parent('middle_02_r_masterCtrlSpace','middle_01_r_ctrl'), mc.parent('middle_01_r_masterCtrlSpace', 'middle_00_r_ctrl')
    mc.parent('index_03_r_masterCtrlSpace', 'index_02_r_ctrl'), mc.parent('index_02_r_masterCtrlSpace','index_01_r_ctrl'), mc.parent('index_01_r_masterCtrlSpace', 'index_00_r_ctrl')
    mc.parent('thumb_03_r_masterCtrlSpace', 'thumb_02_r_ctrl'), mc.parent('thumb_02_r_masterCtrlSpace', 'thumb_01_r_ctrl')
    mc.parent('pinky_00_r_masterCtrlSpace', 'ring_00_r_masterCtrlSpace', 'middle_00_r_masterCtrlSpace','index_00_r_masterCtrlSpace', 'thumb_01_r_masterCtrlSpace', 'hand_r_ctrl')

    armsGrp = mc.group(n='arms_ctrls', em=True)
    mc.parent('clavicle_r_masterCtrlSpace', 'clavicle_l_masterCtrlSpace', armsGrp), mc.select(d=True)

    ######################## twist l_transform
    upperarmTwist_l_jnt_list = ['upperarm_twist_01_l', 'upperarm_twist_02_l', 'lowerarm_twist_01_l', 'lowerarm_twist_02_l']
    mc.select(upperarmTwist_l_jnt_list)
    tranRotScl_const()

    upperarmTwist_l_ctrl_list = ['upperarm_twist_01_l_ctrl', 'upperarm_twist_02_l_ctrl', 'lowerarm_twist_01_l_ctrl','lowerarm_twist_02_l_ctrl']
    upperarmTwist_l_masterGrp_list = ['upperarm_twist_01_l_masterCtrlSpace', 'upperarm_twist_02_l_masterCtrlSpace']
    lowerarmTwist_l_masterGrp_list = ['lowerarm_twist_01_l_masterCtrlSpace', 'lowerarm_twist_02_l_masterCtrlSpace']
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
    upperarmTwist_r_masterGrp_list = ['upperarm_twist_01_r_masterCtrlSpace', 'upperarm_twist_02_r_masterCtrlSpace']
    lowerarmTwist_r_masterGrp_list = ['lowerarm_twist_01_r_masterCtrlSpace', 'lowerarm_twist_02_r_masterCtrlSpace']
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

    mc.parent('toe_l_masterCtrlSpace', 'ball_l_ctrl'), mc.parent('ball_l_masterCtrlSpace', 'foot_l_ctrl'), mc.parent('foot_l_masterCtrlSpace', 'calf_l_ctrl'), mc.parent('calf_l_masterCtrlSpace', 'thigh_l_ctrl')
    mc.parent('toe_r_masterCtrlSpace', 'ball_r_ctrl'), mc.parent('ball_r_masterCtrlSpace', 'foot_r_ctrl'), mc.parent('foot_r_masterCtrlSpace', 'calf_r_ctrl'), mc.parent('calf_r_masterCtrlSpace', 'thigh_r_ctrl')
    legGrp = mc.group(n='leg_controls', em=True)
    mc.parent('thigh_r_masterCtrlSpace', 'thigh_l_masterCtrlSpace', legGrp), mc.select(d=True)

    ######################## twist l_transform
    legTwist_l_jnt_list = ['thigh_twist_01_l', 'thigh_twist_02_l', 'calf_twist_01_l', 'calf_twist_02_l']
    mc.select(legTwist_l_jnt_list)
    tranRotScl_const()

    thighTwist_l_ctrl_list = ['thigh_twist_01_l_ctrl', 'thigh_twist_02_l_ctrl', 'calf_twist_01_l_ctrl','calf_twist_02_l_ctrl']
    thighTwist_l_masterGrp_list = ['thigh_twist_01_l_masterCtrlSpace', 'thigh_twist_02_l_masterCtrlSpace']
    calfTwist_l_masterGrp_list = ['calf_twist_01_l_masterCtrlSpace', 'calf_twist_02_l_masterCtrlSpace']
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
    thighTwist_r_masterGrp_rist = ['thigh_twist_01_r_masterCtrlSpace', 'thigh_twist_02_r_masterCtrlSpace']
    calfTwist_r_masterGrp_rist = ['calf_twist_01_r_masterCtrlSpace', 'calf_twist_02_r_masterCtrlSpace']
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

#######################################################################
#
#
#                           IK System
#
#
#######################################################################

######################################################### spine IK transform #############################################################

def spine_IK_transform():
    # create an ikSpline solver using the 'Spine' joint through to 'Spine2'...
    # ... Adjust Advanced Twist Controls of the ikSpline based off Advanced Skeleton Setup ...
    # ...then create a cluster on cv 0, cv 1&2, and cv3
    mc.ikHandle(n='spine_ik', sj='pelvis', ee='spine_03', sol='ikSplineSolver')

    spine_jnt_list = ['pelvis', 'spine_01', 'spine_02', 'spine_03']

    cv_list = ['curve1.cv[0]', 'curve1.cv[1:2]', 'curve1.cv[3]']
    for each in cv_list:
        mc.cluster(each)
    mc.select(d=True)

    # for each cluster rename it, create a control and snap it to its location then delete the Pcon
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

######################################################### arm IK transform ################################################################

################################# call arm templete ############################################################
myHJntTemp.armT()

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

for arm_fingers_jnt in (arm_fingers_l_jnt_list):
    mc.makeIdentity(arm_fingers_jnt, apply=True, t=True, r=True, s=True)
    mc.select(d=True)

# mirror base arm skeleton
mc.mirrorJoint('clavicle_l', mirrorYZ=True, mirrorBehavior=True, searchReplace=('_l', '_r'))

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

# pole vector templete

mc.select('upperarm_l_ik', 'lowerarm_l_ik', 'hand_l_ik')
selO = mc.ls(sl=True)

start = mc.xform(selO[0], q=True, ws=True, t=True)
mid = mc.xform(selO[1], q=True, ws=True, t=True)
end = mc.xform(selO[2], q=True, ws=True, t=True)

startV = OpenMaya.MVector(start[0], start[1], start[2])
midV = OpenMaya.MVector(mid[0], mid[1], mid[2])
endV = OpenMaya.MVector(end[0], end[1], end[2])

startEnd = endV - startV
startMid = midV - startV

dotP = startMid * startEnd
proj = float(dotP) / float(startEnd.length())
startEndN = startEnd.normal()
projV = startEndN * proj

arrowV = startMid - projV
arrowV*=10
finalV = arrowV + midV

loc_PV = mc.spaceLocator(n='arm_PV_l')
loc_PVSpace = mc.group(loc_PV, n='PV_locSpace'), mc.select(d=True)
mc.xform(loc_PVSpace, ws=True, t=(finalV.x, finalV.y, finalV.z))
mc.parent(loc_PVSpace, 'lowerarm_l_ik')

# mirror ik chain
mc.mirrorJoint('upperarm_l_ik', mirrorYZ=True, mirrorBehavior=True, searchReplace=('_l', '_r'))
mc.rename('arm_PV_l1', 'arm_PV_r')

# create ikhandle rotate plane solver, PV & controls
ikArm_l = mc.ikHandle(n='ikArm_l', sj='upperarm_l_ik', ee='hand_l_ik', sol='ikRPsolver')
ikArm_r = mc.ikHandle(n='ikArm_r', sj='upperarm_r_ik', ee='hand_r_ik', sol='ikRPsolver')
ikArms_list = [ikArm_r, ikArm_r]
mc.select(d=True)

ikHand_jnt_list = ['hand_l_ik', 'hand_r_ik']
for ikH in ikHand_jnt_list:
    myCtrl.square_ctrl(ikH)
itemColor('hand_l_ik_ctrl', 6)
itemColor('hand_r_ik_ctrl', 13)

mc.delete(mc.parentConstraint('hand_r_ik', 'hand_r_ik_ctrlSpaceMaster'))
mc.delete(mc.parentConstraint('hand_l_ik', 'hand_l_ik_ctrlSpaceMaster'))

PV_arm_loc_list = ['arm_PV_l', 'arm_PV_r']
for armPV in PV_arm_loc_list:
    myCtrl.cone_ctrl(armPV)
itemColor('arm_PV_l_ctrl', 6)
itemColor('arm_PV_r_ctrl', 13)

mc.delete(mc.parentConstraint('arm_PV_l', 'arm_PV_l_ctrlSpaceMaster'))
mc.delete(mc.parentConstraint('arm_PV_r', 'arm_PV_r_ctrlSpaceMaster'))

mc.setAttr('arm_PV_l_ctrlSpaceMaster.rx', -90)
mc.setAttr('arm_PV_r_ctrlSpaceMaster.rx', 270)
mc.setAttr('arm_PV_r_ctrlSpaceMaster.sx', -1)
mc.delete('PV_locSpace1', 'PV_locSpace')

# lock PV attrs
armPV_ctrl_list = ['arm_PV_l_ctrl', 'arm_PV_r_ctrl']
for armPV_lockAt in armPV_ctrl_list:
    mc.setAttr(armPV_lockAt + '.rx', l=True, k=False, ch=False)
    mc.setAttr(armPV_lockAt + '.ry', l=True, k=False, ch=False)
    mc.setAttr(armPV_lockAt + '.rz', l=True, k=False, ch=False)
    mc.setAttr(armPV_lockAt + '.sx', l=True, k=False, ch=False)
    mc.setAttr(armPV_lockAt + '.sy', l=True, k=False, ch=False)
    mc.setAttr(armPV_lockAt + '.sz', l=True, k=False, ch=False)
    mc.setAttr(armPV_lockAt + '.v', l=True, k=False, ch=False)

# PV / point / orient constraint
mc.poleVectorConstraint('arm_PV_l_ctrl', 'ikArm_l', w=1), mc.poleVectorConstraint('arm_PV_r_ctrl', 'ikArm_r', w=1)
mc.pointConstraint('hand_l_ik_ctrl', 'ikArm_l', mo=True), mc.pointConstraint('hand_r_ik_ctrl', 'ikArm_r', mo=True)
mc.orientConstraint('hand_l_ik_ctrl', 'hand_l_ik', mo=True), mc.orientConstraint('hand_r_ik_ctrl', 'hand_r_ik', mo=True)


