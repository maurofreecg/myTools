import maya.cmds as mc
import maya.mel as mel

# AGS_Body_Tool
# By MauroFreeCG - Rigger

##############################################################################################################################################
#####################################                                          ###############################################################
#####################################            Create bodyRig                ###############################################################
##############################################################################################################################################
# connect deformation bones (AS) to bind bones - arms legs (AGS)                                                                             #
# need import 'armsLegs_ch' // match arms, legs with current bone position                                                                   #
##############################################################################################################################################

#def BodyCustomButton(*args):
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

BaseJNT_List = ['Hip_R', 'Hip_L', 'Scapula_R', 'Scapula_l_L', 'Neck_M']
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
mc.mirrorJoint('LeftButtock', mirrorYZ=True, mirrorBehavior=True, searchReplace=('Left', 'Right')), mc.select(cl=True)
mc.mirrorJoint('LeftUpLeg', mirrorYZ=True, mirrorBehavior=True, searchReplace=('Left', 'Right')), mc.select(cl=True)
mc.mirrorJoint('LeftSpine2AttachRear', mirrorYZ=True, mirrorBehavior=False,searchReplace=('Left', 'Right')), mc.select(cl=True)
mc.mirrorJoint('LeftBreast', mirrorYZ=True, mirrorBehavior=False, searchReplace=('Left', 'Right')), mc.select( cl=True)
mc.mirrorJoint('LeftScapulaUpVolume', mirrorYZ=True, mirrorBehavior=False,searchReplace=('Left', 'Right')), mc.select(cl=True)
mc.mirrorJoint(ikLeg, mirrorYZ=True, mirrorBehavior=True, searchReplace=('Left', 'Right')), mc.select(cl=True)
mc.mirrorJoint(ikArm, mirrorYZ=True, mirrorBehavior=True, searchReplace=('Left', 'Right')), mc.select(cl=True)

# parent bones

mc.parent('RightUpLeg', 'LeftUpLeg', 'Hips')
mc.parent('Neck', 'LeftShoulder', 'RightShoulder', 'Spine2')
mc.parent('Hips', 'HipsTranslation')
mc.parent('LeftSpine2AttachRear', 'LeftBreast', 'RightSpine2AttachRear', 'RightBreast', 'Spine2'), mc.select(d=True)
mc.parent('LeftHipsAttachSide', 'LeftHipsAttachRear', 'LeftHipsAttachFront', 'RightHipsAttachSide',
          'RightHipsAttachFront', 'RightHipsAttachRear', 'Hips'), mc.select(d=True)

RootMotion = mc.curve(d=1, p=[(0, 0, 108), (36, 0, 36), (12, 0, 36), (12, 0, 12), (36, 0, 12), (36, 0, 24), (60, 0, 0),(36, 0, -24), (36, 0, -12), (12, 0, -12)
                          , (12, 0, -36), (24, 0, -36), (0, 0, -60), (-24, 0, -36), (-12, 0, -36), (-12, 0, -12),
                         (-36, 0, -12), (-36, 0, -24), (-60, 0, 0), (-36, 0, 24),
                         (-36, 0, 12), (-12, 0, 12), (-12, 0, 36), (-36, 0, 36), (0, 0, 108)], n='HipsDirection')

AS_BonesArmLegNeckList = ['Scapula_R', 'Shoulder1_R', 'Elbow_R', 'Wrist_R', 'MiddleFinger1_R', 'MiddleFinger2_R',
                          'MiddleFinger3_R', 'ThumbFinger1_R', 'ThumbFinger2_R', 'ThumbFinger3_R', 'IndexFinger1_R',
                          'IndexFinger2_R', 'IndexFinger3_R',
                          'Cup_R', 'PinkyFinger1_R', 'PinkyFinger2_R', 'PinkyFinger3_R', 'RingFinger1_R',
                          'RingFinger2_R', 'RingFinger3_R', 'Scapula_l_L', 'Shoulder_l_L', 'Elbow_l_L', 'Wrist_l_L',
                          'MiddleFinger1_l_L', 'MiddleFinger2_l_L', 'MiddleFinger3_l_L',
                          'ThumbFinge1_l_L', 'ThumbFinger2_l_L', 'ThumbFinger3_l_L', 'IndexFinger1_l_L', 'IndexFinger2_l_L',
                          'IndexFinger3_l_L', 'Cup_l_L', 'PinkyFinger1_l_L', 'PinkyFinger2_l_L', 'PinkyFinger3_l_L',
                          'RingFinger1_l_L', 'RingFinger2_l_L', 'RingFinger3_l_L',
                          'Hip_L', 'Knee_L', 'Ankle_L', 'Toes_L', 'ToesEnd_L', 'Hip_R', 'Knee_R', 'Ankle_R',
                          'Toes_R', 'ToesEnd_R', 'Neck_M', 'Head_M']

AGS_BonesArmLegNeckList = ['RightShoulder', 'RightArm', 'RightForeArm', 'RightHand', 'RightHandMiddle1',
                           'RightHandMiddle2', 'RightHandMiddle3', 'RightHandThumb1', 'RightHandThumb2',
                           'RightHandThumb3', 'RightHandIndex1', 'RightHandIndex2',
                           'RightHandIndex3', 'RightHandMetacarpal', 'RightHandPinky1', 'RightHandPinky2',
                           'RightHandPinky3', 'RightHandRing1', 'RightHandRing2', 'RightHandRing3', 'LeftShoulder',
                           'LeftArm', 'LeftForeArm', 'LeftHand', 'LeftHandMiddle1', 'LeftHandMiddle2',
                           'LeftHandMiddle3', 'LeftHandThumb1', 'LeftHandThumb2', 'LeftHandThumb3',
                           'LeftHandIndex1', 'LeftHandIndex2', 'LeftHandIndex3', 'LeftHandMetacarpal',
                           'LeftHandPinky1', 'LeftHandPinky2', 'LeftHandPinky3', 'LeftHandRing1', 'LeftHandRing2',
                           'LeftHandRing3',
                           'LeftUpLeg', 'LeftLeg', 'LeftFoot', 'LeftToeBase', 'LeftToeBaseEnd', 'RightUpLeg',
                           'RightLeg', 'RightFoot', 'RightToeBase', 'RightToeBaseEnd', 'Neck', 'Head']

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

mc.parent('LeftFoot_IK', 'LeftHand_IK', 'Head_IK', 'Camera', 'Attach', 'RightFoot_IK', 'RightHand_IK',
          'HipsTranslation')
mc.pointConstraint(RootMotion, 'HipsTranslation', mo=True)
mc.parent(RootMotion, 'Main')

# clean up
mc.delete('HeadEnd_M', 'ThumbFinger4_l_L', 'IndexFinger4_l_L', 'MiddleFinger4_l_L', 'RingFinger4_l_L', 'PinkyFinger4_l_L',
          'ThumbFinger4_R', 'IndexFinger4_R',
          'MiddleFinger4_R', 'RingFinger4_R', 'PinkyFinger4_R')
###########################################################################################################
########################################### extras controls  ##############################################
###########################################################################################################
###################### Left Side

LeftExtrasBn_List = ['LeftWristHelper', 'LeftForeArmRoll', 'LeftLowerarm', 'LeftShoulderarmHelper_02',
                     'LeftArmRoll', 'LeftShoulderarmHelper_01', 'LeftUpperarm',
                     'LeftUpperlegHelper', 'LeftUpperlegHelperUp', 'LeftUpLegRoll', 'LeftUpperlegHelperDn',
                     'LeftLowerleg', 'LeftLegRoll', 'LeftAnkleHelper']

def controlColor(s, c):  # yellow 17, red 13, blue 6, light blue 18, light red 4, light green 23
    mc.setAttr(s + '.overrideEnabled', 1)
    mc.setAttr(s + '.overrideColor', c)

for LeftExtrasBn in (LeftExtrasBn_List):
    crv = mc.circle(n=LeftExtrasBn + '_ctrl', radius=4, ch=False, nr=(1, 0, 0))
    spaceCrv = mc.group(crv, n=LeftExtrasBn + '_ctrlSpace')
    masterSpace = mc.group(spaceCrv, n=LeftExtrasBn + '_ctrlMasterSpace')
    mc.delete(mc.parentConstraint(LeftExtrasBn, masterSpace, mo=False))

for mC in (LeftExtrasBn_List):
    mirrorCtrl = mc.curve(d=1, p=[(-0.0133947, 0, 0.351564), (-0.0130162, 0, 0.916036), (-0.126636, 0, 0.85811),
                                  (0, 0, 1.111383), (0.126636, 0, 0.85811), (0.0121104, 0, 0.916036),
                                  (0.0121104, 0, 0.351564), (0.0935195, 0, 0.281599), (0.0935195, 0, 0.195095),
                                  (-0.0935195, 0, 0.195095), (-0.0935195, 0, 0.281599), (-0.0133947, 0, 0.351564)],
                          n=mC + '_mCtrl')
    mc.scale(6, 6, 6, mirrorCtrl)
    mc.makeIdentity(mirrorCtrl, apply=True, scale=True)
    mirrorCtrlSpace = mc.group(em=True, n=mC + '_mCtrlSpace')
    mirrorCtrlMasterSpace = mc.group(em=True, n=mC + '_mCtrlMasterSpace')
    mc.parent(mirrorCtrl, mirrorCtrlSpace), mc.parent(mirrorCtrlSpace, mirrorCtrlMasterSpace)
    mc.delete(mc.parentConstraint(mC, mirrorCtrlMasterSpace, mo=False))

LeftMirrorCtrl_List = ['LeftWristHelper_mCtrl', 'LeftForeArmRoll_mCtrl', 'LeftLowerarm_mCtrl',
                       'LeftShoulderarmHelper_02_mCtrl', 'LeftArmRoll_mCtrl', 'LeftShoulderarmHelper_01_mCtrl',
                       'LeftUpperarm_mCtrl', 'LeftUpperlegHelper_mCtrl', 'LeftUpperlegHelperUp_mCtrl',
                       'LeftUpLegRoll_mCtrl', 'LeftUpperlegHelperDn_mCtrl', 'LeftLowerleg_mCtrl',
                       'LeftLegRoll_mCtrl', 'LeftAnkleHelper_mCtrl']

LeftMirrorCtrl_Space_List = ['LeftWristHelper_mCtrlSpace', 'LeftForeArmRoll_mCtrlSpace', 'LeftLowerarm_mCtrlSpace',
                             'LeftShoulderarmHelper_02_mCtrlSpace', 'LeftArmRoll_mCtrlSpace',
                             'LeftShoulderarmHelper_01_mCtrlSpace',
                             'LeftUpperarm_mCtrlSpace', 'LeftUpperlegHelper_mCtrlSpace',
                             'LeftUpperlegHelperUp_mCtrlSpace', 'LeftUpLegRoll_mCtrlSpace',
                             'LeftUpperlegHelperDn_mCtrlSpace', 'LeftLowerleg_mCtrlSpace', 'LeftLegRoll_mCtrlSpace',
                             'LeftAnkleHelper_mCtrlSpace']

LeftMirrorCtrl_masterSpace_List = ['LeftWristHelper_mCtrlMasterSpace', 'LeftForeArmRoll_mCtrlMasterSpace',
                                   'LeftLowerarm_mCtrlMasterSpace', 'LeftShoulderarmHelper_02_mCtrlMasterSpace',
                                   'LeftArmRoll_mCtrlMasterSpace', 'LeftShoulderarmHelper_01_mCtrlMasterSpace',
                                   'LeftUpperarm_mCtrlMasterSpace', 'LeftUpperlegHelper_mCtrlMasterSpace',
                                   'LeftUpperlegHelperUp_mCtrlMasterSpace', 'LeftUpLegRoll_mCtrlMasterSpace',
                                   'LeftUpperlegHelperDn_mCtrlMasterSpace', 'LeftLowerleg_mCtrlMasterSpace',
                                   'LeftLegRoll_mCtrlMasterSpace', 'LeftAnkleHelper_mCtrlMasterSpace']

LeftCtrl_List = ['LeftWristHelper_ctrl', 'LeftForeArmRoll_ctrl', 'LeftLowerarm_ctrl',
                 'LeftShoulderarmHelper_02_ctrl', 'LeftArmRoll_ctrl', 'LeftShoulderarmHelper_01_ctrl',
                 'LeftUpperarm_ctrl', 'LeftUpperlegHelper_ctrl',
                 'LeftUpperlegHelperUp_ctrl', 'LeftUpLegRoll_ctrl', 'LeftUpperlegHelperDn_ctrl',
                 'LeftLowerleg_ctrl', 'LeftLegRoll_ctrl', 'LeftAnkleHelper_ctrl']

LeftCtrl_Space_List = ['LeftWristHelper_ctrlSpace', 'LeftForeArmRoll_ctrlSpace', 'LeftLowerarm_ctrlSpace',
                       'LeftShoulderarmHelper_02_ctrlSpace', 'LeftArmRoll_ctrlSpace',
                       'LeftShoulderarmHelper_01_ctrlSpace',
                       'LeftUpperarm_ctrlSpace', 'LeftUpperlegHelper_ctrlSpace', 'LeftUpperlegHelperUp_ctrlSpace',
                       'LeftUpLegRoll_ctrlSpace', 'LeftUpperlegHelperDn_ctrlSpace', 'LeftLowerleg_ctrlSpace',
                       'LeftLegRoll_ctrlSpace', 'LeftAnkleHelper_ctrlSpace']

LeftCtrl_masterSpace_List = ['LeftWristHelper_ctrlMasterSpace', 'LeftForeArmRoll_ctrlMasterSpace',
                             'LeftLowerarm_ctrlMasterSpace', 'LeftShoulderarmHelper_02_ctrlMasterSpace',
                             'LeftArmRoll_ctrlMasterSpace', 'LeftShoulderarmHelper_01_ctrlMasterSpace',
                             'LeftUpperarm_ctrlMasterSpace', 'LeftUpperlegHelper_ctrlMasterSpace',
                             'LeftUpperlegHelperUp_ctrlMasterSpace', 'LeftUpLegRoll_ctrlMasterSpace',
                             'LeftUpperlegHelperDn_ctrlMasterSpace', 'LeftLowerleg_ctrlMasterSpace',
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

RightExtrasBn_List = ['RightWristHelper', 'RightForeArmRoll', 'RightLowerarm', 'RightShoulderarmHelper_02',
                      'RightArmRoll', 'RightShoulderarmHelper_01', 'RightUpperarm',
                      'RightUpperlegHelper', 'RightUpperlegHelperUp', 'RightUpLegRoll', 'RightUpperlegHelperDn',
                      'RightLowerleg', 'RightLegRoll', 'RightAnkleHelper']

for RightExtrasBn in (RightExtrasBn_List):
    crv = mc.circle(n=RightExtrasBn + '_ctrl', radius=4, ch=False, nr=(1, 0, 0))
    spaceCrv = mc.group(crv, n=RightExtrasBn + '_ctrlSpace')
    constCrv = mc.group(spaceCrv, n=RightExtrasBn + '_const')
    masterConst = mc.group(constCrv, n=RightExtrasBn + '_MasterConst')
    mc.delete(mc.parentConstraint(RightExtrasBn, masterConst, mo=False))

RightMasterConst_List = ['RightWristHelper_MasterConst', 'RightForeArmRoll_MasterConst',
                         'RightLowerarm_MasterConst', 'RightShoulderarmHelper_02_MasterConst',
                         'RightArmRoll_MasterConst', 'RightShoulderarmHelper_01_MasterConst',
                         'RightUpperarm_MasterConst', 'RightUpperlegHelper_MasterConst',
                         'RightUpperlegHelperUp_MasterConst', 'RightUpLegRoll_MasterConst',
                         'RightUpperlegHelperDn_MasterConst', 'RightLowerleg_MasterConst',
                         'RightLegRoll_MasterConst', 'RightAnkleHelper_MasterConst']

RightConst_List = ['RightWristHelper_const', 'RightForeArmRoll_const', 'RightLowerarm_const',
                   'RightShoulderarmHelper_02_const', 'RightArmRoll_const', 'RightShoulderarmHelper_01_const',
                   'RightUpperarm_const', 'RightUpperlegHelper_const', 'RightUpperlegHelperUp_const',
                   'RightUpLegRoll_const',
                   'RightUpperlegHelperDn_const', 'RightLowerleg_const', 'RightLegRoll_const',
                   'RightAnkleHelper_const']

RightCtrl_Space = ['RightWristHelper_ctrlSpace', 'RightForeArmRoll_ctrlSpace', 'RightLowerarm_ctrlSpace',
                   'RightShoulderarmHelper_02_ctrlSpace', 'RightArmRoll_ctrlSpace',
                   'RightShoulderarmHelper_01_ctrlSpace', 'RightUpperarm_ctrlSpace',
                   'RightUpperlegHelper_ctrlSpace', 'RightUpperlegHelperUp_ctrlSpace',
                   'RightUpperlegHelperDn_ctrlSpace', 'RightLowerleg_ctrlSpace', 'RightLegRoll_ctrlSpace',
                   'RightAnkleHelper_ctrlSpace']

RightCtrl_List = ['RightWristHelper_ctrl', 'RightForeArmRoll_ctrl', 'RightLowerarm_ctrl',
                  'RightShoulderarmHelper_02_ctrl', 'RightArmRoll_ctrl', 'RightShoulderarmHelper_01_ctrl',
                  'RightUpperarm_ctrl', 'RightUpperlegHelper_ctrl', 'RightUpperlegHelperUp_ctrl',
                  'RightUpLegRoll_ctrl',
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

Left_UpperArm_List = ['LeftShoulderarmHelper_02_mCtrlMasterSpace', 'LeftArmRoll_mCtrlMasterSpace',
                      'LeftShoulderarmHelper_01_mCtrlMasterSpace', 'LeftUpperarm_mCtrlMasterSpace']
Left_lowerArm_list = ['LeftWristHelper_mCtrlMasterSpace', 'LeftForeArmRoll_mCtrlMasterSpace',
                      'LeftLowerarm_mCtrlMasterSpace']
Left_UpperLeg_list = ['LeftUpperlegHelperDn_mCtrlMasterSpace', 'LeftUpLegRoll_mCtrlMasterSpace',
                      'LeftUpperlegHelperUp_mCtrlMasterSpace', 'LeftUpperlegHelper_mCtrlMasterSpace']
Left_lowerLeg_list = ['LeftAnkleHelper_mCtrlMasterSpace', 'LeftLegRoll_mCtrlMasterSpace',
                      'LeftLowerleg_mCtrlMasterSpace']
Right_UpperArm_List = ['RightShoulderarmHelper_02_MasterConst', 'RightArmRoll_MasterConst',
                       'RightShoulderarmHelper_01_MasterConst', 'RightUpperarm_MasterConst']
Right_LowerArm_List = ['RightWristHelper_MasterConst', 'RightForeArmRoll_MasterConst', 'RightLowerarm_MasterConst']
Right_UpperLeg_list = ['RightUpperlegHelperDn_MasterConst', 'RightUpLegRoll_MasterConst',
                       'RightUpperlegHelperUp_MasterConst', 'RightUpperlegHelper_MasterConst']
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

    mc.connectAttr('Shoulder_lPart1_L.rx', rotMD + '.input1X')
    mc.connectAttr(rotMD + '.outputX', LeftCtrl_UpperArm_List[lUpperArm] + '.rotateX')
mc.setAttr("LeftShoulderarmHelper_02_mCtrlSpace_MD.input2X", -1.5)

LeftCtrl_LowerArm_List = ['LeftForeArmRoll_mCtrlSpace', 'LeftWristHelper_mCtrlSpace']

for lLowerArm, item in enumerate(LeftCtrl_LowerArm_List):
    rotMD = mc.createNode('multiplyDivide', n=item + '_MD')
    mc.setAttr(rotMD + '.input2X', -1)

    mc.connectAttr('Elbow_lPart1_L.rx', rotMD + '.input1X')
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

########### hand gimbal controls

LeftGimbalCtrl_crv = mc.curve(d=True, p=(
(-0.5, 0.5, 0.00702787), (0.5, 0.5, 0.00702787), (0.5, -0.5, 0.00702787), (-0.5, -0.5, 0.00702787),
(-0.5, 0.5, 0.00702787)), n='IKLocalArm_L')
LeftGimbalCtrl_space = mc.group(em=True, n='IKLocalArm_L_ctrlSpace')
mc.parent(LeftGimbalCtrl_crv, LeftGimbalCtrl_space), mc.select(d=True)

RightGimbalCtrl_crv = mc.curve(d=True, p=(
(-0.5, 0.5, 0.00702787), (0.5, 0.5, 0.00702787), (0.5, -0.5, 0.00702787), (-0.5, -0.5, 0.00702787),
(-0.5, 0.5, 0.00702787)), n='IKLocalArm_R')
RightGimbalCtrl_space = mc.group(em=True, n='IKLocalArm_R_ctrlSpace')
mc.parent(RightGimbalCtrl_crv, RightGimbalCtrl_space), mc.select(d=True)

mc.delete(mc.parentConstraint('IKArm1_L', LeftGimbalCtrl_space, mo=False))
mc.delete(mc.parentConstraint('IKArm3_R', RightGimbalCtrl_space, mo=False))

gimbalCtrl_cv_list = ['IKLocalArm_L.cv[0:4]', 'IKLocalArm_R.cv[0:4]']
mc.select(gimbalCtrl_cv_list)
mc.rotate(0, 90, 0, fo=True)
mc.select(d=True)

mc.parent(LeftGimbalCtrl_space, 'IKFKAlignedArm1_L'), mc.parent(RightGimbalCtrl_space, 'IKFKAlignedArm3_R')
# mc.delete('IKXWrist_L_orientConstraint1', 'IKXWrist_R_orientConstraint1')
mc.orientConstraint(LeftGimbalCtrl_crv, 'IKXWrist_l_L', mo=True), mc.orientConstraint(RightGimbalCtrl_crv, 'IKXWrist_R', mo=True)

gimbalCtrl_list = [LeftGimbalCtrl_crv, RightGimbalCtrl_crv]

for i in gimbalCtrl_list:
    mc.setAttr(i + '.tx', l=True, k=False, ch=False)
    mc.setAttr(i + '.ty', l=True, k=False, ch=False)
    mc.setAttr(i + '.tz', l=True, k=False, ch=False)
    mc.setAttr(i + '.sx', l=True, k=False, ch=False)
    mc.setAttr(i + '.sy', l=True, k=False, ch=False)
    mc.setAttr(i + '.sz', l=True, k=False, ch=False)
    mc.setAttr(i + '.v', l=True, k=False, ch=False)

controlColor(LeftGimbalCtrl_crv, 6)
controlColor(RightGimbalCtrl_crv, 13)

mc.select(d=True)

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

################################################ scale cv's

mc.select('PoleLeg_L.cv[0:7]', 'PoleLeg_R.cv[0:7]', 'PoleArm_R.cv[0:7]', 'PoleArm_L.cv[0:7]'), mc.scale(9, 9, 9,
                                                                                                        ocp=True)
mc.select('IKLeg_RShape.cv[0:15]', 'IKLeg_LShape.cv[0:15]'), mc.scale(9.5, 1, 1, ocp=True)
mc.select('IKLeg_RShape.cv[3:6]', 'IKLeg_RShape.cv[9:12]', 'IKLeg_LShape.cv[0:2]', 'IKLeg_LShape.cv[7:8]',
          'IKLeg_LShape.cv[13:15]'), mc.move(0, 0, -7, r=True, os=True, wd=True)
mc.select('IKLeg_RShape.cv[2]', 'IKLeg_RShape.cv[7]', 'IKLeg_RShape.cv[14:15]', 'IKLeg_LShape.cv[4:5]',
          'IKLeg_LShape.cv[9]', 'IKLeg_LShape.cv[12]'), mc.move(0, 0, 9.5, r=True, os=True, wd=True)
mc.select('IKToes_LShape.cv[0:7]', 'RollToes_LShape.cv[0:15]', 'RollToesEnd_LShape.cv[0:15]',
          'RollToesEnd_RShape.cv[0:15]', 'RollToes_RShape.cv[0:15]', 'RollHeel_RShape.cv[0:15]',
          'IKToes_RShape.cv[0:7]',
          'RollHeel_LShape.cv[0:15]'), mc.scale(9.3, 9.3, 9.3, ocp=True), mc.select('RollHeel_LShape.cv[0:15]',
                                                                                    'RollHeel_RShape.cv[0:15]'), mc.move(
    0, 3.5, -3, r=True, os=True, wd=True)
mc.select('RollToes_RShape.cv[0:15]', 'RollToes_LShape.cv[0:15]', 'IKToes_LShape.cv[0:7]',
          'IKToes_RShape.cv[0:7]'), mc.scale(1.5, 1.5, 1.5, ocp=True), mc.move(0, 2.6, 1.2, r=True, os=True,
                                                                               wd=True)
mc.select('FKIKLeg_L.cv[0:11]'), mc.scale(2.3, 2.3, 2.3, ocp=True), mc.move(17, 0, 0, r=True, os=True,
                                                                            wd=True), mc.select(
    'FKIKLeg_R.cv[0:11]'), mc.scale(2.3, 2.3, 2.3, ocp=True), mc.move(-17, 0, 0, r=True, os=True, wd=True)
mc.select('IKArm_LShape.cv[0:15]', 'IKArm_RShape.cv[0:15]', 'IKLocalArm_R.cv[0:4]',
          'IKLocalArm_L.cv[0:4]'), mc.scale(8, 8, 8, ocp=True), mc.scale(0.3, 1, 1, ocp=True)
mc.select('FKKnee_LShape.cv[0:7]', 'FKKnee_RShape.cv[0:7]'), mc.scale(11.5, 11.5, 11.5, ocp=True)
mc.select('FKAnkle_LShape.cv[0:7]', 'FKAnkle_RShape.cv[0:7]'), mc.scale(12.5, 12.5, 12.5, ocp=True)
mc.select('FKToes_LShape.cv[0:7]', 'FKToes_RShape.cv[0:7]'), mc.scale(13, 13, 13, ocp=True), mc.move(0, 3, 0,
                                                                                                     r=True)
mc.select('FKHip_LShape.cv[0:7]', 'FKHip_RShape.cv[0:7]'), mc.scale(10.3, 10.3, 10.3, ocp=True), mc.rotate(0, -28,
                                                                                                           0,
                                                                                                           ocp=True), mc.move(
    0, -2.8, 0, r=True)
mc.select('FKIKSpine_M.cv[0:11]'), mc.scale(2, 2, 2, ocp=True), mc.move(20, 0, 0, r=True, os=True, wd=True)
mc.select('FKSpine1_MShape.cv[0:7]', 'FKRoot_MShape.cv[0:7]', 'FKChest_MShape.cv[0:7]',
          'FKSpine2_MShape.cv[0:7]'), mc.scale(12, 12, 12, ocp=True)
mc.select('HipSwinger_M.cv[0:7]'), mc.rotate(0, 0, 90, ocp=True), mc.move(2.5, 0, 0, r=True), mel.eval(
    "CenterPivot"), mc.scale(30, 30, 30, ocp=True)
mc.select('RootX_MShape.cv[0:6]', 'RootX_MShape3.cv[0:6]', 'RootX_MShape1.cv[0:6]',
          'RootX_MShape2.cv[0:6]'), mc.scale(13, 13, 13, ocp=True)
mc.select('IKSpine2_MShape.cv[0:7]', 'IKSpine1_MShape.cv[0:15]', 'IKSpine3_MShape.cv[0:15]',
          'IKhybridSpine3_MShape.cv[0:15]', 'IKhybridSpine2_MShape.cv[0:15]',
          'IKhybridSpine1_MShape.cv[0:15]'), mc.scale(9, 9, 9, ocp=True)
mc.select('FKIKArm_R.cv[0:11]', 'FKIKArm_L.cv[0:11]'), mc.scale(2, 2, 2, ocp=True), mc.select(
    'FKIKArm_L.cv[0:11]'), mc.move(8.9, 8.2, 0, r=True, os=True, wd=True), mc.select('FKIKArm_R.cv[0:11]'), mc.move(
    -8.9, 8.2, 0, r=True, os=True, wd=True)
mc.select('FKNeck_MShape.cv[0:7]'), mc.scale(21.6, 21.6, 21.6, ocp=True), mc.select('FKNeck_MShape.cv[1]',
                                                                                    'FKNeck_MShape.cv[5]'), mc.move(
    4.1, 0, 0, r=True, os=True, wd=True)
mc.select('FKHead_MShape.cv[0:7]'), mc.scale(13, 13, 13, r=True, p=(0, 174, -6.1))
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

AS_leftCtrl_list = ['FKScapula_LShape', 'FKAnkle_LShape', 'FKElbow_LShape', 'FKHip_LShape', 'FKIndexFinger1_LShape',
                    'FKIndexFinger2_LShape', 'FKIndexFinger3_LShape', 'FKKnee_LShape', 'FKMiddleFinger1_LShape',
                    'FKMiddleFinger3_LShape', 'FKPinkyFinger1_LShape', 'FKPinkyFinger2_LShape',
                    'FKPinkyFinger3_LShape', 'FKRingFinger1_LShape', 'FKRingFinger2_LShape', 'FKRingFinger3_LShape',
                    'FKShoulder1_LShape',
                    'FKThumbFinger2_LShape', 'FKThumbFinger3_LShape', 'FKToes_LShape', 'FKWrist_LShape',
                    'IKArm_LShape', 'curveShape16', 'PoleArm_LShape', 'IKLeg_LShape', 'RollHeel_LShape',
                    'RollToesEnd_LShape',
                    'RollToes_LShape', 'Fingers_LShape', 'PoleLeg_LShape', 'FKCup_LShape', 'FKMiddleFinger2_LShape',
                    'FKThumbFinger1_LShape', 'IKToes_LShape']
for AS_lCtrls in AS_leftCtrl_list:
    controlColor(AS_lCtrls, 6)

AS_rightCtrl_list = ['FKScapula_RShape', 'FKAnkle_RShape', 'FKElbow_RShape', 'FKHip_RShape',
                     'FKIndexFinger1_RShape', 'FKIndexFinger2_RShape', 'FKIndexFinger3_RShape', 'FKKnee_RShape',
                     'FKMiddleFinger1_RShape',
                     'FKMiddleFinger3_RShape', 'FKPinkyFinger1_RShape', 'FKPinkyFinger2_RShape',
                     'FKPinkyFinger3_RShape', 'FKRingFinger1_RShape', 'FKRingFinger2_RShape',
                     'FKRingFinger3_RShape', 'FKShoulder1_RShape',
                     'FKThumbFinger2_RShape', 'FKThumbFinger3_RShape', 'FKToes_RShape', 'FKWrist_RShape',
                     'IKArm_RShape', 'curveShape16', 'PoleArm_RShape', 'IKLeg_RShape', 'RollHeel_RShape',
                     'RollToesEnd_RShape',
                     'RollToes_RShape', 'Fingers_RShape', 'PoleLeg_RShape', 'FKCup_RShape',
                     'FKMiddleFinger2_RShape', 'FKThumbFinger1_RShape', 'IKToes_RShape']
for AS_rCtrls in AS_rightCtrl_list:
    controlColor(AS_rCtrls, 13)

######################################################################################################################################
########################                                                            ##################################################
########################                            delete animLayer                ##################################################
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

mc.window(t= 'AGS - Tools', iconName= 'BodyRigTool', w= 300)
mc.columnLayout(adj= True)
mc.text(l='Match arms, legs, neck with current bone position')
mc.text(l='After build Advance Skeleton')
mc.separator()
mc.separator()
mc.button(l= '01 - BodyRig', command= BodyCustomButton)
mc.separator()
mc.separator()
mc.text(l='Delete animLayer')
mc.separator()
mc.separator()
mc.button(l='Delete animLayer', command=deleteAnimLy)
mc.separator()
mc.separator()

mc.showWindow()

