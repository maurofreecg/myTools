import importlib
import utility as ut
import maya.cmds as mc
import pymel.core as pm
importlib.reload(ut)


ut.neckHead_jntT()
ut.neck_FK_transform()
ut.spine_jntT()
ut.spine_FK_transfomr()
ut.arm_jntT()
ut.arm_fingers_FK_transform()
ut.leg_jntT()
ut.biped_jntT()
