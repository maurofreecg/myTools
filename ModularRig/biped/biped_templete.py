# biped templete

import maya.cmds as mc

def itemColor(s, c): # yellow 17, red 13, blue 6, light blue 18
    mc.setAttr(s + '.overrideEnabled', 1)
    mc.setAttr(s + '.overrideColor', c)

### spine
pelvis = mc.joint(p=(0, 97.546, -2.303), rad=2, o=(0,3.538, 90), n='pelvis_templete'), mc.select(d=True)
spine_01 = mc.joint(pelvis, p=(0, 108.888, -2.417), rad=2, o=(0,0.577, 90), n='spine_01_templete'), mc.select(d=True)
spine_02 = mc.joint(spine_01, p=(0, 120.295, -2.532), rad=2, o=(0,-0.577, -90), n='spine_02_templete'), mc.select(d=True)
spine_03 = mc.joint(spine_02, p=(0, 131.688, -2.646), rad=2, o=(0.577, 0, 0), n='spine_03_templete'), mc.select(d=True)

### neck head
neck = mc.joint(p=(0, 155.256, -5.945), rad=2, o=(0, -1.638, 90.000), n='neck_templete'), mc.select(d=True)
head = mc.joint(neck, p=(0, 163.244, -5.717), rad=2, o=(1.638, 0, 0), n='head_templete'), mc.select(d=True)

### arm
clavicle = mc.joint(p=(2.663, 146.853, -1.658), rad=2, o=(0, 15, 0), n='clavicle_templete'), mc.select(d=True)
upperarm = mc.joint(clavicle, p=(16.535, 146.853, -5.454), rad=2, o=(-0.059, -6.599, -56.457), n='upperarm_templete'), mc.select(d=True)
lowerarm = mc.joint(upperarm, p=(32.778, 123.128, -6.494), rad=2, o=(4.422, -14.629, -0.336), n='lowerarm_templete'), mc.select(d=True)
hand = mc.joint(lowerarm, p=(47.184, 103.692, -0.137), rad=2, o=(4.283, -2.541, 0.593), n='hand_templete'), mc.select(d=True)

### fingers
# pinky
pinky_00 = mc.joint(hand, p=(50.260, 98.184, -1.314), rad=1, o=(-5.819, 30.106, -25.631), n='pinky_00_templete'), mc.select(d=True)
pinky_01 = mc.joint(pinky_00, p=(51.084, 94.987, -1.521), rad=1, o=(-0.415, -3.490, -11.557), n='pinky_01_templete'), mc.select(d=True)
pinky_02 = mc.joint(pinky_01, p=(51.200, 92.620, -1.536), rad=1, o=(0, 0, -21.396), n='pinky_02_templete'), mc.select(d=True)
pinky_03 = mc.joint(pinky_02, p=(50.346, 90.078, -1.561), rad=1, o=(0,0,0), n='pinky_03_templete'), mc.select(d=True)

# ring
ring_00 = mc.joint(hand, p=(50.400, 98.309, 0.304), rad=1, o=(-1.869, 19.539, -17.762), n='ring_00_templete'), mc.select(d=True)
ring_01 = mc.joint(ring_00, p=(51.550, 95.069, 0.758), rad=1, o=(0, 0, -17.113), n='ring_01_templete'), mc.select(d=True)
ring_02 = mc.joint(ring_01, p=(51.757, 91.473, 1.179), rad=1, o=(0, 0, -30.849), n='ring_02_templete'), mc.select(d=True)
ring_03 = mc.joint(ring_02, p=(50.213, 88.823, 1.351), rad=1, o=(0,0,0), n='ring_02_templete'), mc.select(d=True)

# middle
middle_00 = mc.joint(hand, p=(50.308, 98.546, 1.929), rad=1, o=(-1.343, 13.133, -17.658), n='middle_00_templete'), mc.select(d=True)
middle_01 = mc.joint(middle_00, p=(51.541, 95.185, 2.824), rad=1, o=(-0.508, 2.101, -10.258), n='middle_01_templete'), mc.select(d=True)
middle_02 = mc.joint(middle_01, p=(52.188, 91.442, 3.579), rad=1, o=(0, 0, -28.791), n='middle_02_templete'), mc.select(d=True)
middle_03 = mc.joint(middle_02, p=(51.111, 88.351, 4.017), rad=1, o=(0,0,0), n='middle_03_templete'), mc.select(d=True)

# index
index_00 = mc.joint(hand, p=(49.854, 99.195, 3.526), rad=1, o=(9.852, -7.280, -16.897), n='index_00_templete'), mc.select(d=True)
index_01 = mc.joint(index_00, p=(51.104, 95.833, 5.040), rad=1, o=(0, 0, -17.958), n='index_01_templete'), mc.select(d=True)
index_02 = mc.joint(index_01, p=(51.215, 92.147, 6.284), rad=1, o=(0, 0, -14.196), n='index_02_templete'), mc.select(d=True)
index_03 = mc.joint(index_02, p=(50.622, 89.423, 6.981), rad=1, o=(0, 0, 0), n='index_03_templete'), mc.select(d=True)

# thumb
thumb_01 = mc.joint(hand, p=(46.422, 102.638, 2.687), rad=1, o=(77.319, -32.718, -26.439), n='thumb_01_templete'), mc.select(d=True)
thumb_02 = mc.joint(thumb_01, p=(46.761, 100.272, 5.341), rad=1, o=(-1.148, 5.425, -11.966), n='thumb_02_templete'), mc.select(d=True)
thumb_03 = mc.joint(thumb_02, p=(47.470, 97.104, 7.638), rad=1, o=(0 ,0 ,0), n='thumb_03_templete'), mc.select(d=True)

### leg
thigh = mc.joint(p=(10.431, 95.474, -2.290), rad=2, o=(0,-5.546,-90.000), n='thigh_templete'), mc.select(d=True)
calf = mc.joint(thigh, p=(10.431, 54.838, 1.656), rad=2, o=(0,15.067,0), n='calf_templete'), mc.select(d=True)
foot = mc.joint(calf, p=(10.431, 12.113, -5.511), rad=2, o=(0, 260.979, 0), n='foot_templete'), mc.select(d=True)
ball = mc.joint(foot, p=(10.431, -0.050, 5.758), rad=2, o=(-90, -90, 0), n='ball_templete'), mc.select(d=True)
toe = mc.joint(ball, p=(10.431, -0.113, 12.968), rad=2, o=(-90, -90, 0), n='toe_templete'), mc.select(d=True)

mc.parent(thigh, pelvis), mc.parent(clavicle, spine_03), mc.parent(neck, spine_03)

itemColor('pelvis_templete', 17)