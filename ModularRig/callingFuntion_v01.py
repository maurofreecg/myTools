import importlib
import utility as ut
import maya.cmds as mc
import pymel.core as pm
importlib.reload(ut)


ut.neckHead_jntT()
ut.neck_FK_transform()
ut.spine_jntT()
ut.spine_FK_transfomr()
ut.spine_IK_transform()
ut.arm_jntT()
ut.arm_fingers_FK_transform()
ut.leg_jntT()
ut.leg_FK_Transform()
ut.biped_jntT()
ut.biped_FK_transform()