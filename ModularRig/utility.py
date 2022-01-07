#######################################################################
#
#
#                            UTILITIES
#
#
#######################################################################

import maya.cmds as mc

#################################################### color ##############################################################################
def itemColor(s, c):  # yellow 17, red 13, blue 6, light blue 18
    mc.setAttr(s + '.overrideEnabled', 1)
    mc.setAttr(s + '.overrideColor', c)

########################################### controls shapes ###########################################################

############### celta cross

def celtCross_crv():
    selO = mc.ls(sl=True)

    for item in (selO):
        celtCrossGrpMaster = mc.group(n=item + '_masterCtrlSpace')
        celtCrossGrp = mc.group(n=item + '_ctrlSpace', em=True)
        celtCross_ctrl = mc.curve(d=1, p=[(0, 1.108194, 0), (0, 0.693935, 0.108972), (0, -0.134583, 0.326917), (0, -0.0517824, -1.82575), (0, 0.341712, 0.326917),
                          (0, -1.833147, 0), (0, 0.341712, -0.326917), (0, -0.0517824, 1.82575), (0, -0.134583, -0.326917), (0, 0.693935, -0.108972,),
                          (0, 1.108194, 0)], n=item + '_ctrl')
        mc.parent(celtCross_ctrl, celtCrossGrp), mc.parent(celtCrossGrp, celtCrossGrpMaster)
        mc.delete(mc.parentConstraint(item, masterGrp, mo=False))

############################################## neckHead templete #########################################################################
def neckHead_jntT(neckP = (0, 155.256, -5.945), neckO = (0, -1.638, 90.000),
                  headP = (0, 163.244, -5.717), headO = (1.638, 0, 0), *kwargs):

    neck = mc.joint(p= neckP, rad=2, o= neckO, n= 'neck'), mc.select(d=True)
    head = mc.joint(neck, p= headP, rad=2, o= headO, n='head'), mc.select(d=True)

############################################# spine templete ##############################################################################
def spine_jntT(pelvisP = (0, 97.546, -2.303), pelvisO = (0 ,0.849, 90),
                spine_01P = (0, 108.888, -2.417), spine_01O = (-0.578, -2.703, 0.027),
                spine_02P = (0, 120.295, -2.532), spine_02O = (0, 0.124, 0),
                spine_03P = (0, 131.688, -2.646), spine_03O = (0.577, 0.534, -0.015), *kwargs):

    pelvis = mc.joint(p= pelvisP, rad=2, o= pelvisO, n='pelvis'), mc.select(d=True)
    spine_01 = mc.joint(pelvis, p= spine_01P, rad=2, o= spine_01O, n='spine_01'), mc.select(d=True)
    spine_02 = mc.joint(spine_01, p= spine_02P, rad=2, o= spine_02O, n='spine_02'), mc.select(d=True)
    spine_03 = mc.joint(spine_02, p= spine_03P, rad=2, o= spine_03O, n='spine_03'), mc.select(d=True)

############################################################ arm templete ##################################################################
def arm_jntT(clavicleP = (2.663, 146.853, -1.658), clavicleO = (0, 15, 0),
             upperarmP = (16.535, 146.853, -5.454), upperarmO = (-0.059, -6.599, -56.457),
             lowerarmP = (32.645, 123.032, -6.348), lowerarmO = (4.422, -14.629, -0.336),
             handP = (47.297, 103.560, -0.915), handO = (4.283, -2.541, 0.593),
             pinky_00P = (50.260, 98.184, -1.314), pinky_00O = (-5.328, 19.160, -24.458),
             pinky_01P = (51.084, 94.987, -1.521), pinky_01O = (-2.604, -2.168, -11.199),
             pinky_02P = (51.180, 92.620, -1.558), pinky_02O = (-3.439, 1.179, -21.202),
             pinky_03P = (50.312, 90.082, -1.547), pinky_03O = (0,0,0),
             ring_00P = (50.400, 98.309, 0.304), ring_00O = (-1.784, 9.108, -17.419),
             ring_01P = (51.550, 95.069, 0.758), ring_01O = (-3.058, 2.084, -16.957),
             ring_02P = (51.734, 91.461, 1.043), ring_02O = (-4.043, 2.126, -30.759),
             ring_03P = (50.298, 88.753, 1.204), ring_03O = (0,0,0),
             middle_00P = (50.308, 98.546, 1.929), middle_00O = (4.373, 2.564, -17.780),
             middle_01P = (51.541, 95.185, 2.824), middle_01O = (-4.050, 1.144, -10.337),
             middle_02P = (52.147, 91.430, 3.550), middle_02O = (0.748, 1.389, -27.195),
             middle_03P = (51.129, 88.314, 3.941), middle_03O = (0,0,0),
             index_00P = (49.854, 99.195, 3.526), index_00O = (9.852, -7.280, -16.897),
             index_01P = (51.104, 95.833, 5.040), index_01O = (0, 0, -17.958),
             index_02P = (51.215, 92.147, 6.284), index_02O = (0, 0, -14.196),
             index_03P = (50.622, 89.423, 6.981), index_03O = (0, 0, 0),
             thumb_01P = (46.422, 102.638, 2.687), thumb_01O = (77.319, -32.718, -26.439),
             thumb_02P = (46.761, 100.272, 5.341), thumb_02O = (-1.148, 5.425, -11.966),
             thumb_03P = (47.470, 97.104, 7.638), thumb_03O = (0 ,0 ,0), *kwargs):

    clavicle_l = mc.joint(p=clavicleP, rad=2, o=clavicleO, n='clavicle_l'), mc.select(d=True)
    upperarm_l = mc.joint(clavicle_l, p=upperarmP, rad=2, o=upperarmO, n='upperarm_l'), mc.select(d=True)
    lowerarm_l = mc.joint(upperarm_l, p= lowerarmP, rad=2, o= lowerarmO, n='lowerarm_l'), mc.select(d=True)
    hand_l = mc.joint(lowerarm_l, p= handP, rad=2, o= handO, n='hand_l'), mc.select(d=True)

    ### pinky
    pinky_00_l = mc.joint(hand_l, p= pinky_00P, rad=1, o= pinky_00O, n='pinky_00_l'), mc.select(d=True)
    pinky_01_l = mc.joint(pinky_00_l, p= pinky_01P, rad=1, o= pinky_01O, n='pinky_01_l'), mc.select(d=True)
    pinky_02_l = mc.joint(pinky_01_l, p= pinky_02P, rad=1, o= pinky_02O, n='pinky_02_l'), mc.select(d=True)
    pinky_03_l = mc.joint(pinky_02_l, p= pinky_03P, rad=1, o= pinky_03O, n='pinky_03_l'), mc.select(d=True)

    ### ring
    ring_00_l = mc.joint(hand_l, p= ring_00P, rad=1, o= ring_00O, n='ring_00_l'), mc.select(d=True)
    ring_01_l = mc.joint(ring_00_l, p= ring_01P, rad=1, o= ring_01O, n='ring_01_l'), mc.select(d=True)
    ring_02_l = mc.joint(ring_01_l, p= ring_02P, rad=1, o= ring_02O, n='ring_02_l'), mc.select(d=True)
    ring_03_l = mc.joint(ring_02_l, p= ring_03P, rad=1, o= ring_03O, n='ring_03_l'), mc.select(d=True)

    ### middle
    middle_00_l = mc.joint(hand_l, p= middle_00P, rad=1, o= middle_00O, n='middle_00_l'), mc.select(d=True)
    middle_01_l = mc.joint(middle_00_l, p= middle_01P, rad=1, o= middle_01O, n='middle_01_l'), mc.select(d=True)
    middle_02_l = mc.joint(middle_01_l, p= middle_02P, rad=1, o= middle_02O, n='middle_02_l'), mc.select(d=True)
    middle_03_l = mc.joint(middle_02_l, p= middle_03P, rad=1, o= middle_03O, n='middle_03_l'), mc.select(d=True)

    ### index
    index_00_l = mc.joint(hand_l, p= index_00P, rad=1, o= index_00O, n='index_00_l'), mc.select(d=True)
    index_01_l = mc.joint(index_00_l, p= index_01P, rad=1, o= index_01O, n='index_01_l'), mc.select(d=True)
    index_02_l = mc.joint(index_01_l, p= index_02P, rad=1, o= index_02O, n='index_02_l'), mc.select(d=True)
    index_03_l = mc.joint(index_02_l, p= index_03P, rad=1, o= index_03O, n='index_03_l'), mc.select(d=True)

    ### thumb
    thumb_01_l = mc.joint(hand_l, p= thumb_01P, rad=1, o= thumb_01O, n='thumb_01_l'), mc.select(d=True)
    thumb_02_l = mc.joint(thumb_01_l, p= thumb_02P, rad=1, o= thumb_02O, n='thumb_02_l'), mc.select(d=True)
    thumb_03_l = mc.joint(thumb_02_l, p= thumb_03P, rad=1, o= thumb_03O, n='thumb_03_l'), mc.select(d=True)

################################################## leg templete ##################################################################################
def leg_jntT(thighP = (10.431, 95.474, -2.290), thighO = (0,-5.546,-90.000),
            calfP = (10.431, 54.838, 1.656), calfO = (0,15.067,0),
            footP = (10.431, 12.113, -5.511), footO = (0, 260.979, 0),
            ballP = (10.431, -0.050, 5.758), ballO = (-90, -90, 0),
            toeP = (10.431, -0.113, 12.968), toeO = (-90, -90, 0), *kwargs):

    thigh_l = mc.joint(p= thighP, rad=2, o= thighO, n='thigh_l'), mc.select(d=True)
    calf_l = mc.joint(thigh_l, p= calfP, rad=2, o= calfO, n='calf_l'), mc.select(d=True)
    foot_l = mc.joint(calf_l, p= footP, rad=2, o= footO, n='foot_l'), mc.select(d=True)
    ball_l = mc.joint(foot_l, p= ballP, rad=2, o= ballO, n='ball_l'), mc.select(d=True)
    toe_l = mc.joint(ball_l, p= toeP, rad=2, o= toeO, n='toe_l'), mc.select(d=True)

################################################# biped templete ###############################################################################
def biped_jntT(neckP = (0, 155.256, -5.945), neckO = (0, -1.638, 90.000), headP = (0, 163.244, -5.717), headO = (1.638, 0, 0),
               pelvisP = (0, 97.546, -2.303), pelvisO = (0 ,0.849, 90), spine_01P = (0, 108.888, -2.417), spine_01O = (-0.578, -2.703, 0.027),
               spine_02P = (0, 120.295, -2.532), spine_02O = (0, 0.124, 0), spine_03P = (0, 131.688, -2.646), spine_03O = (0.577, 0.534, -0.015),
               clavicleP = (2.663, 146.853, -1.658), clavicleO = (0, 15, 0),
               upperarmP = (16.535, 146.853, -5.454), upperarmO = (-0.059, -6.599, -56.457),
               lowerarmP = (32.645, 123.032, -6.348), lowerarmO = (4.422, -14.629, -0.336),
               handP = (47.297, 103.560, -0.915), handO = (4.283, -2.541, 0.593),
               pinky_00P = (50.260, 98.184, -1.314), pinky_00O = (-5.328, 19.160, -24.458),
               pinky_01P = (51.084, 94.987, -1.521), pinky_01O = (-2.604, -2.168, -11.199),
               pinky_02P = (51.180, 92.620, -1.558), pinky_02O = (-3.439, 1.179, -21.202),
               pinky_03P = (50.312, 90.082, -1.547), pinky_03O = (0,0,0),
               ring_00P = (50.400, 98.309, 0.304), ring_00O = (-1.784, 9.108, -17.419),
               ring_01P = (51.550, 95.069, 0.758), ring_01O = (-3.058, 2.084, -16.957),
               ring_02P = (51.734, 91.461, 1.043), ring_02O = (-4.043, 2.126, -30.759),
               ring_03P = (50.298, 88.753, 1.204), ring_03O = (0,0,0),
               middle_00P = (50.308, 98.546, 1.929), middle_00O = (4.373, 2.564, -17.780),
               middle_01P = (51.541, 95.185, 2.824), middle_01O = (-4.050, 1.144, -10.337),
               middle_02P = (52.147, 91.430, 3.550), middle_02O = (0.748, 1.389, -27.195),
               middle_03P = (51.129, 88.314, 3.941), middle_03O = (0,0,0),
               index_00P = (49.854, 99.195, 3.526), index_00O = (9.852, -7.280, -16.897),
               index_01P = (51.104, 95.833, 5.040), index_01O = (0, 0, -17.958),
               index_02P = (51.215, 92.147, 6.284), index_02O = (0, 0, -14.196),
               index_03P = (50.622, 89.423, 6.981), index_03O = (0, 0, 0),
               thumb_01P = (46.422, 102.638, 2.687), thumb_01O = (77.319, -32.718, -26.439),
               thumb_02P = (46.761, 100.272, 5.341), thumb_02O = (-1.148, 5.425, -11.966),
               thumb_03P = (47.470, 97.104, 7.638), thumb_03O = (0 ,0 ,0),
               thighP = (10.431, 95.474, -2.290), thighO = (0,-5.546,-90.000),
              calfP = (10.431, 54.838, 1.656), calfO = (0,15.067,0),
              footP = (10.431, 12.113, -5.511), footO = (0, 260.979, 0),
              ballP = (10.431, -0.050, 5.758), ballO = (-90, -90, 0),
              toeP = (10.431, -0.113, 12.968), toeO = (-90, -90, 0), *kwargs):

    ### spine
    pelvis = mc.joint(p= pelvisP, rad=2, o= pelvisO, n='pelvis'), mc.select(d=True)
    spine_01 = mc.joint(pelvis, p= spine_01P, rad=2, o= spine_01O, n='spine_01'), mc.select(d=True)
    spine_02 = mc.joint(spine_01, p= spine_02P, rad=2, o= spine_02O, n='spine_02'), mc.select(d=True)
    spine_03 = mc.joint(spine_02, p= spine_03P, rad=2, o= spine_03O, n='spine_03'), mc.select(d=True)

    ### leg
    thigh_l = mc.joint(p= thighP, rad=2, o= thighO, n='thigh_l'), mc.select(d=True)
    calf_l = mc.joint(thigh_l, p= calfP, rad=2, o= calfO, n='calf_l'), mc.select(d=True)
    foot_l = mc.joint(calf_l, p= footP, rad=2, o= footO, n='foot_l'), mc.select(d=True)
    ball_l = mc.joint(foot_l, p= ballP, rad=2, o= ballO, n='ball_l'), mc.select(d=True)
    toe_l = mc.joint(ball_l, p= toeP, rad=2, o= toeO, n='toe_l'), mc.select(d=True)

    ### arm
    clavicle_l = mc.joint(p=clavicleP, rad=2, o=clavicleO, n='clavicle_l'), mc.select(d=True)
    upperarm_l = mc.joint(clavicle_l, p=upperarmP, rad=2, o=upperarmO, n='upperarm_l'), mc.select(d=True)
    lowerarm_l = mc.joint(upperarm_l, p= lowerarmP, rad=2, o= lowerarmO, n='lowerarm_l'), mc.select(d=True)
    hand_l = mc.joint(lowerarm_l, p= handP, rad=2, o= handO, n='hand_l'), mc.select(d=True)

    ### pinky
    pinky_00_l = mc.joint(hand_l, p= pinky_00P, rad=1, o= pinky_00O, n='pinky_00_l'), mc.select(d=True)
    pinky_01_l = mc.joint(pinky_00_l, p= pinky_01P, rad=1, o= pinky_01O, n='pinky_01_l'), mc.select(d=True)
    pinky_02_l = mc.joint(pinky_01_l, p= pinky_02P, rad=1, o= pinky_02O, n='pinky_02_l'), mc.select(d=True)
    pinky_03_l = mc.joint(pinky_02_l, p= pinky_03P, rad=1, o= pinky_03O, n='pinky_03_l'), mc.select(d=True)

    ### ring
    ring_00_l = mc.joint(hand_l, p= ring_00P, rad=1, o= ring_00O, n='ring_00_l'), mc.select(d=True)
    ring_01_l = mc.joint(ring_00_l, p= ring_01P, rad=1, o= ring_01O, n='ring_01_l'), mc.select(d=True)
    ring_02_l = mc.joint(ring_01_l, p= ring_02P, rad=1, o= ring_02O, n='ring_02_l'), mc.select(d=True)
    ring_03_l = mc.joint(ring_02_l, p= ring_03P, rad=1, o= ring_03O, n='ring_03_l'), mc.select(d=True)

    ### middle
    middle_00_l = mc.joint(hand_l, p= middle_00P, rad=1, o= middle_00O, n='middle_00_l'), mc.select(d=True)
    middle_01_l = mc.joint(middle_00_l, p= middle_01P, rad=1, o= middle_01O, n='middle_01_l'), mc.select(d=True)
    middle_02_l = mc.joint(middle_01_l, p= middle_02P, rad=1, o= middle_02O, n='middle_02_l'), mc.select(d=True)
    middle_03_l = mc.joint(middle_02_l, p= middle_03P, rad=1, o= middle_03O, n='middle_03_l'), mc.select(d=True)

    ### index
    index_00_l = mc.joint(hand_l, p= index_00P, rad=1, o= index_00O, n='index_00_l'), mc.select(d=True)
    index_01_l = mc.joint(index_00_l, p= index_01P, rad=1, o= index_01O, n='index_01_l'), mc.select(d=True)
    index_02_l = mc.joint(index_01_l, p= index_02P, rad=1, o= index_02O, n='index_02_l'), mc.select(d=True)
    index_03_l = mc.joint(index_02_l, p= index_03P, rad=1, o= index_03O, n='index_03_l'), mc.select(d=True)

    ### thumb
    thumb_01_l = mc.joint(hand_l, p= thumb_01P, rad=1, o= thumb_01O, n='thumb_01_l'), mc.select(d=True)
    thumb_02_l = mc.joint(thumb_01_l, p= thumb_02P, rad=1, o= thumb_02O, n='thumb_02_l'), mc.select(d=True)
    thumb_03_l = mc.joint(thumb_02_l, p= thumb_03P, rad=1, o= thumb_03O, n='thumb_03_l'), mc.select(d=True)

    ### neck
    neck = mc.joint(p= neckP, rad=2, o= neckO, n= 'neck'), mc.select(d=True)
    head = mc.joint(neck, p= headP, rad=2, o= headO, n='head'), mc.select(d=True)

    ### parent
    mc.parent(neck, clavicle_l, spine_03), mc.parent(thigh_l, pelvis), mc.select(d=True)

################################################ translate / rotate / scale - Constraint ###############################################################
def tranRotScl_const():
    selO = mc.ls(sl=True)

    for i in (selO):
        masterGrp = mc.group(n= i + '_masterCtrlSpace', em=True)
        grp = mc.group(n= i + '_ctrlSpace', em=True)
        crv = mc.circle( n= i + '_ctrl', ch=False, radius = 3, nr=(1, 0, 0))
        mc.parent(crv, grp), mc.parent(grp, masterGrp)
        mc.delete(mc.parentConstraint(i, masterGrp, mo=False))
        mc.connectAttr(('%s.r'%crv[0]), ('%s.r'%i))
        mc.connectAttr(('%s.s'%crv[0]), ('%s.s'%i))
        multM = mc.createNode('multMatrix', n= i + '_MM')
        decM = mc.createNode('decomposeMatrix', n= i + '_DM')
        mc.connectAttr(multM + '.matrixSum', decM + '.inputMatrix')
        mc.connectAttr(('%s.worldMatrix[0]'%crv[0]), ('%s.matrixIn[0]'%multM), f=True)
        mc.connectAttr(str(i) + '.parentInverseMatrix[0]', multM + '.matrixIn[1]', f=True)
        mc.connectAttr(decM + '.outputTranslate', i + '.t')

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

################################################# arm finger FK transform ######################################################
#def arm_fingers_FK_transform():

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

### twist transform
twist_l_jnt_list = ['upperarm_twist_01_l', 'upperarm_twist_02_l', 'lowerarm_twist_01_l', 'lowerarm_twist_02_l']









