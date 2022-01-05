#######################################################################
#
#
#                            UTILITIES
#
#
#######################################################################


import maya.cmds as mc

####### color
def itemColor(s, c):  # yellow 17, red 13, blue 6, light blue 18
    mc.setAttr(s + '.overrideEnabled', 1)
    mc.setAttr(s + '.overrideColor', c)

###### neckHead templete
def neckHead_jntT(neckP = (0, 155.256, -5.945), neckO = (0, -1.638, 90.000), neckName= 'neck_templete', headP = (0, 163.244, -5.717), headO = (1.638, 0, 0), *kwargs):

    neck = mc.joint(p= neckP, rad=2, o= neckO, n= neckName), mc.select(d=True)
    head = mc.joint(neck, p= headP, rad=2, o= headO, n='head_templete'), mc.select(d=True)


