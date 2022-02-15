import maya.cmds as mc

#######################################################################
#
#
#                            TEMPLETES
#
#
#######################################################################

class myHierarchyJntTempletes():

    def __init__(self, name=None):
        self.name = name

    ############################################## neckHead templete #########################################################################
    def neckHeadT(self, name='', *args):
        neck = mc.joint(p=(0, 155.256, -5.945), rad=2, o=(0, -1.638, 90.000), n='neck'), mc.select(d=True)
        head = mc.joint(neck, p=(0, 163.244, -5.717), rad=2, o=(1.638, 0, 0), n='head'), mc.select(d=True)

    ############################################## arm templete #########################################################################
    def armT(self, name='', *args):
        clavicle_l = mc.joint(p=(2.663, 146.853, -1.658), rad=2, o=(0, 15, 0), n='clavicle_l'), mc.select(d=True)
        upperarm_l = mc.joint(clavicle_l, p=(16.535, 146.853, -5.454), rad=2, o=(-0.059, -6.599, -56.457), n='upperarm_l'), mc.select(d=True)
        lowerarm_l = mc.joint(upperarm_l, p=(32.645, 123.032, -6.348), rad=2, o=(4.422, -14.629, -0.336), n='lowerarm_l'), mc.select(d=True)
        hand_l = mc.joint(lowerarm_l, p=(47.297, 103.560, -0.915), rad=2, o=(4.283, -2.541, 0.593), n='hand_l'), mc.select(d=True)

        ### pinky
        pinky_00_l = mc.joint(hand_l, p=(50.260, 98.184, -1.314), rad=1, o=(-5.328, 19.160, -24.458), n='pinky_00_l'), mc.select(d=True)
        pinky_01_l = mc.joint(pinky_00_l, p=(51.084, 94.987, -1.521), rad=1, o=(-2.604, -2.168, -11.199), n='pinky_01_l'), mc.select(d=True)
        pinky_02_l = mc.joint(pinky_01_l, p=(51.180, 92.620, -1.558), rad=1, o=(-3.439, 1.179, -21.202), n='pinky_02_l'), mc.select(d=True)
        pinky_03_l = mc.joint(pinky_02_l, p=(50.312, 90.082, -1.547), rad=1, o=(0, 0, 0), n='pinky_03_l'), mc.select(d=True)

        ### ring
        ring_00_l = mc.joint(hand_l, p=(50.400, 98.309, 0.304), rad=1, o=(-1.784, 9.108, -17.419), n='ring_00_l'), mc.select(d=True)
        ring_01_l = mc.joint(ring_00_l, p=(51.550, 95.069, 0.758), rad=1, o=(-3.058, 2.084, -16.957), n='ring_01_l'), mc.select(d=True)
        ring_02_l = mc.joint(ring_01_l, p=(51.734, 91.461, 1.043), rad=1, o=(-4.043, 2.126, -30.759), n='ring_02_l'), mc.select(d=True)
        ring_03_l = mc.joint(ring_02_l, p=(50.298, 88.753, 1.204), rad=1, o=(0, 0, 0), n='ring_03_l'), mc.select(d=True)

        ### middle
        middle_00_l = mc.joint(hand_l, p=(50.308, 98.546, 1.929), rad=1, o=(4.373, 2.564, -17.780), n='middle_00_l'), mc.select(d=True)
        middle_01_l = mc.joint(middle_00_l, p=(51.541, 95.185, 2.824), rad=1, o=(-4.050, 1.144, -10.337), n='middle_01_l'), mc.select(d=True)
        middle_02_l = mc.joint(middle_01_l, p=(52.147, 91.430, 3.550), rad=1, o=(0.748, 1.389, -27.195), n='middle_02_l'), mc.select(d=True)
        middle_03_l = mc.joint(middle_02_l, p=(51.129, 88.314, 3.941), rad=1, o=(0, 0, 0), n='middle_03_l'), mc.select(d=True)

        ### index
        index_00_l = mc.joint(hand_l, p=(49.854, 99.195, 3.526), rad=1, o=(9.852, -7.280, -16.897), n='index_00_l'), mc.select(d=True)
        index_01_l = mc.joint(index_00_l, p=(51.104, 95.833, 5.040), rad=1, o=(0, 0, -17.958), n='index_01_l'), mc.select(d=True)
        index_02_l = mc.joint(index_01_l, p=(51.215, 92.147, 6.284), rad=1, o=(0, 0, -14.196), n='index_02_l'), mc.select(d=True)
        index_03_l = mc.joint(index_02_l, p=(50.622, 89.423, 6.981), rad=1, o=(0, 0, 0), n='index_03_l'), mc.select(d=True)

        ### thumb
        thumb_01_l = mc.joint(hand_l, p=(46.422, 102.638, 2.687), rad=1, o=(77.319, -32.718, -26.439), n='thumb_01_l'), mc.select(d=True)
        thumb_02_l = mc.joint(thumb_01_l, p=(46.761, 100.272, 5.341), rad=1, o=(-1.148, 5.425, -11.966), n='thumb_02_l'), mc.select(d=True)
        thumb_03_l = mc.joint(thumb_02_l, p=(47.470, 97.104, 7.638), rad=1, o=(0, 0, 0), n='thumb_03_l'), mc.select(d=True)

    ########################################### spine templete ############################################################
    def spineT(self, name='', *args):
        pelvis = mc.joint(p=(0, 97.546, -2.303), rad=2, o=(0, 0.849, 90), n='pelvis'), mc.select(d=True)
        spine_01 = mc.joint(pelvis, p=(0, 108.888, -2.417), rad=2, o=(-0.578, -2.703, 0.027), n='spine_01'), mc.select(d=True)
        spine_02 = mc.joint(spine_01, p=(0, 120.295, -2.532), rad=2, o=(0, 0.124, 0), n='spine_02'), mc.select(d=True)
        spine_03 = mc.joint(spine_02, p=(0, 131.688, -2.646), rad=2, o=(0.577, 0.534, -0.015), n='spine_03'), mc.select(d=True)

    ######################################## leg templete ########################################################
    def legT(self, name='', *args):
        thigh_l = mc.joint(p=(10.431, 95.474, -2.290), rad=2, o=(0, -5.546, -90.000), n='thigh_l'), mc.select(d=True)
        calf_l = mc.joint(thigh_l, p=(10.431, 54.838, 1.656), rad=2, o=(0, 15.067, 0), n='calf_l'), mc.select(d=True)
        foot_l = mc.joint(calf_l, p=(10.431, 12.113, -5.511), rad=2, o=(0, 260.979, 0), n='foot_l'), mc.select(d=True)
        ball_l = mc.joint(foot_l, p=(10.431, -0.050, 5.758), rad=2, o=(-90, -90, 0), n='ball_l'), mc.select(d=True)
        toe_l = mc.joint(ball_l, p=(10.431, -0.113, 12.968), rad=2, o=(0, 0, 0), n='toe_l'), mc.select(d=True)

    ######################################### biped templete ##########################################################
    def bipedT(self, name='', *args):
        ### neckHead
        neck = mc.joint(p=(0, 155.256, -5.945), rad=2, o=(0, -1.638, 90.000), n='neck'), mc.select(d=True)
        head = mc.joint(neck, p=(0, 163.244, -5.717), rad=2, o=(1.638, 0, 0), n='head'), mc.select(d=True)

        ### arm
        clavicle_l = mc.joint(p=(2.663, 146.853, -1.658), rad=2, o=(0, 15, 0), n='clavicle_l'), mc.select(d=True)
        upperarm_l = mc.joint(clavicle_l, p=(16.535, 146.853, -5.454), rad=2, o=(-0.059, -6.599, -56.457), n='upperarm_l'), mc.select(d=True)
        lowerarm_l = mc.joint(upperarm_l, p=(32.645, 123.032, -6.348), rad=2, o=(4.422, -14.629, -0.336), n='lowerarm_l'), mc.select(d=True)
        hand_l = mc.joint(lowerarm_l, p=(47.297, 103.560, -0.915), rad=2, o=(4.283, -2.541, 0.593), n='hand_l'), mc.select(d=True)

        # pinky
        pinky_00_l = mc.joint(hand_l, p=(50.260, 98.184, -1.314), rad=1, o=(-5.328, 19.160, -24.458), n='pinky_00_l'), mc.select(d=True)
        pinky_01_l = mc.joint(pinky_00_l, p=(51.084, 94.987, -1.521), rad=1, o=(-2.604, -2.168, -11.199), n='pinky_01_l'), mc.select(d=True)
        pinky_02_l = mc.joint(pinky_01_l, p=(51.180, 92.620, -1.558), rad=1, o=(-3.439, 1.179, -21.202), n='pinky_02_l'), mc.select(d=True)
        pinky_03_l = mc.joint(pinky_02_l, p=(50.312, 90.082, -1.547), rad=1, o=(0, 0, 0), n='pinky_03_l'), mc.select(d=True)

        # ring
        ring_00_l = mc.joint(hand_l, p=(50.400, 98.309, 0.304), rad=1, o=(-1.784, 9.108, -17.419), n='ring_00_l'), mc.select(d=True)
        ring_01_l = mc.joint(ring_00_l, p=(51.550, 95.069, 0.758), rad=1, o=(-3.058, 2.084, -16.957), n='ring_01_l'), mc.select(d=True)
        ring_02_l = mc.joint(ring_01_l, p=(51.734, 91.461, 1.043), rad=1, o=(-4.043, 2.126, -30.759), n='ring_02_l'), mc.select(d=True)
        ring_03_l = mc.joint(ring_02_l, p=(50.298, 88.753, 1.204), rad=1, o=(0, 0, 0), n='ring_03_l'), mc.select(d=True)

        # middle
        middle_00_l = mc.joint(hand_l, p=(50.308, 98.546, 1.929), rad=1, o=(4.373, 2.564, -17.780), n='middle_00_l'), mc.select(d=True)
        middle_01_l = mc.joint(middle_00_l, p=(51.541, 95.185, 2.824), rad=1, o=(-4.050, 1.144, -10.337), n='middle_01_l'), mc.select(d=True)
        middle_02_l = mc.joint(middle_01_l, p=(52.147, 91.430, 3.550), rad=1, o=(0.748, 1.389, -27.195), n='middle_02_l'), mc.select(d=True)
        middle_03_l = mc.joint(middle_02_l, p=(51.129, 88.314, 3.941), rad=1, o=(0, 0, 0), n='middle_03_l'), mc.select(d=True)

        # index
        index_00_l = mc.joint(hand_l, p=(49.854, 99.195, 3.526), rad=1, o=(9.852, -7.280, -16.897), n='index_00_l'), mc.select(d=True)
        index_01_l = mc.joint(index_00_l, p=(51.104, 95.833, 5.040), rad=1, o=(0, 0, -17.958), n='index_01_l'), mc.select(d=True)
        index_02_l = mc.joint(index_01_l, p=(51.215, 92.147, 6.284), rad=1, o=(0, 0, -14.196), n='index_02_l'), mc.select(d=True)
        index_03_l = mc.joint(index_02_l, p=(50.622, 89.423, 6.981), rad=1, o=(0, 0, 0), n='index_03_l'), mc.select(d=True)

        # thumb
        thumb_01_l = mc.joint(hand_l, p=(46.422, 102.638, 2.687), rad=1, o=(77.319, -32.718, -26.439), n='thumb_01_l'), mc.select(d=True)
        thumb_02_l = mc.joint(thumb_01_l, p=(46.761, 100.272, 5.341), rad=1, o=(-1.148, 5.425, -11.966), n='thumb_02_l'), mc.select(d=True)
        thumb_03_l = mc.joint(thumb_02_l, p=(47.470, 97.104, 7.638), rad=1, o=(0, 0, 0), n='thumb_03_l'), mc.select(d=True)

        ### spine
        pelvis = mc.joint(p=(0, 97.546, -2.303), rad=2, o=(0, 0.849, 90), n='pelvis'), mc.select(d=True)
        spine_01 = mc.joint(pelvis, p=(0, 108.888, -2.417), rad=2, o=(-0.578, -2.703, 0.027), n='spine_01'), mc.select(d=True)
        spine_02 = mc.joint(spine_01, p=(0, 120.295, -2.532), rad=2, o=(0, 0.124, 0), n='spine_02'), mc.select(d=True)
        spine_03 = mc.joint(spine_02, p=(0, 131.688, -2.646), rad=2, o=(0.577, 0.534, -0.015), n='spine_03'), mc.select(d=True)

        ### leg
        thigh_l = mc.joint(p=(10.431, 95.474, -2.290), rad=2, o=(0, -5.546, -90.000), n='thigh_l'), mc.select(d=True)
        calf_l = mc.joint(thigh_l, p=(10.431, 54.838, 1.656), rad=2, o=(0, 15.067, 0), n='calf_l'), mc.select(d=True)
        foot_l = mc.joint(calf_l, p=(10.431, 12.113, -5.511), rad=2, o=(0, 260.979, 0), n='foot_l'), mc.select(d=True)
        ball_l = mc.joint(foot_l, p=(10.431, -0.050, 5.758), rad=2, o=(-90, -90, 0), n='ball_l'), mc.select(d=True)
        toe_l = mc.joint(ball_l, p=(10.431, -0.113, 12.968), rad=2, o=(0, 0, 0), n='toe_l'), mc.select(d=True)

myHJntTemp = myHierarchyJntTempletes()