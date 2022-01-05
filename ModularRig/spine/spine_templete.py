# spine templete

import maya.cmds as mc

def itemColor(s, c): # yellow 17, red 13, blue 6, light blue 18
    mc.setAttr(s + '.overrideEnabled', 1)
    mc.setAttr(s + '.overrideColor', c)

pelvis = mc.joint(p=(0, 97.546, -2.303), rad=2, o=(0,3.538, 90), n='pelvis_templete'), mc.select(d=True)
spine_01 = mc.joint(pelvis, p=(0, 108.888, -2.417), rad=2, o=(0,0.577, 90), n='spine_01_templete'), mc.select(d=True)
spine_02 = mc.joint(spine_01, p=(0, 120.295, -2.532), rad=2, o=(0,-0.577, -90), n='spine_02_templete'), mc.select(d=True)
spine_03 = mc.joint(spine_02, p=(0, 131.688, -2.646), rad=2, o=(0.577, 0, 0), n='spine_03_templete'), mc.select(d=True)

itemColor('pelvis_templete', 17)