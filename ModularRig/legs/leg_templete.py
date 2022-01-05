# leg templete

import maya.cmds as mc

def itemColor(s, c): # yellow 17, red 13, blue 6, light blue 18
    mc.setAttr(s + '.overrideEnabled', 1)
    mc.setAttr(s + '.overrideColor', c)

thigh = mc.joint(p=(10.431, 95.474, -2.290), rad=2, o=(0,-5.546,-90.000), n='thigh_templete'), mc.select(d=True)
calf = mc.joint(thigh, p=(10.431, 54.838, 1.656), rad=2, o=(0,15.067,0), n='calf_templete'), mc.select(d=True)
foot = mc.joint(calf, p=(10.431, 12.113, -5.511), rad=2, o=(0, 260.979, 0), n='foot_templete'), mc.select(d=True)
ball = mc.joint(foot, p=(10.431, -0.050, 5.758), rad=2, o=(-90, -90, 0), n='ball_templete'), mc.select(d=True)
toe = mc.joint(ball, p=(10.431, -0.113, 12.968), rad=2, o=(-90, -90, 0), n='toe_templete'), mc.select(d=True)

itemColor('thigh_templete', 17)