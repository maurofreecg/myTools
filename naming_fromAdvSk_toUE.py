import maya.cmds as mc

mc.rename('Root_M', 'pelvis')

# legs

mc.rename('Hip_R', 'thigh_r')
mc.rename('HipPart1_R', 'thigh_twist_01_r')
mc.rename('HipPart2_R', 'thigh_twist_02_r')
mc.rename('Knee_R', 'calf_r')
mc.rename('KneePart1_R', 'calf_twist_02_r')
mc.rename('KneePart2_R', 'calf_twist_01_r')
mc.rename('Ankle_R', 'foot_r')
mc.rename('Toes_R', 'ball_r')

mc.rename('Hip_L', 'thigh_l')
mc.rename('HipPart1_L', 'thigh_twist_01_l')
mc.rename('HipPart2_L', 'thigh_twist_02_l')
mc.rename('Knee_L', 'calf_l')
mc.rename('KneePart1_L', 'calf_twist_02_l')
mc.rename('KneePart2_L', 'calf_twist_01_l')
mc.rename('Ankle_L', 'foot_l')
mc.rename('Toes_L', 'ball_l')

# MiddleJoints

mc.rename('Spine1_M', 'spine_01')
mc.rename('Spine2_M', 'spine_02')
mc.rename('Chest_M', 'spine_03')
mc.rename('Neck_M', 'neck_01')
mc.rename('Head_M', 'head')
#mc.rename('Jaw_M', 'jaw')
#mc.rename('Eye_L', 'eye_l')
#mc.rename('Eye_R', 'eye_r')

# arms

mc.rename('Scapula_R', 'clavicle_r')
mc.rename('Shoulder_R', 'upperarm_r')
mc.rename('ShoulderPart1_R', 'upperarm_twist_01_r')
mc.rename('ShoulderPart2_R', 'upperarm_twist_02_r')
mc.rename('Elbow_R', 'lowerarm_r')
mc.rename('ElbowPart1_R', 'lowerarm_twist_02_r')
mc.rename('ElbowPart2_R', 'lowerarm_twist_01_r')
mc.rename('Wrist_R', 'hand_r')
mc.rename('ThumbFinger1_R', 'thumb_01_r')
mc.rename('ThumbFinger2_R', 'thumb_02_r')
mc.rename('ThumbFinger3_R', 'thumb_03_r')
#mc.rename('IndexFinger_00_R', 'index_00_r')
mc.rename('IndexFinger1_R', 'index_01_r')
mc.rename('IndexFinger2_R', 'index_02_r')
mc.rename('IndexFinger3_R', 'index_03_r')
#mc.rename('MiddleFinger_00_R', 'middle_00_r')
mc.rename('MiddleFinger1_R', 'middle_01_r')
mc.rename('MiddleFinger2_R', 'middle_02_r')
mc.rename('MiddleFinger3_R', 'middle_03_r')
#mc.rename('RingFinger_00_R', 'ring_00_r')
mc.rename('RingFinger1_R', 'ring_01_r')
mc.rename('RingFinger2_R', 'ring_02_r')
mc.rename('RingFinger3_R', 'ring_03_r')
#mc.rename('PinkyFinger_00_R', 'pinky_00_r')
mc.rename('PinkyFinger1_R', 'pinky_01_r')
mc.rename('PinkyFinger2_R', 'pinky_02_r')
mc.rename('PinkyFinger3_R', 'pinky_03_r')

mc.rename('Scapula_L', 'clavicle_l')
mc.rename('Shoulder_L', 'upperarm_l')
mc.rename('ShoulderPart1_L', 'upperarm_twist_01_l')
mc.rename('ShoulderPart2_L', 'upperarm_twist_02_l')
mc.rename('Elbow_L', 'lowerarm_l')
mc.rename('ElbowPart1_L', 'lowerarm_twist_02_l')
mc.rename('ElbowPart2_L', 'lowerarm_twist_01_l')
mc.rename('Wrist_L', 'hand_l')
mc.rename('ThumbFinger1_L', 'thumb_01_l')
mc.rename('ThumbFinger2_L', 'thumb_02_l')
mc.rename('ThumbFinger3_L', 'thumb_03_l')
#mc.rename('IndexFinger_00_L', 'index_00_l')
mc.rename('IndexFinger1_L', 'index_01_l')
mc.rename('IndexFinger2_L', 'index_02_l')
mc.rename('IndexFinger3_L', 'index_03_l')
#mc.rename('MiddleFinger_00_L', 'middle_00_l')
mc.rename('MiddleFinger1_L', 'middle_01_l')
mc.rename('MiddleFinger2_L', 'middle_02_l')
mc.rename('MiddleFinger3_L', 'middle_03_l')
#mc.rename('RingFinger_00_L', 'ring_00_l')
mc.rename('RingFinger1_L', 'ring_01_l')
mc.rename('RingFinger2_L', 'ring_02_l')
mc.rename('RingFinger3_L', 'ring_03_l')
#mc.rename('PinkyFinger_00_L', 'pinky_00_l')
mc.rename('PinkyFinger1_L', 'pinky_01_l')
mc.rename('PinkyFinger2_L', 'pinky_02_l')
mc.rename('PinkyFinger3_L', 'pinky_03_l')

# clean setup

mc.select('MiddleFinger4_R')
mc.delete('MiddleFinger4_R')

mc.select('ThumbFinger4_R')
mc.delete('ThumbFinger4_R')

mc.select('IndexFinger4_R')
mc.delete('IndexFinger4_R')

mc.select('RingFinger4_R')
mc.delete('RingFinger4_R')

mc.select('PinkyFinger4_R')
mc.delete('PinkyFinger4_R')

mc.select('MiddleFinger4_L')
mc.delete('MiddleFinger4_L')

mc.select('ThumbFinger4_L')
mc.delete('ThumbFinger4_L')

mc.select('IndexFinger4_L')
mc.delete('IndexFinger4_L')

mc.select('RingFinger4_L')
mc.delete('RingFinger4_L')

mc.select('PinkyFinger4_L')
mc.delete('PinkyFinger4_L')

mc.select('ToesEnd_R')
mc.delete('ToesEnd_R')

mc.select('ToesEnd_L')
mc.delete('ToesEnd_L')

mc.select('HeadEnd_M')
mc.delete('HeadEnd_M')