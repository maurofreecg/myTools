'''
Loc Retarget tool
Create by MaurofreeCG - Rigger
06/08/2022
'''

import maya.cmds as mc

midB_joint_lits = ['HipsTranslation', 'Hips', 'Neck', 'NeckScale', 'Head', 'LeftShoulder', 'LeftArm', 'LeftForeArm', 'LeftHand', 'LeftHandThumb1',
                   'LeftHandThumb2', 'LeftHandThumb3', 'LeftHandIndex1', 'LeftHandIndex2', 'LeftHandIndex3', 'LeftHandMiddle1', 'LeftHandMiddle2', 'LeftHandMiddle3', 'LeftHandPinky1',
                   'LeftHandPinky2', 'LeftHandPinky3', 'LeftHandRing1', 'LeftHandRing2', 'LeftHandRing3', 'LeftForeArmRoll', 'LeftLowerarm', 'LeftWristHelper', 'LeftArmRoll', 'LeftUpperarm',
                   'LeftShoulderarmHelper_01', 'LeftShoulderarmHelper_02', 'Spine2ExpandHelper', 'Spine2Scale', 'LeftBreast', 'Spine1Scale', 'SpineScale', 'LeftUpLeg',
                   'LeftUpperlegHelperUp', 'LeftUpperlegHelperDn', 'LeftLeg', 'LeftLowerleg', 'LeftLegRoll', 'LeftAnkleHelper', 'LeftFoot', 'LeftToeBase', 'LeftButtock', 'RightLeg', 'RightFoot',
                   'RightToeBase', 'RightLegRoll', 'RightLowerleg', 'RightAnkleHelper', 'RightUpperlegHelperUp', 'RightUpperlegHelperDn', 'RightButtock', 'RightShoulder',
                   'RightArm', 'RightForeArm', 'RightHand', 'RightHandThumb1', 'RightHandThumb2', 'RightHandThumb3', 'RightHandIndex1', 'RightHandIndex2', 'RightHandIndex3', 'RightHandMiddle1',
                   'RightHandMiddle2', 'RightHandMiddle3', 'RightHandPinky1', 'RightHandPinky2', 'RightHandPinky3', 'RightHandRing1', 'RightHandRing2', 'RightHandRing3', 'RightForeArmRoll',
                   'RightLowerarm', 'RightWristHelper', 'RightArmRoll', 'RightUpperarm', 'RightShoulderarmHelper_01', 'RightShoulderarmHelper_02', 'RightBreast', 'LeftHandMetacarpal',
                   'RightHandMetacarpal', 'RightUpLeg']

midB_locs_lits = ['HipsTranslation_loc', 'Hips_loc', 'Neck_loc', 'NeckScale_loc', 'Head_loc', 'LeftShoulder_loc', 'LeftArm_loc', 'LeftForeArm_loc', 'LeftHand_loc', 'LeftHandThumb1_loc',
                  'LeftHandThumb2_loc', 'LeftHandThumb3_loc', 'LeftHandIndex1_loc', 'LeftHandIndex2_loc', 'LeftHandIndex3_loc', 'LeftHandMiddle1_loc', 'LeftHandMiddle2_loc', 'LeftHandMiddle3_loc', 'LeftHandPinky1_loc',
                  'LeftHandPinky2_loc', 'LeftHandPinky3_loc', 'LeftHandRing1_loc', 'LeftHandRing2_loc', 'LeftHandRing3_loc', 'LeftForeArmRoll_loc', 'LeftLowerarm_loc', 'LeftWristHelper_loc', 'LeftArmRoll_loc', 'LeftUpperarm_loc',
                  'LeftShoulderarmHelper_01_loc', 'LeftShoulderarmHelper_02_loc', 'Spine2ExpandHelper_loc', 'Spine2Scale_loc', 'LeftBreast_loc', 'Spine1Scale_loc', 'SpineScale_loc', 'LeftUpLeg_loc',
                  'LeftUpperlegHelperUp_loc', 'LeftUpperlegHelperDn_loc', 'LeftLeg_loc', 'LeftLowerleg_loc', 'LeftLegRoll_loc', 'LeftAnkleHelper_loc', 'LeftFoot_loc', 'LeftToeBase_loc', 'LeftButtock_loc', 'RightLeg_loc', 'RightFoot_loc',
                  'RightToeBase_loc', 'RightLegRoll_loc', 'RightLowerleg_loc', 'RightAnkleHelper_loc', 'RightUpperlegHelperUp_loc', 'RightUpperlegHelperDn_loc', 'RightButtock_loc', 'RightShoulder_loc',
                  'RightArm_loc', 'RightForeArm_loc', 'RightHand_loc', 'RightHandThumb1_loc', 'RightHandThumb2_loc', 'RightHandThumb3_loc', 'RightHandIndex1_loc', 'RightHandIndex2_loc', 'RightHandIndex3_loc', 'RightHandMiddle1_loc',
                  'RightHandMiddle2_loc', 'RightHandMiddle3_loc', 'RightHandPinky1_loc', 'RightHandPinky2_loc', 'RightHandPinky3_loc', 'RightHandRing1_loc', 'RightHandRing2_loc', 'RightHandRing3_loc', 'RightForeArmRoll_loc',
                  'RightLowerarm_loc', 'RightWristHelper_loc', 'RightArmRoll_loc', 'RightUpperarm_loc', 'RightShoulderarmHelper_01_loc', 'RightShoulderarmHelper_02_loc', 'RightBreast_loc', 'LeftHandMetacarpal_loc',
                  'RightHandMetacarpal_loc', 'RightUpLeg_loc']
print(midB_joint_lits)
mc.select(d=True)

midB_locSpace_lits = ['HipsTranslation_locSpace', 'Hips_locSpace', 'Neck_locSpace', 'NeckScale_locSpace', 'Head_locSpace', 'LeftShoulder_locSpace', 'LeftArm_locSpace', 'LeftForeArm_locSpace', 'LeftHand_locSpace', 'LeftHandThumb1_locSpace',
                      'LeftHandThumb2_locSpace', 'LeftHandThumb3_locSpace', 'LeftHandIndex1_locSpace', 'LeftHandIndex2_locSpace', 'LeftHandIndex3_locSpace', 'LeftHandMiddle1_locSpace', 'LeftHandMiddle2_locSpace', 'LeftHandMiddle3_locSpace', 'LeftHandPinky1_locSpace',
                      'LeftHandPinky2_locSpace', 'LeftHandPinky3_locSpace', 'LeftHandRing1_locSpace', 'LeftHandRing2_locSpace', 'LeftHandRing3_locSpace', 'LeftForeArmRoll_locSpace', 'LeftLowerarm_locSpace', 'LeftWristHelper_locSpace', 'LeftArmRoll_locSpace', 'LeftUpperarm_locSpace',
                      'LeftShoulderarmHelper_01_locSpace', 'LeftShoulderarmHelper_02_locSpace', 'Spine2ExpandHelper_locSpace', 'Spine2Scale_locSpace', 'LeftBreast_locSpace', 'Spine1Scale_locSpace', 'SpineScale_locSpace', 'LeftUpLeg_locSpace',
                      'LeftUpperlegHelperUp_locSpace', 'LeftUpperlegHelperDn_locSpace', 'LeftLeg_locSpace', 'LeftLowerleg_locSpace', 'LeftLegRoll_locSpace', 'LeftAnkleHelper_locSpace', 'LeftFoot_locSpace', 'LeftToeBase_locSpace', 'LeftButtock_locSpace', 'RightLeg_locSpace', 'RightFoot_locSpace',
                      'RightToeBase_locSpace', 'RightLegRoll_locSpace', 'RightLowerleg_locSpace', 'RightAnkleHelper_locSpace', 'RightUpperlegHelperUp_locSpace', 'RightUpperlegHelperDn_locSpace', 'RightButtock_locSpace', 'RightShoulder_locSpace',
                      'RightArm_locSpace', 'RightForeArm_locSpace', 'RightHand_locSpace', 'RightHandThumb1_locSpace', 'RightHandThumb2_locSpace', 'RightHandThumb3_locSpace', 'RightHandIndex1_locSpace', 'RightHandIndex2_locSpace', 'RightHandIndex3_locSpace', 'RightHandMiddle1_locSpace',
                      'RightHandMiddle2_locSpace', 'RightHandMiddle3_locSpace', 'RightHandPinky1_locSpace', 'RightHandPinky2_locSpace', 'RightHandPinky3_locSpace', 'RightHandRing1_locSpace', 'RightHandRing2_locSpace', 'RightHandRing3_locSpace', 'RightForeArmRoll_locSpace',
                      'RightLowerarm_locSpace', 'RightWristHelper_locSpace', 'RightArmRoll_locSpace', 'RightUpperarm_locSpace', 'RightShoulderarmHelper_01_locSpace', 'RightShoulderarmHelper_02_locSpace', 'RightBreast_locSpace', 'LeftHandMetacarpal_locSpace',
                      'RightHandMetacarpal_locSpace', 'RightUpLeg_locSpace']

midB_locSpaceMaster_lits = ['HipsTranslation_locSpaceMaster', 'Hips_locSpaceMaster', 'Neck_locSpaceMaster', 'NeckScale_locSpaceMaster', 'Head_locSpaceMaster', 'LeftShoulder_locSpaceMaster', 'LeftArm_locSpaceMaster', 'LeftForeArm_locSpaceMaster', 'LeftHand_locSpaceMaster', 'LeftHandThumb1_locSpaceMaster',
                            'LeftHandThumb2_locSpaceMaster', 'LeftHandThumb3_locSpaceMaster', 'LeftHandIndex1_locSpaceMaster', 'LeftHandIndex2_locSpaceMaster', 'LeftHandIndex3_locSpaceMaster', 'LeftHandMiddle1_locSpaceMaster', 'LeftHandMiddle2_locSpaceMaster', 'LeftHandMiddle3_locSpaceMaster', 'LeftHandPinky1_locSpaceMaster',
                            'LeftHandPinky2_locSpaceMaster', 'LeftHandPinky3_locSpaceMaster', 'LeftHandRing1_locSpaceMaster', 'LeftHandRing2_locSpaceMaster', 'LeftHandRing3_locSpaceMaster', 'LeftForeArmRoll_locSpaceMaster', 'LeftLowerarm_locSpaceMaster', 'LeftWristHelper_locSpaceMaster', 'LeftArmRoll_locSpaceMaster', 'LeftUpperarm_locSpaceMaster',
                            'LeftShoulderarmHelper_01_locSpaceMaster', 'LeftShoulderarmHelper_02_locSpaceMaster', 'Spine2ExpandHelper_locSpaceMaster', 'Spine2Scale_locSpaceMaster', 'LeftBreast_locSpaceMaster', 'Spine1Scale_locSpaceMaster', 'SpineScale_locSpaceMaster', 'LeftUpLeg_locSpaceMaster',
                            'LeftUpperlegHelperUp_locSpaceMaster', 'LeftUpperlegHelperDn_locSpaceMaster', 'LeftLeg_locSpaceMaster', 'LeftLowerleg_locSpaceMaster', 'LeftLegRoll_locSpaceMaster', 'LeftAnkleHelper_locSpaceMaster', 'LeftFoot_locSpaceMaster', 'LeftToeBase_locSpaceMaster', 'LeftButtock_locSpaceMaster', 'RightLeg_locSpaceMaster', 'RightFoot_locSpaceMaster',
                            'RightToeBase_locSpaceMaster', 'RightLegRoll_locSpaceMaster', 'RightLowerleg_locSpaceMaster', 'RightAnkleHelper_locSpaceMaster', 'RightUpperlegHelperUp_locSpaceMaster', 'RightUpperlegHelperDn_locSpaceMaster', 'RightButtock_locSpaceMaster', 'RightShoulder_locSpaceMaster',
                            'RightArm_locSpaceMaster', 'RightForeArm_locSpaceMaster', 'RightHand_locSpaceMaster', 'RightHandThumb1_locSpaceMaster', 'RightHandThumb2_locSpaceMaster', 'RightHandThumb3_locSpaceMaster', 'RightHandIndex1_locSpaceMaster', 'RightHandIndex2_locSpaceMaster', 'RightHandIndex3_locSpaceMaster', 'RightHandMiddle1_locSpaceMaster',
                            'RightHandMiddle2_locSpaceMaster', 'RightHandMiddle3_locSpaceMaster', 'RightHandPinky1_locSpaceMaster', 'RightHandPinky2_locSpaceMaster', 'RightHandPinky3_locSpaceMaster', 'RightHandRing1_locSpaceMaster', 'RightHandRing2_locSpaceMaster', 'RightHandRing3_locSpaceMaster', 'RightForeArmRoll_locSpaceMaster',
                            'RightLowerarm_locSpaceMaster', 'RightWristHelper_locSpaceMaster', 'RightArmRoll_locSpaceMaster', 'RightUpperarm_locSpaceMaster', 'RightShoulderarmHelper_01_locSpaceMaster', 'RightShoulderarmHelper_02_locSpaceMaster', 'RightBreast_locSpaceMaster', 'LeftHandMetacarpal_locSpaceMaster',
                            'RightHandMetacarpal_locSpaceMaster', 'RightUpLeg_locSpaceMaster']
print(midB_locSpace_lits)
mc.select(d=True)

#############################################################################################################################################################################################
###############################################################                                  Create loc                                 #################################################

def createLoc(*args):

    for i in midB_joint_lits:
        loc = mc.spaceLocator(n = i + '_loc')
        locSpace = mc.group(loc, n = i + '_locSpace')
        locSpaceMaster = mc.group(locSpace, n= i + '_locSpaceMaster')
        mc.delete(mc.parentConstraint(i, locSpaceMaster, mo=False))

    for j, item in enumerate(midB_locs_lits):
        mc.parentConstraint(midB_joint_lits[j], item, mo=True)
        mc.connectAttr(midB_joint_lits[j] + '.s', item + '.s')

    mc.group(midB_locSpaceMaster_lits, n='locRetarget_grp')
    mc.select(d=True)

#############################################################################################################################################################################################
###############################################################        Bake locators and delete constrainst                                 #################################################

def bakeLoc(*args):
    startF = mc.playbackOptions(q=True, minTime=True)
    print(startF)
    endF = mc.playbackOptions(q=True, maxTime=True)
    print(endF)
    mc.bakeResults(midB_locs_lits, t=(startF, endF), sm=True)
    ########################################################################################################################################
    ##################################################### delete constraints ###############################################################
    mc.select('*_loc_parentConstraint1')
    loc_pCon = mc.ls(sl=True)
    print(loc_pCon)
    mc.delete(loc_pCon)

################################################################## ###########################################################################################################################
###############################################################        Connect RerargetLoc to source skeleton                                #################################################

def connectSourceSK(*args):
    for n, item in enumerate(midB_locSpaceMaster_lits):
        mc.delete(mc.pointConstraint(midB_joint_lits[n], item, mo=False))

        ########################################################################################################################################
        ##################################################### Connect to source skeleton ###############################################################
    for z, item in enumerate(midB_joint_lits):
        mc.parentConstraint(midB_locs_lits[z], item, mo=True)
        mc.connectAttr(midB_locs_lits[z] + '.s', item + '.s')

    startF = mc.playbackOptions(q=True, minTime=True)
    print(startF)
    endF = mc.playbackOptions(q=True, maxTime=True)
    print(endF)
    mc.bakeResults(midB_joint_lits, t=(startF, endF), sm=True)
    mc.delete('locRetarget_grp')

#############################################################################################################################################################################################
###############################################################                              Window                                         #################################################

mc.window(t= 'Loc Retarget - RD', iconName= 'Loc Retarget', w= 300)
mc.columnLayout(adj= True)
mc.separator(), mc.separator(), mc.separator()
mc.button(l= '01 - Make locs constrained to Anim file', command= createLoc)
mc.separator(), mc.separator(), mc.separator()
mc.button(l= '02 - Bake locConstrained - Make sure timeRange is exact -', command= bakeLoc)
mc.separator(), mc.separator(), mc.separator()
mc.button(l= '03 - Connect locRetarget to Surce Skeleton -', command= connectSourceSK)
mc.separator(), mc.separator(), mc.separator()
mc.text(' --> At the moment works with AGS project (namingConvention) <-- ')
mc.separator(), mc.separator(), mc.separator()
mc.showWindow()
