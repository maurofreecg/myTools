###############################################################################
### Design's tooo by Eduardo Vazquez
### Modify by MuaroFreerCG
##############################################################################

import maya.cmds as mc

base_jnt_list = ['pelvis', 'thigh_r', 'calf_r', 'foot_r', 'ball_r', 'clavicle_r', 'upperarm_r', 'lowerarm_r', 'hand_r',
                 'thigh_l', 'calf_l', 'foot_l', 'ball_l', 'clavicle_l', 'upperarm_l', 'lowerarm_l', 'hand_l',
                 'spine_01', 'spine_02', 'spine_03', 'neck_01', 'head']

for item in (base_jnt_list):
    mc.currentTime(-1)
    mc.setAttr(item + '.rx', 0)
    mc.setAttr(item + '.ry', 0)
    mc.setAttr(item + '.rz', 0)

HIK_rename_list = ['Hips', 'RightUpLeg', 'RightLeg', 'RightFoot', 'RightToeBase', 'RightShoulder', 'RightArm', 'RightForeArm',
                   'RightHand', 'LeftUpLeg', 'LeftLeg', 'LeftFoot', 'LeftToeBase', 'LeftShoulder', 'LeftArm', 'LeftForeArm',
                   'LeftHand', 'Spine', 'Spine1', 'Spine2', 'Neck', 'Head']

rename_list = []

for rename in range(len(base_jnt_list)):
    mc.rename(rename, HIK_rename_list)