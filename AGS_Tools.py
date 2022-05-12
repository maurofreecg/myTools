import maya.cmds as mc
import maya.mel as mel

# AGS_BodyCustom_Tool
# AGS_FacialRig_Tool
# By MauroFreeCG - Rigger

##############################################################################################################################################
#####################################                                          ###############################################################
#####################################            Create bodyRig                ###############################################################
##############################################################################################################################################
# connect deformation bones (AS) to bind bones - arms legs (AGS)                                                                             #
# need import 'armsLegs_ch' // match arms, legs with current bone position                                                                   #
##############################################################################################################################################

def BodyCustomButton(*args):
    mc.rename('Spine1', 'Spine11')
    mc.rename('Spine2', 'Spine22')

    mc.rename('Root_M', 'Hips')
    mc.rename('Spine1_M', 'Spine')
    mc.rename('Spine2_M', 'Spine1')
    mc.rename('Chest_M', 'Spine2')
    mc.rename('FKHeadBase_M', 'FKHead_M')
    mc.rename('FKNeckBase_M', 'FKNeck_M')
    mc.rename('NeckBase_M', 'Neck_M')
    mc.rename('HeadBase_M', 'Head_M')

    BaseJNT_List = ['Hip_R', 'Hip_L', 'Scapula_R', 'Scapula_L', 'Neck_M']
    mc.parent(BaseJNT_List, 'MotionSystem')

    for BaseJNT in (BaseJNT_List):
        mc.setAttr(BaseJNT + '.v', 0)
    mc.select(d=True)

    # ik bones
    ikLeg = mc.joint(n='LeftFoot_IK'), mc.select(d=True)
    mc.delete(mc.parentConstraint('LeftFoot', ikLeg, mo=False)), mc.select(d=True)
    ikArm = mc.joint(n='LeftHand_IK'), mc.select(d=True)
    mc.delete(mc.parentConstraint('LeftHand', ikArm, mo=False)), mc.select(d=True)
    ikHead = mc.joint(n='Head_IK'), mc.select(d=True)
    mc.delete(mc.parentConstraint('Head_M', ikHead, mo=False)), mc.select(d=True)
    cam = mc.joint(n='Camera'), mc.select(d=True)
    Attach = mc.joint(n='Attach'), mc.select(d=True)
    HipTrans = mc.joint(n='HipsTranslation'), mc.select(d=True)

    mc.mirrorJoint('LeftShoulder', mirrorYZ=True, mirrorBehavior=True, searchReplace=('Left', 'Right')), mc.select(cl=True)
    mc.mirrorJoint('LeftButtock', mirrorYZ=True, mirrorBehavior=True, searchReplace=('Left', 'Right')), mc.select( cl=True)
    mc.mirrorJoint('LeftUpLeg', mirrorYZ=True, mirrorBehavior=True, searchReplace=('Left', 'Right')), mc.select(cl=True)
    mc.mirrorJoint('LeftSpine2AttachRear', mirrorYZ=True, mirrorBehavior=False,searchReplace=('Left', 'Right')), mc.select(cl=True)
    mc.mirrorJoint('LeftBreast', mirrorYZ=True, mirrorBehavior=False, searchReplace=('Left', 'Right')), mc.select(cl=True)
    mc.mirrorJoint('LeftScapulaUpVolume', mirrorYZ=True, mirrorBehavior=False,searchReplace=('Left', 'Right')), mc.select(cl=True)
    mc.mirrorJoint(ikLeg, mirrorYZ=True, mirrorBehavior=True, searchReplace=('Left', 'Right')), mc.select(cl=True)
    mc.mirrorJoint(ikArm, mirrorYZ=True, mirrorBehavior=True, searchReplace=('Left', 'Right')), mc.select(cl=True)

    # parent bones

    mc.parent('RightUpLeg', 'LeftUpLeg', 'Hips')
    mc.parent('Neck', 'LeftShoulder', 'RightShoulder', 'Spine2')
    mc.parent('Hips', 'HipsTranslation')
    mc.parent('LeftSpine2AttachRear', 'LeftBreast', 'RightSpine2AttachRear', 'RightBreast', 'Spine2'), mc.select(d=True)
    mc.parent('LeftHipsAttachSide', 'LeftHipsAttachRear', 'LeftHipsAttachFront', 'RightHipsAttachSide','RightHipsAttachFront', 'RightHipsAttachRear', 'Hips'), mc.select(d=True)

    RootMotion = mc.curve(d=1,p=[(0, 0, 108), (36, 0, 36), (12, 0, 36), (12, 0, 12), (36, 0, 12), (36, 0, 24), (60, 0, 0),
                             (36, 0, -24), (36, 0, -12), (12, 0, -12), (12, 0, -36), (24, 0, -36), (0, 0, -60), (-24, 0, -36), (-12, 0, -36), (-12, 0, -12),
                             (-36, 0, -12), (-36, 0, -24), (-60, 0, 0), (-36, 0, 24),(-36, 0, 12), (-12, 0, 12), (-12, 0, 36), (-36, 0, 36), (0, 0, 108)], n='HipsDirection')

    AS_BonesArmLegNeckList = ['Scapula_R', 'Shoulder1_R', 'Elbow_R', 'Wrist_R', 'MiddleFinger1_R', 'MiddleFinger2_R','MiddleFinger3_R', 'ThumbFinger1_R', 'ThumbFinger2_R', 'ThumbFinger3_R', 'IndexFinger1_R',
                              'IndexFinger2_R', 'IndexFinger3_R','Cup_R', 'PinkyFinger1_R', 'PinkyFinger2_R', 'PinkyFinger3_R', 'RingFinger1_R',
                              'RingFinger2_R', 'RingFinger3_R', 'Scapula_L', 'Shoulder1_L', 'Elbow_L', 'Wrist_L','MiddleFinger1_L', 'MiddleFinger2_L', 'MiddleFinger3_L',
                              'ThumbFinger1_L', 'ThumbFinger2_L', 'ThumbFinger3_L', 'IndexFinger1_L', 'IndexFinger2_L','IndexFinger3_L', 'Cup_L', 'PinkyFinger1_L', 'PinkyFinger2_L', 'PinkyFinger3_L',
                              'RingFinger1_L', 'RingFinger2_L', 'RingFinger3_L','Hip_L', 'Knee_L', 'Ankle_L', 'Toes_L', 'ToesEnd_L', 'Hip_R', 'Knee_R', 'Ankle_R',
                              'Toes_R', 'ToesEnd_R', 'Neck_M', 'Head_M']

    AGS_BonesArmLegNeckList = ['RightShoulder', 'RightArm', 'RightForeArm', 'RightHand', 'RightHandMiddle1','RightHandMiddle2', 'RightHandMiddle3', 'RightHandThumb1', 'RightHandThumb2',
                               'RightHandThumb3', 'RightHandIndex1', 'RightHandIndex2','RightHandIndex3', 'RightHandMetacarpal', 'RightHandPinky1', 'RightHandPinky2',
                               'RightHandPinky3', 'RightHandRing1', 'RightHandRing2', 'RightHandRing3', 'LeftShoulder','LeftArm', 'LeftForeArm', 'LeftHand', 'LeftHandMiddle1', 'LeftHandMiddle2',
                               'LeftHandMiddle3', 'LeftHandThumb1', 'LeftHandThumb2', 'LeftHandThumb3','LeftHandIndex1', 'LeftHandIndex2', 'LeftHandIndex3', 'LeftHandMetacarpal',
                               'LeftHandPinky1', 'LeftHandPinky2', 'LeftHandPinky3', 'LeftHandRing1', 'LeftHandRing2','LeftHandRing3',
                               'LeftUpLeg', 'LeftLeg', 'LeftFoot', 'LeftToeBase', 'LeftToeBaseEnd', 'RightUpLeg','RightLeg', 'RightFoot', 'RightToeBase', 'RightToeBaseEnd', 'Neck', 'Head']

    for i, item in enumerate(AS_BonesArmLegNeckList):
        mc.parentConstraint(item, AGS_BonesArmLegNeckList[i], mo=True)
        mc.scaleConstraint(item, AGS_BonesArmLegNeckList[i], mo=True)
        mc.setAttr(AGS_BonesArmLegNeckList[i] + '_parentConstraint1.interpType', 2)

    # parentConstraint ik
    mc.parentConstraint('LeftHand', 'LeftHand_IK', mo=True)
    mc.parentConstraint('RightHand', 'RightHand_IK', mo=True)
    mc.parentConstraint('LeftFoot', 'LeftFoot_IK', mo=True)
    mc.parentConstraint('RightFoot', 'RightFoot_IK', mo=True)
    mc.parentConstraint('Head', 'Head_IK', mo=True)

    mc.parent('LeftFoot_IK', 'LeftHand_IK', 'Head_IK', 'Camera', 'Attach', 'RightFoot_IK', 'RightHand_IK','HipsTranslation')
    mc.pointConstraint(RootMotion, 'HipsTranslation', mo=True)
    mc.parent(RootMotion, 'Main')

    # clean up
    mc.delete('HeadEnd_M', 'ThumbFinger4_L', 'IndexFinger4_L', 'MiddleFinger4_L', 'RingFinger4_L', 'PinkyFinger4_L','ThumbFinger4_R', 'IndexFinger4_R','MiddleFinger4_R', 'RingFinger4_R', 'PinkyFinger4_R')

    print('Mirror and clean up complete -> 01')
    ###########################################################################################################
    ########################################### extras controls  ##############################################
    ###########################################################################################################
    ###################### Left Side

    LeftExtrasBn_List = ['LeftWristHelper', 'LeftForeArmRoll', 'LeftLowerarm', 'LeftShoulderarmHelper_02','LeftArmRoll', 'LeftShoulderarmHelper_01', 'LeftUpperarm',
                         'LeftUpperlegHelper', 'LeftUpperlegHelperUp', 'LeftUpLegRoll', 'LeftUpperlegHelperDn','LeftLowerleg', 'LeftLegRoll', 'LeftAnkleHelper']

    def controlColor(s, c):  # yellow 17, red 13, blue 6, light blue 18, light red 4, light green 23
        mc.setAttr(s + '.overrideEnabled', 1)
        mc.setAttr(s + '.overrideColor', c)

    for LeftExtrasBn in (LeftExtrasBn_List):
        crv = mc.circle(n=LeftExtrasBn + '_ctrl', radius=4, ch=False, nr=(1, 0, 0))
        spaceCrv = mc.group(crv, n=LeftExtrasBn + '_ctrlSpace')
        masterSpace = mc.group(spaceCrv, n=LeftExtrasBn + '_ctrlMasterSpace')
        mc.delete(mc.parentConstraint(LeftExtrasBn, masterSpace, mo=False))

    for mC in (LeftExtrasBn_List):
        mirrorCtrl = mc.curve(d=1, p=[(-0.0133947, 0, 0.351564), (-0.0130162, 0, 0.916036), (-0.126636, 0, 0.85811),(0, 0, 1.111383), (0.126636, 0, 0.85811), (0.0121104, 0, 0.916036),
                                      (0.0121104, 0, 0.351564), (0.0935195, 0, 0.281599), (0.0935195, 0, 0.195095),(-0.0935195, 0, 0.195095), (-0.0935195, 0, 0.281599), (-0.0133947, 0, 0.351564)],n=mC + '_mCtrl')
        mc.scale(6, 6, 6, mirrorCtrl)
        mc.makeIdentity(mirrorCtrl, apply=True, scale=True)
        mirrorCtrlSpace = mc.group(em=True, n=mC + '_mCtrlSpace')
        mirrorCtrlMasterSpace = mc.group(em=True, n=mC + '_mCtrlMasterSpace')
        mc.parent(mirrorCtrl, mirrorCtrlSpace), mc.parent(mirrorCtrlSpace, mirrorCtrlMasterSpace)
        mc.delete(mc.parentConstraint(mC, mirrorCtrlMasterSpace, mo=False))

    LeftMirrorCtrl_List = ['LeftWristHelper_mCtrl', 'LeftForeArmRoll_mCtrl', 'LeftLowerarm_mCtrl','LeftShoulderarmHelper_02_mCtrl', 'LeftArmRoll_mCtrl', 'LeftShoulderarmHelper_01_mCtrl',
                           'LeftUpperarm_mCtrl', 'LeftUpperlegHelper_mCtrl', 'LeftUpperlegHelperUp_mCtrl','LeftUpLegRoll_mCtrl', 'LeftUpperlegHelperDn_mCtrl', 'LeftLowerleg_mCtrl',
                           'LeftLegRoll_mCtrl', 'LeftAnkleHelper_mCtrl']

    LeftMirrorCtrl_Space_List = ['LeftWristHelper_mCtrlSpace', 'LeftForeArmRoll_mCtrlSpace', 'LeftLowerarm_mCtrlSpace','LeftShoulderarmHelper_02_mCtrlSpace', 'LeftArmRoll_mCtrlSpace',
                                 'LeftShoulderarmHelper_01_mCtrlSpace','LeftUpperarm_mCtrlSpace', 'LeftUpperlegHelper_mCtrlSpace',
                                 'LeftUpperlegHelperUp_mCtrlSpace', 'LeftUpLegRoll_mCtrlSpace','LeftUpperlegHelperDn_mCtrlSpace', 'LeftLowerleg_mCtrlSpace', 'LeftLegRoll_mCtrlSpace','LeftAnkleHelper_mCtrlSpace']

    LeftMirrorCtrl_masterSpace_List = ['LeftWristHelper_mCtrlMasterSpace', 'LeftForeArmRoll_mCtrlMasterSpace','LeftLowerarm_mCtrlMasterSpace', 'LeftShoulderarmHelper_02_mCtrlMasterSpace',
                                       'LeftArmRoll_mCtrlMasterSpace', 'LeftShoulderarmHelper_01_mCtrlMasterSpace','LeftUpperarm_mCtrlMasterSpace', 'LeftUpperlegHelper_mCtrlMasterSpace',
                                       'LeftUpperlegHelperUp_mCtrlMasterSpace', 'LeftUpLegRoll_mCtrlMasterSpace','LeftUpperlegHelperDn_mCtrlMasterSpace', 'LeftLowerleg_mCtrlMasterSpace',
                                       'LeftLegRoll_mCtrlMasterSpace', 'LeftAnkleHelper_mCtrlMasterSpace']

    LeftCtrl_List = ['LeftWristHelper_ctrl', 'LeftForeArmRoll_ctrl', 'LeftLowerarm_ctrl', 'LeftShoulderarmHelper_02_ctrl', 'LeftArmRoll_ctrl', 'LeftShoulderarmHelper_01_ctrl',
                     'LeftUpperarm_ctrl', 'LeftUpperlegHelper_ctrl','LeftUpperlegHelperUp_ctrl', 'LeftUpLegRoll_ctrl', 'LeftUpperlegHelperDn_ctrl',
                     'LeftLowerleg_ctrl', 'LeftLegRoll_ctrl', 'LeftAnkleHelper_ctrl']

    LeftCtrl_Space_List = ['LeftWristHelper_ctrlSpace', 'LeftForeArmRoll_ctrlSpace', 'LeftLowerarm_ctrlSpace','LeftShoulderarmHelper_02_ctrlSpace', 'LeftArmRoll_ctrlSpace',
                           'LeftShoulderarmHelper_01_ctrlSpace','LeftUpperarm_ctrlSpace', 'LeftUpperlegHelper_ctrlSpace', 'LeftUpperlegHelperUp_ctrlSpace',
                           'LeftUpLegRoll_ctrlSpace', 'LeftUpperlegHelperDn_ctrlSpace', 'LeftLowerleg_ctrlSpace','LeftLegRoll_ctrlSpace', 'LeftAnkleHelper_ctrlSpace']

    LeftCtrl_masterSpace_List = ['LeftWristHelper_ctrlMasterSpace', 'LeftForeArmRoll_ctrlMasterSpace','LeftLowerarm_ctrlMasterSpace', 'LeftShoulderarmHelper_02_ctrlMasterSpace',
                                 'LeftArmRoll_ctrlMasterSpace', 'LeftShoulderarmHelper_01_ctrlMasterSpace','LeftUpperarm_ctrlMasterSpace', 'LeftUpperlegHelper_ctrlMasterSpace',
                                 'LeftUpperlegHelperUp_ctrlMasterSpace', 'LeftUpLegRoll_ctrlMasterSpace','LeftUpperlegHelperDn_ctrlMasterSpace', 'LeftLowerleg_ctrlMasterSpace',
                                 'LeftLegRoll_ctrlMasterSpace', 'LeftAnkleHelper_ctrlMasterSpace']

    ############## parent ctrls to mirror controls

    for i, item in enumerate(LeftCtrl_masterSpace_List):
        mc.parent(item, LeftMirrorCtrl_List[i])

    #################### parent / scale constraint from  extra ctrls to extra bones - Left Side

    for const, item in enumerate(LeftCtrl_List):
        mc.parentConstraint(item, LeftExtrasBn_List[const], mo=True)
        mc.scaleConstraint(item, LeftExtrasBn_List[const], mo=True)
        mc.setAttr(LeftExtrasBn_List[const] + '_parentConstraint1.interpType', 2)

    #################### Right Side

    RightExtrasBn_List = ['RightWristHelper', 'RightForeArmRoll', 'RightLowerarm', 'RightShoulderarmHelper_02','RightArmRoll', 'RightShoulderarmHelper_01', 'RightUpperarm',
                          'RightUpperlegHelper', 'RightUpperlegHelperUp', 'RightUpLegRoll', 'RightUpperlegHelperDn','RightLowerleg', 'RightLegRoll', 'RightAnkleHelper']

    for RightExtrasBn in (RightExtrasBn_List):
        crv = mc.circle(n=RightExtrasBn + '_ctrl', radius=4, ch=False, nr=(1, 0, 0))
        spaceCrv = mc.group(crv, n=RightExtrasBn + '_ctrlSpace')
        constCrv = mc.group(spaceCrv, n=RightExtrasBn + '_const')
        masterConst = mc.group(constCrv, n=RightExtrasBn + '_MasterConst')
        mc.delete(mc.parentConstraint(RightExtrasBn, masterConst, mo=False))

    RightMasterConst_List = ['RightWristHelper_MasterConst', 'RightForeArmRoll_MasterConst','RightLowerarm_MasterConst', 'RightShoulderarmHelper_02_MasterConst',
                             'RightArmRoll_MasterConst', 'RightShoulderarmHelper_01_MasterConst','RightUpperarm_MasterConst', 'RightUpperlegHelper_MasterConst',
                             'RightUpperlegHelperUp_MasterConst', 'RightUpLegRoll_MasterConst','RightUpperlegHelperDn_MasterConst', 'RightLowerleg_MasterConst',
                             'RightLegRoll_MasterConst', 'RightAnkleHelper_MasterConst']

    RightConst_List = ['RightWristHelper_const', 'RightForeArmRoll_const', 'RightLowerarm_const','RightShoulderarmHelper_02_const', 'RightArmRoll_const', 'RightShoulderarmHelper_01_const',
                       'RightUpperarm_const', 'RightUpperlegHelper_const', 'RightUpperlegHelperUp_const','RightUpLegRoll_const',
                       'RightUpperlegHelperDn_const', 'RightLowerleg_const', 'RightLegRoll_const','RightAnkleHelper_const']

    RightCtrl_Space = ['RightWristHelper_ctrlSpace', 'RightForeArmRoll_ctrlSpace', 'RightLowerarm_ctrlSpace','RightShoulderarmHelper_02_ctrlSpace', 'RightArmRoll_ctrlSpace',
                       'RightShoulderarmHelper_01_ctrlSpace', 'RightUpperarm_ctrlSpace','RightUpperlegHelper_ctrlSpace', 'RightUpperlegHelperUp_ctrlSpace',
                       'RightUpperlegHelperDn_ctrlSpace', 'RightLowerleg_ctrlSpace', 'RightLegRoll_ctrlSpace','RightAnkleHelper_ctrlSpace']

    RightCtrl_List = ['RightWristHelper_ctrl', 'RightForeArmRoll_ctrl', 'RightLowerarm_ctrl','RightShoulderarmHelper_02_ctrl', 'RightArmRoll_ctrl', 'RightShoulderarmHelper_01_ctrl',
                      'RightUpperarm_ctrl', 'RightUpperlegHelper_ctrl', 'RightUpperlegHelperUp_ctrl', 'RightUpLegRoll_ctrl',
                      'RightUpperlegHelperDn_ctrl', 'RightLowerleg_ctrl', 'RightLegRoll_ctrl', 'RightAnkleHelper_ctrl']

    #################### parent / scale constraint from  extra ctrls to extra bones - Right Side

    for constR, item in enumerate(RightCtrl_List):
        mc.parentConstraint(item, RightExtrasBn_List[constR], mo=True)
        mc.scaleConstraint(item, RightExtrasBn_List[constR], mo=True)
        mc.setAttr(RightExtrasBn_List[constR] + '_parentConstraint1.interpType', 2)

    ####################### controls color

    for lCtrl in (LeftCtrl_List):
        controlColor(lCtrl, 18)

    for rCtrl in (RightCtrl_List):
        controlColor(rCtrl, 4)

    for mCtrl in (LeftMirrorCtrl_List):
        controlColor(mCtrl, 18)

    ###################### mirror controls connections

    transMD_list = []
    rotMD_List = []
    sclMD_List = []

    for i in (LeftMirrorCtrl_List):
        transMD = mc.createNode('multiplyDivide', n=i + '_Trans_MD')
        rotMD = mc.createNode('multiplyDivide', n=i + '_Rot_MD')
        sclMD = mc.createNode('multiplyDivide', n=i + '_Scl_MD')

        transMD_list.append(transMD)
        rotMD_List.append(rotMD)
        sclMD_List.append(sclMD)

        mc.setAttr(transMD + '.input2X', -1)
        mc.setAttr(transMD + '.input2Y', -1)
        mc.setAttr(transMD + '.input2Z', -1)

    ################################################# translation

    for transInput in range(len(LeftMirrorCtrl_List)):
        mc.connectAttr(LeftMirrorCtrl_List[transInput] + '.tx', transMD_list[transInput] + '.input1X')
        mc.connectAttr(LeftMirrorCtrl_List[transInput] + '.ty', transMD_list[transInput] + '.input1Y')
        mc.connectAttr(LeftMirrorCtrl_List[transInput] + '.tz', transMD_list[transInput] + '.input1Z')

    for transOutput in range(len(RightConst_List)):
        mc.connectAttr(transMD_list[transOutput] + '.outputX', RightConst_List[transOutput] + '.tx')
        mc.connectAttr(transMD_list[transOutput] + '.outputY', RightConst_List[transOutput] + '.ty')
        mc.connectAttr(transMD_list[transOutput] + '.outputZ', RightConst_List[transOutput] + '.tz')

    ############################################## rotation

    for rotInput in range(len(LeftMirrorCtrl_List)):
        mc.connectAttr(LeftMirrorCtrl_List[rotInput] + '.rx', rotMD_List[rotInput] + '.input1X')
        mc.connectAttr(LeftMirrorCtrl_List[rotInput] + '.ry', rotMD_List[rotInput] + '.input1Y')
        mc.connectAttr(LeftMirrorCtrl_List[rotInput] + '.rz', rotMD_List[rotInput] + '.input1Z')

    for rotOutput in range(len(RightConst_List)):
        mc.connectAttr(rotMD_List[rotOutput] + '.outputX', RightConst_List[rotOutput] + '.rx')
        mc.connectAttr(rotMD_List[rotOutput] + '.outputY', RightConst_List[rotOutput] + '.ry')
        mc.connectAttr(rotMD_List[rotOutput] + '.outputZ', RightConst_List[rotOutput] + '.rz')

    ################################################ scale

    for sclInput in range(len(LeftMirrorCtrl_List)):
        mc.connectAttr(LeftMirrorCtrl_List[sclInput] + '.sx', sclMD_List[sclInput] + '.input1X')
        mc.connectAttr(LeftMirrorCtrl_List[sclInput] + '.sy', sclMD_List[sclInput] + '.input1Y')
        mc.connectAttr(LeftMirrorCtrl_List[sclInput] + '.sz', sclMD_List[sclInput] + '.input1Z')

    for sclOutput in range(len(RightConst_List)):
        mc.connectAttr(sclMD_List[sclOutput] + '.outputX', RightConst_List[sclOutput] + '.sx')
        mc.connectAttr(sclMD_List[sclOutput] + '.outputY', RightConst_List[sclOutput] + '.sy')
        mc.connectAttr(sclMD_List[sclOutput] + '.outputZ', RightConst_List[sclOutput] + '.sz')

    ######################### parentConstraint per segments

    Left_UpperArm_List = ['LeftShoulderarmHelper_02_mCtrlMasterSpace', 'LeftArmRoll_mCtrlMasterSpace', 'LeftShoulderarmHelper_01_mCtrlMasterSpace', 'LeftUpperarm_mCtrlMasterSpace']
    Left_lowerArm_list = ['LeftWristHelper_mCtrlMasterSpace', 'LeftForeArmRoll_mCtrlMasterSpace', 'LeftLowerarm_mCtrlMasterSpace']
    Left_UpperLeg_list = ['LeftUpperlegHelperDn_mCtrlMasterSpace', 'LeftUpLegRoll_mCtrlMasterSpace', 'LeftUpperlegHelperUp_mCtrlMasterSpace', 'LeftUpperlegHelper_mCtrlMasterSpace']
    Left_lowerLeg_list = ['LeftAnkleHelper_mCtrlMasterSpace', 'LeftLegRoll_mCtrlMasterSpace', 'LeftLowerleg_mCtrlMasterSpace']
    Right_UpperArm_List = ['RightShoulderarmHelper_02_MasterConst', 'RightArmRoll_MasterConst', 'RightShoulderarmHelper_01_MasterConst', 'RightUpperarm_MasterConst']
    Right_LowerArm_List = ['RightWristHelper_MasterConst', 'RightForeArmRoll_MasterConst', 'RightLowerarm_MasterConst']
    Right_UpperLeg_list = ['RightUpperlegHelperDn_MasterConst', 'RightUpLegRoll_MasterConst', 'RightUpperlegHelperUp_MasterConst', 'RightUpperlegHelper_MasterConst']
    Right_LowerLeg_List = ['RightAnkleHelper_MasterConst', 'RightLegRoll_MasterConst', 'RightLowerleg_MasterConst']

    for Left_UpperArm in (Left_UpperArm_List):
        mc.parentConstraint('LeftArm', Left_UpperArm, mo=True)
        mc.setAttr(Left_UpperArm + '_parentConstraint1.interpType', 2)

    for Left_lowerArm in (Left_lowerArm_list):
        mc.parentConstraint('LeftForeArm', Left_lowerArm, mo=True)
        mc.setAttr(Left_lowerArm + '_parentConstraint1.interpType', 2)

    for Left_UpperLeg in (Left_UpperLeg_list):
        mc.parentConstraint('LeftUpLeg', Left_UpperLeg, mo=True)
        mc.setAttr(Left_UpperLeg + '_parentConstraint1.interpType', 2)

    for Left_lowerLeg in (Left_lowerLeg_list):
        mc.parentConstraint('LeftLeg', Left_lowerLeg, mo=True)
        mc.setAttr(Left_lowerLeg + '_parentConstraint1.interpType', 2)

    for Right_UpperArm in (Right_UpperArm_List):
        mc.parentConstraint('RightArm', Right_UpperArm, mo=True)
        mc.setAttr(Right_UpperArm + '_parentConstraint1.interpType', 2)

    for Right_LowerArm in (Right_LowerArm_List):
        mc.parentConstraint('RightForeArm', Right_LowerArm, mo=True)
        mc.setAttr(Right_LowerArm + '_parentConstraint1.interpType', 2)

    for Right_UpperLeg in (Right_UpperLeg_list):
        mc.parentConstraint('RightUpLeg', Right_UpperLeg, mo=True)
        mc.setAttr(Right_UpperLeg + '_parentConstraint1.interpType', 2)

    for Right_LowerLeg in (Right_LowerLeg_List):
        mc.parentConstraint('RightLeg', Right_LowerLeg, mo=True)
        mc.setAttr(Right_LowerLeg + '_parentConstraint1.interpType', 2)

    #################### connections from proxyBones to masterSpace ctrls - Left Side

    LeftCtrl_UpperArm_List = ['LeftArmRoll_mCtrlSpace', 'LeftShoulderarmHelper_02_mCtrlSpace']

    for lUpperArm, item in enumerate(LeftCtrl_UpperArm_List):
        rotMD = mc.createNode('multiplyDivide', n=item + '_MD')
        mc.setAttr(rotMD + '.input2X', -1)

        mc.connectAttr('Shoulder1Part1_L.rx', rotMD + '.input1X')
        mc.connectAttr(rotMD + '.outputX', LeftCtrl_UpperArm_List[lUpperArm] + '.rotateX')
    mc.setAttr("LeftShoulderarmHelper_02_mCtrlSpace_MD.input2X", -1.5)

    LeftCtrl_LowerArm_List = ['LeftForeArmRoll_mCtrlSpace', 'LeftWristHelper_mCtrlSpace']

    for lLowerArm, item in enumerate(LeftCtrl_LowerArm_List):
        rotMD = mc.createNode('multiplyDivide', n=item + '_MD')
        mc.setAttr(rotMD + '.input2X', -1)

        mc.connectAttr('ElbowPart1_L.rx', rotMD + '.input1X')
        mc.connectAttr(rotMD + '.outputX', LeftCtrl_LowerArm_List[lLowerArm] + '.rx')
    mc.setAttr('LeftWristHelper_mCtrlSpace_MD.input2X', -1.5)

    LeftCtrl_UpperLeg_List = ['LeftUpLegRoll_mCtrlSpace', 'LeftUpperlegHelperDn_mCtrlSpace']

    for lUpperLeg, item in enumerate(LeftCtrl_UpperLeg_List):
        rotMD = mc.createNode('multiplyDivide', n=item + '_MD')
        mc.setAttr(rotMD + '.input2X', -1)

        mc.connectAttr('HipPart1_L.rx', rotMD + '.input1X')
        mc.connectAttr(rotMD + '.outputX', LeftCtrl_UpperLeg_List[lUpperLeg] + '.rx')
    mc.setAttr('LeftUpperlegHelperDn_mCtrlSpace_MD.input2X', -1.5)

    LeftCtrl_LowerLeg_List = ['LeftLegRoll_mCtrlSpace', 'LeftAnkleHelper_mCtrlSpace']

    for lLowerLeg, item in enumerate(LeftCtrl_LowerLeg_List):
        rotMD = mc.createNode('multiplyDivide', n=item + '_MD')
        mc.setAttr(rotMD + '.input2X', -1)

        mc.connectAttr('KneePart1_L.rx', rotMD + '.input1X')
        mc.connectAttr(rotMD + '.outputX', LeftCtrl_LowerLeg_List[lLowerLeg] + '.rx')
    mc.setAttr('LeftAnkleHelper_mCtrlSpace_MD.input2X', -1.5)

    #################### connections from proxyBones to masterSpace ctrls - Right Side

    RightCtrl_UpperArm_List = ['RightArmRoll_ctrlSpace', 'RightShoulderarmHelper_02_ctrlSpace']

    for rUpperArm, item in enumerate(RightCtrl_UpperArm_List):
        rotMD = mc.createNode('multiplyDivide', n=item + '_MD')
        mc.setAttr(rotMD + '.input2X', -1)

        mc.connectAttr('Shoulder1Part1_R.rx', rotMD + '.input1X')
        mc.connectAttr(rotMD + '.outputX', RightCtrl_UpperArm_List[rUpperArm] + '.rotateX')
    mc.setAttr("RightShoulderarmHelper_02_ctrlSpace_MD.input2X", -1.5)

    RightCtrl_LowerArm_List = ['RightForeArmRoll_ctrlSpace', 'RightWristHelper_ctrlSpace']

    for rLowerArm, item in enumerate(RightCtrl_LowerArm_List):
        rotMD = mc.createNode('multiplyDivide', n=item + '_MD')
        mc.setAttr(rotMD + '.input2X', -1)

        mc.connectAttr('ElbowPart1_R.rx', rotMD + '.input1X')
        mc.connectAttr(rotMD + '.outputX', RightCtrl_LowerArm_List[rLowerArm] + '.rx')
    mc.setAttr('RightWristHelper_ctrlSpace_MD.input2X', -1.5)

    RightCtrl_UpperLeg_List = ['RightUpLegRoll_ctrlSpace', 'RightUpperlegHelperDn_ctrlSpace']

    for rUpperLeg, item in enumerate(RightCtrl_UpperLeg_List):
        rotMD = mc.createNode('multiplyDivide', n=item + '_MD')
        mc.setAttr(rotMD + '.input2X', -1)

        mc.connectAttr('HipPart1_R.rx', rotMD + '.input1X')
        mc.connectAttr(rotMD + '.outputX', RightCtrl_UpperLeg_List[rUpperLeg] + '.rx')
    mc.setAttr('RightUpperlegHelperDn_ctrlSpace_MD.input2X', -1.5)

    RightCtrl_LowerLeg_List = ['RightLegRoll_ctrlSpace', 'RightAnkleHelper_ctrlSpace']

    for rLowerLeg, item in enumerate(RightCtrl_LowerLeg_List):
        rotMD = mc.createNode('multiplyDivide', n=item + '_MD')
        mc.setAttr(rotMD + '.input2X', -1)

        mc.connectAttr('KneePart1_R.rx', rotMD + '.input1X')
        mc.connectAttr(rotMD + '.outputX', RightCtrl_LowerLeg_List[rLowerLeg] + '.rx')
    mc.setAttr('RightAnkleHelper_ctrlSpace_MD.input2X', -1.5)

    print('Extras bones + controls connection completed -> 02')

    #####################################################################################################################################
    ######################################################### hand gimbal controls

    LeftGimbalCtrl_crv = mc.curve(d=True, p=(
    (-0.5, 0.5, 0.00702787), (0.5, 0.5, 0.00702787), (0.5, -0.5, 0.00702787), (-0.5, -0.5, 0.00702787),(-0.5, 0.5, 0.00702787)), n='IKLocalArm_L')
    LeftGimbalCtrl_space = mc.group(em=True, n='IKLocalArm_L_ctrlSpace')
    mc.parent(LeftGimbalCtrl_crv, LeftGimbalCtrl_space), mc.select(d=True)

    RightGimbalCtrl_crv = mc.curve(d=True, p=(
    (-0.5, 0.5, 0.00702787), (0.5, 0.5, 0.00702787), (0.5, -0.5, 0.00702787), (-0.5, -0.5, 0.00702787),(-0.5, 0.5, 0.00702787)), n='IKLocalArm_R')
    RightGimbalCtrl_space = mc.group(em=True, n='IKLocalArm_R_ctrlSpace')
    mc.parent(RightGimbalCtrl_crv, RightGimbalCtrl_space), mc.select(d=True)

    mc.delete(mc.parentConstraint('IKArm_L', LeftGimbalCtrl_space, mo=False)), mc.delete(mc.parentConstraint('IKArm_R', RightGimbalCtrl_space, mo=False))

    gimbalCtrl_cv_list = ['IKLocalArm_L.cv[0:4]', 'IKLocalArm_R.cv[0:4]']
    mc.select(gimbalCtrl_cv_list)
    mc.rotate(0, 90, 0, fo=True)
    mc.select(d=True)

    mc.parent(LeftGimbalCtrl_space, 'IKFKAlignedArm_L'), mc.parent(RightGimbalCtrl_space, 'IKFKAlignedArm_R')
    # mc.delete('IKXWrist_L_orientConstraint1', 'IKXWrist_R_orientConstraint1')
    mc.orientConstraint(LeftGimbalCtrl_crv, 'IKXWrist_L', mo=True), mc.orientConstraint(RightGimbalCtrl_crv,'IKXWrist_R', mo=True)

    gimbalCtrl_list = [LeftGimbalCtrl_crv, RightGimbalCtrl_crv]

    for i in gimbalCtrl_list:
        mc.setAttr(i + '.tx', l=True, k=False, ch=False)
        mc.setAttr(i + '.ty', l=True, k=False, ch=False)
        mc.setAttr(i + '.tz', l=True, k=False, ch=False)
        mc.setAttr(i + '.sx', l=True, k=False, ch=False)
        mc.setAttr(i + '.sy', l=True, k=False, ch=False)
        mc.setAttr(i + '.sz', l=True, k=False, ch=False)
        mc.setAttr(i + '.v', l=True, k=False, ch=False)

    controlColor(LeftGimbalCtrl_crv, 13)
    controlColor(RightGimbalCtrl_crv, 6)

    mc.select(d=True)

    print('Gimbal control completed -> 03')
    ##################################### neck twist
    MDNode = mc.createNode('multiplyDivide', n='neckTwist_MD')
    mc.connectAttr('Head.rx', MDNode + '.input1X')
    mc.connectAttr(MDNode + '.outputX', 'NeckScale.ry')
    mc.setAttr(MDNode + '.input2X', 0.5)

    ################################# clean up

    ExtraCtrl_GRP = mc.group(LeftMirrorCtrl_masterSpace_List, RightMasterConst_List, n='extraControls_GRP')
    mc.parent(ExtraCtrl_GRP, 'MotionSystem')
    mc.select(d=True)

    mc.parent('LeftScapulaUpVolume', 'RightScapulaUpVolume', 'Spine2')
    mc.parent('LeftButtock', 'RightButtock', 'Hips'), mc.parent('HipsExpand', 'Hips')

    mc.addAttr('Main', ln='extraCtrls', at='bool', k=True)
    mc.connectAttr('Main.extraCtrls', 'extraControls_GRP.v')
    mc.select('MainShape.cv[0:7]'), mc.scale(2.1, 2.1, 2.1, ocp=True), mc.move(0, 0, 21, r=True, os=True, wd=True)

    mc.select(d=True)

    print('Neck twist completed -> 04')
    ################################################ scale cv's

    mc.select('PoleLeg_L.cv[0:7]', 'PoleLeg_R.cv[0:7]', 'PoleArm_R.cv[0:7]', 'PoleArm_L.cv[0:7]'), mc.scale(9, 9, 9,ocp=True)
    mc.select('IKLeg_RShape.cv[0:15]', 'IKLeg_LShape.cv[0:15]'), mc.scale(9.5, 1, 1, ocp=True)
    mc.select('IKLeg_RShape.cv[3:6]', 'IKLeg_RShape.cv[9:12]', 'IKLeg_LShape.cv[0:2]', 'IKLeg_LShape.cv[7:8]', 'IKLeg_LShape.cv[13:15]'), mc.move(0, 0, -7, r=True, os=True, wd=True)
    mc.select('IKLeg_RShape.cv[2]', 'IKLeg_RShape.cv[7]', 'IKLeg_RShape.cv[14:15]', 'IKLeg_LShape.cv[4:5]','IKLeg_LShape.cv[9]', 'IKLeg_LShape.cv[12]'), mc.move(0, 0, 9.5, r=True, os=True, wd=True)
    mc.select('IKToes_LShape.cv[0:7]', 'RollToes_LShape.cv[0:15]', 'RollToesEnd_LShape.cv[0:15]','RollToesEnd_RShape.cv[0:15]', 'RollToes_RShape.cv[0:15]', 'RollHeel_RShape.cv[0:15]','IKToes_RShape.cv[0:7]',
              'RollHeel_LShape.cv[0:15]'), mc.scale(9.3, 9.3, 9.3, ocp=True), mc.select('RollHeel_LShape.cv[0:15]','RollHeel_RShape.cv[0:15]'), mc.move(0, 3.5, -3, r=True, os=True, wd=True)
    mc.select('RollToes_RShape.cv[0:15]', 'RollToes_LShape.cv[0:15]', 'IKToes_LShape.cv[0:7]','IKToes_RShape.cv[0:7]'), mc.scale(1.5, 1.5, 1.5, ocp=True), mc.move(0, 2.6, 1.2, r=True, os=True, wd=True)
    mc.select('FKIKLeg_L.cv[0:11]'), mc.scale(2.3, 2.3, 2.3, ocp=True), mc.move(17, 0, 0, r=True, os=True,wd=True), mc.select('FKIKLeg_R.cv[0:11]'), mc.scale(2.3, 2.3, 2.3, ocp=True), mc.move(-17, 0, 0, r=True, os=True, wd=True)
    mc.select('IKArm_LShape.cv[0:15]', 'IKArm_RShape.cv[0:15]', 'IKLocalArm_R.cv[0:4]','IKLocalArm_L.cv[0:4]'), mc.scale(8, 8, 8, ocp=True), mc.scale(0.3, 1, 1, ocp=True)
    mc.select('FKKnee_LShape.cv[0:7]', 'FKKnee_RShape.cv[0:7]'), mc.scale(11.5, 11.5, 11.5, ocp=True)
    mc.select('FKAnkle_LShape.cv[0:7]', 'FKAnkle_RShape.cv[0:7]'), mc.scale(12.5, 12.5, 12.5, ocp=True)
    mc.select('FKToes_LShape.cv[0:7]', 'FKToes_RShape.cv[0:7]'), mc.scale(13, 13, 13, ocp=True), mc.move(0, 3, 0,r=True)
    mc.select('FKHip_LShape.cv[0:7]', 'FKHip_RShape.cv[0:7]'), mc.scale(10.3, 10.3, 10.3, ocp=True), mc.rotate(0, -28,0,ocp=True), mc.move( 0, -2.8, 0, r=True)
    mc.select('FKIKSpine_M.cv[0:11]'), mc.scale(2, 2, 2, ocp=True), mc.move(20, 0, 0, r=True, os=True, wd=True)
    mc.select('FKSpine1_MShape.cv[0:7]', 'FKRoot_MShape.cv[0:7]', 'FKChest_MShape.cv[0:7]','FKSpine2_MShape.cv[0:7]'), mc.scale(12, 12, 12, ocp=True)
    mc.select('HipSwinger_M.cv[0:7]'), mc.rotate(0, 0, 90, ocp=True), mc.move(2.5, 0, 0, r=True), mel.eval("CenterPivot"), mc.scale(30, 30, 30, ocp=True)
    mc.select('RootX_MShape.cv[0:6]', 'RootX_MShape3.cv[0:6]', 'RootX_MShape1.cv[0:6]','RootX_MShape2.cv[0:6]'), mc.scale(13, 13, 13, ocp=True)
    mc.select('IKSpine2_MShape.cv[0:7]', 'IKSpine1_MShape.cv[0:15]', 'IKSpine3_MShape.cv[0:15]','IKhybridSpine3_MShape.cv[0:15]', 'IKhybridSpine2_MShape.cv[0:15]','IKhybridSpine1_MShape.cv[0:15]'), mc.scale(9, 9, 9, ocp=True)
    mc.select('FKIKArm_R.cv[0:11]', 'FKIKArm_L.cv[0:11]'), mc.scale(2, 2, 2, ocp=True), mc.select('FKIKArm_L.cv[0:11]'), mc.move(8.9, 8.2, 0, r=True, os=True, wd=True), mc.select('FKIKArm_R.cv[0:11]'), mc.move(-8.9, 8.2, 0, r=True, os=True, wd=True)
    mc.select('FKNeck_MShape.cv[0:7]'), mc.scale(21.6, 21.6, 21.6, ocp=True), mc.select('FKNeck_MShape.cv[1]','FKNeck_MShape.cv[5]'), mc.move(4.1, 0, 0, r=True, os=True, wd=True)
    mc.select('FKHead_MShape.cv[0:7]'), mc.scale(13, 13, 13, ocp=True) # 0 174 -6.1
    mc.select('FKScapula_LShape.cv[0:20]'), mc.scale(12.5, 12.5, 12.5, ocp=True), mc.move(-8.5, 0, 0, r=True, os=True, wd=True), mc.scale(0.3, 1, 1,r=True, p=(0.5, 115.9, -8.8))
    mc.select('FKScapula_RShape.cv[0:20]'), mc.scale(12.5, 12.5, 12.5, ocp=True), mc.move(8.5, 0, 0, r=True, os=True, wd=True), mc.scale(0.3, 1, 1, r=True, p=(-10.5, 115.9, 8.8))
    mc.select('FKShoulder1_RShape.cv[0:7]', 'FKShoulder1_LShape.cv[0:7]', 'FKElbow_LShape.cv[0:7]', 'FKElbow_RShape.cv[0:7]', 'FKWrist_RShape.cv[0:7]', 'FKWrist_LShape.cv[0:7]'), mc.scale(10, 10, 10, ocp=True)
    mc.select('FKIndexFinger3_RShape.cv[0:7]', 'FKPinkyFinger1_RShape.cv[0:7]', 'FKIndexFinger3_LShape.cv[0:7]', 'FKPinkyFinger1_LShape.cv[0:7]', 'FKMiddleFinger2_RShape.cv[0:7]',
              'FKThumbFinger1_LShape.cv[0:7]', 'FKRingFinger2_LShape.cv[0:7]', 'FKIndexFinger2_LShape.cv[0:7]', 'FKIndexFinger2_RShape.cv[0:7]', 'FKThumbFinger2_LShape.cv[0:7]',
              'FKRingFinger3_RShape.cv[0:7]', 'FKThumbFinger3_RShape.cv[0:7]', 'FKCup_LShape.cv[0:7]', 'FKRingFinger2_RShape.cv[0:7]', 'FKPinkyFinger3_RShape.cv[0:7]', 'FKIndexFinger1_RShape.cv[0:7]',
              'FKMiddleFinger2_LShape.cv[0:7]', 'FKPinkyFinger3_LShape.cv[0:7]', 'FKMiddleFinger3_RShape.cv[0:7]', 'FKThumbFinger1_RShape.cv[0:7]', 'FKRingFinger1_RShape.cv[0:7]', 'FKPinkyFinger2_RShape.cv[0:7]',
              'FKPinkyFinger2_LShape.cv[0:7]', 'FKThumbFinger2_RShape.cv[0:7]', 'FKIndexFinger1_LShape.cv[0:7]', 'FKThumbFinger3_LShape.cv[0:7]', 'FKCup_RShape.cv[0:7]', 'FKMiddleFinger1_LShape.cv[0:7]',
              'FKRingFinger1_LShape.cv[0:7]', 'FKMiddleFinger3_LShape.cv[0:7]', 'FKRingFinger3_LShape.cv[0:7]', 'FKMiddleFinger1_RShape.cv[0:7]'), mc.scale(8, 8, 8, ocp=True)
    mc.select('FKCup_RShape.cv[0:7]', 'FKCup_LShape.cv[0:7]'), mc.scale(3, 3, 3, ocp=True)

    mc.select(d=True)

    ########################################################################################################################################################################################
    ################################################################################################### control colors

    AS_leftCtrl_list = ['FKScapula_LShape', 'FKAnkle_LShape', 'FKElbow_LShape', 'FKHip_LShape', 'FKIndexFinger1_LShape','FKIndexFinger2_LShape', 'FKIndexFinger3_LShape', 'FKKnee_LShape', 'FKMiddleFinger1_LShape',
                        'FKMiddleFinger3_LShape', 'FKPinkyFinger1_LShape', 'FKPinkyFinger2_LShape','FKPinkyFinger3_LShape', 'FKRingFinger1_LShape', 'FKRingFinger2_LShape', 'FKRingFinger3_LShape',
                        'FKShoulder1_LShape','FKThumbFinger2_LShape', 'FKThumbFinger3_LShape', 'FKToes_LShape', 'FKWrist_LShape','IKArm_LShape', 'curveShape16', 'PoleArm_LShape', 'IKLeg_LShape', 'RollHeel_LShape',
                        'RollToesEnd_LShape','RollToes_LShape', 'Fingers_LShape', 'PoleLeg_LShape', 'FKCup_LShape', 'FKMiddleFinger2_LShape','FKThumbFinger1_LShape', 'IKToes_LShape']
    for AS_lCtrls in AS_leftCtrl_list:
        controlColor(AS_lCtrls, 6)

    AS_rightCtrl_list = ['FKScapula_RShape', 'FKAnkle_RShape', 'FKElbow_RShape', 'FKHip_RShape','FKIndexFinger1_RShape', 'FKIndexFinger2_RShape', 'FKIndexFinger3_RShape', 'FKKnee_RShape','FKMiddleFinger1_RShape',
                         'FKMiddleFinger3_RShape', 'FKPinkyFinger1_RShape', 'FKPinkyFinger2_RShape','FKPinkyFinger3_RShape', 'FKRingFinger1_RShape', 'FKRingFinger2_RShape',
                         'FKRingFinger3_RShape', 'FKShoulder1_RShape','FKThumbFinger2_RShape', 'FKThumbFinger3_RShape', 'FKToes_RShape', 'FKWrist_RShape',
                         'IKArm_RShape', 'curveShape16', 'PoleArm_RShape', 'IKLeg_RShape', 'RollHeel_RShape','RollToesEnd_RShape','RollToes_RShape', 'Fingers_RShape', 'PoleLeg_RShape', 'FKCup_RShape',
                         'FKMiddleFinger2_RShape', 'FKThumbFinger1_RShape', 'IKToes_RShape']
    for AS_rCtrls in AS_rightCtrl_list:
        controlColor(AS_rCtrls, 13)

    print('Cvs scaled completed -> 05')
    ###############################################################################################################################################################
    ############################################################################ camera setup
    cam = mc.camera(n='Cine_Cam1', hfa=1.417, vfa=0.945, fl=20, lsr=1, fs=5, sa=144, coi=5), mc.rotate(0, -180, 0,fo=True)
    camCtrl = mc.circle(n='Camera_ctrl', ch=False)
    mc.select('Camera_ctrl.cv[0:7]'), mc.rotate(90, 0, 0, ocp=True), mc.scale(30, 30, 30, ocp=True), mc.scale(1, 1, 1.5,ocp=True)
    mc.select('Camera_ctrl.cv[4]', 'Camera_ctrl.cv[6]', 'Camera_ctrl.cv[0]', 'Camera_ctrl.cv[2]'), mc.scale(0.15, 1, 1,ocp=True), mc.scale(1, 1, 0.5, ocp=True)
    camCtrlSpace = mc.group(camCtrl, n='Camera_ctrlSpace')
    attCtrl = mc.circle(n='Attach_ctrl', ch=False)
    attCtrlSpace = mc.group(attCtrl, n='Attach_ctrlSpace')
    mc.select('Attach_ctrl.cv[0:7]'), mc.rotate(90, 0, 0, ocp=True), mc.scale(15, 15, 15, ocp=True), mc.select('Attach_ctrl.cv[1]'), mc.move(0, 0, 30, r=True, os=True, wd=True)
    mc.select('Attach_ctrl.cv[0]', 'Attach_ctrl.cv[2]'), mc.scale(0.3, 1, 1, ocp=True), mc.select(d=True)

    mc.parentConstraint('Camera', 'Cine_Cam1', mo=True)
    mc.parentConstraint('RootX_M', camCtrlSpace, mo=False)
    mc.parentConstraint('HipsDirection', camCtrlSpace, mo=False)
    mc.parentConstraint('Main', camCtrlSpace, mo=False)
    mc.parentConstraint('RootX_M', attCtrlSpace, mo=False)
    mc.parentConstraint('HipsDirection', attCtrlSpace, mo=False)
    mc.parentConstraint('Main', attCtrlSpace, mo=False)

    mc.setAttr('Camera_ctrlSpace_parentConstraint1.MainW2', 0)
    mc.setAttr('Camera_ctrlSpace_parentConstraint1.RootX_MW0', 0)
    mc.setAttr('Camera_ctrlSpace_parentConstraint1.HipsDirectionW1', 0)

    mc.setAttr('Attach_ctrlSpace_parentConstraint1.MainW2', 0)
    mc.setAttr('Attach_ctrlSpace_parentConstraint1.RootX_MW0', 0)
    mc.setAttr('Attach_ctrlSpace_parentConstraint1.HipsDirectionW1', 0)

    ctrls_list = ['Attach_ctrl', 'Camera_ctrl']
    for i in ctrls_list:
        mc.addAttr(i, longName='root_ctrl', min=0, max=1, defaultValue=1.0, k=True)
        mc.addAttr(i, longName='hips_translation_ctrl', min=0, max=1, defaultValue=0, k=True)
        mc.addAttr(i, longName='main_ctrl', min=0, max=1, defaultValue=0, k=True)

    mc.setDrivenKeyframe('Camera_ctrlSpace_parentConstraint1.MainW2', currentDriver='Camera_ctrl.main_ctrl')
    mc.setAttr('Camera_ctrl.main_ctrl', 1), mc.setAttr('Camera_ctrlSpace_parentConstraint1.MainW2', 1)
    mc.setDrivenKeyframe('Camera_ctrlSpace_parentConstraint1.MainW2', currentDriver='Camera_ctrl.main_ctrl')
    mc.setAttr('Camera_ctrl.main_ctrl', 0), mc.setAttr('Camera_ctrlSpace_parentConstraint1.MainW2', 0)
    mc.setDrivenKeyframe('Camera_ctrlSpace_parentConstraint1.MainW2', currentDriver='Camera_ctrl.main_ctrl')

    mc.setDrivenKeyframe('Camera_ctrlSpace_parentConstraint1.HipsDirectionW1',currentDriver='Camera_ctrl.hips_translation_ctrl')
    mc.setAttr('Camera_ctrl.hips_translation_ctrl', 1), mc.setAttr('Camera_ctrlSpace_parentConstraint1.HipsDirectionW1',1)
    mc.setDrivenKeyframe('Camera_ctrlSpace_parentConstraint1.HipsDirectionW1',currentDriver='Camera_ctrl.hips_translation_ctrl')
    mc.setAttr('Camera_ctrl.hips_translation_ctrl', 0), mc.setAttr('Camera_ctrlSpace_parentConstraint1.HipsDirectionW1',0)
    mc.setDrivenKeyframe('Camera_ctrlSpace_parentConstraint1.HipsDirectionW1',currentDriver='Camera_ctrl.hips_translation_ctrl')

    mc.setDrivenKeyframe('Camera_ctrlSpace_parentConstraint1.RootX_MW0', currentDriver='Camera_ctrl.root_ctrl')
    mc.setAttr('Camera_ctrl.root_ctrl', 1), mc.setAttr('Camera_ctrlSpace_parentConstraint1.RootX_MW0', 1)
    mc.setDrivenKeyframe('Camera_ctrlSpace_parentConstraint1.RootX_MW0', currentDriver='Camera_ctrl.root_ctrl')
    mc.setAttr('Camera_ctrl.root_ctrl', 0), mc.setAttr('Camera_ctrlSpace_parentConstraint1.RootX_MW0', 0)
    mc.setDrivenKeyframe('Camera_ctrlSpace_parentConstraint1.RootX_MW0', currentDriver='Camera_ctrl.root_ctrl')
    mc.setAttr('Camera_ctrl.main_ctrl', 1)

    mc.setDrivenKeyframe('Attach_ctrlSpace_parentConstraint1.MainW2', currentDriver='Attach_ctrl.main_ctrl')
    mc.setAttr('Attach_ctrl.main_ctrl', 1), mc.setAttr('Attach_ctrlSpace_parentConstraint1.MainW2', 1)
    mc.setDrivenKeyframe('Attach_ctrlSpace_parentConstraint1.MainW2', currentDriver='Attach_ctrl.main_ctrl')
    mc.setAttr('Attach_ctrl.main_ctrl', 0), mc.setAttr('Attach_ctrlSpace_parentConstraint1.MainW2', 0)
    mc.setDrivenKeyframe('Attach_ctrlSpace_parentConstraint1.MainW2', currentDriver='Attach_ctrl.main_ctrl')

    mc.setDrivenKeyframe('Attach_ctrlSpace_parentConstraint1.HipsDirectionW1', currentDriver='Attach_ctrl.hips_translation_ctrl')
    mc.setAttr('Attach_ctrl.hips_translation_ctrl', 1), mc.setAttr('Attach_ctrlSpace_parentConstraint1.HipsDirectionW1', 1)
    mc.setDrivenKeyframe('Attach_ctrlSpace_parentConstraint1.HipsDirectionW1', currentDriver='Attach_ctrl.hips_translation_ctrl')
    mc.setAttr('Attach_ctrl.hips_translation_ctrl', 0), mc.setAttr('Attach_ctrlSpace_parentConstraint1.HipsDirectionW1',0)
    mc.setDrivenKeyframe('Attach_ctrlSpace_parentConstraint1.HipsDirectionW1',currentDriver='Attach_ctrl.hips_translation_ctrl')

    mc.setDrivenKeyframe('Attach_ctrlSpace_parentConstraint1.RootX_MW0', currentDriver='Attach_ctrl.root_ctrl')
    mc.setAttr('Attach_ctrl.root_ctrl', 1), mc.setAttr('Attach_ctrlSpace_parentConstraint1.RootX_MW0', 1)
    mc.setDrivenKeyframe('Attach_ctrlSpace_parentConstraint1.RootX_MW0', currentDriver='Attach_ctrl.root_ctrl')
    mc.setAttr('Attach_ctrl.root_ctrl', 0), mc.setAttr('Attach_ctrlSpace_parentConstraint1.RootX_MW0', 0)
    mc.setDrivenKeyframe('Attach_ctrlSpace_parentConstraint1.RootX_MW0', currentDriver='Attach_ctrl.root_ctrl')
    mc.setAttr('Attach_ctrl.main_ctrl', 1)

    mc.parent(camCtrlSpace, attCtrlSpace, 'Cine_Cam1', 'Group')
    controlColor('Camera_ctrl', 17)
    controlColor('Attach_ctrl', 18)
    mc.setAttr('Cine_Cam1.v', 0)
    mc.parentConstraint(camCtrl, 'Camera', mo=True), mc.parentConstraint(attCtrl, 'Attach', mo=True)
    mc.select(d=True)

    print('Camera setup completed -> 06')


######################################################################################################################################
########################                                                            ##################################################
########################                            Create facialTemplete           ##################################################
######################################################################################################################################

def templeteFacialButton(*args):

    #create locator position

    ################################################# middleFace

    FrontHead = mc.spaceLocator(n = 'FrontHead_loc')
    FrontHeadSpace = mc.group(FrontHead, n = 'FrontHead_locSpace'),  mc.move(0, 186.346, 13.845)
    mc.setAttr('FrontHead_loc.displayLocalAxis', 1)

    Frown = mc.spaceLocator(n = 'Frown_loc')
    FrownSpace = mc.group(Frown, n = 'Frown_locSpace'),  mc.move(0, 182.258, 14.371)
    mc.setAttr('Frown_loc.displayLocalAxis', 1)

    UpperHead = mc.spaceLocator(n = 'UpperHead_loc')
    UpperHeadSpace = mc.group(UpperHead, n = 'UpperHead_locSpace'),  mc.move(0, 183.351, 3.069)
    mc.setAttr('UpperHead_loc.displayLocalAxis', 1)

    Chin = mc.spaceLocator(n = 'Chin_loc')
    ChinSpace = mc.group(Chin, n = 'Chin_locSpace'),  mc.move(0, 168.967, 14.493)
    mc.setAttr('Chin_loc.displayLocalAxis', 1)

    JawDn = mc.spaceLocator(n = 'JawDn_loc')
    JawDnSpace = mc.group(JawDn, n = 'JawDn_locSpace'),  mc.move(0, 165.996, 8.59)
    mc.setAttr('JawDn_loc.displayLocalAxis', 1)

    ###################################################### lips

    LipUp = mc.spaceLocator(n = 'LipUp_loc')
    LipUpSpace = mc.group(LipUp, n = 'LipUp_locSpace'),  mc.move(0, 172.946, 14.779)
    mc.setAttr('LipUp_loc.displayLocalAxis', 1)

    LeftLipUp1 = mc.spaceLocator(n = 'LeftLipUp1_loc')
    LeftLipUp1Space = mc.group(LeftLipUp1, n = 'LeftLipUp1_locSpace'),  mc.move(1.429, 172.891, 14.388), mc.rotate(0, 20, 0)
    mc.setAttr('LeftLipUp1_loc.displayLocalAxis', 1)

    LeftLipUp2 = mc.spaceLocator(n = 'LeftLipUp2_loc')
    LeftLipUp2Space = mc.group(LeftLipUp2, n = 'LeftLipUp2_locSpace'),  mc.move(2.504, 172.793, 13.454), mc.rotate(0, 27, 0)
    mc.setAttr('LeftLipUp2_loc.displayLocalAxis', 1)

    LeftLipDn2 = mc.spaceLocator(n = 'LeftLipDn2_loc')
    LeftLipDn2Space = mc.group(LeftLipDn2, n = 'LeftLipDn2_locSpace'),  mc.move(2.504, 172.618, 13.454), mc.rotate(0, 27, 0)
    mc.setAttr('LeftLipDn2_loc.displayLocalAxis', 1)

    LeftLipDn1 = mc.spaceLocator(n = 'LeftLipDn1_loc')
    LeftLipDn1Space = mc.group(LeftLipDn1, n = 'LeftLipDn1_locSpace'),  mc.move(1.388, 172.524, 14.219), mc.rotate(0, 20, 0)
    mc.setAttr('LeftLipDn1_loc.displayLocalAxis', 1)

    LipDn = mc.spaceLocator(n = 'LipDn_loc')
    LipDnSpace = mc.group(LipDn, n = 'LipDn_locSpace'),  mc.move(0, 172.382, 14.493)
    mc.setAttr('LipDn_loc.displayLocalAxis', 1)

    LipDnOut = mc.spaceLocator(n = 'LipDnOut_loc')
    LipDnOutSpace = mc.group(LipDnOut, n = 'LipDnOut_locSpace'),  mc.move(0, 171.8, 14.493)
    mc.setAttr('LipDnOut_loc.displayLocalAxis', 1)

    LeftLipDn1Out = mc.spaceLocator(n = 'LeftLipDn1Out_loc')
    LeftLipDn1OutSpace = mc.group(LeftLipDn1Out, n = 'LeftLipDn1Out_locSpace'),  mc.move(1.388, 172.023, 14.219), mc.rotate(0, 20, 0)
    mc.setAttr('LeftLipDn1Out_loc.displayLocalAxis', 1)

    LeftLipUp1Out = mc.spaceLocator(n = 'LeftLipUp1Out_loc')
    LeftLipUp1OutSpace = mc.group(LeftLipUp1Out, n = 'LeftLipUp1Out_locSpace'),  mc.move(1.429, 173.365, 14.388),  mc.rotate(0, 20, 0)
    mc.setAttr('LeftLipUp1Out_loc.displayLocalAxis', 1)

    LipUpOut = mc.spaceLocator(n = 'LipUpOut_loc')
    LipUpOutSpace = mc.group(LipUpOut, n = 'LipUpOut_locSpace'),  mc.move(0, 173.427, 14.779)
    mc.setAttr('LipUpOut_loc.displayLocalAxis', 1)

    ######################################################## eyelids

    LeftEyeLidMaster = mc.spaceLocator(n = 'LeftEyeLidMaster_loc')
    LeftEyeLidMasterSpace = mc.group(LeftEyeLidMaster, n = 'LeftEyeLidMaster_locSpace'),  mc.move(3.247, 180.656, 11.398)
    mc.setAttr('LeftEyeLidMaster_loc.displayLocalAxis', 1)

    LeftEyeLidUp = mc.spaceLocator(n = 'LeftEyeLidUp_loc')
    LeftEyeLidUpSpace = mc.group(LeftEyeLidUp, n = 'LeftEyeLidUp_locSpace'),  mc.move(3.247, 180.944, 13.331)
    mc.setAttr('LeftEyeLidUp_loc.displayLocalAxis', 1)

    LeftEyeLidDn = mc.spaceLocator(n = 'LeftEyeLidDn_loc')
    LeftEyeLidDnSpace = mc.group(LeftEyeLidDn, n = 'LeftEyeLidDn_locSpace'),  mc.move(3.247, 179.904, 13.182)
    mc.setAttr('LeftEyeLidDn_loc.displayLocalAxis', 1)

    LeftEyeLidOut = mc.spaceLocator(n = 'LeftEyeLidOut_loc')
    LeftEyeLidOutSpace = mc.group(LeftEyeLidOut, n = 'LeftEyeLidOut_locSpace'),  mc.move(4.702, 180.467, 12.369), mc.rotate(0, 11, 0)
    mc.setAttr('LeftEyeLidOut_loc.displayLocalAxis', 1)

    LeftEyeLidIn = mc.spaceLocator(n = 'LeftEyeLidIn_loc')
    LeftEyeLidInSpace = mc.group(LeftEyeLidIn, n = 'LeftEyeLidIn_locSpace'),  mc.move(1.621, 180.129, 12.482),  mc.rotate(0, -11, 0)
    mc.setAttr('LeftEyeLidIn_loc.displayLocalAxis', 1)

    LeftEyeLidUpOut = mc.spaceLocator(n = 'LeftEyeLidUpOut_loc')
    LeftEyeLidUpOutSpace = mc.group(LeftEyeLidUpOut, n = 'LeftEyeLidUpOut_locSpace'),  mc.move(4.185, 180.842, 13.158),  mc.rotate(0, 11, 0)
    mc.setAttr('LeftEyeLidUpOut_loc.displayLocalAxis', 1)

    LeftEyeLidUpIn = mc.spaceLocator(n = 'LeftEyeLidUpIn_loc')
    LeftEyeLidUpInSpace = mc.group(LeftEyeLidUpIn, n = 'LeftEyeLidUpIn_locSpace'),  mc.move(2.36, 180.665, 12.937),  mc.rotate(0, -11, 0)
    mc.setAttr('LeftEyeLidUpIn_loc.displayLocalAxis', 1)

    LeftEyeLidDnIn = mc.spaceLocator(n = 'LeftEyeLidDnIn_loc')
    LeftEyeLidDnInSpace = mc.group(LeftEyeLidDnIn, n = 'LeftEyeLidDnIn_locSpace'),  mc.move(2.411, 179.994, 13.011),  mc.rotate(0, -11, 0)
    mc.setAttr('LeftEyeLidDnIn_loc.displayLocalAxis', 1)

    LeftEyeLidDnOut = mc.spaceLocator(n = 'LeftEyeLidDnOut_loc')
    LeftEyeLidDnOutSpace = mc.group(LeftEyeLidDnOut, n = 'LeftEyeLidDnOut_locSpace'),  mc.move(4.341, 179.994, 12.872),  mc.rotate(0, 11, 0)
    mc.setAttr('LeftEyeLidDnOut_loc.displayLocalAxis', 1)

    ############################################################# cheeks

    LeftCheekBoneFront = mc.spaceLocator(n = 'LeftCheekBoneFront_loc')
    LeftCheekBoneFrontSpace = mc.group(LeftCheekBoneFront, n = 'LeftCheekBoneFront_locSpace'),  mc.move(3.876, 177.592, 12.738)
    mc.setAttr('LeftCheekBoneFront_loc.displayLocalAxis', 1)

    LeftCheekbone = mc.spaceLocator(n = 'LeftCheekbone_loc')
    LeftCheekboneSpace = mc.group(LeftCheekbone, n = 'LeftCheekbone_locSpace'),  mc.move(5.87, 178.305, 11.614),  mc.rotate(0, 70, 0)
    mc.setAttr('LeftCheekbone_loc.displayLocalAxis', 1)

    LeftCheekboneDn = mc.spaceLocator(n = 'LeftCheekboneDn_loc')
    LeftCheekboneDnSpace = mc.group(LeftCheekboneDn, n = 'LeftCheekboneDn_locSpace'),  mc.move(4.117, 175.307, 13.178),  mc.rotate(0, 50, 0)
    mc.setAttr('LeftCheekboneDn_loc.displayLocalAxis', 1)

    LeftCheekDn = mc.spaceLocator(n = 'LeftCheekDn_loc')
    LeftCheekDnSpace = mc.group(LeftCheekDn, n = 'LeftCheekDn_locSpace'),  mc.move(5.025, 173.304, 12.2),  mc.rotate(0, 60, 0)
    mc.setAttr('LeftCheekDn_loc.displayLocalAxis', 1)

    LeftCheekUp = mc.spaceLocator(n = 'LeftCheekUp_loc')
    LeftCheekUpSpace = mc.group(LeftCheekUp, n = 'LeftCheekUp_locSpace'),  mc.move(7.436, 175.181, 8.273),  mc.rotate(0, 90, 0)
    mc.setAttr('LeftCheekUp_loc.displayLocalAxis', 1)

    ############################################################## ear

    LeftLobe = mc.spaceLocator(n = 'LeftLobe_loc')
    LeftLobeSpace = mc.group(LeftLobe, n = 'LeftLobe_locSpace'),  mc.move(8.994, 175.103, 3.667), mc.rotate(0, 75, 0)
    mc.setAttr('LeftLobe_loc.displayLocalAxis', 1)

    LeftEarUp = mc.spaceLocator(n = 'LeftEarUp_loc')
    LeftEarUpSpace = mc.group(LeftEarUp, n = 'LeftEarUp_locSpace'),  mc.move(10.191, 181.143, 1.767), mc.rotate(0, 75, 0)
    mc.setAttr('LeftEarUp_loc.displayLocalAxis', 1)

    LeftEar = mc.spaceLocator(n = 'LeftEar_loc')
    LeftEarSpace = mc.group(LeftEar, n = 'LeftEar_locSpace'),  mc.move(7.91, 178.088, 3.775)
    mc.setAttr('LeftEar_loc.displayLocalAxis', 1)

    ########################################################## leftSide

    LeftUpperHead = mc.spaceLocator(n = 'LeftUpperHead_loc')
    LeftUpperHeadSpace = mc.group(LeftUpperHead, n = 'LeftUpperHead_locSpace'), mc.move(8.513, 182.356, 3.069)
    mc.setAttr('LeftUpperHead_loc.displayLocalAxis', 1)

    LeftOcularDn = mc.spaceLocator(n = 'LeftOcularDn_loc')
    LeftOcularDnSpace = mc.group(LeftOcularDn, n = 'LeftOcularDn_locSpace'), mc.move(1.872, 178.846, 13.159)
    mc.setAttr('LeftOcularDn_loc.displayLocalAxis', 1)

    LeftMaxilarDn = mc.spaceLocator(n = 'LeftMaxilarDn_loc')
    LeftMaxilarDnSpace = mc.group(LeftMaxilarDn, n = 'LeftMaxilarDn_locSpace'),  mc.move(4.697, 169.6, 10.449), mc.rotate(0, 70, 0)
    mc.setAttr('LeftMaxilarDn_loc.displayLocalAxis', 1)

    LeftMaxilarUp = mc.spaceLocator(n = 'LeftMaxilarUp_loc')
    LeftMaxilarUpSpace = mc.group(LeftMaxilarUp, n = 'LeftMaxilarUp_locSpace'),  mc.move(7.811, 173.91, 5.038), mc.rotate(0, 90, 0)
    mc.setAttr('LeftMaxilarUp_loc.displayLocalAxis', 1)

    LeftMaxilarNeck = mc.spaceLocator(n = 'LeftMaxilarNeck_loc')
    LeftMaxilarNeckSpace = mc.group(LeftMaxilarNeck, n = 'LeftMaxilarNeck_locSpace'), mc.move(5.131, 165.262, 7.070), mc.rotate(0, 90, 0)
    mc.setAttr('LeftMaxilarNeck_loc.displayLocalAxis', 1)

    LeftMaxilarHead = mc.spaceLocator(n = 'LeftMaxilarHead_loc')
    LeftMaxilarHeadSpace = mc.group(LeftMaxilarHead, n = 'LeftMaxilarHead_locSpace'), mc.move(8.614, 178.088, 6.880), mc.rotate(0, 90, 0)
    mc.setAttr('LeftMaxilarHead_loc.displayLocalAxis', 1)

    LeftTemples = mc.spaceLocator(n = 'LeftTemples_loc')
    LeftTemplesSpace = mc.group(LeftTemples, n = 'LeftTemples_locSpace'), mc.move(8.614, 182.256, 8.526), mc.rotate(0, 90, 0)
    mc.setAttr('LeftTemples_loc.displayLocalAxis', 1)

    leftSide = mc.spaceLocator(n = 'LeftSide_loc')
    LeftSideSpace = mc.group(leftSide, n = 'LeftSide_locSpace'), mc.move(5.912, 178.088, 3.775)
    mc.setAttr('LeftSide_loc.displayLocalAxis', 1)

    ##################################################### leftEyebrow

    LeftEyeBrow1 = mc.spaceLocator(n = 'LeftEyeBrow1_loc')
    LeftEyeBrow1Space = mc.group(LeftEyeBrow1, n = 'LeftEyeBrow1_locSpace'),  mc.move(1.936, 181.891, 14.34)
    mc.setAttr('LeftEyeBrow1_loc.displayLocalAxis', 1)

    LeftEyeBrow2 = mc.spaceLocator(n = 'LeftEyeBrow2_loc')
    LeftEyeBrow2Space = mc.group(LeftEyeBrow2, n = 'LeftEyeBrow2_locSpace'),  mc.move(4.039, 182.164, 14.224)
    mc.setAttr('LeftEyeBrow2_loc.displayLocalAxis', 1)

    LeftEyeBrow3 = mc.spaceLocator(n = 'LeftEyeBrow3_loc')
    LeftEyeBrow3Space = mc.group(LeftEyeBrow3, n = 'LeftEyeBrow3_locSpace'),  mc.move(5.915, 182.164, 13.410)
    mc.setAttr('LeftEyeBrow3_loc.displayLocalAxis', 1)

    ####################################################### nose

    LeftNasalUp = mc.spaceLocator(n = 'LeftNasalUp_loc')
    LeftNasalUpSpace = mc.group(LeftNasalUp, n = 'LeftNasalUp_locSpace'),  mc.move(1.643, 178.22, 13.578), mc.rotate(-12.698, 32.438, -15.888)
    mc.setAttr('LeftNasalUp_loc.displayLocalAxis', 1)

    LeftNostril = mc.spaceLocator(n = 'LeftNostril_loc')
    LeftNostrilSpace = mc.group(LeftNostril, n = 'LeftNostril_locSpace'),  mc.move(1.923, 175.829, 14.28)
    mc.setAttr('LeftNostril_loc.displayLocalAxis', 1)

    Nose = mc.spaceLocator(n = 'Nose_loc')
    NoseSpace = mc.group(Nose, n = 'Nose_locSpace'),  mc.move(0, 175.87, 16.261)
    mc.setAttr('Nose_loc.displayLocalAxis', 1)

    NoseUp = mc.spaceLocator(n = 'NoseUp_loc')
    NoseUpSpace = mc.group(NoseUp, n = 'NoseUp_locSpace'),  mc.move(0, 177.87, 16.261)
    mc.setAttr('NoseUp_loc.displayLocalAxis', 1)

    NoseDn = mc.spaceLocator(n = 'NoseDn_loc')
    NoseDnSpace = mc.group(NoseDn, n = 'NoseDn_locSpace'),  mc.move(0, 174.726, 15.212)
    mc.setAttr('NoseDn_loc.displayLocalAxis', 1)

    NoseBrige = mc.spaceLocator(n = 'NoseBrige_loc')
    NoseBrigeSpace = mc.group(NoseBrige, n = 'NoseBrige_locSpace'),  mc.move(0, 178.437, 15.644)
    mc.setAttr('NoseBrige_loc.displayLocalAxis', 1)

    NasalSeptum = mc.spaceLocator(n = 'NasalSeptum_loc')
    NasalSeptumSpace = mc.group(NasalSeptum, n = 'NasalSeptum_locSpace'),  mc.move(0, 180.451, 14.712)
    mc.setAttr('NasalSeptum_loc.displayLocalAxis', 1)

    ########################################## mouth master and pivots

    LipDnPivotMaster = mc.spaceLocator(n = 'LipDnPivotMaster')
    LipDnPivotMasterSpace = mc.group(LipDnPivotMaster, n = 'LipDnPivotMaster_Space'),  mc.move(0, 172.506, 13.278)

    LipUpPivotMaster = mc.spaceLocator(n = 'LipUpPivotMaster')
    LipUpPivotMasterSpace = mc.group(LipUpPivotMaster, n = 'LipUpPivotMaster_Space'),  mc.move(0, 172.624, 13.278)

    ############################################### master mirror

    LeftMaxilarMaster = mc.spaceLocator(n= 'LeftMaxilarMaster')
    LeftMaxilarMasterSpace = mc.group(LeftMaxilarMaster, n= 'LeftMaxilarMasterSpace'), mc.move(6.254, 171.755, 7.744), mc.rotate(0, 80, 0)
    mc.setAttr('LeftMaxilarMaster.displayLocalAxis', 1)

    LeftMaxilarDn_Master = mc.spaceLocator(n= 'LeftMaxilarDn_Master')
    LeftMaxilarDn_MasterSpace = mc.group(LeftMaxilarDn_Master, n= 'LeftMaxilarDn_MasterSpace'), mc.move(8.185, 171.755, 7.744), mc.rotate(0, 80, 0)
    mc.setAttr('LeftMaxilarDn_Master.displayLocalAxis', 1)

    LeftTempleMaster = mc.spaceLocator(n= 'LeftTempleMaster')
    LeftTempleMasterSpace = mc.group(LeftTempleMaster, n= 'LeftTempleMasterSpace'), mc.move(8.614, 180.172, 7.703), mc.rotate(0, 90, 0)
    mc.setAttr('LeftTempleMaster.displayLocalAxis', 1)

    LeftNoseMaster = mc.spaceLocator(n= 'LeftNoseMaster')
    LeftNoseMasterSpace = mc.group(LeftNoseMaster, n= 'LeftNose_MasterSpace'), mc.setAttr('LeftNoseMaster.displayLocalAxis', 1)
    mc.parentConstraint('LeftNostril_loc', 'LeftNasalUp_loc', LeftNoseMasterSpace, mo=False)

    LeftCheekMaster = mc.spaceLocator(n= 'LeftCheekMaster')
    LeftCheekMasterSpace = mc.group(LeftCheekMaster, n= 'LeftCheek_MasterSpace'), mc.setAttr('LeftCheekMaster.displayLocalAxis', 1)
    mc.parentConstraint('LeftCheekbone_loc', 'LeftCheekboneDn_loc', 'LeftCheekBoneFront_loc', LeftCheekMasterSpace, mo= False)

    LeftEyeBrowMaster = mc.spaceLocator(n= 'LeftEyeBrowMaster')
    LeftEyeBrowMasterSpace = mc.group(LeftEyeBrowMaster, n= 'LeftEyeBrow_MasterSpace'), mc.setAttr('LeftEyeBrowMaster.displayLocalAxis', 1)
    mc.parentConstraint('LeftEyeBrow1_loc', 'LeftEyeBrow2_loc', 'LeftEyeBrow3_loc', LeftEyeBrowMasterSpace, mo=False)

    #################################################### parent groups

    mc.parent(LeftEyeLidUpOutSpace, LeftEyeLidUpInSpace, LeftEyeLidDnInSpace, LeftEyeLidDnOutSpace, LeftEyeLidInSpace, LeftEyeLidOutSpace, LeftEyeLidDnSpace, LeftEyeLidUpSpace, LeftEyeLidMaster)
    mc.parent(LipDnOutSpace, LipDn), mc.parent(LeftLipDn1OutSpace, LeftLipDn1)
    mc.parent(LipUpOutSpace, LipUp), mc.parent(LeftLipUp1OutSpace, LeftLipUp1)

    mouthPivots = mc.group(LipDnPivotMasterSpace, LipUpPivotMasterSpace, n = 'mouthPivot')

    locTemp_grp = mc.group(LeftUpperHeadSpace, UpperHeadSpace, LeftCheekBoneFrontSpace, NoseDnSpace, NoseBrigeSpace, LeftEarSpace, ChinSpace, LeftCheekUpSpace, LeftCheekDnSpace, LeftTempleMasterSpace, NoseUpSpace,
    LipDnSpace, LeftLipDn1Space, LeftLipDn2Space, LeftLipUp2Space, LeftMaxilarDnSpace, LeftLipUp1Space, LipUpSpace, LeftNostrilSpace, LeftNasalUpSpace, LeftCheekboneSpace, LeftOcularDnSpace, LeftNoseMasterSpace,
    LeftEyeBrow2Space, LeftEyeBrow1Space, NoseSpace, LeftMaxilarUpSpace, FrontHeadSpace, LeftLobeSpace, FrownSpace, LeftEarUpSpace, LeftCheekboneDnSpace, LeftEyeLidMasterSpace, NasalSeptumSpace, LeftEyeBrowMasterSpace,
    LeftEyeBrow3Space, LeftMaxilarNeckSpace, LeftTemplesSpace, LeftMaxilarHeadSpace, LeftSideSpace, LeftMaxilarDn_MasterSpace, LeftMaxilarMasterSpace, JawDnSpace, LeftCheekMasterSpace, n = 'FacialTempleteRig')

    mc.select(d = True)

######################################################################################################################################
########################                                                            ##################################################
########################                            Create facialRig                ##################################################
######################################################################################################################################

def facialRigButton(*args):

######################### eyelids

    LeftEyeLidUpOut_JNT = mc.joint(n = 'LeftEyeLidUpOut', radius=0.5)
    mc.delete(mc.parentConstraint('LeftEyeLidUpOut_loc', LeftEyeLidUpOut_JNT, mo = False)), mc.select(d = True)

    LeftEyeLidUpIn_JNT = mc.joint(n = 'LeftEyeLidUpIn', radius=0.5)
    mc.delete(mc.parentConstraint('LeftEyeLidUpIn_loc', LeftEyeLidUpIn_JNT, mo = False)), mc.select(d = True)

    LeftEyeLidDnIn_JNT = mc.joint(n = 'LeftEyeLidDnIn', radius=0.5)
    mc.delete(mc.parentConstraint('LeftEyeLidDnIn_loc', LeftEyeLidDnIn_JNT, mo = False)), mc.select(d = True)

    LeftEyeLidDnOut_JNT = mc.joint(n = 'LeftEyeLidDnOut', radius=0.5)
    mc.delete(mc.parentConstraint('LeftEyeLidDnOut_loc', LeftEyeLidDnOut_JNT, mo = False)), mc.select(d = True)

    LeftEyeLidMaster_JNT = mc.joint(n = 'LeftEyeLidMaster', radius=0.5)
    mc.delete(mc.parentConstraint('LeftEyeLidMaster_loc', LeftEyeLidMaster_JNT, mo = False)), mc.select(d = True)

    LeftEyeLidUp_JNT = mc.joint(n = 'LeftEyeLidUp', radius=0.5)
    mc.delete(mc.parentConstraint('LeftEyeLidUp_loc', LeftEyeLidUp_JNT, mo = False)), mc.select(d = True)

    LeftEyeLidDn_JNT = mc.joint(n = 'LeftEyeLidDn', radius=0.5)
    mc.delete(mc.parentConstraint('LeftEyeLidDn_loc', LeftEyeLidDn_JNT, mo = False)), mc.select(d = True)

    LeftEyeLidIn_JNT = mc.joint(n = 'LeftEyeLidIn', radius=0.5)
    mc.delete(mc.parentConstraint('LeftEyeLidIn_loc', LeftEyeLidIn_JNT, mo = False)), mc.select(d = True)

    LeftEyeLidOut_JNT = mc.joint(n = 'LeftEyeLidOut', radius=0.5)
    mc.delete(mc.parentConstraint('LeftEyeLidOut_loc', LeftEyeLidOut_JNT, mo = False)), mc.select(d = True)

    ############################## lips

    LeftLipDn1Out_JNT = mc.joint(n = 'LeftLipDn1Out', radius=0.5)
    mc.delete(mc.parentConstraint('LeftLipDn1Out_loc', LeftLipDn1Out_JNT, mo = False)), mc.select(d = True)

    LeftLipUp1Out_JNT = mc.joint(n = 'LeftLipUp1Out', radius=0.5)
    mc.delete(mc.parentConstraint('LeftLipUp1Out_loc', LeftLipUp1Out_JNT, mo = False)), mc.select(d = True)

    LipDnOut_JNT = mc.joint(n = 'LipDnOut', radius=0.5)
    mc.delete(mc.parentConstraint('LipDnOut_loc', LipDnOut_JNT, mo = False)), mc.select(d = True)

    LipUpOut_JNT = mc.joint(n = 'LipUpOut', radius=0.5)
    mc.delete(mc.parentConstraint('LipUpOut_loc', LipUpOut_JNT, mo = False)), mc.select(d = True)

    LipUp_JNT = mc.joint(n = 'LipUp', radius=0.5)
    mc.delete(mc.parentConstraint('LipUp_loc', LipUp_JNT, mo = False)), mc.select(d = True)

    LeftLipUp1_JNT = mc.joint(n = 'LeftLipUp1', radius=0.5)
    mc.delete(mc.parentConstraint('LeftLipUp1_loc', LeftLipUp1_JNT, mo = False)), mc.select(d = True)

    LeftLipUp2_JNT = mc.joint(n = 'LeftLipUp2', radius=0.5)
    mc.delete(mc.parentConstraint('LeftLipUp2_loc', LeftLipUp2_JNT, mo = False)), mc.select(d = True)

    LeftLipDn1_JNT = mc.joint(n = 'LeftLipDn1', radius=0.5)
    mc.delete(mc.parentConstraint('LeftLipDn1_loc', LeftLipDn1_JNT, mo = False)), mc.select(d = True)

    LeftLipDn2_JNT = mc.joint(n = 'LeftLipDn2', radius=0.5)
    mc.delete(mc.parentConstraint('LeftLipDn2_loc', LeftLipDn2_JNT, mo = False)), mc.select(d = True)

    LipDn_JNT = mc.joint(n = 'LipDn', radius=0.5)
    mc.delete(mc.parentConstraint('LipDn_loc', LipDn_JNT, mo = False)), mc.select(d = True)

    ############################ ear

    LeftEar_JNT = mc.joint(n = 'LeftEar', radius=0.5)
    mc.delete(mc.parentConstraint('LeftEar_loc', LeftEar_JNT, mo = False)), mc.select(d = True)

    LeftLobe_JNT = mc.joint(n = 'LeftLobe', radius=0.5)
    mc.delete(mc.parentConstraint('LeftLobe_loc', LeftLobe_JNT, mo = False)), mc.select(d = True)

    LeftEarUp_JNT = mc.joint(n = 'LeftEarUp', radius=0.5)
    mc.delete(mc.parentConstraint('LeftEarUp_loc', LeftEarUp_JNT, mo = False)), mc.select(d = True)

    ################################# nose

    NoseDn_JNT = mc.joint(n = 'NoseDn', radius=0.5)
    mc.delete(mc.parentConstraint('NoseDn_loc', NoseDn_JNT, mo = False)), mc.select(d = True)

    NoseBrige_JNT = mc.joint(n = 'NoseBrige', radius=0.5)
    mc.delete(mc.parentConstraint('NoseBrige_loc', NoseBrige_JNT, mo = False)), mc.select(d = True)

    NasalSeptum_JNT = mc.joint(n = 'NasalSeptum', radius=0.5)
    mc.delete(mc.parentConstraint('NasalSeptum_loc', NasalSeptum_JNT, mo = False)), mc.select(d = True)

    LeftNasalUp_JNT = mc.joint(n = 'LeftNasalUp', radius=0.5)
    mc.delete(mc.parentConstraint('LeftNasalUp_loc', LeftNasalUp_JNT, mo = False)), mc.select(d = True)

    Nose_JNT = mc.joint(n = 'Nose', radius=0.5)
    mc.delete(mc.parentConstraint('Nose_loc', Nose_JNT, mo = False)), mc.select(d = True)

    NoseUp_JNT = mc.joint(n = 'NoseUp', radius=0.5)
    mc.delete(mc.parentConstraint('NoseUp_loc', NoseUp_JNT, mo = False)), mc.select(d = True)

    LeftNostril_JNT = mc.joint(n = 'LeftNostril', radius=0.5)
    mc.delete(mc.parentConstraint('LeftNostril_loc', LeftNostril_JNT, mo = False)), mc.select(d = True)

    ############################################### eyebrow

    LeftEyeBrow1_JNT = mc.joint(n = 'LeftEyeBrow1', radius=0.5)
    mc.delete(mc.parentConstraint('LeftEyeBrow1_loc', LeftEyeBrow1_JNT, mo = False)), mc.select(d = True)

    LeftEyeBrow2_JNT = mc.joint(n = 'LeftEyeBrow2', radius=0.5)
    mc.delete(mc.parentConstraint('LeftEyeBrow2_loc', LeftEyeBrow2_JNT, mo = False)), mc.select(d = True)

    LeftEyeBrow3_JNT = mc.joint(n = 'LeftEyeBrow3', radius=0.5)
    mc.delete(mc.parentConstraint('LeftEyeBrow3_loc', LeftEyeBrow3_JNT, mo = False)), mc.select(d = True)

    ############################################## middle

    Chin_JNT = mc.joint(n = 'Chin', radius=0.5)
    mc.delete(mc.parentConstraint('Chin_loc', Chin_JNT, mo = False)), mc.select(d = True)

    UpperHead_JNT = mc.joint(n = 'UpperHead', radius=0.5)
    mc.delete(mc.parentConstraint('UpperHead_loc', UpperHead_JNT, mo = False)), mc.select(d = True)

    FrontHead_JNT = mc.joint(n = 'FrontHead', radius=0.5)
    mc.delete(mc.parentConstraint('FrontHead_loc', FrontHead_JNT, mo = False)), mc.select(d = True)

    Frown_JNT = mc.joint(n = 'Frown', radius=0.5)
    mc.delete(mc.parentConstraint('Frown_loc', Frown_JNT, mo = False)), mc.select(d = True)

    JawDn_JNT = mc.joint(n = 'JawDn', radius=0.5)
    mc.delete(mc.parentConstraint('JawDn_loc', JawDn_JNT, mo = False)), mc.select(d = True)

    ####################################### left side

    LeftMaxilarHead_JNT = mc.joint(n = 'LeftMaxilarHead', radius=0.5)
    mc.delete(mc.parentConstraint('LeftMaxilarHead_loc', LeftMaxilarHead_JNT, mo = False)), mc.select(d = True)

    LeftTemples_JNT = mc.joint(n = 'LeftTemples', radius=0.5)
    mc.delete(mc.parentConstraint('LeftTemples_loc', LeftTemples_JNT, mo = False)), mc.select(d = True)

    LeftUpperHead_JNT = mc.joint(n = 'LeftUpperHead', radius=0.5)
    mc.delete(mc.parentConstraint('LeftUpperHead_loc', LeftUpperHead_JNT, mo = False)), mc.select(d = True)

    LeftCheekBoneFront_JNT = mc.joint(n = 'LeftCheekBoneFront', radius=0.5)
    mc.delete(mc.parentConstraint('LeftCheekBoneFront_loc', LeftCheekBoneFront_JNT, mo = False)), mc.select(d = True)

    LeftMaxilarDn_JNT = mc.joint(n = 'LeftMaxilarDn', radius=0.5)
    mc.delete(mc.parentConstraint('LeftMaxilarDn_loc', LeftMaxilarDn_JNT, mo = False)), mc.select(d = True)

    LeftCheekboneDn_JNT = mc.joint(n = 'LeftCheekboneDn', radius=0.5)
    mc.delete(mc.parentConstraint('LeftCheekboneDn_loc', LeftCheekboneDn_JNT, mo = False)), mc.select(d = True)

    LeftOcularDn_JNT = mc.joint(n = 'LeftOcularDn', radius=0.5)
    mc.delete(mc.parentConstraint('LeftOcularDn_loc', LeftOcularDn_JNT, mo = False)), mc.select(d = True)

    LeftCheekbone_JNT = mc.joint(n = 'LeftCheekbone', radius=0.5)
    mc.delete(mc.parentConstraint('LeftCheekbone_loc', LeftCheekbone_JNT, mo = False)), mc.select(d = True)

    LeftCheekDn_JNT = mc.joint(n = 'LeftCheekDn', radius=0.5)
    mc.delete(mc.parentConstraint('LeftCheekDn_loc', LeftCheekDn_JNT, mo = False)), mc.select(d = True)

    LeftCheekUp_JNT = mc.joint(n = 'LeftCheekUp', radius=0.5)
    mc.delete(mc.parentConstraint('LeftCheekUp_loc', LeftCheekUp_JNT, mo = False)), mc.select(d = True)

    LeftMaxilarUp_JNT = mc.joint(n = 'LeftMaxilarUp', radius=0.5)
    mc.delete(mc.parentConstraint('LeftMaxilarUp_loc', LeftMaxilarUp_JNT, mo = False)), mc.select(d = True)

    LeftMaxilarNeck_JNT = mc.joint(n = 'LeftMaxilarNeck', radius=0.5)
    mc.delete(mc.parentConstraint('LeftMaxilarNeck_loc', LeftMaxilarNeck_JNT, mo = False)), mc.select(d = True)

    LeftSide_JNT = mc.joint(n = 'LeftSide', radius=0.5)
    mc.delete(mc.parentConstraint('LeftSide_loc', LeftSide_JNT, mo = False)), mc.select(d = True)

    Left_jointList = [LeftEyeLidDnOut_JNT, LeftEyeLidDnIn_JNT, LeftEyeLidUpIn_JNT, LeftEyeLidUpOut_JNT, LeftEyeLidOut_JNT, LeftEyeLidIn_JNT, LeftEyeLidDn_JNT, LeftEyeLidUp_JNT, LeftEyeLidMaster_JNT,
                      LeftLobe_JNT, LeftEarUp_JNT, LeftEar_JNT, LeftEyeBrow1_JNT, LeftEyeBrow2_JNT, LeftEyeBrow3_JNT, LeftLipUp1_JNT, LeftLipUp2_JNT, LeftLipDn2_JNT, LeftLipDn1_JNT, LeftLipDn1Out_JNT,
                      LeftLipUp1Out_JNT, LeftNasalUp_JNT, LeftNostril_JNT, LeftOcularDn_JNT, LeftCheekbone_JNT, LeftCheekboneDn_JNT, LeftCheekDn_JNT, LeftCheekUp_JNT, LeftMaxilarDn_JNT, LeftMaxilarUp_JNT,
                      LeftCheekBoneFront_JNT, LeftUpperHead_JNT, LeftMaxilarNeck_JNT, LeftMaxilarHead_JNT, LeftTemples_JNT, LeftSide_JNT]

    Center_jointList = [Chin_JNT, UpperHead_JNT, FrontHead_JNT, Frown_JNT, Nose_JNT, NasalSeptum_JNT, NoseBrige_JNT, NoseDn_JNT, LipDn_JNT, LipUp_JNT, LipUpOut_JNT, LipDnOut_JNT, JawDn_JNT, NoseUp_JNT]

    ################################################################# parent bones
    mc.parent(LeftEyeLidDnOut_JNT, LeftEyeLidDnIn_JNT, LeftEyeLidUpIn_JNT, LeftEyeLidUpOut_JNT, LeftEyeLidOut_JNT, LeftEyeLidIn_JNT, LeftEyeLidDn_JNT, LeftEyeLidUp_JNT, LeftEyeLidMaster_JNT)
    mc.parent(LeftLobe_JNT, LeftEarUp_JNT, LeftEar_JNT)
    mc.parent(LipDnOut_JNT, LeftLipDn1Out_JNT, LeftLipDn2_JNT, LeftLipDn1_JNT, LipDn_JNT, JawDn_JNT, 'jaw') #C_jaw_JNT - RoartyDigital faceRig
    mc.parent( LeftMaxilarHead_JNT, LeftMaxilarUp_JNT, LeftCheekUp_JNT, LeftUpperHead_JNT, LeftEar_JNT, LeftTemples_JNT, LeftSide_JNT)
    mc.parent(NoseDn_JNT, LeftCheekBoneFront_JNT, LeftCheekboneDn_JNT, FrontHead_JNT, NasalSeptum_JNT, LeftEyeBrow1_JNT, LeftEyeBrow3_JNT, LeftEyeBrow2_JNT,
    LeftOcularDn_JNT, LeftCheekbone_JNT, LeftNasalUp_JNT, UpperHead_JNT, NoseBrige_JNT, LeftMaxilarDn_JNT, Frown_JNT, LeftEyeLidMaster_JNT, LeftLipUp1_JNT, Chin_JNT, Nose_JNT, LipUp_JNT,
    LipUpOut_JNT, LeftLipUp1Out_JNT, LeftCheekDn_JNT, LeftLipUp2_JNT, LeftMaxilarNeck_JNT, LeftNostril_JNT, LeftSide_JNT, NoseUp_JNT, 'Head')#C_head_JNT - RoartyDigital faceRig
    mc.select(d=True)

    ################################################### main locators

    jawMain = mc.spaceLocator(n= 'jawMain_lipSupport_loc')
    jawMainSpace = mc.group(em=True, n= 'jawMain_lipSupport_locSpace')
    mc.parent(jawMain, jawMainSpace), mc.delete(mc.parentConstraint('jaw', jawMainSpace, mo=False)), mc.parentConstraint('jaw', jawMain,  mo=True)
    headMain = mc.spaceLocator(n= 'headMain_lipSupport_loc')
    headMainSpace = mc.group(em=True, n= 'headMain_lipSupport_locSpace')
    mc.parent(headMain, headMainSpace), mc.delete(mc.parentConstraint('Head', headMainSpace, mo=False)), mc.parentConstraint('Head', headMain, mo=True)

    mc.select(d = True)

    ############################################################### orient joint axis -> freeze transformation

    for LeftSideFace in Left_jointList:
        mc.makeIdentity(LeftSideFace, apply=True, t=True, r=True, s=True)
        mc.select(d=True)

    for CenterSideFace in Center_jointList:
        mc.makeIdentity(CenterSideFace, apply=True, t=True, r=True, s=True)
        mc.select(d=True)

    ########################################################################## mirror bones

    mc.mirrorJoint(LeftEyeBrow1_JNT, mirrorYZ=True, mirrorBehavior=True, searchReplace=('Left', 'Right')), mc.select(cl=True)
    mc.mirrorJoint(LeftEyeBrow2_JNT, mirrorYZ=True, mirrorBehavior=True, searchReplace=('Left', 'Right')), mc.select(cl=True)
    mc.mirrorJoint(LeftEyeBrow3_JNT, mirrorYZ=True, mirrorBehavior=True, searchReplace=('Left', 'Right')), mc.select(cl=True)

    mc.mirrorJoint(LeftLipUp1_JNT, mirrorYZ=True, mirrorBehavior=True, searchReplace=('Left', 'Right')), mc.select(cl=True)
    mc.mirrorJoint(LeftLipUp2_JNT, mirrorYZ=True, mirrorBehavior=True, searchReplace=('Left', 'Right')), mc.select(cl=True)
    mc.mirrorJoint(LeftLipDn2_JNT, mirrorYZ=True, mirrorBehavior=True, searchReplace=('Left', 'Right')), mc.select(cl=True)
    mc.mirrorJoint(LeftLipDn1_JNT, mirrorYZ=True, mirrorBehavior=True, searchReplace=('Left', 'Right')), mc.select(cl=True)
    mc.mirrorJoint(LeftLipDn1Out_JNT, mirrorYZ=True, mirrorBehavior=True, searchReplace=('Left', 'Right')), mc.select(cl=True)
    mc.mirrorJoint(LeftLipUp1Out_JNT, mirrorYZ=True, mirrorBehavior=True, searchReplace=('Left', 'Right')), mc.select(cl=True)

    mc.mirrorJoint(LeftNasalUp_JNT, mirrorYZ=True, mirrorBehavior=True, searchReplace=('Left', 'Right')), mc.select(cl=True)
    mc.mirrorJoint(LeftNostril_JNT, mirrorYZ=True, mirrorBehavior=True, searchReplace=('Left', 'Right')), mc.select(cl=True)

    mc.mirrorJoint(LeftOcularDn_JNT, mirrorYZ=True, mirrorBehavior=True, searchReplace=('Left', 'Right')), mc.select(cl=True)
    mc.mirrorJoint(LeftCheekbone_JNT, mirrorYZ=True, mirrorBehavior=True, searchReplace=('Left', 'Right')), mc.select(cl=True)
    mc.mirrorJoint(LeftCheekboneDn_JNT, mirrorYZ=True, mirrorBehavior=True, searchReplace=('Left', 'Right')), mc.select(cl=True)
    mc.mirrorJoint(LeftCheekDn_JNT, mirrorYZ=True, mirrorBehavior=True, searchReplace=('Left', 'Right')), mc.select(cl=True)
    mc.mirrorJoint(LeftEyeLidMaster_JNT, mirrorYZ=True, mirrorBehavior=True, searchReplace=('Left', 'Right')), mc.select(cl=True)
    mc.mirrorJoint(LeftMaxilarDn_JNT, mirrorYZ=True, mirrorBehavior=True, searchReplace=('Left', 'Right')), mc.select(cl=True)
    mc.mirrorJoint(LeftCheekBoneFront_JNT, mirrorYZ=True, mirrorBehavior=True, searchReplace=('Left', 'Right')), mc.select(cl=True)
    mc.mirrorJoint(LeftMaxilarNeck_JNT, mirrorYZ=True, mirrorBehavior=True, searchReplace=('Left', 'Right')), mc.select(cl=True)
    mc.mirrorJoint(LeftSide_JNT, mirrorYZ=True, mirrorBehavior=True, searchReplace=('Left', 'Right')), mc.select(cl=True)

    Right_jointList = ['RightEyeLidDnOut', 'RightEyeLidDnIn', 'RightEyeLidUpIn', 'RightEyeLidUpOut', 'RightEyeLidOut', 'RightEyeLidIn',
    'RightEyeLidDn', 'RightEyeLidUp', 'RightEyeLidMaster', 'RightLobe', 'RightEarUp', 'RightEar', 'RightEyeBrow1', 'RightEyeBrow2',
    'RightEyeBrow3', 'RightLipUp1', 'RightLipUp2', 'RightLipDn2', 'RightLipDn1', 'RightLipDn1Out', 'RightLipUp1Out', 'RightNasalUp',
    'RightNostril', 'RightOcularDn', 'RightCheekbone', 'RightCheekboneDn', 'RightCheekDn', 'RightCheekUp', 'RightMaxilarDn',
    'RightMaxilarUp', 'RightCheekBoneFront', 'RightUpperHead', 'RightMaxilarNeck', 'RightMaxilarHead', 'RightTemples', 'RightSide']

    ###############################################################################################
    ########################################## controls ###########################################
    ###############################################################################################

    def controlColor(s, c): # yellow 17, red 13, blue 6, light blue 18
        mc.setAttr(s + '.overrideEnabled', 1)
        mc.setAttr(s + '.overrideColor', c)

    ############################## pivot mouth controls
    mouthPivots_list = ['LipUpPivotMaster', 'LipDnPivotMaster']

    for mP in (mouthPivots_list):
        mPiv = mc.curve(d = 1, p = [(0, 0, -0.0110532), (0, 0, 5.065693), (-0.422277, 0 ,5.48797), (0, 0, 5.910243), (0.34552, 0, 5.523996), (0, 0, 5.065693), (0, 0, -0.0110532), (0, 0, 5.065693)], n= mP + '_ctrl')
        mPSpc = mc.group(em=True, n= mP + '_ctrlSpace')
        mPCust = mc.group(em=True, n=mP + '_customization_ctrlSpace')
        mPMasterSpc = mc.group(em=True, n= mP + '_ctrlMasterSpace')
        mc.parent(mPiv, mPSpc), mc.parent(mPSpc, mPCust), mc.parent(mPCust, mPMasterSpc)

    ###################################### leftSide
    for l_ctrl in (Left_jointList):
        crv = mc.circle(n= l_ctrl + '_ctrl', radius= 1.1, ch=False)
        custCrv = mc.group(crv, n= l_ctrl + '_customization_ctrlSpace')
        spaceCrv = mc.group(custCrv, n= l_ctrl + '_ctrlSpace')
        mc.delete(mc.parentConstraint(l_ctrl, spaceCrv, mo=False))
        mc.parentConstraint(crv, l_ctrl, mo=True), mc.scaleConstraint(crv, l_ctrl, mo=True)

    Left_CtrlsList = ['LeftEyeLidDnOut_ctrl', 'LeftEyeLidDnIn_ctrl', 'LeftEyeLidUpIn_ctrl', 'LeftEyeLidUpOut_ctrl', 'LeftEyeLidOut_ctrl', 'LeftEyeLidIn_ctrl', 'LeftEyeLidDn_ctrl', 'LeftEyeLidUp_ctrl',
                      'LeftEyeLidMaster_ctrl', 'LeftLobe_ctrl', 'LeftEarUp_ctrl', 'LeftEar_ctrl', 'LeftEyeBrow1_ctrl', 'LeftEyeBrow2_ctrl', 'LeftEyeBrow3_ctrl', 'LeftLipUp1_ctrl', 'LeftLipUp2_ctrl',
                      'LeftLipDn2_ctrl', 'LeftLipDn1_ctrl', 'LeftLipDn1Out_ctrl', 'LeftLipUp1Out_ctrl', 'LeftNasalUp_ctrl', 'LeftNostril_ctrl', 'LeftOcularDn_ctrl', 'LeftCheekbone_ctrl', 'LeftCheekboneDn_ctrl',
                      'LeftCheekDn_ctrl', 'LeftCheekUp_ctrl', 'LeftMaxilarDn_ctrl', 'LeftMaxilarUp_ctrl', 'LeftCheekBoneFront_ctrl', 'LeftUpperHead_ctrl', 'LeftMaxilarNeck_ctrl', 'LeftMaxilarHead_ctrl',
                      'LeftTemples_ctrl', 'LeftSide_ctrl']

    for lC in (Left_CtrlsList):
        controlColor(lC, 6)

    ################################### rightSide
    for r_ctrl in (Right_jointList):
        crv = mc.circle(n = r_ctrl + '_ctrl', radius= 1.1, ch=False)
        spaceCrv = mc.group(crv, n= r_ctrl + '_ctrlSpace')
        spaceCust = mc.group(spaceCrv, n=r_ctrl + '_customization_ctrlSpace')
        masterSpace = mc.group(spaceCust, n= r_ctrl + '_ctrlMasterSpace')
        const = mc.group(masterSpace, n= r_ctrl + '_const')
        constSpace = mc.group(const, n= r_ctrl + '_constSpace')
        constCust = mc.group(constSpace, n=r_ctrl + '_customization_constSpace')
        constMasterSpace = mc.group(constCust, n= r_ctrl + '_constMasterSpace')
        mc.delete(mc.parentConstraint(r_ctrl, constMasterSpace, mo=False))
        mc.parentConstraint(crv, r_ctrl, mo=True), mc.scaleConstraint(crv, r_ctrl, mo=True)

    Right_CtrlsList = ['RightEyeLidDnOut_ctrl', 'RightEyeLidDnIn_ctrl', 'RightEyeLidUpIn_ctrl', 'RightEyeLidUpOut_ctrl', 'RightEyeLidOut_ctrl', 'RightEyeLidIn_ctrl', 'RightEyeLidDn_ctrl',
                       'RightEyeLidUp_ctrl', 'RightEyeLidMaster_ctrl', 'RightLobe_ctrl', 'RightEarUp_ctrl', 'RightEar_ctrl', 'RightEyeBrow1_ctrl', 'RightEyeBrow2_ctrl', 'RightEyeBrow3_ctrl', 'RightLipUp1_ctrl',
                       'RightLipUp2_ctrl', 'RightLipDn2_ctrl', 'RightLipDn1_ctrl', 'RightLipDn1Out_ctrl', 'RightLipUp1Out_ctrl', 'RightNasalUp_ctrl', 'RightNostril_ctrl', 'RightOcularDn_ctrl', 'RightCheekbone_ctrl',
                       'RightCheekboneDn_ctrl', 'RightCheekDn_ctrl', 'RightCheekUp_ctrl', 'RightMaxilarDn_ctrl', 'RightMaxilarUp_ctrl', 'RightCheekBoneFront_ctrl', 'RightUpperHead_ctrl', 'RightMaxilarNeck_ctrl',
                       'RightMaxilarHead_ctrl', 'RightTemples_ctrl', 'RightSide_ctrl']

    for rC in (Right_CtrlsList):
        controlColor(rC, 13)

    ################################### center
    for c_ctrl in (Center_jointList):
        crv = mc.circle(n = c_ctrl + '_ctrl', radius= 1.1, ch=False)
        spaceCrv = mc.group(crv, n=c_ctrl + '_ctrlSpace')
        spaceCust = mc.group(spaceCrv, n=c_ctrl + '_customization_ctrlSpace')
        masterSpace = mc.group(spaceCust, n=c_ctrl + '_ctrlMasterSpace')
        mc.delete(mc.parentConstraint(c_ctrl, masterSpace, mo=False))
        mc.parentConstraint(crv, c_ctrl, mo=True), mc.scaleConstraint(crv, c_ctrl, mo=True)

    Center_CtrlsList = ['Chin_ctrl', 'UpperHead_ctrl', 'FrontHead_ctrl', 'Frown_ctrl', 'Nose_ctrl', 'NasalSeptum_ctrl', 'NoseBrige_ctrl',
    'NoseDn_ctrl', 'LipDn_ctrl', 'LipUp_ctrl', 'LipUpOut_ctrl', 'LipDnOut_ctrl', 'JawDn_ctrl', 'LipDnPivotMaster_ctrl', 'LipUpPivotMaster_ctrl', 'NoseUp_ctrl']

    for cC in (Center_CtrlsList):
        controlColor(cC, 17)

    ######################################################## master lip pivot constraints
    lipsM = mc.circle(n= 'lipsMaster_ctrl', ch=False)
    lispMSpc = mc.group(lipsM, n= 'lipsMaster_ctrlSpace')
    lispM_MasterSpc = mc.group(lispMSpc, n= 'lipsMaster_ctrlMasterSpace')

    mc.delete(mc.parentConstraint('LipDnPivotMaster', 'LipDnPivotMaster_ctrlMasterSpace', mo=False))
    mc.delete(mc.parentConstraint('LipUpPivotMaster', 'LipUpPivotMaster_ctrlMasterSpace', mo=False))
    mc.delete(mc.parentConstraint('LipUpPivotMaster_ctrlMasterSpace', 'LipDnPivotMaster_ctrlMasterSpace', lispM_MasterSpc, mo=False))

    #############################################################################################################################################
    ########################################                                      ################################################################
    ########################################         mirror controls              ###############################################################
    ########################################                                      ###############################################################
    #############################################################################################################################################

    for mC in (Left_jointList):
        mirrorCtrl = mc.curve(d = 1, p = [(-0.0133947, 0, 0.351564), (-0.0130162, 0, 0.916036), (-0.126636, 0, 0.85811), (0, 0, 1.111383), (0.126636, 0, 0.85811), (0.0121104, 0, 0.916036),
        (0.0121104, 0, 0.351564), (0.0935195, 0, 0.281599), (0.0935195, 0, 0.195095), (-0.0935195, 0, 0.195095), (-0.0935195, 0, 0.281599), (-0.0133947, 0, 0.351564)], n= mC + '_mCtrl')
        mirrorCtrlSpace = mc.group(em=True, n= mC + '_mCtrlSpace')
        mirrorCtrlCustSpace = mc.group(em=True, n=mC + '_customization_mCtrlSpace')
        mirrorCtrlMasterSpace = mc.group(em= True, n= mC + '_mCtrlMasterSpace')
        mc.parent(mirrorCtrl, mirrorCtrlSpace), mc.parent(mirrorCtrlSpace, mirrorCtrlCustSpace), mc.parent(mirrorCtrlCustSpace, mirrorCtrlMasterSpace)
        mc.delete(mc.parentConstraint(mC, mirrorCtrlMasterSpace, mo=False))

    Master_list = ['LeftMaxilarDn_Master', 'LeftMaxilarMaster', 'LeftTempleMaster', 'LeftCheekMaster', 'LeftNoseMaster', 'LeftEyeBrowMaster']

    for mM in (Master_list):
        mirrorCtrl = mc.curve(d = 1, p = [(-0.0133947, 0, 0.351564), (-0.0130162, 0, 0.916036), (-0.126636, 0, 0.85811), (0, 0, 1.111383), (0.126636, 0, 0.85811), (0.0121104, 0, 0.916036),
        (0.0121104, 0, 0.351564), (0.0935195, 0, 0.281599), (0.0935195, 0, 0.195095), (-0.0935195, 0, 0.195095), (-0.0935195, 0, 0.281599), (-0.0133947, 0, 0.351564)], n= mM + '_mCtrl')
        mirrorCtrlCustSpace = mc.group(em=True, n=mM + '_customization_mCtrlSpace')
        mirrorCtrlSpace = mc.group(em=True, n= mM + '_mCtrlSpace')
        mc.parent(mirrorCtrl, mirrorCtrlCustSpace), mc.parent(mirrorCtrlCustSpace, mirrorCtrlSpace)
        mc.delete(mc.parentConstraint(mM, mirrorCtrlSpace, mo=False))

    mC_ctrlsList = ['LeftEyeLidDnOut_mCtrl', 'LeftEyeLidDnIn_mCtrl', 'LeftEyeLidUpIn_mCtrl', 'LeftEyeLidUpIn_mCtrl', 'LeftEyeLidOut_mCtrl', 'LeftEyeLidIn_mCtrl',
                    'LeftEyeLidDn_mCtrl', 'LeftEyeLidUp_mCtrl', 'LeftEyeLidMaster_mCtrl', 'LeftLobe_mCtrl', 'LeftEarUp_mCtrl', 'LeftEar_mCtrl', 'LeftEyeBrow1_mCtrl', 'LeftEyeLidUpOut_mCtrl',
                    'LeftEyeBrow2_mCtrl', 'LeftEyeBrow3_mCtrl', 'LeftLipUp1_mCtrl', 'LeftLipUp2_mCtrl', 'LeftLipDn2_mCtrl', 'LeftLipDn1_mCtrl', 'LeftLipDn1Out_mCtrl', 'LeftEyeBrowMaster_mCtrl',
                    'LeftLipUp1Out_mCtrl', 'LeftNasalUp_mCtrl', 'LeftNostril_mCtrl', 'LeftOcularDn_mCtrl', 'LeftCheekbone_mCtrl', 'LeftCheekboneDn_mCtrl', 'LeftCheekDn_mCtrl',
                    'LeftCheekUp_mCtrl', 'LeftMaxilarDn_mCtrl', 'LeftMaxilarUp_mCtrl', 'LeftCheekBoneFront_mCtrl', 'LeftUpperHead_mCtrl', 'LeftMaxilarNeck_mCtrl', 'LeftMaxilarHead_mCtrl',
                    'LeftTemples_mCtrl', 'LeftSide_mCtrl', 'LeftMaxilarMaster_mCtrl', 'LeftMaxilarDn_Master_mCtrl', 'LeftTempleMaster_mCtrl', 'LeftNoseMaster_mCtrl', 'LeftCheekMaster_mCtrl']

    mc.parent('LeftMaxilarMaster_mCtrlSpace', 'LeftMaxilarDn_Master_mCtrl')

    for mCtrlC in (mC_ctrlsList):
        controlColor(mCtrlC, 18)

    ################################### parent mCtrls left Side ##########################################################

    mc.parent('LeftCheekUp_ctrlSpace', 'LeftCheekUp_mCtrl'), mc.parent('LeftMaxilarHead_ctrlSpace', 'LeftMaxilarHead_mCtrl'),
    mc.parent('LeftTemples_ctrlSpace', 'LeftTemples_mCtrl'), mc.parent('LeftMaxilarUp_ctrlSpace', 'LeftMaxilarUp_mCtrl'),
    mc.parent('LeftUpperHead_ctrlSpace', 'LeftUpperHead_mCtrl'), mc.parent('LeftSide_ctrlSpace', 'LeftSide_mCtrl')

    mc.parent('LeftEar_ctrlSpace', 'LeftEar_mCtrl'), mc.parent('LeftLobe_ctrlSpace', 'LeftLobe_mCtrl')
    mc.parent('LeftEarUp_ctrlSpace', 'LeftEarUp_mCtrl'), mc.parent('LeftLobe_mCtrlMasterSpace', 'LeftEarUp_mCtrlMasterSpace', 'LeftEar_ctrl')

    mc.parent('LeftMaxilarHead_mCtrlMasterSpace', 'LeftTemples_mCtrlMasterSpace', 'LeftTempleMaster_mCtrl')

    mc.parent('LeftCheekUp_mCtrlMasterSpace', 'LeftEar_mCtrlMasterSpace', 'LeftUpperHead_mCtrlMasterSpace', 'LeftTempleMaster_mCtrlSpace', 'LeftSide_ctrl')

    #################################################### parent mCtrls eyelid ####################################################
    mc.parent('LeftEyeLidMaster_ctrlSpace', 'LeftEyeLidMaster_mCtrl'), mc.parent('LeftEyeLidDnOut_ctrlSpace', 'LeftEyeLidDnOut_mCtrl'),
    mc.parent('LeftEyeLidDnIn_ctrlSpace', 'LeftEyeLidDnIn_mCtrl'), mc.parent('LeftEyeLidUpIn_ctrlSpace', 'LeftEyeLidUpIn_mCtrl'),
    mc.parent('LeftEyeLidUpOut_ctrlSpace', 'LeftEyeLidUpOut_mCtrl'), mc.parent('LeftEyeLidIn_ctrlSpace', 'LeftEyeLidIn_mCtrl'),
    mc.parent('LeftEyeLidDn_ctrlSpace', 'LeftEyeLidDn_mCtrl'), mc.parent('LeftEyeLidOut_ctrlSpace', 'LeftEyeLidOut_mCtrl'),
    mc.parent('LeftEyeLidUp_ctrlSpace', 'LeftEyeLidUp_mCtrl')

    mc.parent('LeftEyeLidUp_mCtrlMasterSpace', 'LeftEyeLidDn_mCtrlMasterSpace', 'LeftEyeLidIn_mCtrlMasterSpace', 'LeftEyeLidOut_mCtrlMasterSpace', 'LeftEyeLidUpOut_mCtrlMasterSpace',
    'LeftEyeLidUpIn_mCtrlMasterSpace', 'LeftEyeLidDnIn_mCtrlMasterSpace', 'LeftEyeLidDnOut_mCtrlMasterSpace', 'LeftEyeLidMaster_ctrl')

    ################################################## parent mCtrls Center #######################################################

    mc.parent('LeftEyeBrow1_ctrlSpace', 'LeftEyeBrow1_mCtrl'), mc.parent('LeftEyeBrow2_ctrlSpace', 'LeftEyeBrow2_mCtrl'), mc.parent('LeftEyeBrow3_ctrlSpace', 'LeftEyeBrow3_mCtrl'),
    mc.parent('LeftOcularDn_ctrlSpace', 'LeftOcularDn_mCtrl'), mc.parent('LeftMaxilarNeck_ctrlSpace', 'LeftMaxilarNeck_mCtrl'), mc.parent('LeftMaxilarDn_ctrlSpace', 'LeftMaxilarDn_mCtrl'),
    mc.parent('LeftNasalUp_ctrlSpace', 'LeftNasalUp_mCtrl'), mc.parent('LeftCheekBoneFront_ctrlSpace', 'LeftCheekBoneFront_mCtrl'), mc.parent('LeftCheekbone_ctrlSpace', 'LeftCheekbone_mCtrl'),
    mc.parent('LeftNostril_ctrlSpace', 'LeftNostril_mCtrl'), mc.parent('LeftCheekboneDn_ctrlSpace', 'LeftCheekboneDn_mCtrl'), mc.parent('LeftCheekDn_ctrlSpace', 'LeftCheekDn_mCtrl'),
    mc.parent('LeftLipUp1Out_ctrlSpace', 'LeftLipUp1Out_mCtrl'),  mc.parent('LeftLipUp1_ctrlSpace', 'LeftLipUp1_mCtrl'), mc.parent('LeftLipUp2_ctrlSpace', 'LeftLipUp2_mCtrl'),
    mc.parent('LeftLipDn2_ctrlSpace', 'LeftLipDn2_mCtrl'), mc.parent('LeftLipDn1Out_ctrlSpace', 'LeftLipDn1Out_mCtrl'), mc.parent('LeftLipDn1_ctrlSpace', 'LeftLipDn1_mCtrl')

    ######################################### mirror maxilar /  templete master

    masterMirrorCtrls = ['LeftMaxilarMaster_mCtrl', 'LeftMaxilarDn_Master_mCtrl', 'LeftTempleMaster_mCtrl', 'LeftEyeBrowMaster_mCtrl', 'LeftCheekMaster_mCtrl', 'LeftNoseMaster_mCtrl']

    for rmMC in (masterMirrorCtrls):
        rightMasterConst = mc.group(em=True, n= rmMC + '_const')
        rightMasterConstSpace = mc.group(rightMasterConst, n= rmMC + '_constSpace')
        rightMasterMasterConstSpace = mc.group(rightMasterConstSpace, n= rmMC + '_masterConstSpace')
        mc.delete(mc.parentConstraint(rmMC, rightMasterMasterConstSpace, mo=False))

    mc.rename('LeftMaxilarMaster_mCtrl_masterConstSpace', 'RightMaxilarMaster_mCtrl_masterConstSpace'), mc.rename('LeftMaxilarMaster_mCtrl_constSpace', 'RightMaxilarMaster_mCtrl_constSpace'), mc.rename('LeftMaxilarMaster_mCtrl_const', 'RightMaxilarMaster_mCtrl_const')
    mc.rename('LeftMaxilarDn_Master_mCtrl_masterConstSpace', 'RightMaxilarDn_Master_mCtrl_masterConstSpace'), mc.rename('LeftMaxilarDn_Master_mCtrl_constSpace', 'RightMaxilarDn_Master_mCtrl_constSpace'), mc.rename('LeftMaxilarDn_Master_mCtrl_const', 'RightMaxilarDn_Master_mCtrl_const')
    mc.rename('LeftTempleMaster_mCtrl_masterConstSpace', 'RightTempleMaster_mCtrl_masterConstSpace'), mc.rename('LeftTempleMaster_mCtrl_constSpace', 'RightTempleMaster_mCtrl_constSpace'), mc.rename('LeftTempleMaster_mCtrl_const', 'RightTempleMaster_mCtrl_const')
    mc.rename('LeftEyeBrowMaster_mCtrl_masterConstSpace', 'RightEyeBrowMaster_mCtrl_masterConstSpace'), mc.rename('LeftEyeBrowMaster_mCtrl_constSpace', 'RightEyeBrowMaster_mCtrl_constSpace'), mc.rename('LeftEyeBrowMaster_mCtrl_const', 'RightEyeBrowMaster_mCtrl_const')
    mc.rename('LeftCheekMaster_mCtrl_masterConstSpace', 'RightCheekMaster_mCtrl_masterConstSpace'), mc.rename('LeftCheekMaster_mCtrl_constSpace', 'RightCheekMaster_mCtrl_constSpace'), mc.rename('LeftCheekMaster_mCtrl_const', 'RightCheekMaster_mCtrl_const')
    mc.rename('LeftNoseMaster_mCtrl_masterConstSpace', 'RightNoseMaster_mCtrl_masterConstSpace'), mc.rename('LeftNoseMaster_mCtrl_constSpace', 'RightNoseMaster_mCtrl_constSpace'), mc.rename('LeftNoseMaster_mCtrl_const', 'RightNoseMaster_mCtrl_const')

    mc.parent('RightMaxilarMaster_mCtrl_masterConstSpace', 'RightMaxilarDn_Master_mCtrl_const')
    rightMasterGRP = mc.group(em=True, n= 'RightMasterConst_GRP')
    mc.parent('RightMaxilarDn_Master_mCtrl_masterConstSpace', 'RightEyeBrowMaster_mCtrl_masterConstSpace', 'RightCheekMaster_mCtrl_masterConstSpace', 'RightNoseMaster_mCtrl_masterConstSpace', rightMasterGRP)
    mc.setAttr(rightMasterGRP + '.sx', -1)

    mc.parent('RightMaxilarDn_constMasterSpace', 'RightMaxilarUp_constMasterSpace', 'RightMaxilarMaster_mCtrl_const')
    mc.parent('RightCheekDn_constMasterSpace', 'RightCheekUp_constMasterSpace', 'RightMaxilarDn_Master_mCtrl_const')
    mc.parent('RightEyeBrow1_constMasterSpace', 'RightEyeBrow2_constMasterSpace', 'RightEyeBrow3_constMasterSpace', 'RightEyeBrowMaster_mCtrl_const')
    mc.parent('RightNostril_constMasterSpace', 'RightNasalUp_constMasterSpace', 'RightNoseMaster_mCtrl_const')
    mc.parent('RightTemples_constMasterSpace', 'RightMaxilarHead_constMasterSpace', 'RightTempleMaster_mCtrl_const')
    mc.parent('RightCheekBoneFront_constMasterSpace', 'RightCheekbone_constMasterSpace', 'RightCheekMaster_mCtrl_const')
    mc.parent('RightEar_constMasterSpace', 'RightUpperHead_constMasterSpace', 'RightTempleMaster_mCtrl_masterConstSpace', 'RightSide_ctrl')

    ########################################################################################################################
    ########################################                                           ######################################
    ########################################       Right Nodes mirror connections      #####################################
    ########################################                                           #####################################
    ########################################################################################################################

    left_MCtrls = ['LeftSide_mCtrl', 'LeftEar_mCtrl', 'LeftUpperHead_mCtrl', 'LeftEarUp_mCtrl', 'LeftLobe_mCtrl', 'LeftTemples_mCtrl', 'LeftEyeBrowMaster_mCtrl',
    'LeftMaxilarHead_mCtrl', 'LeftMaxilarUp_mCtrl', 'LeftCheekUp_mCtrl', 'LeftEyeLidMaster_mCtrl', 'LeftEyeLidUp_mCtrl', 'LeftEyeLidDn_mCtrl',
    'LeftEyeLidIn_mCtrl', 'LeftEyeLidOut_mCtrl', 'LeftEyeLidUpOut_mCtrl', 'LeftEyeLidUpIn_mCtrl', 'LeftEyeLidDnIn_mCtrl', 'LeftEyeLidDnOut_mCtrl',
    'LeftOcularDn_mCtrl', 'LeftEyeBrow1_mCtrl', 'LeftEyeBrow2_mCtrl', 'LeftEyeBrow3_mCtrl', 'LeftNasalUp_mCtrl', 'LeftCheekBoneFront_mCtrl', 'LeftCheekbone_mCtrl',
    'LeftNostril_mCtrl', 'LeftCheekboneDn_mCtrl', 'LeftCheekDn_mCtrl', 'LeftMaxilarDn_mCtrl', 'LeftMaxilarNeck_mCtrl', 'LeftLipUp1Out_mCtrl', 'LeftLipUp1_mCtrl', 'LeftTempleMaster_mCtrl',
    'LeftLipDn1_mCtrl', 'LeftLipDn1Out_mCtrl', 'LeftLipUp2_mCtrl', 'LeftLipDn2_mCtrl', 'LeftMaxilarMaster_mCtrl', 'LeftMaxilarDn_Master_mCtrl', 'LeftNoseMaster_mCtrl', 'LeftCheekMaster_mCtrl']

    right_MCtrls = ['RightSide_constSpace', 'RightEar_constSpace', 'RightUpperHead_constSpace', 'RightEarUp_constSpace', 'RightLobe_constSpace', 'RightTemples_constSpace', 'RightEyeBrowMaster_mCtrl_constSpace',
    'RightMaxilarHead_constSpace', 'RightMaxilarUp_constSpace', 'RightCheekUp_constSpace', 'RightEyeLidMaster_constSpace', 'RightEyeLidUp_constSpace', 'RightEyeLidDn_constSpace',
    'RightEyeLidIn_constSpace', 'RightEyeLidOut_constSpace', 'RightEyeLidUpOut_constSpace', 'RightEyeLidUpIn_constSpace', 'RightEyeLidDnIn_constSpace', 'RightEyeLidDnOut_constSpace',
    'RightOcularDn_constSpace', 'RightEyeBrow1_constSpace', 'RightEyeBrow2_constSpace', 'RightEyeBrow3_constSpace', 'RightNasalUp_constSpace', 'RightCheekBoneFront_constSpace', 'RightCheekbone_constSpace',
    'RightNostril_constSpace', 'RightCheekboneDn_constSpace', 'RightCheekDn_constSpace', 'RightMaxilarDn_constSpace', 'RightMaxilarNeck_constSpace', 'RightLipUp1Out_constSpace', 'RightLipUp1_constSpace', 'RightTempleMaster_mCtrl_constSpace',
    'RightLipDn1_constSpace', 'RightLipDn1Out_constSpace', 'RightLipUp2_constSpace', 'RightLipDn2_constSpace', 'RightMaxilarMaster_mCtrl_constSpace', 'RightMaxilarDn_Master_mCtrl_constSpace', 'RightNoseMaster_mCtrl_constSpace', 'RightCheekMaster_mCtrl_constSpace']
    transMD_list = []
    rotMD_List = []
    sclMD_List = []

    for i in (left_MCtrls):
        transMD = mc.createNode('multiplyDivide', n= i + '_Trans_MD')
        rotMD = mc.createNode('multiplyDivide', n= i + '_Rot_MD')
        sclMD = mc.createNode('multiplyDivide', n = i + '_Scl_MD')

        transMD_list.append(transMD)
        rotMD_List.append(rotMD)
        sclMD_List.append(sclMD)

        mc.setAttr(transMD + '.input2X', -1)
        mc.setAttr(transMD + '.input2Y', -1)
        mc.setAttr(transMD + '.input2Z', -1)

    ################################################# translation

    for transInput in range(len(left_MCtrls)):
        mc.connectAttr(left_MCtrls[transInput] + '.tx', transMD_list[transInput] + '.input1X')
        mc.connectAttr(left_MCtrls[transInput] + '.ty', transMD_list[transInput] + '.input1Y')
        mc.connectAttr(left_MCtrls[transInput] + '.tz', transMD_list[transInput] + '.input1Z')

    for transOutput in range(len(right_MCtrls)):
        mc.connectAttr(transMD_list[transOutput] + '.outputX', right_MCtrls[transOutput] + '.tx')
        mc.connectAttr(transMD_list[transOutput] + '.outputY', right_MCtrls[transOutput] + '.ty')
        mc.connectAttr(transMD_list[transOutput] + '.outputZ', right_MCtrls[transOutput] + '.tz')

    ############################################## rotation

    for rotInput in range(len(left_MCtrls)):
        mc.connectAttr(left_MCtrls[rotInput] + '.rx', rotMD_List[rotInput] + '.input1X')
        mc.connectAttr(left_MCtrls[rotInput] + '.ry', rotMD_List[rotInput] + '.input1Y')
        mc.connectAttr(left_MCtrls[rotInput] + '.rz', rotMD_List[rotInput] + '.input1Z')

    for rotOutput in range(len(right_MCtrls)):
        mc.connectAttr(rotMD_List[rotOutput] + '.outputX', right_MCtrls[rotOutput] + '.rx')
        mc.connectAttr(rotMD_List[rotOutput] + '.outputY', right_MCtrls[rotOutput] + '.ry')
        mc.connectAttr(rotMD_List[rotOutput] + '.outputZ', right_MCtrls[rotOutput] + '.rz')

    ################################################ scale

    for sclInput in range(len(left_MCtrls)):
        mc.connectAttr(left_MCtrls[sclInput] + '.sx', sclMD_List[sclInput] + '.input1X')
        mc.connectAttr(left_MCtrls[sclInput] + '.sy', sclMD_List[sclInput] + '.input1Y')
        mc.connectAttr(left_MCtrls[sclInput] + '.sz', sclMD_List[sclInput] + '.input1Z')

    for sclOutput in range(len(right_MCtrls)):
        mc.connectAttr(sclMD_List[sclOutput] + '.outputX', right_MCtrls[sclOutput] + '.sx')
        mc.connectAttr(sclMD_List[sclOutput] + '.outputY', right_MCtrls[sclOutput] + '.sy')
        mc.connectAttr(sclMD_List[sclOutput] + '.outputZ', right_MCtrls[sclOutput] + '.sz')

    ################################## master mirror controls setAttr axis

    mCtrl_TransMD_List = ['LeftMaxilarDn_Master_mCtrl_Trans_MD', 'LeftMaxilarMaster_mCtrl_Trans_MD', 'LeftNoseMaster_mCtrl_Trans_MD',
    'LeftCheekMaster_mCtrl_Trans_MD', 'LeftTempleMaster_mCtrl_Trans_MD']

    for mCtrltransMD in (mCtrl_TransMD_List):
        mc.setAttr(mCtrltransMD + '.input2X', 1)
        mc.setAttr(mCtrltransMD + '.input2Y', 1)
        mc.setAttr(mCtrltransMD + '.input2Z', 1)

    mc.setAttr('LeftEyeBrowMaster_mCtrl_Trans_MD.input2X', 1)
    mc.setAttr('LeftEyeBrowMaster_mCtrl_Trans_MD.input2Y', 1)
    mc.setAttr('LeftEyeBrowMaster_mCtrl_Trans_MD.input2Z', 1)

    ##############################################################################################################################################
    #####################################                                          ###############################################################
    #####################################            clean up                      ###############################################################
    #####################################                                          ###############################################################
    ##############################################################################################################################################

    ############################### parent lipsMaster pivots
    mc.parent('lipsMaster_ctrlMasterSpace', 'LipDnPivotMaster_ctrlMasterSpace', 'LipUpPivotMaster_ctrlMasterSpace', 'mouthPivot')

    ################################# parent  right eyelid
    mc.parent('RightEyeLidDnOut_constMasterSpace', 'RightEyeLidDnIn_constMasterSpace', 'RightEyeLidUpIn_constMasterSpace', 'RightEyeLidUpOut_constMasterSpace',
    'RightEyeLidOut_constMasterSpace', 'RightEyeLidIn_constMasterSpace', 'RightEyeLidDn_constMasterSpace', 'RightEyeLidUp_constMasterSpace', 'RightEyeLidMaster_ctrl')

    ############################ parent right ear
    mc.parent('RightLobe_constMasterSpace', 'RightEarUp_constMasterSpace', 'RightEar_ctrl')

    mc.parent('RightEyeLidMaster_constMasterSpace', 'RightLipUp1_constMasterSpace', 'RightLipUp2_constMasterSpace', 'RightLipDn2_constMasterSpace', 'RightLipDn1_constMasterSpace', 'RightLipDn1Out_constMasterSpace',
              'RightLipUp1Out_constMasterSpace', 'RightOcularDn_constMasterSpace', 'RightCheekboneDn_constMasterSpace', 'RightMaxilarNeck_constMasterSpace', 'RightSide_constMasterSpace', rightMasterGRP)

    ################################### parent left side controls
    mc.parent('LeftEyeBrow1_mCtrlMasterSpace', 'LeftEyeBrow2_mCtrlMasterSpace', 'LeftEyeBrow3_mCtrlMasterSpace', 'LeftEyeBrowMaster_mCtrl')
    mc.parent('LeftMaxilarDn_mCtrlMasterSpace', 'LeftMaxilarUp_mCtrlMasterSpace', 'LeftMaxilarMaster_mCtrl')
    mc.parent('LeftCheekDn_mCtrlMasterSpace', 'LeftCheekUp_mCtrlMasterSpace', 'LeftMaxilarDn_Master_mCtrl')
    mc.parent('LeftNostril_mCtrlMasterSpace', 'LeftNasalUp_mCtrlMasterSpace', 'LeftNoseMaster_mCtrl')
    mc.parent('LeftCheekBoneFront_mCtrlMasterSpace', 'LeftCheekbone_mCtrlMasterSpace', 'LeftCheekMaster_mCtrl')
    leftMasterGRP = mc.group('LeftEyeLidMaster_mCtrlMasterSpace', 'LeftLipUp1_mCtrlMasterSpace', 'LeftLipUp2_mCtrlMasterSpace', 'LeftLipDn2_mCtrlMasterSpace', 'LeftLipDn1_mCtrlMasterSpace', 'LeftLipDn1Out_mCtrlMasterSpace',
                             'LeftLipUp1Out_mCtrlMasterSpace', 'LeftOcularDn_mCtrlMasterSpace', 'LeftCheekboneDn_mCtrlMasterSpace', 'LeftMaxilarNeck_mCtrlMasterSpace', 'LeftSide_mCtrlMasterSpace', 'LeftMaxilarDn_Master_mCtrlSpace',
                             'LeftCheekMaster_mCtrlSpace', 'LeftNoseMaster_mCtrlSpace', 'LeftEyeBrowMaster_mCtrlSpace', n= 'LeftMasterCtrl_GRP')

    ############################### parent center controls
    centerMasterGRP = mc.group('Chin_ctrlMasterSpace', 'UpperHead_ctrlMasterSpace', 'FrontHead_ctrlMasterSpace', 'Frown_ctrlMasterSpace', 'Nose_ctrlMasterSpace', 'NasalSeptum_ctrlMasterSpace', 'NoseBrige_ctrlMasterSpace',
                               'NoseDn_ctrlMasterSpace', 'LipDn_ctrlMasterSpace', 'LipUp_ctrlMasterSpace', 'LipUpOut_ctrlMasterSpace', 'LipDnOut_ctrlMasterSpace', 'JawDn_ctrlMasterSpace', 'NoseUp_ctrlMasterSpace', n= 'CenterMasterCtrl_GRP')

    ############################# parent facial master control
    facialMasterCtrl_GRP = mc.group(leftMasterGRP, centerMasterGRP, rightMasterGRP, 'mouthPivot', 'jawMain_lipSupport_locSpace', 'headMain_lipSupport_locSpace', n= 'FacialMasterCtrl_GRP')
    mc.parent(facialMasterCtrl_GRP, 'MotionSystem')
    mc.parentConstraint('Head_M', facialMasterCtrl_GRP, mo=True)

    mc.delete('FacialTempleteRig')

    mc.select(d = True)

    ########################################################################################################################
    ########################################                                           #####################################
    ########################################          jaw open system connections      #####################################
    ########################################                                           #####################################
    ########################################################################################################################

    ######################################## master lips pivots

    lipPiv_List = ['LipUpPivotMaster_ctrlSpace', 'LipDnPivotMaster_ctrlSpace']

    for lipM_ctrl in (lipPiv_List):
        mc.connectAttr('lipsMaster_ctrl.tx', lipM_ctrl + '.tx')
        mc.connectAttr('lipsMaster_ctrl.ty', lipM_ctrl + '.ty')
        mc.connectAttr('lipsMaster_ctrl.tz', lipM_ctrl + '.tz')

        mc.connectAttr('lipsMaster_ctrl.rx', lipM_ctrl + '.rx')
        mc.connectAttr('lipsMaster_ctrl.ry', lipM_ctrl + '.ry')
        mc.connectAttr('lipsMaster_ctrl.rz', lipM_ctrl + '.rz')

        mc.connectAttr('lipsMaster_ctrl.sx', lipM_ctrl + '.sx')
        mc.connectAttr('lipsMaster_ctrl.sy', lipM_ctrl + '.sy')
        mc.connectAttr('lipsMaster_ctrl.sz', lipM_ctrl + '.sz')

    mc.parentConstraint('LipUpPivotMaster_ctrl', 'LipUpPivotMaster', mo=True), mc.setAttr('LipUpPivotMaster_parentConstraint1.interpType', 2)
    mc.parentConstraint('LipDnPivotMaster_ctrl', 'LipDnPivotMaster', mo=True), mc.setAttr('LipDnPivotMaster_parentConstraint1.interpType', 2)
    mc.scaleConstraint('LipUpPivotMaster_ctrl', 'LipUpPivotMaster', mo=True), mc.scaleConstraint('LipDnPivotMaster_ctrl', 'LipDnPivotMaster', mo=True)
    mc.parentConstraint('jawMain_lipSupport_loc', 'LipDnPivotMaster_ctrlMasterSpace', mo=True), mc.setAttr('LipDnPivotMaster_ctrlMasterSpace_parentConstraint1.interpType', 2)

    LipDn_List = ['LeftLipDn1Out_mCtrlSpace', 'LeftLipDn1_mCtrlSpace', 'RightLipDn1_const', 'RightLipDn1Out_const']
    LipUp_List = ['LeftLipUp1Out_mCtrlSpace', 'LeftLipUp1_mCtrlSpace', 'RightLipUp1_const', 'RightLipUp1Out_const']
    LipComDn_List = ['LeftLipDn2_mCtrlSpace', 'RightLipDn2_const']
    LipComUp_List = ['LeftLipUp2_mCtrlSpace', 'RightLipUp2_const']
    LipCenDn_List = ['LipDnOut_ctrlSpace', 'LipDn_ctrlSpace']
    LipCenUp_List = ['LipUpOut_ctrlSpace', 'LipUp_ctrlSpace']
    MaxMaster_List = ['LeftMaxilarDn_Master_mCtrlSpace', 'RightMaxilarDn_Master_mCtrl_masterConstSpace']
    ChinJawDn_List = ['Chin_ctrlSpace', 'JawDn_ctrlSpace']

    for lipDn in (LipDn_List):
        mc.parentConstraint('LipDnPivotMaster', lipDn, w=0.9, mo=True)
        mc.parentConstraint('headMain_lipSupport_loc', lipDn, w=0.1, mo=True)
        mc.setAttr(lipDn + '_parentConstraint1.interpType', 2)

    for lipUp in (LipUp_List):
        mc.parentConstraint('LipUpPivotMaster', lipUp, w=0.8, mo=True)
        mc.parentConstraint('jawMain_lipSupport_loc', lipUp, w=0.2, mo=True)
        mc.setAttr(lipUp + '_parentConstraint1.interpType', 2)

    for lipComDn in (LipComDn_List):
        mc.parentConstraint('headMain_lipSupport_loc', lipComDn, w=0.4, mo=True)
        mc.parentConstraint('LipDnPivotMaster', lipComDn, w=0.6, mo=True)
        mc.setAttr(lipComDn + '_parentConstraint1.interpType', 2)

    for lipComUp in (LipComUp_List):
        mc.parentConstraint('jawMain_lipSupport_loc', lipComUp, w=0.45, mo=True)
        mc.parentConstraint('LipUpPivotMaster', lipComUp, w=0.55, mo=True)
        mc.setAttr(lipComUp + '_parentConstraint1.interpType', 2)

    for LipCenDn in (LipCenDn_List):
        mc.parentConstraint('LipDnPivotMaster', LipCenDn, w=0.95, mo=True)
        mc.parentConstraint('headMain_lipSupport_loc', LipCenDn, w=0.05, mo=True)
        mc.setAttr(LipCenDn + '_parentConstraint1.interpType', 2)

    for LipCenUp in (LipCenUp_List):
        mc.parentConstraint('LipUpPivotMaster', LipCenUp, w=0.95, mo=True)
        mc.parentConstraint('jawMain_lipSupport_loc', LipCenUp, w=0.05, mo=True)
        mc.setAttr(LipCenUp + '_parentConstraint1.interpType', 2)

    for MaxMaster in (MaxMaster_List):
        mc.parentConstraint('jawMain_lipSupport_loc', MaxMaster, w=0.7, mo=True)
        mc.parentConstraint('headMain_lipSupport_loc', MaxMaster, w=0.3, mo=True)
        mc.setAttr(MaxMaster + '_parentConstraint1.interpType', 2)

    for ChinJawDn in (ChinJawDn_List):
        mc.parentConstraint('jawMain_lipSupport_loc', ChinJawDn, w=0.98, mo=True)
        mc.parentConstraint('headMain_lipSupport_loc', ChinJawDn, w=0.02, mo=True)
        mc.setAttr(ChinJawDn + '_parentConstraint1.interpType', 2)

    LeftSideMaxUpDn_List = ['LeftMaxilarUp_mCtrlSpace', 'LeftCheekUp_mCtrlSpace']
    RightSideMaxUpDn_List = ['RightMaxilarUp_const', 'RightCheekUp_const']
    transMD_list = []

    for LeftSideMaxUpDn in (LeftSideMaxUpDn_List):
        transMD = mc.createNode('multiplyDivide', n= LeftSideMaxUpDn + '_Trans_MD')
        transMD_list.append(transMD)
        mc.setAttr(transMD + '.input2Z', -1)

        mc.connectAttr('LeftSide_mCtrl.tx', transMD + '.input1X')
        mc.connectAttr('LeftSide_mCtrl.ty', transMD + '.input1Y')
        mc.connectAttr('LeftSide_mCtrl.tz', transMD + '.input1Z')

        mc.connectAttr(transMD + '.outputX', LeftSideMaxUpDn + '.tz')
        mc.connectAttr(transMD + '.outputY', LeftSideMaxUpDn + '.ty')
        mc.connectAttr(transMD + '.outputZ', LeftSideMaxUpDn + '.tx')

    for RightSideMaxUpDn in (RightSideMaxUpDn_List):
        transMD = mc.createNode('multiplyDivide', n= RightSideMaxUpDn + '_Trans_MD')
        transMD_list.append(transMD)
        mc.setAttr(transMD + '.input2Z', -1)

        mc.connectAttr('RightSide_constSpace.tx', transMD + '.input1X')
        mc.connectAttr('RightSide_constSpace.ty', transMD + '.input1Y')
        mc.connectAttr('RightSide_constSpace.tz', transMD + '.input1Z')

        mc.connectAttr(transMD + '.outputX', RightSideMaxUpDn + '.tz')
        mc.connectAttr(transMD + '.outputY', RightSideMaxUpDn + '.ty')
        mc.connectAttr(transMD + '.outputZ', RightSideMaxUpDn + '.tx')

    mc.setAttr('LeftSide_mCtrl.rx', l=True, keyable=False, ch=False)
    mc.setAttr('LeftSide_mCtrl.ry', l=True, keyable=False, ch=False)
    mc.setAttr('LeftSide_mCtrl.rz', l=True, keyable=False, ch=False)

    mc.setAttr('LeftSide_mCtrl.sx', l=True, keyable=False, ch=False)
    mc.setAttr('LeftSide_mCtrl.sy', l=True, keyable=False, ch=False)
    mc.setAttr('LeftSide_mCtrl.sz', l=True, keyable=False, ch=False)

    mc.select(d=True)

    ######################################################################################################################################################
    #################################################################################### scale cv's
    ################################################ center
    mc.select('lipsMaster_ctrl.cv[0:7]'), mc.move(0, 0, 4, r=True, ws=True)
    mc.select('Nose_ctrl.cv[0:7]'), mc.move(0, 0, 1.4, r=True, ws=True)
    mc.select('NoseBrige_ctrl.cv[0:7]', 'NasalSeptum_ctrl.cv[0:7]', 'NoseUp_ctrl.cv[0:7]', 'NoseDn_ctrl.cv[0:7]'), mc.rotate(90, 0, 0, ocp=True)
    mc.select('FrontHead_ctrl.cv[0:7]', 'Frown_ctrl.cv[0:7]'), mc.move(0, 0, 0.375, r=True, ws=True), mc.scale(0.7, 0.7, 0.7, ocp=True)
    mc.select('UpperHead_ctrl.cv[0:7]'), mc.scale(11.5, 11.5, 11.5, ocp=True)
    mc.select('Chin_ctrl.cv[0:7]'), mc.move(0, 0, 1.4, r=True, os=True, wd=True)
    mc.select('JawDn_ctrl.cv[0:7]'), mc.scale(3.9, 1, 1, ocp=True), mc.select('JawDn_ctrl.cv[3]', 'JawDn_ctrl.cv[7]'), mc.move(0, 1.17, 0, r=True, os=True, wd=True)

    ########################################### lips
    mc.select('LeftLipUp2_ctrl.cv[0:7]', 'LeftLipDn2_ctrl.cv[0:7]', 'RightLipDn2_ctrl.cv[0:7]', 'LipDn_ctrl.cv[0:7]', 'LeftLipDn1Out_ctrl.cv[0:7]', 'RightLipUp1_ctrl.cv[0:7]',
              'LeftLipUp1Out_ctrl.cv[0:7]', 'RightLipDn1_ctrl.cv[0:7]', 'LeftLipUp1_ctrl.cv[0:7]', 'RightLipUp1Out_ctrl.cv[0:7]', 'LeftLipDn1_ctrl.cv[0:7]', 'RightLipDn1Out_ctrl.cv[0:7]',
              'LipDnOut_ctrl.cv[0:7]', 'RightLipUp2_ctrl.cv[0:7]', 'LipUpOut_ctrl.cv[0:7]', 'LipUp_ctrl.cv[0:7]'), mc.scale(0.4, 0.4, 0.4, ocp=True)
    mc.select('LipUpOut_ctrl.cv[0:7]', 'LipUp_ctrl.cv[0:7]'), mc.move(0, 0.156, 0.47, r=True, ws=True)
    mc.select('LipDn_ctrl.cv[0:7]', 'LipDnOut_ctrl.cv[0:7]'), mc.move(0, -0.33, 0.7, r=True, ws=True)

    ### left
    mc.select('LeftLipUp1Out_ctrl.cv[0:7]', 'LeftLipUp1_ctrl.cv[0:7]'), mc.move(0, 0.29, 0.76, r=True, os=True, wd=True)
    mc.select('LeftLipDn1Out_ctrl.cv[0:7]', 'LeftLipDn1_ctrl.cv[0:7]'), mc.move(0, -0.5, 0.61, r=True, os=True, wd=True)
    mc.select('LeftLipUp2_ctrl.cv[0:7]'), mc.move(0, 0.38, 0.8, r=True, os=True, wd=True), mc.select('LeftLipDn2_ctrl.cv[0:7]'), mc.move(0, -0.5, 0.6, r=True, os=True, wd=True)

    ### right
    mc.select('RightLipUp2_ctrl.cv[0:7]'), mc.move(0, -0.38, -0.8, r=True, os=True, wd=True), mc.select('RightLipDn2_ctrl.cv[0:7]'), mc.move(0, 0.5, -0.6, r=True, os=True, wd=True)
    mc.select('RightLipDn1Out_ctrl.cv[0:7]', 'RightLipDn1_ctrl.cv[0:7]'), mc.move(0, 0.5, -0.61, r=True, os=True, wd=True)
    mc.select('RightLipUp1Out_ctrl.cv[0:7]', 'RightLipUp1_ctrl.cv[0:7]'), mc.move(0, -0.29, -0.76, r=True, os=True, wd=True)

    ############################################## eyebrow
    mc.select('LeftEyeBrow2_ctrl.cv[0:7]', 'LeftEyeBrow3_ctrl.cv[0:7]', 'LeftEyeBrow1_ctrl.cv[0:7]'), mc.scale(00.5, 0.5, 0.5, ocp=True), mc.move(0, 0, 0.3, r=True, os=True, wd=True)
    mc.select('RightEyeBrow2_ctrl.cv[0:7]', 'RightEyeBrow3_ctrl.cv[0:7]', 'RightEyeBrow1_ctrl.cv[0:7]'), mc.scale(00.5, 0.5, 0.5, ocp=True), mc.move(0, 0, -0.3, r=True, os=True, wd=True)

    ########################################### left side
    mc.select('LeftCheekBoneFront_ctrl.cv[0:7]', 'LeftCheekDn_ctrl.cv[0:7]', 'LeftNasalUp_ctrl.cv[0:7]', 'LeftCheekboneDn_ctrl.cv[0:7]', 'LeftMaxilarHead_ctrl.cv[0:7]',
              'LeftMaxilarDn_ctrl.cv[0:7]', 'LeftOcularDn_ctrl.cv[0:7]', 'LeftMaxilarUp_ctrl.cv[0:7]', 'LeftCheekbone_ctrl.cv[0:7]', 'LeftTemples_ctrl.cv[0:7]', 'LeftMaxilarNeck_ctrl.cv[0:7]',
              'LeftCheekUp_ctrl.cv[0:7]'), mc.scale(0.4, 0.4, 0.4, ocp=True), mc.move(0, 0, 0.25, r=True, os=True, wd=True)
    mc.select('LeftEyeLidMaster_ctrlShape.cv[0:7]'), mc.scale(5, 5, 5, ocp=True)
    mc.select('LeftEyeLidUpIn_ctrl.cv[0:7]', 'LeftEyeLidDnIn_ctrl.cv[0:7]', 'LeftEyeLidDnOut_ctrl.cv[0:7]', 'LeftEyeLidUp_ctrl.cv[0:7]', 'LeftEyeLidUpOut_ctrl.cv[0:7]',
              'LeftEyeLidDn_ctrl.cv[0:7]', 'LeftEyeLidIn_ctrl.cv[0:7]', 'LeftEyeLidOut_ctrl.cv[0:7]'), mc.scale(0.2, 0.2, 0.2, ocp=True), mc.move(0, 0, 0.35, r=True, os=True, wd=True)
    mc.select('LeftNostril_ctrl.cv[0:7]'), mc.rotate(0, -27, 0, ocp=True), mc.move(0, 0.65, 0.15, r=True, os=True, wd=True)
    mc.select('curveShape29.cv[0:11]', 'LeftLobe_ctrl.cv[0:7]'), mc.move(0, 0, 0.45, r=True, os=True, wd=True)
    mc.select('LeftEar_ctrlShape.cv[0:7]'), mc.move(0.55, 0, 0, r=True, os=True, wd=True)
    mc.select('LeftSide_ctrl.cv[0:7]'), mc.scale(5.2, 5.2, 5.2, ocp=True)
    mc.select('LeftUpperHead_ctrl.cv[0:7]'), mc.scale(6.5, 5.6, 5.6, ocp=True)

    ########################################## right side
    mc.select('RightCheekBoneFront_ctrl.cv[0:7]', 'RightCheekDn_ctrl.cv[0:7]', 'RightNasalUp_ctrl.cv[0:7]', 'RightCheekboneDn_ctrl.cv[0:7]', 'RightMaxilarHead_ctrl.cv[0:7]',
              'RightMaxilarDn_ctrl.cv[0:7]', 'RightOcularDn_ctrl.cv[0:7]', 'RightMaxilarUp_ctrl.cv[0:7]', 'RightCheekbone_ctrl.cv[0:7]', 'RightTemples_ctrl.cv[0:7]', 'RightMaxilarNeck_ctrl.cv[0:7]',
              'RightCheekUp_ctrl.cv[0:7]'), mc.scale(0.4, 0.4, 0.4, ocp=True), mc.move(0, 0, -0.25, r=True, os=True, wd=True)
    mc.select('RightEyeLidMaster_ctrlShape.cv[0:7]'), mc.scale(5, 5, 5, ocp=True)
    mc.select('RightEyeLidUpIn_ctrl.cv[0:7]', 'RightEyeLidDnIn_ctrl.cv[0:7]', 'RightEyeLidDnOut_ctrl.cv[0:7]', 'RightEyeLidUp_ctrl.cv[0:7]', 'RightEyeLidUpOut_ctrl.cv[0:7]',
              'RightEyeLidDn_ctrl.cv[0:7]', 'RightEyeLidIn_ctrl.cv[0:7]', 'RightEyeLidOut_ctrl.cv[0:7]'), mc.scale(0.2, 0.2, 0.2, ocp=True), mc.move(0, 0, -0.35, r=True, os=True, wd=True)
    mc.select('RightNostril_ctrl.cv[0:7]'), mc.rotate(0, -27, 0, ocp=True), mc.move(0, -0.65, -0.15, r=True, os=True, wd=True)
    mc.select('RightLobe_ctrl.cv[0:7]'), mc.move(0, 0, -0.45, r=True, os=True, wd=True)
    mc.select('RightEar_ctrlShape.cv[0:7]'), mc.move(-0.55, 0, 0, r=True, os=True, wd=True)
    mc.select('RightSide_ctrl.cv[0:7]'), mc.scale(5.2, 5.2, 5.2, ocp=True)
    mc.select('RightUpperHead_ctrl.cv[0:7]'), mc.scale(6.5, 5.6, 5.6, ocp=True)

    ######################################## mirror controls
    mc.select('curveShape28.cv[0:11]'), mc.move(0, 0, 3.5, r=True, os=True, wd=True)
    mc.select('curveShape42.cv[0:11]'), mc.scale(0.5, 0.5, 0.5, ocp=True)
    mc.select('curveShape31.cv[0:11]'), mc.move(1.1, 0, 0, r=True, os=True, wd=True)
    mc.select('curveShape55.cv[0:11]'), mc.scale(3, 3, 3, ocp=True), mc.rotate(0, 90, 0, ocp=True), mc.move(5, 0, 0, r=True, os=True, wd=True)
    mc.select('curveShape51.cv[0:11]'), mc.scale(1.7, 1.7, 1.7, ocp=True), mc.move(6, 0, 0, r=True, os=True, wd=True)

    mc.select(d=True)

    ######################################################################################################################################
    ########################                                                            ##################################################
    ########################                            Aim Head                        ##################################################
    ########################                                                            ##################################################
    ######################################################################################################################################

def aimHead(*args):

    mc.spaceLocator(n='HeadAim_Loc', p=(0,0,0))
    mc.parentConstraint('Head','HeadAim_Loc', mo=False)
    mc.delete('HeadAim_Loc_parentConstraint1')
    mc.setAttr('HeadAim_Loc.translateZ', 40)
    mc.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    mc.group('HeadAim_Loc', n='HeadAim_Grp')

    mc.setAttr('HeadAim_LocShape.localScaleX', 15)
    mc.setAttr('HeadAim_LocShape.localScaleY', 15)
    mc.setAttr('HeadAim_LocShape.localScaleZ', 15)

    #create aim constraint
    mc.group(em=True, n='FollowHeadNode')
    mc.parentConstraint('FKHead_M', 'FollowHeadNode', mo=False)
    mc.delete('FollowHeadNode_parentConstraint1')
    mc.parent('FollowHeadNode','FKExtraHeadBase_M')
    mc.select('FollowHeadNode')
    mc.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    mc.parent('FKHead_M', 'FollowHeadNode')
    mc.aimConstraint('HeadAim_Loc', 'FollowHeadNode', mo=True)

    #create attribute on main controller to toggle the visibility of HeadAim_Grp

    mc.addAttr('Main', longName='HeadAim_Vis', min=0, max=1, defaultValue=1.0, k=True)
    mc.setAttr('Main.HeadAim_Vis',e=True, keyable=True, l=False)

    #set driven key from Main to turn vis off of Group
    mc.setDrivenKeyframe ('HeadAim_Grp.v', currentDriver = 'Main.HeadAim_Vis')
    mc.setAttr ('Main.HeadAim_Vis', 1)
    mc.setAttr ('HeadAim_Grp.v', 1)
    mc.setDrivenKeyframe ('HeadAim_Grp.v', currentDriver = 'Main.HeadAim_Vis')
    mc.setAttr ('Main.HeadAim_Vis', 0)
    mc.setAttr ('HeadAim_Grp.v', 0)
    mc.setDrivenKeyframe ('HeadAim_Grp.v', currentDriver = 'Main.HeadAim_Vis')

    #set driven key from HeadAim_Grp to turn the aimConstraint off when visibility is off
    mc.setDrivenKeyframe ('FollowHeadNode_aimConstraint1.HeadAim_LocW0', currentDriver = 'HeadAim_Grp.v')
    mc.setAttr ('HeadAim_Grp.v', 1)
    mc.setAttr ('FollowHeadNode_aimConstraint1.HeadAim_LocW0', 1)
    mc.setDrivenKeyframe ('FollowHeadNode_aimConstraint1.HeadAim_LocW0', currentDriver = 'HeadAim_Grp.v')
    mc.setAttr ('HeadAim_Grp.v', 0)
    mc.setAttr ('FollowHeadNode_aimConstraint1.HeadAim_LocW0', 0)
    mc.setDrivenKeyframe ('FollowHeadNode_aimConstraint1.HeadAim_LocW0', currentDriver = 'HeadAim_Grp.v')

    #connect HeadAim_Grp to follow neck
    mc.parent('HeadAim_Grp','Main')
    mc.parentConstraint('FKNeck_M','HeadAim_Grp', mo=True)

    mc.select(d=True)

######################################################################################################################################
########################                                                            ##################################################
########################                            Delete animLayer                ##################################################
########################                                                            ##################################################
######################################################################################################################################

def deleteAnimLy(*args):

    mc.select('BaseAnimation')
    mel.eval("delete")

######################################################################################################################################
########################                                                            ##################################################
########################                            Window                          ##################################################
########################                                                            ##################################################
######################################################################################################################################
mc.window(t= 'AGS - Tools', iconName= 'FacialRigTool', w= 300)
mc.columnLayout(adj= True)
mc.text(l='Need import - armsLegs_ch -')
mc.text(l='Match arms, legs, neck with current bone position')
mc.button(l= '01 - BodyRig', command= BodyCustomButton)
mc.separator()
mc.text(l='Need - jaw / head bone -')
mc.button(l= '02 - FaceTemplete', command= templeteFacialButton)
mc.button(l= '03 - FaceFacialRig', command= facialRigButton)
mc.separator()
mc.text(l='Aim Head')
mc.button(l='AimHead_Ctrl', command=aimHead)
mc.separator()
mc.text(l='Delete animLayer')
mc.button(l='Delete animLayer', command=deleteAnimLy)

mc.showWindow()




