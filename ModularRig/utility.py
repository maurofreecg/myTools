#######################################################################
#
#
#                            UTILITIES
#
#
#######################################################################

import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm
from maya import cmds, OpenMaya
import controls
import hierarchyJntTempletes
import importlib
importlib.reload(controls)
myCtrl = controls.myControls()
importlib.reload(hierarchyJntTempletes)
myHJntTemp = hierarchyJntTempletes.myHierarchyJntTempletes()

#################################################################################################################################################################
#
#                                                           Color
#
##################################################################################################################################################################
def itemColor(s, c):  # yellow 17, red 13, blue 6, light blue 18
    mc.setAttr(s + '.overrideEnabled', 1)
    mc.setAttr(s + '.overrideColor', c)

#################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################
#
#                                                            ARM MODULE SYSTEM SETUP
#
##################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################
arm_fingers_l_jnt_list = ['clavicle_l', 'upperarm_l', 'lowerarm_l', 'hand_l', 'pinky_00_l', 'pinky_01_l', 'pinky_02_l', 'pinky_03_l', 'ring_00_l', 'ring_01_l',
                          'ring_02_l', 'ring_03_l', 'index_00_l', 'index_01_l', 'index_02_l', 'index_03_l', 'middle_00_l', 'middle_01_l', 'middle_02_l', 'middle_03_l',
                          'thumb_03_l']

for arm_jnt in arm_fingers_l_jnt_list:
    mc.makeIdentity(arm_jnt, apply=True, t=True, r=True, s=True)
    mc.select(d=True)

# mirror base arm skeleton
mc.mirrorJoint('clavicle_l', mirrorYZ=True, mirrorBehavior=True, searchReplace=('_l', '_r'))
mc.select(d=True)

#################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################
#
#                                                            ARM -> FK SYSTEM
#
##################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################
mc.duplicate('clavicle_l')
pm.select('clavicle_l1')
mel.eval('searchReplaceNames "_l" "_l2" "hierarchy"')
mc.rename('clavicle_l21', 'clavicle_l2')
mc.select('clavicle_l2', hi=True)
fkJnt = mc.ls(sl=True)

for i in fkJnt:
    name = i.replace('l2', 'l_fk')
    mc.rename(i, name)

mc.mirrorJoint('clavicle_l_fk', mirrorYZ=True, mirrorBehavior=True, searchReplace=('_l', '_r')), mc.select(d=True)

########################################################################################################################### fk fingers controls

fingerFK_l_jnts_list = ['upperarm_l_fk', 'lowerarm_l_fk', 'hand_l_fk', 'pinky_00_l_fk', 'pinky_01_l_fk', 'pinky_02_l_fk', 'pinky_03_l_fk', 'ring_00_l_fk', 'ring_01_l_fk', 'ring_02_l_fk', 'ring_03_l_fk',
                        'middle_00_l_fk', 'middle_01_l_fk', 'middle_02_l_fk', 'middle_03_l_fk', 'index_00_l_fk', 'index_01_l_fk', 'index_02_l_fk', 'index_03_l_fk', 'thumb_01_l_fk', 'thumb_02_l_fk', 'thumb_03_l_fk']

fingerFK_r_jnts_list = ['upperarm_r_fk', 'lowerarm_r_fk', 'hand_r_fk', 'pinky_00_r_fk', 'pinky_01_r_fk', 'pinky_02_r_fk', 'pinky_03_r_fk', 'ring_00_r_fk', 'ring_01_r_fk', 'ring_02_r_fk', 'ring_03_r_fk',
                        'middle_00_r_fk', 'middle_01_r_fk', 'middle_02_r_fk', 'middle_03_r_fk', 'index_00_r_fk', 'index_01_r_fk', 'index_02_r_fk', 'index_03_r_fk', 'thumb_01_r_fk', 'thumb_02_r_fk', 'thumb_03_r_fk']

for fingerfkL in fingerFK_l_jnts_list:
    myCtrl.fk_ctrl(fingerfkL)

for fingerfkR in fingerFK_r_jnts_list:
    myCtrl.fk_ctrl(fingerfkR)

fingerFK_l_ctrlSpaceMaster_list = ['upperarm_l_fk_ctrlSpaceMaster', 'lowerarm_l_fk_ctrlSpaceMaster', 'hand_l_fk_ctrlSpaceMaster',  'pinky_00_l_fk_ctrlSpaceMaster', 'pinky_01_l_fk_ctrlSpaceMaster',
                                   'pinky_02_l_fk_ctrlSpaceMaster', 'pinky_03_l_fk_ctrlSpaceMaster', 'ring_00_l_fk_ctrlSpaceMaster', 'ring_01_l_fk_ctrlSpaceMaster', 'ring_02_l_fk_ctrlSpaceMaster',
                                   'ring_03_l_fk_ctrlSpaceMaster', 'middle_00_l_fk_ctrlSpaceMaster', 'middle_01_l_fk_ctrlSpaceMaster', 'middle_02_l_fk_ctrlSpaceMaster', 'middle_03_l_fk_ctrlSpaceMaster',
                                   'index_00_l_fk_ctrlSpaceMaster', 'index_01_l_fk_ctrlSpaceMaster', 'index_02_l_fk_ctrlSpaceMaster', 'index_03_l_fk_ctrlSpaceMaster', 'thumb_01_l_fk_ctrlSpaceMaster',
                                   'thumb_02_l_fk_ctrlSpaceMaster', 'thumb_03_l_fk_ctrlSpaceMaster']

fingerFK_l_ctrlSpace_list = ['upperarm_l_fk_ctrlSpace', 'lowerarm_l_fk_ctrlSpace', 'hand_l_fk_ctrlSpace',  'pinky_00_l_fk_ctrlSpace', 'pinky_01_l_fk_ctrlSpace', 'pinky_02_l_fk_ctrlSpace', 'pinky_03_l_fk_ctrlSpace',
                             'ring_00_l_fk_ctrlSpace', 'ring_01_l_fk_ctrlSpace', 'ring_02_l_fk_ctrlSpace', 'ring_03_l_fk_ctrlSpace', 'middle_00_l_fk_ctrlSpace', 'middle_01_l_fk_ctrlSpace', 'middle_02_l_fk_ctrlSpace',
                             'middle_03_l_fk_ctrlSpace', 'index_00_l_fk_ctrlSpace', 'index_01_l_fk_ctrlSpace', 'index_02_l_fk_ctrlSpace', 'index_03_l_fk_ctrlSpace', 'thumb_01_l_fk_ctrlSpace',
                             'thumb_02_l_fk_ctrlSpace', 'thumb_03_l_fk_ctrlSpace']

fingerFK_l_ctrl_list = ['upperarm_l_fk_ctrl', 'lowerarm_l_fk_ctrl', 'hand_l_fk_ctrl',  'pinky_00_l_fk_ctrl', 'pinky_01_l_fk_ctrl', 'pinky_02_l_fk_ctrl', 'pinky_03_l_fk_ctrl',  'ring_00_l_fk_ctrl', 'ring_01_l_fk_ctrl',
                        'ring_02_l_fk_ctrl', 'ring_03_l_fk_ctrl', 'middle_00_l_fk_ctrl', 'middle_01_l_fk_ctrl', 'middle_02_l_fk_ctrl',  'middle_03_l_fk_ctrl', 'index_00_l_fk_ctrl', 'index_01_l_fk_ctrl',
                        'index_02_l_fk_ctrl', 'index_03_l_fk_ctrl', 'thumb_01_l_fk_ctrl', 'thumb_02_l_fk_ctrl', 'thumb_03_l_fk_ctrl']

fingerFK_r_ctrlSpaceMaster_list = ['upperarm_r_fk_ctrlSpaceMaster', 'lowerarm_r_fk_ctrlSpaceMaster', 'hand_r_fk_ctrlSpaceMaster',  'pinky_00_r_fk_ctrlSpaceMaster', 'pinky_01_r_fk_ctrlSpaceMaster',
                                   'pinky_02_r_fk_ctrlSpaceMaster', 'pinky_03_r_fk_ctrlSpaceMaster', 'ring_00_r_fk_ctrlSpaceMaster', 'ring_01_r_fk_ctrlSpaceMaster', 'ring_02_r_fk_ctrlSpaceMaster',
                                   'ring_03_r_fk_ctrlSpaceMaster', 'middle_00_r_fk_ctrlSpaceMaster', 'middle_01_r_fk_ctrlSpaceMaster', 'middle_02_r_fk_ctrlSpaceMaster', 'middle_03_r_fk_ctrlSpaceMaster',
                                   'index_00_r_fk_ctrlSpaceMaster', 'index_01_r_fk_ctrlSpaceMaster', 'index_02_r_fk_ctrlSpaceMaster', 'index_03_r_fk_ctrlSpaceMaster', 'thumb_01_r_fk_ctrlSpaceMaster',
                                   'thumb_02_r_fk_ctrlSpaceMaster', 'thumb_03_r_fk_ctrlSpaceMaster']

fingerFK_r_ctrlSpace_list = ['upperarm_r_fk_ctrlSpace', 'lowerarm_r_fk_ctrlSpace', 'hand_r_fk_ctrlSpace',  'pinky_00_r_fk_ctrlSpace', 'pinky_01_r_fk_ctrlSpace', 'pinky_02_r_fk_ctrlSpace', 'pinky_03_r_fk_ctrlSpace',
                             'ring_00_r_fk_ctrlSpace', 'ring_01_r_fk_ctrlSpace', 'ring_02_r_fk_ctrlSpace', 'ring_03_r_fk_ctrlSpace', 'middle_00_r_fk_ctrlSpace', 'middle_01_r_fk_ctrlSpace', 'middle_02_r_fk_ctrlSpace',
                             'middle_03_r_fk_ctrlSpace', 'index_00_r_fk_ctrlSpace', 'index_01_r_fk_ctrlSpace', 'index_02_r_fk_ctrlSpace', 'index_03_r_fk_ctrlSpace', 'thumb_01_r_fk_ctrlSpace',
                             'thumb_02_r_fk_ctrlSpace', 'thumb_03_r_fk_ctrlSpace']

fingerFK_r_ctrl_list = ['upperarm_r_fk_ctrl', 'lowerarm_r_fk_ctrl', 'hand_r_fk_ctrl',  'pinky_00_r_fk_ctrl', 'pinky_01_r_fk_ctrl', 'pinky_02_r_fk_ctrl', 'pinky_03_r_fk_ctrl',  'ring_00_r_fk_ctrl', 'ring_01_r_fk_ctrl',
                        'ring_02_r_fk_ctrl', 'ring_03_r_fk_ctrl', 'middle_00_r_fk_ctrl', 'middle_01_r_fk_ctrl', 'middle_02_r_fk_ctrl',  'middle_03_r_fk_ctrl', 'index_00_r_fk_ctrl', 'index_01_r_fk_ctrl',
                        'index_02_r_fk_ctrl', 'index_03_r_fk_ctrl', 'thumb_01_r_fk_ctrl', 'thumb_02_r_fk_ctrl', 'thumb_03_r_fk_ctrl']



################################################################################################################################## position on bones
for i, item in enumerate(fingerFK_l_jnts_list):
    mc.delete(mc.parentConstraint(item, fingerFK_l_ctrlSpaceMaster_list[i]))

for j, item in enumerate(fingerFK_r_jnts_list):
    mc.delete(mc.parentConstraint(item, fingerFK_r_ctrlSpaceMaster_list[j]))

################################################################################################################################### finger fk control scale
fingerFK_cv_list = ['pinky_00_l_fk_ctrl.cv[0:26]', 'pinky_01_l_fk_ctrl.cv[0:26]', 'pinky_02_l_fk_ctrl.cv[0:26]', 'pinky_03_l_fk_ctrl.cv[0:26]', 'ring_00_l_fk_ctrl.cv[0:26]', 'ring_01_l_fk_ctrl.cv[0:26]',
                    'ring_02_l_fk_ctrl.cv[0:26]', 'ring_03_l_fk_ctrl.cv[0:26]', 'middle_00_l_fk_ctrl.cv[0:26]','middle_01_l_fk_ctrl.cv[0:26]', 'middle_02_l_fk_ctrl.cv[0:26]', 'middle_03_l_fk_ctrl.cv[0:26]',
                    'index_00_l_fk_ctrl.cv[0:26]', 'index_01_l_fk_ctrl.cv[0:26]', 'index_02_l_fk_ctrl.cv[0:26]', 'index_03_l_fk_ctrl.cv[0:26]', 'thumb_01_l_fk_ctrl.cv[0:26]', 'thumb_02_l_fk_ctrl.cv[0:26]',
                    'thumb_03_l_fk_ctrl.cv[0:26]', 'pinky_00_r_fk_ctrl.cv[0:26]', 'pinky_01_r_fk_ctrl.cv[0:26]', 'pinky_02_r_fk_ctrl.cv[0:26]', 'pinky_03_r_fk_ctrl.cv[0:26]', 'ring_00_r_fk_ctrl.cv[0:26]',
                    'ring_01_r_fk_ctrl.cv[0:26]', 'ring_02_r_fk_ctrl.cv[0:26]', 'ring_03_r_fk_ctrl.cv[0:26]', 'middle_00_r_fk_ctrl.cv[0:26]', 'middle_01_r_fk_ctrl.cv[0:26]', 'middle_02_r_fk_ctrl.cv[0:26]',
                    'middle_03_r_fk_ctrl.cv[0:26]', 'index_00_r_fk_ctrl.cv[0:26]', 'index_01_r_fk_ctrl.cv[0:26]', 'index_02_r_fk_ctrl.cv[0:26]', 'index_03_r_fk_ctrl.cv[0:26]', 'thumb_01_r_fk_ctrl.cv[0:26]',
                    'thumb_02_r_fk_ctrl.cv[0:26]', 'thumb_03_r_fk_ctrl.cv[0:26]']
fingerFK_l_cv_sel = mc.select(fingerFK_cv_list)
mc.scale(0.128653, 0.128653, 0.128653, ocp=True), mc.select(d=True)

mc.select('upperarm_r_fk_ctrl.cv[0:26]', 'lowerarm_r_fk_ctrl.cv[0:26]', 'hand_r_fk_ctrl.cv[0:26]', 'pinky_00_r_fk_ctrl.cv[0:26]', 'pinky_01_r_fk_ctrl.cv[0:26]', 'pinky_02_r_fk_ctrl.cv[0:26]', 'pinky_03_r_fk_ctrl.cv[0:26]',
          'ring_00_r_fk_ctrl.cv[0:26]', 'ring_01_r_fk_ctrl.cv[0:26]', 'ring_02_r_fk_ctrl.cv[0:26]', 'ring_03_r_fk_ctrl.cv[0:26]', 'middle_00_r_fk_ctrl.cv[0:26]', 'middle_01_r_fk_ctrl.cv[0:26]', 'middle_02_r_fk_ctrl.cv[0:26]',
          'middle_03_r_fk_ctrl.cv[0:26]', 'index_00_r_fk_ctrl.cv[0:26]', 'index_01_r_fk_ctrl.cv[0:26]', 'index_02_r_fk_ctrl.cv[0:26]', 'index_03_r_fk_ctrl.cv[0:26]', 'thumb_01_r_fk_ctrl.cv[0:26]',
          'thumb_02_r_fk_ctrl.cv[0:26]', 'thumb_03_r_fk_ctrl.cv[0:26]')
mc.rotate(0, 180, 0, ocp=True)
mc.select(d=True)

####################################################################################################################################### section scale per phalange
### finger 00
mc.select('pinky_00_l_fk_ctrl.cv[0:26]', 'index_00_l_fk_ctrl.cv[0:26]', 'middle_00_l_fk_ctrl.cv[0:26]', 'ring_00_l_fk_ctrl.cv[0:26]', 'pinky_00_r_fk_ctrl.cv[0:26]', 'index_00_r_fk_ctrl.cv[0:26]', 'middle_00_r_fk_ctrl.cv[0:26]',
          'ring_00_r_fk_ctrl.cv[0:26]')
mc.scale(2.213146, 2.213146, 2.213146, ocp=True), mc.scale(0.417209, 1, 1, ocp=True), mc.scale(1.264578, 1.264578, 1.264578, ocp=True), mc.scale(1, 1, 0.568709, ocp=True), mc.scale(0.71982, 1, 1, ocp=True), mc.select(d=True)

### finger 01
mc.select('pinky_01_l_fk_ctrl.cv[0:26]', 'index_01_l_fk_ctrl.cv[0:26]', 'middle_01_l_fk_ctrl.cv[0:26]', 'ring_01_l_fk_ctrl.cv[0:26]', 'pinky_01_r_fk_ctrl.cv[0:26]', 'index_01_r_fk_ctrl.cv[0:26]', 'middle_01_r_fk_ctrl.cv[0:26]',
          'ring_01_r_fk_ctrl.cv[0:26]')
mc.scale(2.037736, 2.037736, 2.037736, ocp=True), mc.scale(0.424699, 1, 1, ocp=True), mc.scale(1, 1, 0.707371, ocp=True), mc.select(d=True)

### finger 02
mc.select('pinky_02_l_fk_ctrl.cv[0:26]', 'index_02_l_fk_ctrl.cv[0:26]', 'middle_02_l_fk_ctrl.cv[0:26]', 'ring_02_l_fk_ctrl.cv[0:26]', 'pinky_02_r_fk_ctrl.cv[0:26]', 'index_02_r_fk_ctrl.cv[0:26]', 'middle_02_r_fk_ctrl.cv[0:26]',
          'ring_02_r_fk_ctrl.cv[0:26]')
mc.scale(1.565238, 1.565238, 1.565238, ocp=True), mc.scale(0.34634, 1, 1, ocp=True), mc.select(d=True)

### finger 03
mc.select('pinky_03_l_fk_ctrl.cv[0:26]', 'index_03_l_fk_ctrl.cv[0:26]', 'middle_03_l_fk_ctrl.cv[0:26]', 'ring_03_l_fk_ctrl.cv[0:26]', 'pinky_03_r_fk_ctrl.cv[0:26]', 'index_03_r_fk_ctrl.cv[0:26]', 'middle_03_r_fk_ctrl.cv[0:26]',
          'ring_03_r_fk_ctrl.cv[0:26]')
mc.scale(1.243849, 1.243849, 1.243849, ocp=True), mc.scale(0.433078, 1, 1, ocp=True), mc.select(d=True)

### thumb 01
mc.select('thumb_01_l_fk_ctrl.cv[0:26]', 'thumb_01_r_fk_ctrl.cv[0:26]')
mc.scale(2.828923, 2.828923, 2.828923, ocp=True), mc.scale(0.331514, 1, 1, ocp=True), mc.select(d=True)

### thumb 02
mc.select('thumb_02_l_fk_ctrl.cv[0:26]', 'thumb_02_r_fk_ctrl.cv[0:26]')
mc.scale(2.15293, 2.15293, 2.15293, ocp=True), mc.scale(0.43488, 1, 1, ocp=True), mc.select(d=True)

### thumb 03
mc.select('thumb_03_l_fk_ctrl.cv[0:26]', 'thumb_03_r_fk_ctrl.cv[0:26]')
mc.scale(1.850562, 1.850562, 1.850562, ocp=True), mc.scale(0.374072, 1, 1, ocp=True), mc.select(d=True)

### upperarm_l
mc.select('upperarm_l_fk_ctrl.cv[7:13]', 'upperarm_l_fk_ctrl.cv[16:17]', 'upperarm_l_fk_ctrl.cv[20:21]', 'upperarm_l_fk_ctrl.cv[24:25]')
mc.scale(1.5, 1.5, 1.5, ocp=True), mc.move(1.2, 0, 0, r=True, os=True)

### upperarm_r
mc.select('upperarm_r_fk_ctrl.cv[7:13]', 'upperarm_r_fk_ctrl.cv[16:17]', 'upperarm_r_fk_ctrl.cv[20:21]', 'upperarm_r_fk_ctrl.cv[24:25]')
mc.scale(1.5, 1.5, 1.5, ocp=True), mc.move(-1.2, 0, 0, r=True, os=True)

### lowerarm_l
mc.select('lowerarm_l_fk_ctrl.cv[0:6]', 'lowerarm_l_fk_ctrl.cv[14:15]', 'lowerarm_l_fk_ctrl.cv[18:19]', 'lowerarm_l_fk_ctrl.cv[22:23]', 'lowerarm_l_fk_ctrl.cv[26]')
mc.move(-4, 0, 0, r=True, os=True)

### lowerarm_r
mc.select('lowerarm_r_fk_ctrl.cv[0:6]', 'lowerarm_r_fk_ctrl.cv[14:15]', 'lowerarm_r_fk_ctrl.cv[18:19]', 'lowerarm_r_fk_ctrl.cv[22:23]', 'lowerarm_r_fk_ctrl.cv[26]')
mc.move(4, 0, 0, r=True, os=True)

### hand_l
mc.select('hand_l_fk_ctrl.cv[0:6]', 'hand_l_fk_ctrl.cv[14:15]', 'hand_l_fk_ctrl.cv[18:19]', 'hand_l_fk_ctrl.cv[22:23]', 'hand_l_fk_ctrl.cv[26]')
mc.move(-24, 0, 0, r=True, os=True), mc.scale(1.2, 1.2, 1.2, ocp=True)

### hand_r
mc.select('hand_r_fk_ctrl.cv[0:6]', 'hand_r_fk_ctrl.cv[14:15]', 'hand_r_fk_ctrl.cv[18:19]', 'hand_r_fk_ctrl.cv[22:23]', 'hand_r_fk_ctrl.cv[26]')
mc.move(24, 0, 0, r=True, os=True), mc.scale(1.2, 1.2, 1.2, ocp=True)
mc.select(d=True)

#################################################################################################################### fingers lef side parent controls
### thumb
mc.parent('thumb_03_l_fk_ctrlSpaceMaster', 'thumb_02_l_fk_ctrl'), mc.parent('thumb_02_l_fk_ctrlSpaceMaster', 'thumb_01_l_fk_ctrl'), mc.select(d=True)
mc.parent('thumb_03_r_fk_ctrlSpaceMaster', 'thumb_02_r_fk_ctrl'), mc.parent('thumb_02_r_fk_ctrlSpaceMaster', 'thumb_01_r_fk_ctrl'), mc.select(d=True)

### index
mc.parent('index_03_l_fk_ctrlSpaceMaster', 'index_02_l_fk_ctrl'), mc.parent('index_02_l_fk_ctrlSpaceMaster', 'index_01_l_fk_ctrl'), mc.parent('index_01_l_fk_ctrlSpaceMaster', 'index_00_l_fk_ctrl'), mc.select(d=True)
mc.parent('index_03_r_fk_ctrlSpaceMaster', 'index_02_r_fk_ctrl'), mc.parent('index_02_r_fk_ctrlSpaceMaster', 'index_01_r_fk_ctrl'), mc.parent('index_01_r_fk_ctrlSpaceMaster', 'index_00_r_fk_ctrl'), mc.select(d=True)

### middle
mc.parent('middle_03_l_fk_ctrlSpaceMaster', 'middle_02_l_fk_ctrl'), mc.parent('middle_02_l_fk_ctrlSpaceMaster', 'middle_01_l_fk_ctrl'), mc.parent('middle_01_l_fk_ctrlSpaceMaster', 'middle_00_l_fk_ctrl'), mc.select(d=True)
mc.parent('middle_03_r_fk_ctrlSpaceMaster', 'middle_02_r_fk_ctrl'), mc.parent('middle_02_r_fk_ctrlSpaceMaster', 'middle_01_r_fk_ctrl'), mc.parent('middle_01_r_fk_ctrlSpaceMaster', 'middle_00_r_fk_ctrl'), mc.select(d=True)

### ring
mc.parent('ring_03_l_fk_ctrlSpaceMaster', 'ring_02_l_fk_ctrl'), mc.parent('ring_02_l_fk_ctrlSpaceMaster', 'ring_01_l_fk_ctrl'), mc.parent('ring_01_l_fk_ctrlSpaceMaster', 'ring_00_l_fk_ctrl'), mc.select(d=True)
mc.parent('ring_03_r_fk_ctrlSpaceMaster', 'ring_02_r_fk_ctrl'), mc.parent('ring_02_r_fk_ctrlSpaceMaster', 'ring_01_r_fk_ctrl'), mc.parent('ring_01_r_fk_ctrlSpaceMaster', 'ring_00_r_fk_ctrl'), mc.select(d=True)

### pinky
mc.parent('pinky_03_l_fk_ctrlSpaceMaster', 'pinky_02_l_fk_ctrl'), mc.parent('pinky_02_l_fk_ctrlSpaceMaster', 'pinky_01_l_fk_ctrl'), mc.parent('pinky_01_l_fk_ctrlSpaceMaster', 'pinky_00_l_fk_ctrl'), mc.select(d=True)
mc.parent('pinky_03_r_fk_ctrlSpaceMaster', 'pinky_02_r_fk_ctrl'), mc.parent('pinky_02_r_fk_ctrlSpaceMaster', 'pinky_01_r_fk_ctrl'), mc.parent('pinky_01_r_fk_ctrlSpaceMaster', 'pinky_00_r_fk_ctrl'), mc.select(d=True)

### global parent
mc.parent('lowerarm_l_fk_ctrlSpaceMaster', 'upperarm_l_fk_ctrl'), mc.parent('hand_l_fk_ctrlSpaceMaster', 'lowerarm_l_fk_ctrl')
mc.parent('pinky_00_l_fk_ctrlSpaceMaster', 'ring_00_l_fk_ctrlSpaceMaster', 'middle_00_l_fk_ctrlSpaceMaster', 'middle_00_l_fk_ctrlSpaceMaster', 'index_00_l_fk_ctrlSpaceMaster', 'thumb_01_l_fk_ctrlSpaceMaster', 'hand_l_fk_ctrl')

mc.parent('lowerarm_r_fk_ctrlSpaceMaster', 'upperarm_r_fk_ctrl'), mc.parent('hand_r_fk_ctrlSpaceMaster', 'lowerarm_r_fk_ctrl')
mc.parent('pinky_00_r_fk_ctrlSpaceMaster', 'ring_00_r_fk_ctrlSpaceMaster', 'middle_00_r_fk_ctrlSpaceMaster', 'middle_00_r_fk_ctrlSpaceMaster', 'index_00_r_fk_ctrlSpaceMaster', 'thumb_01_r_fk_ctrlSpaceMaster', 'hand_r_fk_ctrl')

mc.select(d=True)

####################################################################################################################### connect FK finger control to FK finger joints

for k, item in enumerate(fingerFK_l_jnts_list):
    mc.pointConstraint(fingerFK_l_ctrl_list[k], item, mo=True)
    mc.connectAttr(fingerFK_l_ctrl_list[k] + '.rx', item + '.rx')
    mc.connectAttr(fingerFK_l_ctrl_list[k] + '.ry', item + '.ry')
    mc.connectAttr(fingerFK_l_ctrl_list[k] + '.rz', item + '.rz')
    mc.connectAttr(fingerFK_l_ctrl_list[k] + '.sx', item + '.sx')
    mc.connectAttr(fingerFK_l_ctrl_list[k] + '.sy', item + '.sy')
    mc.connectAttr(fingerFK_l_ctrl_list[k] + '.sz', item + '.sz')

for f, item in enumerate(fingerFK_r_jnts_list):
    mc.pointConstraint(fingerFK_r_ctrl_list[f], item, mo=True)
    mc.connectAttr(fingerFK_r_ctrl_list[f] + '.rx', item + '.rx')
    mc.connectAttr(fingerFK_r_ctrl_list[f] + '.ry', item + '.ry')
    mc.connectAttr(fingerFK_r_ctrl_list[f] + '.rz', item + '.rz')
    mc.connectAttr(fingerFK_r_ctrl_list[f] + '.sx', item + '.sx')
    mc.connectAttr(fingerFK_r_ctrl_list[f] + '.sy', item + '.sy')
    mc.connectAttr(fingerFK_r_ctrl_list[f] + '.sz', item + '.sz')

itemColor('upperarm_l_fk_ctrlSpaceMaster', 6)
itemColor('upperarm_r_fk_ctrlSpaceMaster', 13)

#################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################
#
#                                                            ARM -> IK SYSTEM
#
##################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################
mc.duplicate('clavicle_l')
pm.select('clavicle_l1')
mel.eval('searchReplaceNames "_l" "_l2" "hierarchy"')
mc.rename('clavicle_l21', 'clavicle_l2')
mc.select('clavicle_l2', hi=True)
ikJnt = mc.ls(sl=True)

for i in ikJnt:
    name = i.replace('l2', 'l_ik')
    mc.rename(i, name)

mc.select('upperarm_l_ik', 'lowerarm_l_ik', 'hand_l_ik')
selO = mc.ls(sl=True)

upperarmIK = mc.xform(selO[0], q=True, ws=True, t=True)
lowerarmIK = mc.xform(selO[1], q=True, ws=True, t=True)
handIK = mc.xform(selO[2], q=True, ws=True, t=True)

################################################################################### pole vector templete
upperarmIKV = OpenMaya.MVector(upperarmIK[0], upperarmIK[1], upperarmIK[2])
lowerarmIKV = OpenMaya.MVector(lowerarmIK[0], lowerarmIK[1], lowerarmIK[2])
handIKV = OpenMaya.MVector(handIK[0], handIK[1], handIK[2])

startEnd = handIKV - upperarmIKV
startMid = lowerarmIKV - upperarmIKV

dotP = startMid * startEnd
proj = float(dotP) / float(startEnd.length())
startEndN = startEnd.normal()
projV = startEndN * proj

arrowV = startMid - projV
arrowV*=5
finalV = arrowV + lowerarmIKV

loc_PV = mc.spaceLocator(n='arm_PV_l')
loc_PVSpace = mc.group(loc_PV, n='PV_locSpace'), mc.select(d=True)
mc.xform(loc_PVSpace, ws=True, t=(finalV.x, finalV.y, finalV.z))
mc.parent(loc_PVSpace, 'lowerarm_l_ik')

############################################################################################################################## mirror ik chain
mc.mirrorJoint('clavicle_l_ik', mirrorYZ=True, mirrorBehavior=True, searchReplace=('_l', '_r'))
mc.rename('arm_PV_l1', 'arm_PV_r')

################################################################################################### create ikhandle rotate plane solver, PV & controls
ikArm_l = mc.ikHandle(n='ikArm_l', sj='upperarm_l_ik', ee='hand_l_ik', sol='ikRPsolver')
ikArm_r = mc.ikHandle(n='ikArm_r', sj='upperarm_r_ik', ee='hand_r_ik', sol='ikRPsolver')
ikArms_list = [ikArm_r, ikArm_r]
mc.select(d=True)

###################################################################################################################################################
#
#                                                           IK Control
#
####################################################################################################################################################
ikHand_jnt_list = ['hand_l_ik', 'hand_r_ik']
for ikH in ikHand_jnt_list:
    myCtrl.square_ctrl(ikH)

ikHand_ctrl_list = ['hand_l_ik_ctrl', 'hand_r_ik_ctrl']
for ikHand_ctrl in ikHand_ctrl_list:
    mc.setAttr(ikHand_ctrl + '.sx', l=True, k=False, ch=False)
    mc.setAttr(ikHand_ctrl + '.sy', l=True, k=False, ch=False)
    mc.setAttr(ikHand_ctrl + '.sz', l=True, k=False, ch=False)
    mc.setAttr(ikHand_ctrl + '.v', l=True, k=False, ch=False)
    mc.addAttr(ikHand_ctrl, ln='_', at='enum', en='_', k=True)
    mc.addAttr(ikHand_ctrl, ln='stretch', at='float', dv=0, min=0, max=1, k=True)
    mc.addAttr(ikHand_ctrl, ln='volumePreservation', at='float', dv=0, min=0, max=1, k=True)

######################################################################################################### ik gimbal control setup
ikHand_gimbalCtrl_list = ['hand_l_ik', 'hand_r_ik']
for ikHGimbal in ikHand_gimbalCtrl_list:
    myCtrl.diamondLow_ctrl(ikHGimbal)
mc.select('hand_l_ik_ctrlSpaceMaster1', 'hand_r_ik_ctrlSpaceMaster1', hi=True)
ikHGimbalCtrlSpaceMaster = mc.ls(sl=True)

for gimbal in ikHGimbalCtrlSpaceMaster:
    mel.eval('searchReplaceNames "ik_ctrl" "ik_gimbal_ctrl" "hierarchy"')
mc.rename('hand_l_ik_gimbal_ctrlSpaceMaster1', 'hand_l_ik_gimbal_ctrlSpaceMaster'), mc.rename('hand_r_ik_gimbal_ctrlSpaceMaster1', 'hand_r_ik_gimbal_ctrlSpaceMaster')
mc.select(d=True)

mc.parent('hand_l_ik_gimbal_ctrlSpaceMaster', 'hand_l_ik_ctrl'), mc.parent('hand_r_ik_gimbal_ctrlSpaceMaster', 'hand_r_ik_ctrl'), mc.select(d=True)
mc.delete(mc.parentConstraint('hand_r_ik', 'hand_r_ik_ctrlSpaceMaster')), mc.delete(mc.parentConstraint('hand_l_ik', 'hand_l_ik_ctrlSpaceMaster'))

mc.select('hand_l_ik_gimbal_ctrl.cv[0:18]', 'hand_r_ik_gimbal_ctrl.cv[0:18]')
mc.rotate(0,90,0, fo=True), mc.select(d=True)

ikHGimbalCtrl_list = ['hand_l_ik_gimbal_ctrl', 'hand_r_ik_gimbal_ctrl']
for ikRot in ikHGimbalCtrl_list:
    mc.setAttr(ikRot + '.tx', l=True, k=False, ch=False)
    mc.setAttr(ikRot + '.ty', l=True, k=False, ch=False)
    mc.setAttr(ikRot + '.tz', l=True, k=False, ch=False)
    mc.setAttr(ikRot + '.sx', l=True, k=False, ch=False)
    mc.setAttr(ikRot + '.sy', l=True, k=False, ch=False)
    mc.setAttr(ikRot + '.sz', l=True, k=False, ch=False)
    mc.setAttr(ikRot + '.v', l=True, k=False, ch=False)

############################################################################################################# pole vector ctrl setup
PV_arm_loc_list = ['arm_PV_l', 'arm_PV_r']
for armPV in PV_arm_loc_list:
    myCtrl.cone_ctrl(armPV)

mc.delete(mc.parentConstraint('arm_PV_l', 'arm_PV_l_ctrlSpaceMaster')), mc.delete(mc.parentConstraint('arm_PV_r', 'arm_PV_r_ctrlSpaceMaster'))

mc.setAttr('arm_PV_l_ctrlSpaceMaster.rx', -90)
mc.setAttr('arm_PV_r_ctrlSpaceMaster.rx', 270)
mc.setAttr('arm_PV_r_ctrlSpaceMaster.sx', -1)
mc.delete('PV_locSpace1', 'PV_locSpace')

armPV_ctrl_list = ['arm_PV_l_ctrl', 'arm_PV_r_ctrl']
for armPV_lockAt in armPV_ctrl_list:
    mc.setAttr(armPV_lockAt + '.rx', l=True, k=False, ch=False)
    mc.setAttr(armPV_lockAt + '.ry', l=True, k=False, ch=False)
    mc.setAttr(armPV_lockAt + '.rz', l=True, k=False, ch=False)
    mc.setAttr(armPV_lockAt + '.sx', l=True, k=False, ch=False)
    mc.setAttr(armPV_lockAt + '.sy', l=True, k=False, ch=False)
    mc.setAttr(armPV_lockAt + '.sz', l=True, k=False, ch=False)
    mc.setAttr(armPV_lockAt + '.v', l=True, k=False, ch=False)

#################################################################################################################### PV / point / orient constraint and curve guide referenced
mc.poleVectorConstraint('arm_PV_l_ctrl', 'ikArm_l', w=1), mc.poleVectorConstraint('arm_PV_r_ctrl', 'ikArm_r', w=1)
mc.pointConstraint('hand_l_ik_ctrl', 'ikArm_l', mo=True), mc.pointConstraint('hand_r_ik_ctrl', 'ikArm_r', mo=True)
mc.orientConstraint('hand_l_ik_gimbal_ctrl', 'hand_l_ik', mo=True), mc.orientConstraint('hand_r_ik_gimbal_ctrl', 'hand_r_ik', mo=True)

for PVCGuide in PV_arm_loc_list:
    myCtrl.lineCrv_ctrl(PVCGuide)

PVGuide_cvs_list = ['arm_PV_l_lCrvCtrl.cv[0]', 'arm_PV_l_lCrvCtrl.cv[1]', 'arm_PV_r_lCrvCtrl.cv[0]', 'arm_PV_r_lCrvCtrl.cv[1]']

for cl, item in enumerate(PVGuide_cvs_list):
    mc.cluster(PVGuide_cvs_list[cl], item, rel=True)

mc.rename('cluster1Handle', 'arm_PV_l_cl'), mc.rename('cluster2Handle', 'arm_l_cl'), mc.rename('cluster3Handle', 'arm_PV_r_cl'), mc.rename('cluster4Handle', 'arm_r_cl')

armsPV_cl_list = ['arm_PV_l_cl', 'arm_l_cl', 'arm_PV_r_cl', 'arm_r_cl']
armsPV_jntCtrl_list = ['arm_PV_l_ctrl', 'lowerarm_l_ik', 'arm_PV_r_ctrl', 'lowerarm_r_ik']

for pv, item in enumerate(armsPV_cl_list):
    mc.pointConstraint(armsPV_jntCtrl_list[pv], item, mo=False)

pvCl_master_grp = mc.group(armsPV_cl_list, n='armsPV_cl_grp')
mc.setAttr(pvCl_master_grp + '.v', 0)

armsPV_cGuides_list = ['arm_PV_l_lCrvCtrl', 'arm_PV_r_lCrvCtrl']
for cG in armsPV_cGuides_list:
    mc.setAttr(cG + '.overrideEnabled', 1)
    mc.setAttr(cG + '.overrideDisplayType', 2)

########################################################################################################
#
#                                      finger IK system setup
#
######################################################################################################

############################################################################################################################# finger's IK setup -> Finger 00
finger00_jnt_list = ['pinky_00_l_ik', 'ring_00_l_ik', 'middle_00_l_ik', 'index_00_l_ik', 'pinky_00_r_ik', 'ring_00_r_ik', 'middle_00_r_ik', 'index_00_r_ik']
for finger00 in finger00_jnt_list:
    myCtrl.bombomboom_ctrl(finger00)

finger00_ctrlMaster_list = ['pinky_00_l_ik_ctrlSpaceMaster', 'ring_00_l_ik_ctrlSpaceMaster', 'middle_00_l_ik_ctrlSpaceMaster', 'index_00_l_ik_ctrlSpaceMaster',
                            'pinky_00_r_ik_ctrlSpaceMaster', 'ring_00_r_ik_ctrlSpaceMaster', 'middle_00_r_ik_ctrlSpaceMaster', 'index_00_r_ik_ctrlSpaceMaster']

finger00_l_ctrlMaster_list = ['pinky_00_l_ik_ctrlSpaceMaster', 'ring_00_l_ik_ctrlSpaceMaster', 'middle_00_l_ik_ctrlSpaceMaster', 'index_00_l_ik_ctrlSpaceMaster']
finger00_r_trlMaster_list = ['pinky_00_r_ik_ctrlSpaceMaster', 'ring_00_r_ik_ctrlSpaceMaster', 'middle_00_r_ik_ctrlSpaceMaster', 'index_00_r_ik_ctrlSpaceMaster']

fi00_ctrlSpaceMaster_l_grp = mc.group(finger00_l_ctrlMaster_list, n='fingersIK_l_00_grp')
fi00_ctrlSpaceMaster_r_grp = mc.group(finger00_r_trlMaster_list, n='fingersIK_r_00_grp')

finger00_ctrl_list = ['pinky_00_l_ik_ctrl', 'ring_00_l_ik_ctrl', 'middle_00_l_ik_ctrl', 'index_00_l_ik_ctrl', 'pinky_00_r_ik_ctrl', 'ring_00_r_ik_ctrl', 'middle_00_r_ik_ctrl', 'index_00_r_ik_ctrl']

for l in finger00_ctrl_list:
    mc.setAttr(l + '.sx', l=True, k=False, ch=False)
    mc.setAttr(l + '.sy', l=True, k=False, ch=False)
    mc.setAttr(l + '.sz', l=True, k=False, ch=False)
    mc.setAttr(l + '.v', l=True, k=False, ch=False)
    mc.addAttr(l, ln='ikFK_switch', at='float', dv=0, min=0, max=1, k=True)

for f00, item in enumerate(finger00_ctrlMaster_list):
    mc.delete(mc.parentConstraint(finger00_jnt_list[f00], item, mo=False))

mc.select('ring_00_r_ik_ctrl.cv[0:7]', 'index_00_r_ik_ctrl.cv[0:7]', 'pinky_00_r_ik_ctrl.cv[0:7]', 'middle_00_r_ik_ctrl.cv[0:7]')
mc.rotate(-180, 0, 0, ocp=True)

for f00Connect, item in enumerate(finger00_jnt_list):
    mc.pointConstraint(finger00_ctrl_list[f00Connect], item, mo=True)
    mc.connectAttr(finger00_ctrl_list[f00Connect] + '.rx', item + '.rx')
    mc.connectAttr(finger00_ctrl_list[f00Connect] + '.ry', item + '.ry')
    mc.connectAttr(finger00_ctrl_list[f00Connect] + '.rz', item + '.rz')
    mc.connectAttr(finger00_ctrl_list[f00Connect] + '.sx', item + '.sx')
    mc.connectAttr(finger00_ctrl_list[f00Connect] + '.sy', item + '.sy')
    mc.connectAttr(finger00_ctrl_list[f00Connect] + '.sz', item + '.sz')
mc.select(d=True)

# delete right fingers to make mirror with correct pole vector on each left finger
mc.delete('pinky_01_r_ik', 'ring_01_r_ik', 'middle_01_r_ik', 'index_01_r_ik', 'thumb_01_r_ik')

# un parent left fingers to make mirror finger with correct pole vector position
mc.parent('pinky_01_l_ik', 'ring_01_l_ik', 'middle_01_l_ik', 'index_01_l_ik', 'thumb_01_l_ik', w=True), mc.select(d=True)

############################################################################################################ pinky l ik setup
mc.select('pinky_01_l_ik', 'pinky_02_l_ik', 'pinky_03_l_ik')
fingersPSel = mc.ls(sl=True)

fingPSel01_IK = mc.xform(fingersPSel[0], q=True, ws=True, t=True)
fingPSel02_IK = mc.xform(fingersPSel[1], q=True, ws=True, t=True)
fingPSel03_IK = mc.xform(fingersPSel[2], q=True, ws=True, t=True)

fingP01_IKV = OpenMaya.MVector(fingPSel01_IK[0], fingPSel01_IK[1], fingPSel01_IK[2])
fingP02_IKV = OpenMaya.MVector(fingPSel02_IK[0], fingPSel02_IK[1], fingPSel02_IK[2])
fingP03_IKV = OpenMaya.MVector(fingPSel03_IK[0], fingPSel03_IK[1], fingPSel03_IK[2])

startEndP = fingP03_IKV - fingP01_IKV
startMidP = fingP02_IKV - fingP01_IKV

dotPP = startMidP * startEndP
projP = float(dotPP) / float(startEndP.length())
startEndPN = startEndP.normal()
projPV = startEndPN * projP

arrowPV = startMidP - projPV
arrowPV *= 5
finalPV = arrowPV + fingP02_IKV

locP_PV = mc.spaceLocator(n='pinky_l_PV')
locP_PVSpace = mc.group(locP_PV, n='pinky_l_ik_locSpace'), mc.select(d=True)
mc.xform(locP_PVSpace, ws=True, t=(finalPV.x, finalPV.y, finalPV.z))
mc.parent(locP_PVSpace, 'pinky_02_l_ik')
mc.orientConstraint('pinky_02_l_ik', 'pinky_l_ik_locSpace', mo=False)

mc.mirrorJoint('pinky_01_l_ik', mirrorYZ=True, mirrorBehavior=True, searchReplace=('_l', '_r')), mc.rename('pinky_l_PV1', 'pinky_r_PV')
mc.parent('pinky_01_r_ik', 'pinky_00_r_ik'), mc.parent('pinky_01_l_ik', 'pinky_00_l_ik')
mc.orientConstraint('pinky_02_r_ik', 'pinky_l_ik_locSpace1', mo=False), mc.select(d=True)

######################################################################################################################### ring l ik setup
mc.select('ring_01_l_ik', 'ring_02_l_ik', 'ring_03_l_ik')
fingersRSel = mc.ls(sl=True)

fingRSel01_IK = mc.xform(fingersRSel[0], q=True, ws=True, t=True)
fingRSel02_IK = mc.xform(fingersRSel[1], q=True, ws=True, t=True)
fingRSel03_IK = mc.xform(fingersRSel[2], q=True, ws=True, t=True)

fingR01_IKV = OpenMaya.MVector(fingRSel01_IK[0], fingRSel01_IK[1], fingRSel01_IK[2])
fingR02_IKV = OpenMaya.MVector(fingRSel02_IK[0], fingRSel02_IK[1], fingRSel02_IK[2])
fingR03_IKV = OpenMaya.MVector(fingRSel03_IK[0], fingRSel03_IK[1], fingRSel03_IK[2])

startEndR = fingR03_IKV - fingR01_IKV
startMidR = fingR02_IKV - fingR01_IKV

dotRR = startMidR * startEndR
projR = float(dotRR) / float(startEndR.length())
startEndRN = startEndR.normal()
projRV = startEndRN * projR

arrowRV = startMidR - projRV
arrowRV *= 4
finalRV = arrowRV + fingR02_IKV

locR_PV = mc.spaceLocator(n='ring_l_PV')
locR_PVSpace = mc.group(locR_PV, n='ring_l_ik_locSpace'), mc.select(d=True)
mc.xform(locR_PVSpace, ws=True, t=(finalRV.x, finalRV.y, finalRV.z))
mc.parent(locR_PVSpace, 'ring_02_l_ik')
mc.orientConstraint('ring_02_l_ik', 'ring_l_ik_locSpace', mo=False)

mc.mirrorJoint('ring_01_l_ik', mirrorYZ=True, mirrorBehavior=True, searchReplace=('_l', '_r')), mc.rename('ring_l_PV1', 'ring_r_PV')
mc.parent('ring_01_r_ik', 'ring_00_r_ik'), mc.parent('ring_01_l_ik', 'ring_00_l_ik')
mc.orientConstraint('ring_02_r_ik', 'ring_l_ik_locSpace1', mo=False), mc.select(d=True)

########################################################################################################################### middle l ik setup
mc.select('middle_01_l_ik', 'middle_02_l_ik', 'middle_03_l_ik')
fingersMSel = mc.ls(sl=True)

fingMSel01_IK = mc.xform(fingersMSel[0], q=True, ws=True, t=True)
fingMSel02_IK = mc.xform(fingersMSel[1], q=True, ws=True, t=True)
fingMSel03_IK = mc.xform(fingersMSel[2], q=True, ws=True, t=True)

fingM01_IKV = OpenMaya.MVector(fingMSel01_IK[0], fingMSel01_IK[1], fingMSel01_IK[2])
fingM02_IKV = OpenMaya.MVector(fingMSel02_IK[0], fingMSel02_IK[1], fingMSel02_IK[2])
fingM03_IKV = OpenMaya.MVector(fingMSel03_IK[0], fingMSel03_IK[1], fingMSel03_IK[2])

startEndM = fingM03_IKV - fingM01_IKV
startMidM = fingM02_IKV - fingM01_IKV

dotMP = startMidM * startEndM
projM = float(dotMP) / float(startEndM.length())
startEndMN = startEndM.normal()
projMV = startEndMN * projM

arrowMV = startMidM - projMV
arrowMV *= 4
finalMV = arrowMV + fingM02_IKV

locM_PV = mc.spaceLocator(n='middle_l_PV')
locM_PVSpace = mc.group(locM_PV, n='middle_l_ik_locSpace'), mc.select(d=True)
mc.xform(locM_PVSpace, ws=True, t=(finalMV.x, finalMV.y, finalMV.z))
mc.parent(locM_PVSpace, 'middle_02_l_ik')
mc.orientConstraint('middle_02_l_ik', 'middle_l_ik_locSpace', mo=False)

mc.mirrorJoint('middle_01_l_ik', mirrorYZ=True, mirrorBehavior=True, searchReplace=('_l', '_r')), mc.rename('middle_l_PV1', 'middle_r_PV')
mc.parent('middle_01_r_ik', 'middle_00_r_ik'), mc.parent('middle_01_l_ik', 'middle_00_l_ik')
mc.orientConstraint('middle_02_r_ik', 'middle_l_ik_locSpace1', mo=False), mc.select(d=True)

####################################################################################################################### index l ik setup
mc.select('index_01_l_ik', 'index_02_l_ik', 'index_03_l_ik')
fingersISel = mc.ls(sl=True)

fingISel01_IK = mc.xform(fingersISel[0], q=True, ws=True, t=True)
fingISel02_IK = mc.xform(fingersISel[1], q=True, ws=True, t=True)
fingISel03_IK = mc.xform(fingersISel[2], q=True, ws=True, t=True)

fingI01_IKV = OpenMaya.MVector(fingISel01_IK[0], fingISel01_IK[1], fingISel01_IK[2])
fingI02_IKV = OpenMaya.MVector(fingISel02_IK[0], fingISel02_IK[1], fingISel02_IK[2])
fingI03_IKV = OpenMaya.MVector(fingISel03_IK[0], fingISel03_IK[1], fingISel03_IK[2])

startEndI = fingI03_IKV - fingI01_IKV
startMidI = fingI02_IKV - fingI01_IKV

dotIP = startMidI * startEndI
projI = float(dotIP) / float(startEndI.length())
startEndIN = startEndI.normal()
projIV = startEndIN * projI

arrowIV = startMidI - projIV
arrowIV *= 8
finalIV = arrowIV + fingI02_IKV

locI_PV = mc.spaceLocator(n='index_l_PV')
locI_PVSpace = mc.group(locI_PV, n='index_l_ik_locSpace'), mc.select(d=True)
mc.xform(locI_PVSpace, ws=True, t=(finalIV.x, finalIV.y, finalIV.z))
mc.parent(locI_PVSpace, 'index_02_l_ik')
mc.orientConstraint('index_02_l_ik', 'index_l_ik_locSpace', mo=False)

mc.mirrorJoint('index_01_l_ik', mirrorYZ=True, mirrorBehavior=True, searchReplace=('_l', '_r')), mc.rename('index_l_PV1', 'index_r_PV')
mc.parent('index_01_r_ik', 'index_00_r_ik'), mc.parent('index_01_l_ik', 'index_00_l_ik')
mc.orientConstraint('index_02_r_ik', 'index_l_ik_locSpace1', mo=False), mc.select(d=True)

#################################################################################################################### thumb l ik setup
mc.select('thumb_01_l_ik', 'thumb_02_l_ik', 'thumb_03_l_ik')
fingersTSel = mc.ls(sl=True)

fingTSel01_IK = mc.xform(fingersTSel[0], q=True, ws=True, t=True)
fingTSel02_IK = mc.xform(fingersTSel[1], q=True, ws=True, t=True)
fingTSel03_IK = mc.xform(fingersTSel[2], q=True, ws=True, t=True)

fingT01_IKV = OpenMaya.MVector(fingTSel01_IK[0], fingTSel01_IK[1], fingTSel01_IK[2])
fingT02_IKV = OpenMaya.MVector(fingTSel02_IK[0], fingTSel02_IK[1], fingTSel02_IK[2])
fingT03_IKV = OpenMaya.MVector(fingTSel03_IK[0], fingTSel03_IK[1], fingTSel03_IK[2])

startEndT = fingT03_IKV - fingT01_IKV
startMidT = fingT02_IKV - fingT01_IKV

dotTP = startMidT * startEndT
projT = float(dotTP) / float(startEndT.length())
startEndTN = startEndT.normal()
projTV = startEndTN * projT

arrowTV = startMidT - projTV
arrowTV *= 8
finalTV = arrowTV + fingT02_IKV

locT_PV = mc.spaceLocator(n='thumb_l_PV')
locT_PVSpace = mc.group(locT_PV, n='thumb_l_ik_locSpace'), mc.select(d=True)
mc.xform(locT_PVSpace, ws=True, t=(finalTV.x, finalTV.y, finalTV.z))
mc.parent(locT_PVSpace, 'thumb_02_l_ik')
mc.orientConstraint('thumb_02_l_ik', 'thumb_l_ik_locSpace', mo=False)

mc.mirrorJoint('thumb_01_l_ik', mirrorYZ=True, mirrorBehavior=True, searchReplace=('_l', '_r')), mc.rename('thumb_l_PV1', 'thumb_r_PV')
mc.parent('thumb_01_r_ik', 'hand_r_ik'), mc.parent('thumb_01_l_ik', 'hand_l_ik')
mc.orientConstraint('thumb_02_r_ik', 'thumb_l_ik_locSpace1', mo=False), mc.select(d=True)

################################################################################################# fingers IK handle setup - Left side

ikPinky_l = mc.ikHandle(n='pinky_l_ik', sj='pinky_01_l_ik', ee='pinky_03_l_ik', sol='ikRPsolver')
ikRing_l = mc.ikHandle(n='ring_l_ik', sj='ring_01_l_ik', ee='ring_03_l_ik', sol='ikRPsolver')
ikMiddle_l = mc.ikHandle(n='middle_l_ik', sj='middle_01_l_ik', ee='middle_03_l_ik', sol='ikRPsolver')
ikIndex_l = mc.ikHandle(n='index_l_ik', sj='index_01_l_ik', ee='index_03_l_ik', sol='ikRPsolver')
ikThumb_l = mc.ikHandle(n='thumb_l_ik', sj='thumb_01_l_ik', ee='thumb_03_l_ik', sol='ikRPsolver')

######################################################################################################## fingers IK handle setup - Right side

ikPinky_r = mc.ikHandle(n='pinky_r_ik', sj='pinky_01_r_ik', ee='pinky_03_r_ik', sol='ikRPsolver')
ikRing_r = mc.ikHandle(n='ring_r_ik', sj='ring_01_r_ik', ee='ring_03_r_ik', sol='ikRPsolver')
ikMiddle_r = mc.ikHandle(n='middle_r_ik', sj='middle_01_r_ik', ee='middle_03_r_ik', sol='ikRPsolver')
ikIndex_r = mc.ikHandle(n='index_r_ik', sj='index_01_r_ik', ee='index_03_r_ik', sol='ikRPsolver')
ikThumb_r = mc.ikHandle(n='thumb_r_ik', sj='thumb_01_r_ik', ee='thumb_03_r_ik', sol='ikRPsolver')

mc.select(d=True)

############################################################################################################## finger IK controls
finger03_jnt_ik_list = ['pinky_03_l_ik', 'ring_03_l_ik', 'middle_03_l_ik', 'index_03_l_ik', 'thumb_03_l_ik', 'pinky_03_r_ik', 'ring_03_r_ik', 'middle_03_r_ik', 'index_03_r_ik', 'thumb_03_r_ik']
for f03 in finger03_jnt_ik_list:
    myCtrl.diamondMid_ctrl(f03)

############################################### rename ik finger control
mc.rename('pinky_03_l_ik_ctrl', 'pinky_l_ik_ctrl'), mc.rename('ring_03_l_ik_ctrl', 'ring_l_ik_ctrl'), mc.rename('middle_03_l_ik_ctrl', 'middle_l_ik_ctrl')
mc.rename('index_03_l_ik_ctrl', 'index_l_ik_ctrl'), mc.rename('thumb_03_l_ik_ctrl', 'thumb_l_ik_ctrl')
mc.rename('pinky_03_r_ik_ctrl', 'pinky_r_ik_ctrl'), mc.rename('ring_03_r_ik_ctrl', 'ring_r_ik_ctrl'), mc.rename('middle_03_r_ik_ctrl', 'middle_r_ik_ctrl')
mc.rename('index_03_r_ik_ctrl', 'index_r_ik_ctrl'), mc.rename('thumb_03_r_ik_ctrl', 'thumb_r_ik_ctrl')

mc.rename('pinky_03_l_ik_ctrlSpace', 'pinky_l_ik_ctrlSpace'), mc.rename('ring_03_l_ik_ctrlSpace', 'ring_l_ik_ctrlSpace'), mc.rename('middle_03_l_ik_ctrlSpace', 'middle_l_ik_ctrlSpace')
mc.rename('index_03_l_ik_ctrlSpace', 'index_l_ik_ctrlSpace'), mc.rename('thumb_03_l_ik_ctrlSpace', 'thumb_l_ik_ctrlSpace')
mc.rename('pinky_03_r_ik_ctrlSpace', 'pinky_r_ik_ctrlSpace'), mc.rename('ring_03_r_ik_ctrlSpace', 'ring_r_ik_ctrlSpace'), mc.rename('middle_03_r_ik_ctrlSpace', 'middle_r_ik_ctrlSpace')
mc.rename('index_03_r_ik_ctrlSpace', 'index_r_ik_ctrlSpace'), mc.rename('thumb_03_r_ik_ctrlSpace', 'thumb_r_ik_ctrlSpace')

mc.rename('pinky_03_l_ik_ctrlSpaceMaster', 'pinky_l_ik_ctrlSpaceMaster'), mc.rename('ring_03_l_ik_ctrlSpaceMaster', 'ring_l_ik_ctrlSpaceMaster')
mc.rename('middle_03_l_ik_ctrlSpaceMaster', 'middle_l_ik_ctrlSpaceMaster'), mc.rename('index_03_l_ik_ctrlSpaceMaster', 'index_l_ik_ctrlSpaceMaster')
mc.rename('thumb_03_l_ik_ctrlSpaceMaster', 'thumb_l_ik_ctrlSpaceMaster'), mc.rename('pinky_03_r_ik_ctrlSpaceMaster', 'pinky_r_ik_ctrlSpaceMaster')
mc.rename('ring_03_r_ik_ctrlSpaceMaster', 'ring_r_ik_ctrlSpaceMaster'), mc.rename('middle_03_r_ik_ctrlSpaceMaster', 'middle_r_ik_ctrlSpaceMaster')
mc.rename('index_03_r_ik_ctrlSpaceMaster', 'index_r_ik_ctrlSpaceMaster'), mc.rename('thumb_03_r_ik_ctrlSpaceMaster', 'thumb_r_ik_ctrlSpaceMaster')

fik_ctrlMaster_list = ['pinky_l_ik_ctrlSpaceMaster', 'ring_l_ik_ctrlSpaceMaster', 'middle_l_ik_ctrlSpaceMaster', 'index_l_ik_ctrlSpaceMaster', 'thumb_l_ik_ctrlSpaceMaster',
                       'pinky_r_ik_ctrlSpaceMaster', 'ring_r_ik_ctrlSpaceMaster', 'middle_r_ik_ctrlSpaceMaster', 'index_r_ik_ctrlSpaceMaster', 'thumb_r_ik_ctrlSpaceMaster']

fik_l_ctrlMaster_list = ['pinky_l_ik_ctrlSpaceMaster', 'ring_l_ik_ctrlSpaceMaster', 'middle_l_ik_ctrlSpaceMaster', 'index_l_ik_ctrlSpaceMaster', 'thumb_l_ik_ctrlSpaceMaster']
fik_r_ctrlMaster_list = ['pinky_r_ik_ctrlSpaceMaster', 'ring_r_ik_ctrlSpaceMaster', 'middle_r_ik_ctrlSpaceMaster', 'index_r_ik_ctrlSpaceMaster', 'thumb_r_ik_ctrlSpaceMaster']

fik_l_ctrlSpaceMaster_grp = mc.group(fik_l_ctrlMaster_list, n='fingersIK_l_grp')
fik_r_ctrlSpaceMaster_grp = mc.group(fik_r_ctrlMaster_list, n='fingersIK_r_grp')
mc.select(d=True)

for f03Pos, item in enumerate(fik_ctrlMaster_list):
    mc.delete(mc.parentConstraint(finger03_jnt_ik_list[f03Pos], item, mo=False))

fingerPV_list = ['pinky_l_PV', 'ring_l_PV', 'middle_l_PV', 'index_l_PV', 'thumb_l_PV', 'pinky_r_PV', 'ring_r_PV', 'middle_r_PV', 'index_r_PV', 'thumb_r_PV']
for finPV in fingerPV_list:
    myCtrl.lineCross_ctrl(finPV)

finger_PV_ctrlSpaceMaster_list = ['pinky_l_PV_ctrlSpaceMaster', 'ring_l_PV_ctrlSpaceMaster', 'middle_l_PV_ctrlSpaceMaster', 'index_l_PV_ctrlSpaceMaster', 'thumb_l_PV_ctrlSpaceMaster',
                                  'pinky_r_PV_ctrlSpaceMaster', 'ring_r_PV_ctrlSpaceMaster', 'middle_r_PV_ctrlSpaceMaster', 'index_r_PV_ctrlSpaceMaster', 'thumb_r_PV_ctrlSpaceMaster']

finger_PV_loc_list = ['pinky_l_PV', 'ring_l_PV', 'middle_l_PV', 'index_l_PV', 'thumb_l_PV', 'pinky_r_PV', 'ring_r_PV', 'middle_r_PV', 'index_r_PV', 'thumb_r_PV']

for i, item in enumerate(finger_PV_loc_list):
    mc.delete(mc.parentConstraint(item, finger_PV_ctrlSpaceMaster_list[i]))
mc.select(d=True)

######################################################################################################### fingers setup - Point / PV / Orient - Constraint
fingersIK_ctrl_list = ['pinky_l_ik_ctrl', 'ring_l_ik_ctrl', 'middle_l_ik_ctrl', 'index_l_ik_ctrl', 'thumb_l_ik_ctrl', 'pinky_r_ik_ctrl', 'ring_r_ik_ctrl',
                       'middle_r_ik_ctrl', 'index_r_ik_ctrl', 'thumb_r_ik_ctrl']

fingersIK_handles_list = ['pinky_l_ik', 'ring_l_ik', 'middle_l_ik', 'index_l_ik', 'thumb_l_ik', 'pinky_r_ik', 'ring_r_ik', 'middle_r_ik', 'index_r_ik', 'thumb_r_ik']

fingersIK_PV_ctrl_list = ['pinky_l_PV_ctrl', 'ring_l_PV_ctrl', 'middle_l_PV_ctrl', 'index_l_PV_ctrl', 'thumb_l_PV_ctrl', 'pinky_r_PV_ctrl', 'ring_r_PV_ctrl', 'middle_r_PV_ctrl',
                          'index_r_PV_ctrl', 'thumb_r_PV_ctrl']

for fIKH, item in enumerate(fingersIK_handles_list):
    mc.pointConstraint(fingersIK_ctrl_list[fIKH], item, mo=True)

for fIKPV, item in enumerate(fingersIK_handles_list):
    mc.poleVectorConstraint(fingersIK_PV_ctrl_list[fIKPV], item)

for fIKoConst, item in enumerate(finger03_jnt_ik_list):
    mc.orientConstraint(fingersIK_ctrl_list[fIKoConst], item, mo=True)

#################################################################################################################### fingers ik cv scale
mc.select('pinky_l_ik_ctrl.cv[0:20]', 'ring_l_ik_ctrl.cv[0:20]', 'middle_l_ik_ctrl.cv[0:20]', 'index_l_ik_ctrl.cv[0:20]', 'thumb_l_ik_ctrl.cv[0:20]', 'pinky_r_ik_ctrl.cv[0:20]',
          'ring_r_ik_ctrl.cv[0:20]', 'middle_r_ik_ctrl.cv[0:20]', 'index_r_ik_ctrl.cv[0:20]', 'thumb_r_ik_ctrl.cv[0:20]')
mc.scale(0.25, 0.25, 0.25, ocp=True), mc.select(d=True)

mc.select('pinky_l_PV_ctrl.cv[0:7]', 'ring_l_PV_ctrl.cv[0:7]', 'middle_l_PV_ctrl.cv[0:7]', 'index_l_PV_ctrl.cv[0:7]', 'thumb_l_PV_ctrl.cv[0:7]', 'pinky_r_PV_ctrl.cv[0:7]', 'ring_r_PV_ctrl.cv[0:7]',
          'middle_r_PV_ctrl.cv[0:7]', 'index_r_PV_ctrl.cv[0:7]', 'thumb_r_PV_ctrl.cv[0:7]')
mc.scale(0.156885, 0.156885, 0.156885, ocp=True), mc.select(d=True)

############################################################################################################ Delete locFinker PV pos reference
mc.delete(locP_PVSpace, locI_PVSpace, locT_PVSpace, locR_PVSpace, locM_PVSpace, 'pinky_l_ik_locSpace1', 'ring_l_ik_locSpace1', 'middle_l_ik_locSpace1', 'index_l_ik_locSpace1', 'thumb_l_ik_locSpace1')

#################################################################################################################### finger IK lock attrs
for finIK_ctrl in fingersIK_ctrl_list:
    mc.setAttr(finIK_ctrl + '.sx', l=True, k=False, ch=False)
    mc.setAttr(finIK_ctrl + '.sy', l=True, k=False, ch=False)
    mc.setAttr(finIK_ctrl + '.sz', l=True, k=False, ch=False)
    mc.setAttr(finIK_ctrl + '.v', l=True, k=False, ch=False)
    mc.addAttr(finIK_ctrl, ln='followPhalange', at='float', dv=0, min=0, max=1, k=True)

for finIK_PV_ctrl in fingersIK_PV_ctrl_list:
    mc.setAttr(finIK_PV_ctrl + '.rx', l=True, k=False, ch=False)
    mc.setAttr(finIK_PV_ctrl + '.ry', l=True, k=False, ch=False)
    mc.setAttr(finIK_PV_ctrl + '.rz', l=True, k=False, ch=False)
    mc.setAttr(finIK_PV_ctrl + '.sx', l=True, k=False, ch=False)
    mc.setAttr(finIK_PV_ctrl + '.sy', l=True, k=False, ch=False)
    mc.setAttr(finIK_PV_ctrl + '.sz', l=True, k=False, ch=False)
    mc.setAttr(finIK_PV_ctrl + '.v', l=True, k=False, ch=False)

############################################################################################################ Fingers curve guides referenced
for n in fingersIK_handles_list:
    myCtrl.lineCrv_ctrl(n)

fiLCrvGuide_spaceMaster_list = ['pinky_l_ik_lCrvCtrlSpaceMaster', 'ring_l_ik_lCrvCtrlSpaceMaster', 'middle_l_ik_lCrvCtrlSpaceMaster', 'index_l_ik_lCrvCtrlSpaceMaster',
                                'thumb_l_ik_lCrvCtrlSpaceMaster', 'pinky_r_ik_lCrvCtrlSpaceMaster', 'ring_r_ik_lCrvCtrlSpaceMaster', 'middle_r_ik_lCrvCtrlSpaceMaster',
                                'index_r_ik_lCrvCtrlSpaceMaster', 'thumb_r_ik_lCrvCtrlSpaceMaster']
fiLCrv_master_grp = mc.group(fiLCrvGuide_spaceMaster_list,'arm_PV_r_lCrvCtrlSpaceMaster', 'arm_PV_l_lCrvCtrlSpaceMaster', n='fingersIK_curveGuide_grp')

flCrvGuide_list = ['pinky_l_ik_lCrvCtrl.cv[0]', 'pinky_l_ik_lCrvCtrl.cv[1]', 'ring_l_ik_lCrvCtrl.cv[0]', 'ring_l_ik_lCrvCtrl.cv[1]', 'middle_l_ik_lCrvCtrl.cv[0]', 'middle_l_ik_lCrvCtrl.cv[1]',
                   'index_l_ik_lCrvCtrl.cv[0]', 'index_l_ik_lCrvCtrl.cv[1]', 'thumb_l_ik_lCrvCtrl.cv[0]', 'thumb_l_ik_lCrvCtrl.cv[1]', 'pinky_r_ik_lCrvCtrl.cv[0]', 'pinky_r_ik_lCrvCtrl.cv[1]',
                   'ring_r_ik_lCrvCtrl.cv[0]', 'ring_r_ik_lCrvCtrl.cv[1]', 'middle_r_ik_lCrvCtrl.cv[0]', 'middle_r_ik_lCrvCtrl.cv[1]', 'index_r_ik_lCrvCtrl.cv[0]', 'index_r_ik_lCrvCtrl.cv[1]',
                   'thumb_r_ik_lCrvCtrl.cv[0]', 'thumb_r_ik_lCrvCtrl.cv[1]']

for fIkCl, item in enumerate(flCrvGuide_list):
    mc.cluster(flCrvGuide_list[fIkCl], item, rel=True)

mc.rename('cluster1Handle', 'pinky_l_01_cl'), mc.rename('cluster2Handle', 'pinky_l_02_cl'), mc.rename('cluster3Handle', 'ring_l_01_cl'), mc.rename('cluster4Handle', 'ring_l_02_cl')
mc.rename('cluster5Handle', 'middle_l_01_cl'), mc.rename('cluster6Handle', 'middle_l_02_cl'), mc.rename('cluster7Handle', 'index_l_01_cl'), mc.rename('cluster8Handle', 'index_l_02_cl')
mc.rename('cluster9Handle', 'thumb_l_01_cl'), mc.rename('cluster10Handle', 'thumb_l_02_cl')

mc.rename('cluster11Handle', 'pinky_r_01_cl'), mc.rename('cluster12Handle', 'pinky_r_02_cl'), mc.rename('cluster13Handle', 'ring_r_01_cl'), mc.rename('cluster14Handle', 'ring_r_02_cl')
mc.rename('cluster15Handle', 'middle_r_01_cl'), mc.rename('cluster16Handle', 'middle_r_02_cl'), mc.rename('cluster17Handle', 'index_r_01_cl'), mc.rename('cluster18Handle', 'index_r_02_cl')
mc.rename('cluster19Handle', 'thumb_r_01_cl'), mc.rename('cluster20Handle', 'thumb_r_02_cl')

fCl01_list = ['pinky_l_01_cl', 'ring_l_01_cl', 'middle_l_01_cl', 'index_l_01_cl', 'thumb_l_01_cl', 'pinky_r_01_cl', 'ring_r_01_cl', 'middle_r_01_cl', 'index_r_01_cl', 'thumb_r_01_cl']
for fCl01, item in enumerate(fCl01_list):
    mc.pointConstraint(fingersIK_PV_ctrl_list[fCl01], item, mo=False)

fCl02_list = ['pinky_l_02_cl', 'ring_l_02_cl', 'middle_l_02_cl', 'index_l_02_cl', 'thumb_l_02_cl', 'pinky_r_02_cl', 'ring_r_02_cl', 'middle_r_02_cl', 'index_r_02_cl', 'thumb_r_02_cl']
fIk02_jnt_list = ['pinky_02_l_ik', 'ring_02_l_ik', 'middle_02_l_ik', 'index_02_l_ik', 'thumb_02_l_ik', 'pinky_02_r_ik', 'ring_02_r_ik', 'middle_02_r_ik', 'index_02_r_ik', 'thumb_02_r_ik']
for fCl02, item in enumerate(fCl02_list):
    mc.pointConstraint(fIk02_jnt_list[fCl02], item, mo=False)
mc.select(d=True)

fCluster_master_grp = mc.group(fCl01_list, fCl02_list, n='fingersIK_cl_grp')
mc.setAttr(fCluster_master_grp + '.v', 0)

fiLCrvGuide_list = ['pinky_l_ik_lCrvCtrl', 'ring_l_ik_lCrvCtrl', 'middle_l_ik_lCrvCtrl', 'index_l_ik_lCrvCtrl', 'thumb_l_ik_lCrvCtrl', 'pinky_r_ik_lCrvCtrl',
                   'ring_r_ik_lCrvCtrl', 'middle_r_ik_lCrvCtrl', 'index_r_ik_lCrvCtrl', 'thumb_r_ik_lCrvCtrl']
for fiRef in fiLCrvGuide_list:
    mc.setAttr(fiRef + '.overrideEnabled', 1)
    mc.setAttr(fiRef + '.overrideDisplayType', 2)

######################################################################################################### parent fingers PV top fingers ik controls
for fIkParent, item in enumerate(fingersIK_ctrl_list):
    mc.parent(finger_PV_ctrlSpaceMaster_list[fIkParent], item)

iks_master_grp = mc.group(fingersIK_handles_list, 'ikArm_l', 'ikArm_r', n='armsFingers_ikHandle_grp')
mc.setAttr(iks_master_grp + '.v', 0)

############################################################################################################ follow phalange setup

fIk_02_ctrlSpaceMaster_list = ['pinky_l_ik_ctrlSpaceMaster', 'ring_l_ik_ctrlSpaceMaster', 'middle_l_ik_ctrlSpaceMaster', 'index_l_ik_ctrlSpaceMaster',
                               'pinky_r_ik_ctrlSpaceMaster', 'ring_r_ik_ctrlSpaceMaster', 'middle_r_ik_ctrlSpaceMaster', 'index_r_ik_ctrlSpaceMaster']

for f00Cons, item in enumerate(fIk_02_ctrlSpaceMaster_list):
    mc.parentConstraint(finger00_ctrl_list[f00Cons], item, mo=True)

fik_phalangeConst_list = ['pinky_l_ik_ctrlSpaceMaster_parentConstraint1.pinky_00_l_ik_ctrlW0', 'ring_l_ik_ctrlSpaceMaster_parentConstraint1.ring_00_l_ik_ctrlW0',
                          'middle_l_ik_ctrlSpaceMaster_parentConstraint1.middle_00_l_ik_ctrlW0', 'index_l_ik_ctrlSpaceMaster_parentConstraint1.index_00_l_ik_ctrlW0',
                          'pinky_r_ik_ctrlSpaceMaster_parentConstraint1.pinky_00_r_ik_ctrlW0', 'ring_r_ik_ctrlSpaceMaster_parentConstraint1.ring_00_r_ik_ctrlW0',
                          'middle_r_ik_ctrlSpaceMaster_parentConstraint1.middle_00_r_ik_ctrlW0', 'index_r_ik_ctrlSpaceMaster_parentConstraint1.index_00_r_ik_ctrlW0']

fIk_02_ctrl_list = ['pinky_l_ik_ctrl', 'ring_l_ik_ctrl', 'middle_l_ik_ctrl', 'index_l_ik_ctrl', 'pinky_r_ik_ctrl',  'ring_r_ik_ctrl', 'middle_r_ik_ctrl', 'index_r_ik_ctrl']
for c, item in enumerate(fik_phalangeConst_list):
    mc.connectAttr(fIk_02_ctrl_list[c] + '.followPhalange', item)

############################################################################################################# parent fingers control to gimbal control / color and cleanup
mc.parent(fi00_ctrlSpaceMaster_l_grp, fik_l_ctrlSpaceMaster_grp, 'hand_l_ik_gimbal_ctrl')
mc.parent(fi00_ctrlSpaceMaster_r_grp, fik_r_ctrlSpaceMaster_grp, 'hand_r_ik_gimbal_ctrl')
arm_leftSide_master_grp = mc.group('hand_l_ik_ctrlSpaceMaster', 'arm_PV_l_ctrlSpaceMaster', n='arm_l_master_grp')
arm_rightSide_master_grp = mc.group('hand_r_ik_ctrlSpaceMaster', 'arm_PV_r_ctrlSpaceMaster', n='arm_r_master_grp')
arm_ik_master_grp = mc.group(arm_leftSide_master_grp, arm_rightSide_master_grp, fiLCrv_master_grp, iks_master_grp, fCluster_master_grp, pvCl_master_grp, n='arm_IK_master_grp')

itemColor(arm_leftSide_master_grp, 6)
itemColor(arm_rightSide_master_grp, 13)
mc.select(d=True)

print(' ---> ik system completed <--- ')
#################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################
#
#                                                            ARM -> IK / FK SYSTEM
#
##################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################

################################################################################################################################ switch control
myCtrl.gear_ctrl(name='ik_fk_switch_l_arm')
myCtrl.gear_ctrl(name='ik_fk_switch_r_arm')

ikFK_ctrl_list = ['ik_fk_switch_l_arm_ctrl', 'ik_fk_switch_r_arm_ctrl']
for i in ikFK_ctrl_list:
    mc.setAttr(i + '.tx', l=True, k=False, ch=False)
    mc.setAttr(i + '.ty', l=True, k=False, ch=False)
    mc.setAttr(i + '.tz', l=True, k=False, ch=False)
    mc.setAttr(i + '.rx', l=True, k=False, ch=False)
    mc.setAttr(i + '.ry', l=True, k=False, ch=False)
    mc.setAttr(i + '.rz', l=True, k=False, ch=False)
    mc.setAttr(i + '.sx', l=True, k=False, ch=False)
    mc.setAttr(i + '.sy', l=True, k=False, ch=False)
    mc.setAttr(i + '.sz', l=True, k=False, ch=False)
    mc.setAttr(i + '.v', l=True, k=False, ch=False)
    mc.addAttr(i, ln='switch', at='float', dv=0, min=0, max=1, k=True)

mc.delete(mc.parentConstraint('hand_l', 'ik_fk_switch_l_arm_ctrlSpaceMaster'))
mc.select('ik_fk_switch_l_arm_ctrlSpace'), mc.move(0, 25, 0, r=True, os=True, wd=True)

mc.delete(mc.parentConstraint('hand_r', 'ik_fk_switch_r_arm_ctrlSpaceMaster'))
mc.select('ik_fk_switch_r_arm_ctrlSpace'), mc.move(0, -25, 0, r=True, os=True, wd=True)

mc.select('ik_fk_switch_r_arm_ctrl.cv[0:24]', 'ik_fk_switch_l_arm_ctrl.cv[0:24]'), mc.scale(0.5, 0.5, 0.5, ocp=True)

mc.parentConstraint('hand_l', 'ik_fk_switch_l_arm_ctrlSpaceMaster', mo=True), mc.parentConstraint('hand_r', 'ik_fk_switch_r_arm_ctrlSpaceMaster', mo=True)

print('-> ikFk switch complete <-')

########################################################################################################################################### ik fk switch blend color setup -> arm left side

bindArm_l_jnt_list = ['upperarm_l', 'lowerarm_l', 'hand_l']

IKArm_l_jnt_list = ['upperarm_l_ik', 'lowerarm_l_ik', 'hand_l_ik']

FKArm_l_jnt_list = ['upperarm_l_fk', 'lowerarm_l_fk', 'hand_l_fk']

trans_arm_l_bColorNode_list = []
rot_arm_l_bColorNode_List = []
scl_arm_l_bColorNode_List = []

for bA_arm_l_bColoNode in bindArm_l_jnt_list:
    bC_arm_l_transNode = mc.createNode('blendColors', n=bA_arm_l_bColoNode + '_switch_trans_bColor')
    bC_arm_l_rotNode = mc.createNode('blendColors', n=bA_arm_l_bColoNode + '_switch_rot_bColor')
    bC_arm_l_scaleNode = mc.createNode('blendColors', n=bA_arm_l_bColoNode + '_switch_scale_bColor')
    mc.connectAttr('ik_fk_switch_l_arm_ctrl.switch', bC_arm_l_transNode + '.blender')
    mc.connectAttr('ik_fk_switch_l_arm_ctrl.switch', bC_arm_l_rotNode + '.blender')
    mc.connectAttr('ik_fk_switch_l_arm_ctrl.switch', bC_arm_l_scaleNode + '.blender')

    trans_arm_l_bColorNode_list.append(bC_arm_l_transNode)
    rot_arm_l_bColorNode_List.append(bC_arm_l_rotNode)
    scl_arm_l_bColorNode_List.append(bC_arm_l_scaleNode)

################################ connect translate attr to blendColor translate -> ikFk switch

for bC_arm_l_transInput in range(len(IKArm_l_jnt_list)):
    mc.connectAttr(IKArm_l_jnt_list[bC_arm_l_transInput] + '.tx', trans_arm_l_bColorNode_list[bC_arm_l_transInput] + '.color2.color2R')
    mc.connectAttr(IKArm_l_jnt_list[bC_arm_l_transInput] + '.ty', trans_arm_l_bColorNode_list[bC_arm_l_transInput] + '.color2.color2G')
    mc.connectAttr(IKArm_l_jnt_list[bC_arm_l_transInput] + '.tz', trans_arm_l_bColorNode_list[bC_arm_l_transInput] + '.color2.color2B')

for bC_arm_l_transOutput in range(len(bindArm_l_jnt_list)):
    mc.connectAttr(trans_arm_l_bColorNode_list[bC_arm_l_transOutput] + '.output.outputR', bindArm_l_jnt_list[bC_arm_l_transOutput] + '.tx')
    mc.connectAttr(trans_arm_l_bColorNode_list[bC_arm_l_transOutput] + '.output.outputG', bindArm_l_jnt_list[bC_arm_l_transOutput] + '.ty')
    mc.connectAttr(trans_arm_l_bColorNode_list[bC_arm_l_transOutput] + '.output.outputB', bindArm_l_jnt_list[bC_arm_l_transOutput] + '.tz')

for bC_arm_l_transInput in range(len(FKArm_l_jnt_list)):
    mc.connectAttr(FKArm_l_jnt_list[bC_arm_l_transInput] + '.tx', trans_arm_l_bColorNode_list[bC_arm_l_transInput] + '.color1.color1R')
    mc.connectAttr(FKArm_l_jnt_list[bC_arm_l_transInput] + '.ty', trans_arm_l_bColorNode_list[bC_arm_l_transInput] + '.color1.color1G')
    mc.connectAttr(FKArm_l_jnt_list[bC_arm_l_transInput] + '.tz', trans_arm_l_bColorNode_list[bC_arm_l_transInput] + '.color1.color1B')

################################ connect rotate attr to blendColor rotate -> ikFk switch

for bC_arm_l_rotInput in range(len(IKArm_l_jnt_list)):
    mc.connectAttr(IKArm_l_jnt_list[bC_arm_l_rotInput] + '.rx', rot_arm_l_bColorNode_List[bC_arm_l_rotInput] + '.color2.color2R')
    mc.connectAttr(IKArm_l_jnt_list[bC_arm_l_rotInput] + '.ry', rot_arm_l_bColorNode_List[bC_arm_l_rotInput] + '.color2.color2G')
    mc.connectAttr(IKArm_l_jnt_list[bC_arm_l_rotInput] + '.rz', rot_arm_l_bColorNode_List[bC_arm_l_rotInput] + '.color2.color2B')

for bC_arm_l_rotOutput in range(len(bindArm_l_jnt_list)):
    mc.connectAttr(rot_arm_l_bColorNode_List[bC_arm_l_rotOutput] + '.output.outputR', bindArm_l_jnt_list[bC_arm_l_rotOutput] + '.rx')
    mc.connectAttr(rot_arm_l_bColorNode_List[bC_arm_l_rotOutput] + '.output.outputG', bindArm_l_jnt_list[bC_arm_l_rotOutput] + '.ry')
    mc.connectAttr(rot_arm_l_bColorNode_List[bC_arm_l_rotOutput] + '.output.outputB', bindArm_l_jnt_list[bC_arm_l_rotOutput] + '.rz')

for bC_arm_l_rotInput in range(len(FKArm_l_jnt_list)):
    mc.connectAttr(FKArm_l_jnt_list[bC_arm_l_rotInput] + '.rx', rot_arm_l_bColorNode_List[bC_arm_l_rotInput] + '.color1.color1R')
    mc.connectAttr(FKArm_l_jnt_list[bC_arm_l_rotInput] + '.ry', rot_arm_l_bColorNode_List[bC_arm_l_rotInput] + '.color1.color1G')
    mc.connectAttr(FKArm_l_jnt_list[bC_arm_l_rotInput] + '.rz', rot_arm_l_bColorNode_List[bC_arm_l_rotInput] + '.color1.color1B')

################################ connect scale attr to blendColor scale -> ikFk switch

for bC_arm_l_scaleInput in range(len(IKArm_l_jnt_list)):
    mc.connectAttr(IKArm_l_jnt_list[bC_arm_l_scaleInput] + '.sx', scl_arm_l_bColorNode_List[bC_arm_l_scaleInput] + '.color2.color2R')
    mc.connectAttr(IKArm_l_jnt_list[bC_arm_l_scaleInput] + '.sy', scl_arm_l_bColorNode_List[bC_arm_l_scaleInput] + '.color2.color2G')
    mc.connectAttr(IKArm_l_jnt_list[bC_arm_l_scaleInput] + '.sz', scl_arm_l_bColorNode_List[bC_arm_l_scaleInput] + '.color2.color2B')

for bC_arm_l_scaleOutput in range(len(bindArm_l_jnt_list)):
    mc.connectAttr(scl_arm_l_bColorNode_List[bC_arm_l_scaleOutput] + '.output.outputR', bindArm_l_jnt_list[bC_arm_l_scaleOutput] + '.sx')
    mc.connectAttr(scl_arm_l_bColorNode_List[bC_arm_l_scaleOutput] + '.output.outputG', bindArm_l_jnt_list[bC_arm_l_scaleOutput] + '.sy')
    mc.connectAttr(scl_arm_l_bColorNode_List[bC_arm_l_scaleOutput] + '.output.outputB', bindArm_l_jnt_list[bC_arm_l_scaleOutput] + '.sz')

for bC_arm_l_scaleInput in range(len(FKArm_l_jnt_list)):
    mc.connectAttr(FKArm_l_jnt_list[bC_arm_l_scaleInput] + '.sx', scl_arm_l_bColorNode_List[bC_arm_l_scaleInput] + '.color1.color1R')
    mc.connectAttr(FKArm_l_jnt_list[bC_arm_l_scaleInput] + '.sy', scl_arm_l_bColorNode_List[bC_arm_l_scaleInput] + '.color1.color1G')
    mc.connectAttr(FKArm_l_jnt_list[bC_arm_l_scaleInput] + '.sz', scl_arm_l_bColorNode_List[bC_arm_l_scaleInput] + '.color1.color1B')

### contonue with connect blend color to finger





























#######################################################################
#
#
#                          FK System
#
#
#######################################################################

################################################# neck head fk transform ###################################################################
def neck_FK_transform(*args):
    neckHead_jnt_list = ['neck', 'head']

    for neckHead in (neckHead_jnt_list):
        mc.makeIdentity(neckHead, apply=True, t=True, r=True, s=True)
        mc.select(d=True)

    mc.select(neckHead_jnt_list)
    tranRotScl_const()
    itemColor('neck_ctrl', 17)
    mc.parent('head_ctrlSpaceMaster', 'neck_ctrl')
    neckCtrl = mc.group(n= 'neck_controls', em=True)
    mc.parent('neck_ctrlSpaceMaster', neckCtrl)

    ### neck twist
    neckTwist = mc.joint('neck', n= 'neck_twist', rad=2)
    mc.delete(mc.pointConstraint('neck', 'head', neckTwist, mo=False))
    neck_PB = mc.createNode('pairBlend', n= 'neck_twist_PB')
    mc.setAttr(neck_PB + '.weight', 0.5)
    mc.connectAttr('head_ctrl.rotateX', neck_PB + '.inRotateX2')
    mc.connectAttr(neck_PB + '.outRotateX', neckTwist + '.rx')

    mc.select(d=True)
    print('neckHead_FK_completed')

################################################## spine FK transform ################################################################
def spine_FK_transfomr(*args):
    spine_jnt_list = ['pelvis', 'spine_01', 'spine_02', 'spine_03']

    for spine_jnt in (spine_jnt_list):
        mc.makeIdentity(spine_jnt, apply=True, t=True, r=True, s=True)
        mc.select(d=True)

    mc.select(spine_jnt_list)
    tranRotScl_const()
    mc.parent('spine_03_ctrlSpaceMaster', 'spine_02_ctrl'), mc.parent('spine_02_ctrlSpaceMaster', 'spine_01_ctrl')
    mc.parent('spine_01_ctrlSpaceMaster', 'pelvis_ctrl')
    itemColor('pelvis_ctrl', 17)
    spineCtrlGrp = mc.group(n = 'spine_controls', em=True)
    mc.parent('pelvis_ctrlSpaceMaster', spineCtrlGrp)

    mc.select(d=True)
    print('spine_FK_completed')



##################################################### leg FK transform ##############################################################
def leg_FK_Transform(*args):

    leg_l_jnt_list = ['thigh_l', 'calf_l', 'foot_l', 'ball_l', 'toe_l']

    for leg_l_jnt in (leg_l_jnt_list):
        mc.makeIdentity(leg_l_jnt, apply=True, t=True, r=True, s=True)
        mc.select(d=True)

    ### twist leg
    thighTwist_01_l = mc.joint('thigh_l', n='thigh_twist_fk_01_l', rad=2)
    thighTConst_01_l = mc.pointConstraint('thigh_l', 'calf_l', thighTwist_01_l ,mo=False), mc.setAttr('thigh_twist_fk_01_l_pointConstraint1.thigh_lW0', 2)
    thighTwist_02_l = mc.joint('thigh_l', n='thigh_twist_fk_02_l', rad=2)
    thighTConst_02_l = mc.pointConstraint('thigh_l', 'calf_l', thighTwist_02_l ,mo=False), mc.setAttr('thigh_twist_fk_02_l_pointConstraint1.calf_lW1', 2)
    mc.delete('thigh_twist_fk_01_l_pointConstraint1', 'thigh_twist_fk_02_l_pointConstraint1')

    calfTwist_01_l = mc.joint('calf_l', n='calf_twist_fk_01_l', rad=2)
    calfTConst_01_l = mc.pointConstraint('calf_l', 'foot_l', calfTwist_01_l ,mo=False), mc.setAttr('calf_twist_fk_01_l_pointConstraint1.calf_lW0', 2)
    calfTwist_02_l = mc.joint('calf_l', n='calf_twist_fk_02_l', rad=2)
    calfTConst_02_l = mc.pointConstraint('calf_l', 'foot_l', calfTwist_02_l ,mo=False), mc.setAttr('calf_twist_fk_02_l_pointConstraint1.foot_lW1', 2)
    mc.delete('calf_twist_fk_01_l_pointConstraint1', 'calf_twist_fk_02_l_pointConstraint1')
    mc.select(d=True)

    mc.mirrorJoint('thigh_l', mirrorYZ=True, mirrorBehavior=True, searchReplace=('_l', '_r')), mc.select(d=True)

    leg_r_jnt_list = ['thigh_r', 'calf_r', 'foot_r', 'ball_r', 'toe_r']

    mc.select(leg_r_jnt_list, leg_l_jnt_list)
    tranRotScl_const()

    ##### controls
    leg_l_ctrl_list = ['thigh_l_ctrl', 'calf_l_ctrl', 'foot_l_ctrl', 'ball_l_ctrl', 'toe_l_ctrl']
    leg_r_ctrl_list = ['thigh_r_ctrl', 'calf_r_ctrl', 'foot_r_ctrl', 'ball_r_ctrl', 'toe_r_ctrl']

    for leg_l_color in leg_l_ctrl_list:
        itemColor(leg_l_color, 6)

    for leg_r_color in leg_r_ctrl_list:
        itemColor(leg_r_color, 13)

    mc.parent('toe_l_ctrlSpaceMaster', 'ball_l_ctrl'), mc.parent('ball_l_ctrlSpaceMaster', 'foot_l_ctrl'), mc.parent('foot_l_ctrlSpaceMaster', 'calf_l_ctrl'), mc.parent('calf_l_ctrlSpaceMaster', 'thigh_l_ctrl')
    mc.parent('toe_r_ctrlSpaceMaster', 'ball_r_ctrl'), mc.parent('ball_r_ctrlSpaceMaster', 'foot_r_ctrl'), mc.parent('foot_r_ctrlSpaceMaster', 'calf_r_ctrl'), mc.parent('calf_r_ctrlSpaceMaster', 'thigh_r_ctrl')
    legGrp = mc.group(n= 'leg_controls', em=True)
    mc.parent('thigh_r_ctrlSpaceMaster', 'thigh_l_ctrlSpaceMaster', legGrp), mc.select(d=True)

    ######################## twist l_transform
    legTwist_l_jnt_list = ['thigh_twist_fk_01_l', 'thigh_twist_fk_02_l', 'calf_twist_fk_01_l', 'calf_twist_fk_02_l']
    mc.select(legTwist_l_jnt_list)
    tranRotScl_const()

    thighTwist_l_ctrl_list = ['thigh_twist_fk_01_l_ctrl', 'thigh_twist_fk_02_l_ctrl', 'calf_twist_fk_01_l_ctrl', 'calf_twist_fk_02_l_ctrl']
    thighTwist_l_masterGrp_list = ['thigh_twist_fk_01_l_ctrlSpaceMaster', 'thigh_twist_fk_02_l_ctrlSpaceMaster']
    calfTwist_l_masterGrp_list = ['calf_twist_fk_01_l_ctrlSpaceMaster', 'calf_twist_fk_02_l_ctrlSpaceMaster']
    mc.parent(thighTwist_l_masterGrp_list, 'thigh_l_ctrl'), mc.parent(calfTwist_l_masterGrp_list, 'calf_l_ctrl')
    mc.select(d=True)

    mc.disconnectAttr('thigh_l_ctrl.rx', 'thigh_l.rx')
    mc.disconnectAttr('thigh_twist_fk_01_l_ctrl.rx', 'thigh_twist_fk_01_l.rx')
    mc.disconnectAttr('thigh_twist_fk_02_l_ctrl.rx', 'thigh_twist_fk_02_l.rx')
    mc.disconnectAttr('calf_twist_fk_01_l_ctrl.rx', 'calf_twist_fk_01_l.rx')
    mc.disconnectAttr('calf_twist_fk_02_l_ctrl.rx', 'calf_twist_fk_02_l.rx')

    ####### legTwist PB transform

    mc.select(legTwist_l_jnt_list)
    thighT_l_01_PB = mc.createNode('pairBlend', n='thigh_twist_fk_01_l_PB')
    mc.setAttr(thighT_l_01_PB + '.weight', 0.4)
    mc.connectAttr('thigh_l_ctrl.rx', thighT_l_01_PB + '.inRotateX2')
    mc.connectAttr(thighT_l_01_PB + '.outRotateX', 'thigh_twist_fk_01_l.rx', f=True)

    thighT_l_02_PB = mc.createNode('pairBlend', n='thigh_twist_fk_02_l_PB')
    mc.setAttr(thighT_l_02_PB + '.weight', 0.8)
    mc.connectAttr('thigh_l_ctrl.rx', thighT_l_02_PB + '.inRotateX2')
    mc.connectAttr(thighT_l_02_PB + '.outRotateX', 'thigh_twist_fk_02_l.rx', f=True)

    calfT_l_01_PB = mc.createNode('pairBlend', n='calf_twist_fk_01_l_PB')
    mc.setAttr(calfT_l_01_PB + '.weight', -0.4)
    mc.connectAttr('foot_l_ctrl.rz', calfT_l_01_PB + '.inRotateX2')
    mc.connectAttr(calfT_l_01_PB + '.outRotateX', 'calf_twist_fk_01_l.rx', f=True)

    calfT_l_02_PB = mc.createNode('pairBlend', n='calf_twist_fk_02_l_PB')
    mc.setAttr(calfT_l_02_PB + '.weight', -0.8)
    mc.connectAttr('foot_l_ctrl.rz', calfT_l_02_PB + '.inRotateX2')
    mc.connectAttr(calfT_l_02_PB + '.outRotateX', 'calf_twist_fk_02_l.rx', f=True)

    ######################## twist r_transform
    legTwist_r_jnt_rist = ['thigh_twist_fk_01_r', 'thigh_twist_fk_02_r', 'calf_twist_fk_01_r', 'calf_twist_fk_02_r']
    mc.select(legTwist_r_jnt_rist)
    tranRotScl_const()

    thighTwist_r_ctrl_rist = ['thigh_twist_fk_01_r_ctrl', 'thigh_twist_fk_02_r_ctrl', 'calf_twist_fk_01_r_ctrl', 'calf_twist_fk_02_r_ctrl']
    thighTwist_r_masterGrp_rist = ['thigh_twist_fk_01_r_ctrlSpaceMaster', 'thigh_twist_fk_02_r_ctrlSpaceMaster']
    calfTwist_r_masterGrp_rist = ['calf_twist_fk_01_r_ctrlSpaceMaster', 'calf_twist_fk_02_r_ctrlSpaceMaster']
    mc.parent(thighTwist_r_masterGrp_rist, 'thigh_r_ctrl'), mc.parent(calfTwist_r_masterGrp_rist, 'calf_r_ctrl')
    mc.select(d=True)

    mc.disconnectAttr('thigh_r_ctrl.rx', 'thigh_r.rx')
    mc.disconnectAttr('thigh_twist_fk_01_r_ctrl.rx', 'thigh_twist_fk_01_r.rx')
    mc.disconnectAttr('thigh_twist_fk_02_r_ctrl.rx', 'thigh_twist_fk_02_r.rx')
    mc.disconnectAttr('calf_twist_fk_01_r_ctrl.rx', 'calf_twist_fk_01_r.rx')
    mc.disconnectAttr('calf_twist_fk_02_r_ctrl.rx', 'calf_twist_fk_02_r.rx')

    ####### legTwist PB transform

    mc.select(legTwist_r_jnt_rist)
    thighT_r_01_PB = mc.createNode('pairBlend', n='thigh_twist_fk_01_r_PB')
    mc.setAttr(thighT_r_01_PB + '.weight', 0.4)
    mc.connectAttr('thigh_r_ctrl.rx', thighT_r_01_PB + '.inRotateX2')
    mc.connectAttr(thighT_r_01_PB + '.outRotateX', 'thigh_twist_fk_01_r.rx', f=True)

    thighT_r_02_PB = mc.createNode('pairBlend', n='thigh_twist_fk_02_r_PB')
    mc.setAttr(thighT_r_02_PB + '.weight', 0.8)
    mc.connectAttr('thigh_r_ctrl.rx', thighT_r_02_PB + '.inRotateX2')
    mc.connectAttr(thighT_r_02_PB + '.outRotateX', 'thigh_twist_fk_02_r.rx', f=True)

    calfT_r_01_PB = mc.createNode('pairBlend', n='calf_twist_fk_01_r_PB')
    mc.setAttr(calfT_r_01_PB + '.weight', -0.4)
    mc.connectAttr('foot_r_ctrl.rz', calfT_r_01_PB + '.inRotateX2')
    mc.connectAttr(calfT_r_01_PB + '.outRotateX', 'calf_twist_fk_01_r.rx', f=True)

    calfT_r_02_PB = mc.createNode('pairBlend', n='calf_twist_fk_02_r_PB')
    mc.setAttr(calfT_r_02_PB + '.weight', -0.8)
    mc.connectAttr('foot_r_ctrl.rz', calfT_r_02_PB + '.inRotateX2')
    mc.connectAttr(calfT_r_02_PB + '.outRotateX', 'calf_twist_fk_02_r.rx', f=True)

    mc.select(d=True)
    print('leg_FK_Completed')

##################################################### biped FK transform #########################################################

def biped_FK_transform(*args):

    ##################################### FK bones

    spine_jnt_list = ['pelvis', 'spine_01', 'spine_02', 'spine_03']

    for spine_jnt in (spine_jnt_list):
            mc.makeIdentity(spine_jnt, apply=True, t=True, r=True, s=True)
            mc.select(d=True)

    neckHead_jnt_list = ['neck', 'head']

    for neckHead in (neckHead_jnt_list):
            mc.makeIdentity(neckHead, apply=True, t=True, r=True, s=True)
            mc.select(d=True)

    arm_fingers_l_jnt_list = ['clavicle_l', 'upperarm_l', 'lowerarm_l', 'hand_l', 'pinky_00_l', 'pinky_01_l', 'pinky_02_l','pinky_03_l',
                              'ring_00_l', 'ring_01_l', 'ring_02_l', 'ring_03_l', 'middle_00_l', 'middle_01_l',
                              'middle_02_l', 'middle_03_l','index_00_l', 'index_01_l', 'index_02_l', 'index_03_l', 'thumb_01_l', 'thumb_02_l','thumb_03_l']

    for arm_fingers_jnt in (arm_fingers_l_jnt_list):
            mc.makeIdentity(arm_fingers_jnt, apply=True, t=True, r=True, s=True)
            mc.select(d=True)

    ### twist arm
    upperarmTwist_01_l = mc.joint('upperarm_l', n='upperarm_twist_01_l', rad=2)
    upperarmTConst_01_l = mc.pointConstraint('upperarm_l', 'lowerarm_l', upperarmTwist_01_l, mo=False), mc.setAttr('upperarm_twist_01_l_pointConstraint1.upperarm_lW0', 2)
    upperarmTwist_02_l = mc.joint('upperarm_l', n='upperarm_twist_02_l', rad=2)
    upperarmTConst_02_l = mc.pointConstraint('upperarm_l', 'lowerarm_l', upperarmTwist_02_l, mo=False), mc.setAttr('upperarm_twist_02_l_pointConstraint1.lowerarm_lW1', 2)
    mc.delete('upperarm_twist_01_l_pointConstraint1', 'upperarm_twist_02_l_pointConstraint1')

    lowerarmTwist_01_l = mc.joint('lowerarm_l', n='lowerarm_twist_01_l', rad=2)
    lowerarmTConst_01_l = mc.pointConstraint('lowerarm_l', 'hand_l', lowerarmTwist_01_l, mo=False), mc.setAttr('lowerarm_twist_01_l_pointConstraint1.lowerarm_lW0', 1.5)
    lowerarmTwist_02_l = mc.joint('lowerarm_l', n='lowerarm_twist_02_l', rad=2)
    lowerarmTConst_02_l = mc.pointConstraint('lowerarm_l', 'hand_l', lowerarmTwist_02_l, mo=False), mc.setAttr('lowerarm_twist_02_l_pointConstraint1.hand_lW1', 3)
    mc.delete('lowerarm_twist_01_l_pointConstraint1', 'lowerarm_twist_02_l_pointConstraint1')
    mc.select(d=True)

    leg_l_jnt_list = ['thigh_l', 'calf_l', 'foot_l', 'ball_l', 'toe_l']

    for leg_l_jnt in (leg_l_jnt_list):
            mc.makeIdentity(leg_l_jnt, apply=True, t=True, r=True, s=True)
            mc.select(d=True)

    ### twist leg
    thighTwist_01_l = mc.joint('thigh_l', n='thigh_twist_01_l', rad=2)
    thighTConst_01_l = mc.pointConstraint('thigh_l', 'calf_l', thighTwist_01_l, mo=False), mc.setAttr('thigh_twist_01_l_pointConstraint1.thigh_lW0', 2)
    thighTwist_02_l = mc.joint('thigh_l', n='thigh_twist_02_l', rad=2)
    thighTConst_02_l = mc.pointConstraint('thigh_l', 'calf_l', thighTwist_02_l, mo=False), mc.setAttr('thigh_twist_02_l_pointConstraint1.calf_lW1', 2)
    mc.delete('thigh_twist_01_l_pointConstraint1', 'thigh_twist_02_l_pointConstraint1')

    calfTwist_01_l = mc.joint('calf_l', n='calf_twist_01_l', rad=2)
    calfTConst_01_l = mc.pointConstraint('calf_l', 'foot_l', calfTwist_01_l, mo=False), mc.setAttr('calf_twist_01_l_pointConstraint1.calf_lW0', 2)
    calfTwist_02_l = mc.joint('calf_l', n='calf_twist_02_l', rad=2)
    calfTConst_02_l = mc.pointConstraint('calf_l', 'foot_l', calfTwist_02_l, mo=False), mc.setAttr('calf_twist_02_l_pointConstraint1.foot_lW1', 2)
    mc.delete('calf_twist_01_l_pointConstraint1', 'calf_twist_02_l_pointConstraint1')
    mc.select(d=True)

    mc.mirrorJoint('clavicle_l', mirrorYZ=True, mirrorBehavior=True, searchReplace=('_l', '_r')), mc.select(d=True)
    mc.mirrorJoint('thigh_l', mirrorYZ=True, mirrorBehavior=True, searchReplace=('_l', '_r')), mc.select(d=True)

    ###################################################################### spine FK

    mc.select(spine_jnt_list)
    tranRotScl_const()
    mc.parent('spine_03_ctrlSpaceMaster', 'spine_02_ctrl'), mc.parent('spine_02_ctrlSpaceMaster', 'spine_01_ctrl')
    mc.parent('spine_01_ctrlSpaceMaster', 'pelvis_ctrl')
    itemColor('pelvis_ctrl', 17)
    spineGrp = mc.group(n='spine_controls', em=True)
    mc.parent('pelvis_ctrlSpaceMaster', spineGrp)

    mc.select(d=True)

    ################################################################## neck FK

    mc.select(neckHead_jnt_list)
    tranRotScl_const()
    itemColor('neck_ctrl', 17)
    mc.parent('head_ctrlSpaceMaster', 'neck_ctrl')
    neckHeadGrp = mc.group(n= 'neck_controls', em=True)
    mc.parent('neck_ctrlSpaceMaster', neckHeadGrp)

    ### neck twist
    neckTwist = mc.joint('neck', n= 'neck_twist', rad=2)
    mc.delete(mc.pointConstraint('neck', 'head', neckTwist, mo=False))
    neck_PB = mc.createNode('pairBlend', n= 'neck_twist_PB')
    mc.setAttr(neck_PB + '.weight', 0.5)
    mc.connectAttr('head_ctrl.rotateX', neck_PB + '.inRotateX2')
    mc.connectAttr(neck_PB + '.outRotateX', neckTwist + '.rx')

    mc.select(d=True)

    ############################################################################# arm FK


    arm_fingers_r_jnt_list = ['clavicle_r', 'upperarm_r', 'lowerarm_r', 'hand_r', 'pinky_00_r', 'pinky_01_r', 'pinky_02_r',
                              'pinky_03_r','ring_00_r', 'ring_01_r', 'ring_02_r', 'ring_03_r', 'middle_00_r', 'middle_01_r',
                              'middle_02_r', 'middle_03_r','index_00_r', 'index_01_r', 'index_02_r', 'index_03_r', 'thumb_01_r', 'thumb_02_r','thumb_03_r']

    mc.select(arm_fingers_l_jnt_list, arm_fingers_r_jnt_list)
    tranRotScl_const()

    ### controls
    arm_fingers_l_ctrl_list = ['clavicle_l_ctrl', 'upperarm_l_ctrl', 'lowerarm_l_ctrl', 'hand_l_ctrl', 'pinky_00_l_ctrl',
                               'pinky_01_l_ctrl', 'pinky_02_l_ctrl', 'pinky_03_l_ctrl','ring_00_l_ctrl', 'ring_01_l_ctrl', 'ring_02_l_ctrl', 'ring_03_l_ctrl', 'middle_00_l_ctrl',
                               'middle_01_l_ctrl', 'middle_02_l_ctrl', 'middle_03_l_ctrl','index_00_l_ctrl', 'index_01_l_ctrl', 'index_02_l_ctrl', 'index_03_l_ctrl',
                               'thumb_01_l_ctrl', 'thumb_02_l_ctrl', 'thumb_03_l_ctrl']

    arm_fingers_r_ctrl_list = ['clavicle_r_ctrl', 'upperarm_r_ctrl', 'lowerarm_r_ctrl', 'hand_r_ctrl', 'pinky_00_r_ctrl','pinky_01_r_ctrl', 'pinky_02_r_ctrl', 'pinky_03_r_ctrl',
                               'ring_00_r_ctrl', 'ring_01_r_ctrl', 'ring_02_r_ctrl', 'ring_03_r_ctrl', 'middle_00_r_ctrl',
                               'middle_01_r_ctrl', 'middle_02_r_ctrl', 'middle_03_r_ctrl','index_00_r_ctrl', 'index_01_r_ctrl', 'index_02_r_ctrl', 'index_03_r_ctrl',
                               'thumb_01_r_ctrl', 'thumb_02_r_ctrl', 'thumb_03_r_ctrl']

    for armF_l in arm_fingers_l_ctrl_list:
            itemColor(armF_l, 6)

    for armF_r in arm_fingers_r_ctrl_list:
            itemColor(armF_r, 13)

    ### parent controls
    mc.parent('upperarm_l_ctrlSpaceMaster', 'clavicle_l_ctrl'), mc.parent('lowerarm_l_ctrlSpaceMaster','upperarm_l_ctrl'), mc.parent('hand_l_ctrlSpaceMaster', 'lowerarm_l_ctrl')
    mc.parent('pinky_03_l_ctrlSpaceMaster', 'pinky_02_l_ctrl'), mc.parent('pinky_02_l_ctrlSpaceMaster','pinky_01_l_ctrl'), mc.parent('pinky_01_l_ctrlSpaceMaster', 'pinky_00_l_ctrl')
    mc.parent('ring_03_l_ctrlSpaceMaster', 'ring_02_l_ctrl'), mc.parent('ring_02_l_ctrlSpaceMaster','ring_01_l_ctrl'), mc.parent('ring_01_l_ctrlSpaceMaster', 'ring_00_l_ctrl')
    mc.parent('middle_03_l_ctrlSpaceMaster', 'middle_02_l_ctrl'), mc.parent('middle_02_l_ctrlSpaceMaster','middle_01_l_ctrl'), mc.parent('middle_01_l_ctrlSpaceMaster', 'middle_00_l_ctrl')
    mc.parent('index_03_l_ctrlSpaceMaster', 'index_02_l_ctrl'), mc.parent('index_02_l_ctrlSpaceMaster','index_01_l_ctrl'), mc.parent('index_01_l_ctrlSpaceMaster', 'index_00_l_ctrl')
    mc.parent('thumb_03_l_ctrlSpaceMaster', 'thumb_02_l_ctrl'), mc.parent('thumb_02_l_ctrlSpaceMaster', 'thumb_01_l_ctrl')
    mc.parent('pinky_00_l_ctrlSpaceMaster', 'ring_00_l_ctrlSpaceMaster', 'middle_00_l_ctrlSpaceMaster', 'index_00_l_ctrlSpaceMaster', 'thumb_01_l_ctrlSpaceMaster', 'hand_l_ctrl')

    mc.parent('upperarm_r_ctrlSpaceMaster', 'clavicle_r_ctrl'), mc.parent('lowerarm_r_ctrlSpaceMaster','upperarm_r_ctrl'), mc.parent('hand_r_ctrlSpaceMaster', 'lowerarm_r_ctrl')
    mc.parent('pinky_03_r_ctrlSpaceMaster', 'pinky_02_r_ctrl'), mc.parent('pinky_02_r_ctrlSpaceMaster','pinky_01_r_ctrl'), mc.parent('pinky_01_r_ctrlSpaceMaster', 'pinky_00_r_ctrl')
    mc.parent('ring_03_r_ctrlSpaceMaster', 'ring_02_r_ctrl'), mc.parent('ring_02_r_ctrlSpaceMaster','ring_01_r_ctrl'), mc.parent('ring_01_r_ctrlSpaceMaster', 'ring_00_r_ctrl')
    mc.parent('middle_03_r_ctrlSpaceMaster', 'middle_02_r_ctrl'), mc.parent('middle_02_r_ctrlSpaceMaster','middle_01_r_ctrl'), mc.parent('middle_01_r_ctrlSpaceMaster', 'middle_00_r_ctrl')
    mc.parent('index_03_r_ctrlSpaceMaster', 'index_02_r_ctrl'), mc.parent('index_02_r_ctrlSpaceMaster','index_01_r_ctrl'), mc.parent('index_01_r_ctrlSpaceMaster', 'index_00_r_ctrl')
    mc.parent('thumb_03_r_ctrlSpaceMaster', 'thumb_02_r_ctrl'), mc.parent('thumb_02_r_ctrlSpaceMaster', 'thumb_01_r_ctrl')
    mc.parent('pinky_00_r_ctrlSpaceMaster', 'ring_00_r_ctrlSpaceMaster', 'middle_00_r_ctrlSpaceMaster','index_00_r_ctrlSpaceMaster', 'thumb_01_r_ctrlSpaceMaster', 'hand_r_ctrl')

    armsGrp = mc.group(n='arms_ctrls', em=True)
    mc.parent('clavicle_r_ctrlSpaceMaster', 'clavicle_l_ctrlSpaceMaster', armsGrp), mc.select(d=True)

    ######################## twist l_transform
    upperarmTwist_l_jnt_list = ['upperarm_twist_01_l', 'upperarm_twist_02_l', 'lowerarm_twist_01_l', 'lowerarm_twist_02_l']
    mc.select(upperarmTwist_l_jnt_list)
    tranRotScl_const()

    upperarmTwist_l_ctrl_list = ['upperarm_twist_01_l_ctrl', 'upperarm_twist_02_l_ctrl', 'lowerarm_twist_01_l_ctrl','lowerarm_twist_02_l_ctrl']
    upperarmTwist_l_masterGrp_list = ['upperarm_twist_01_l_ctrlSpaceMaster', 'upperarm_twist_02_l_ctrlSpaceMaster']
    lowerarmTwist_l_masterGrp_list = ['lowerarm_twist_01_l_ctrlSpaceMaster', 'lowerarm_twist_02_l_ctrlSpaceMaster']
    mc.parent(upperarmTwist_l_masterGrp_list, 'upperarm_l_ctrl'), mc.parent(lowerarmTwist_l_masterGrp_list,'lowerarm_l_ctrl')
    mc.select(d=True)

    mc.disconnectAttr('upperarm_l_ctrl.rx', 'upperarm_l.rx')
    mc.disconnectAttr('upperarm_twist_01_l_ctrl.rx', 'upperarm_twist_01_l.rx')
    mc.disconnectAttr('upperarm_twist_02_l_ctrl.rx', 'upperarm_twist_02_l.rx')
    mc.disconnectAttr('lowerarm_twist_01_l_ctrl.rx', 'lowerarm_twist_01_l.rx')
    mc.disconnectAttr('lowerarm_twist_02_l_ctrl.rx', 'lowerarm_twist_02_l.rx')

    #### armTwist PB connection
    mc.select(upperarmTwist_l_jnt_list)

    upperarmT_l_01_PB = mc.createNode('pairBlend', n='upperarm_twist_01_l_PB')
    mc.setAttr(upperarmT_l_01_PB + '.weight', 0.2)
    mc.connectAttr('upperarm_l_ctrl.rx', upperarmT_l_01_PB + '.inRotateX2')
    mc.connectAttr(upperarmT_l_01_PB + '.outRotateX', 'upperarm_twist_01_l.rx', f=True)

    upperarmT_l_02_PB = mc.createNode('pairBlend', n='upperarm_twist_02_l_PB')
    mc.setAttr(upperarmT_l_02_PB + '.weight', 0.8)
    mc.connectAttr('upperarm_l_ctrl.rx', upperarmT_l_02_PB + '.inRotateX2')
    mc.connectAttr(upperarmT_l_02_PB + '.outRotateX', 'upperarm_twist_02_l.rx', f=True)

    lowerarmT_l_01_PB = mc.createNode('pairBlend', n='lowerarm_twist_01_l_PB')
    mc.setAttr(lowerarmT_l_01_PB + '.weight', 0.4)
    mc.connectAttr('hand_l_ctrl.rx', lowerarmT_l_01_PB + '.inRotateX2')
    mc.connectAttr(lowerarmT_l_01_PB + '.outRotateX', 'lowerarm_twist_01_l.rx', f=True)

    lowerarmT_l_02_PB = mc.createNode('pairBlend', n='lowerarm_twist_02_l_PB')
    mc.setAttr(lowerarmT_l_02_PB + '.weight', 0.8)
    mc.connectAttr('hand_l_ctrl.rx', lowerarmT_l_02_PB + '.inRotateX2')
    mc.connectAttr(lowerarmT_l_02_PB + '.outRotateX', 'lowerarm_twist_02_l.rx', f=True)

    ######################## twist r_transform
    upperarmTwist_r_jnt_list = ['upperarm_twist_01_r', 'upperarm_twist_02_r', 'lowerarm_twist_01_r', 'lowerarm_twist_02_r']
    mc.select(upperarmTwist_r_jnt_list)
    tranRotScl_const()

    upperarmTwist_r_ctrl_list = ['upperarm_twist_01_r_ctrl', 'upperarm_twist_02_r_ctrl', 'lowerarm_twist_01_r_ctrl','lowerarm_twist_02_r_ctrl']
    upperarmTwist_r_masterGrp_list = ['upperarm_twist_01_r_ctrlSpaceMaster', 'upperarm_twist_02_r_ctrlSpaceMaster']
    lowerarmTwist_r_masterGrp_list = ['lowerarm_twist_01_r_ctrlSpaceMaster', 'lowerarm_twist_02_r_ctrlSpaceMaster']
    mc.parent(upperarmTwist_r_masterGrp_list, 'upperarm_r_ctrl'), mc.parent(lowerarmTwist_r_masterGrp_list, 'lowerarm_r_ctrl')
    mc.select(d=True)

    mc.disconnectAttr('upperarm_r_ctrl.rx', 'upperarm_r.rx')
    mc.disconnectAttr('upperarm_twist_01_r_ctrl.rx', 'upperarm_twist_01_r.rx')
    mc.disconnectAttr('upperarm_twist_02_r_ctrl.rx', 'upperarm_twist_02_r.rx')
    mc.disconnectAttr('lowerarm_twist_01_r_ctrl.rx', 'lowerarm_twist_01_r.rx')
    mc.disconnectAttr('lowerarm_twist_02_r_ctrl.rx', 'lowerarm_twist_02_r.rx')

    #### armTwist PB connection
    mc.select(upperarmTwist_r_jnt_list)

    upperarmT_r_01_PB = mc.createNode('pairBlend', n='upperarm_twist_01_r_PB')
    mc.setAttr(upperarmT_r_01_PB + '.weight', 0.2)
    mc.connectAttr('upperarm_r_ctrl.rx', upperarmT_r_01_PB + '.inRotateX2')
    mc.connectAttr(upperarmT_r_01_PB + '.outRotateX', 'upperarm_twist_01_r.rx', f=True)

    upperarmT_r_02_PB = mc.createNode('pairBlend', n='upperarm_twist_02_r_PB')
    mc.setAttr(upperarmT_r_02_PB + '.weight', 0.8)
    mc.connectAttr('upperarm_r_ctrl.rx', upperarmT_r_02_PB + '.inRotateX2')
    mc.connectAttr(upperarmT_r_02_PB + '.outRotateX', 'upperarm_twist_02_r.rx', f=True)

    lowerarmT_r_01_PB = mc.createNode('pairBlend', n='lowerarm_twist_01_r_PB')
    mc.setAttr(lowerarmT_r_01_PB + '.weight', 0.4)
    mc.connectAttr('hand_r_ctrl.rx', lowerarmT_r_01_PB + '.inRotateX2')
    mc.connectAttr(lowerarmT_r_01_PB + '.outRotateX', 'lowerarm_twist_01_r.rx', f=True)

    lowerarmT_r_02_PB = mc.createNode('pairBlend', n='lowerarm_twist_02_r_PB')
    mc.setAttr(lowerarmT_r_02_PB + '.weight', 0.8)
    mc.connectAttr('hand_r_ctrl.rx', lowerarmT_r_02_PB + '.inRotateX2')
    mc.connectAttr(lowerarmT_r_02_PB + '.outRotateX', 'lowerarm_twist_02_r.rx', f=True)

    mc.select(d=True)

    ##################################################################################### leg FK

    leg_r_jnt_list = ['thigh_r', 'calf_r', 'foot_r', 'ball_r', 'toe_r']

    mc.select(leg_r_jnt_list, leg_l_jnt_list)
    tranRotScl_const()

    ##### controls
    leg_l_ctrl_list = ['thigh_l_ctrl', 'calf_l_ctrl', 'foot_l_ctrl', 'ball_l_ctrl', 'toe_l_ctrl']
    leg_r_ctrl_list = ['thigh_r_ctrl', 'calf_r_ctrl', 'foot_r_ctrl', 'ball_r_ctrl', 'toe_r_ctrl']

    for leg_l_color in leg_l_ctrl_list:
            itemColor(leg_l_color, 6)

    for leg_r_color in leg_r_ctrl_list:
            itemColor(leg_r_color, 13)

    mc.parent('toe_l_ctrlSpaceMaster', 'ball_l_ctrl'), mc.parent('ball_l_ctrlSpaceMaster', 'foot_l_ctrl'), mc.parent('foot_l_ctrlSpaceMaster', 'calf_l_ctrl'), mc.parent('calf_l_ctrlSpaceMaster', 'thigh_l_ctrl')
    mc.parent('toe_r_ctrlSpaceMaster', 'ball_r_ctrl'), mc.parent('ball_r_ctrlSpaceMaster', 'foot_r_ctrl'), mc.parent('foot_r_ctrlSpaceMaster', 'calf_r_ctrl'), mc.parent('calf_r_ctrlSpaceMaster', 'thigh_r_ctrl')
    legGrp = mc.group(n='leg_controls', em=True)
    mc.parent('thigh_r_ctrlSpaceMaster', 'thigh_l_ctrlSpaceMaster', legGrp), mc.select(d=True)

    ######################## twist l_transform
    legTwist_l_jnt_list = ['thigh_twist_01_l', 'thigh_twist_02_l', 'calf_twist_01_l', 'calf_twist_02_l']
    mc.select(legTwist_l_jnt_list)
    tranRotScl_const()

    thighTwist_l_ctrl_list = ['thigh_twist_01_l_ctrl', 'thigh_twist_02_l_ctrl', 'calf_twist_01_l_ctrl','calf_twist_02_l_ctrl']
    thighTwist_l_masterGrp_list = ['thigh_twist_01_l_ctrlSpaceMaster', 'thigh_twist_02_l_ctrlSpaceMaster']
    calfTwist_l_masterGrp_list = ['calf_twist_01_l_ctrlSpaceMaster', 'calf_twist_02_l_ctrlSpaceMaster']
    mc.parent(thighTwist_l_masterGrp_list, 'thigh_l_ctrl'), mc.parent(calfTwist_l_masterGrp_list, 'calf_l_ctrl')
    mc.select(d=True)

    mc.disconnectAttr('thigh_l_ctrl.rx', 'thigh_l.rx')
    mc.disconnectAttr('thigh_twist_01_l_ctrl.rx', 'thigh_twist_01_l.rx')
    mc.disconnectAttr('thigh_twist_02_l_ctrl.rx', 'thigh_twist_02_l.rx')
    mc.disconnectAttr('calf_twist_01_l_ctrl.rx', 'calf_twist_01_l.rx')
    mc.disconnectAttr('calf_twist_02_l_ctrl.rx', 'calf_twist_02_l.rx')

    ####### legTwist PB transform

    mc.select(legTwist_l_jnt_list)
    thighT_l_01_PB = mc.createNode('pairBlend', n='thigh_twist_01_l_PB')
    mc.setAttr(thighT_l_01_PB + '.weight', 0.4)
    mc.connectAttr('thigh_l_ctrl.rx', thighT_l_01_PB + '.inRotateX2')
    mc.connectAttr(thighT_l_01_PB + '.outRotateX', 'thigh_twist_01_l.rx', f=True)

    thighT_l_02_PB = mc.createNode('pairBlend', n='thigh_twist_02_l_PB')
    mc.setAttr(thighT_l_02_PB + '.weight', 0.8)
    mc.connectAttr('thigh_l_ctrl.rx', thighT_l_02_PB + '.inRotateX2')
    mc.connectAttr(thighT_l_02_PB + '.outRotateX', 'thigh_twist_02_l.rx', f=True)

    calfT_l_01_PB = mc.createNode('pairBlend', n='calf_twist_01_l_PB')
    mc.setAttr(calfT_l_01_PB + '.weight', -0.4)
    mc.connectAttr('foot_l_ctrl.rz', calfT_l_01_PB + '.inRotateX2')
    mc.connectAttr(calfT_l_01_PB + '.outRotateX', 'calf_twist_01_l.rx', f=True)

    calfT_l_02_PB = mc.createNode('pairBlend', n='calf_twist_02_l_PB')
    mc.setAttr(calfT_l_02_PB + '.weight', -0.8)
    mc.connectAttr('foot_l_ctrl.rz', calfT_l_02_PB + '.inRotateX2')
    mc.connectAttr(calfT_l_02_PB + '.outRotateX', 'calf_twist_02_l.rx', f=True)

    ######################## twist r_transform
    legTwist_r_jnt_rist = ['thigh_twist_01_r', 'thigh_twist_02_r', 'calf_twist_01_r', 'calf_twist_02_r']
    mc.select(legTwist_r_jnt_rist)
    tranRotScl_const()

    thighTwist_r_ctrl_rist = ['thigh_twist_01_r_ctrl', 'thigh_twist_02_r_ctrl', 'calf_twist_01_r_ctrl','calf_twist_02_r_ctrl']
    thighTwist_r_masterGrp_rist = ['thigh_twist_01_r_ctrlSpaceMaster', 'thigh_twist_02_r_ctrlSpaceMaster']
    calfTwist_r_masterGrp_rist = ['calf_twist_01_r_ctrlSpaceMaster', 'calf_twist_02_r_ctrlSpaceMaster']
    mc.parent(thighTwist_r_masterGrp_rist, 'thigh_r_ctrl'), mc.parent(calfTwist_r_masterGrp_rist, 'calf_r_ctrl')
    mc.select(d=True)

    mc.disconnectAttr('thigh_r_ctrl.rx', 'thigh_r.rx')
    mc.disconnectAttr('thigh_twist_01_r_ctrl.rx', 'thigh_twist_01_r.rx')
    mc.disconnectAttr('thigh_twist_02_r_ctrl.rx', 'thigh_twist_02_r.rx')
    mc.disconnectAttr('calf_twist_01_r_ctrl.rx', 'calf_twist_01_r.rx')
    mc.disconnectAttr('calf_twist_02_r_ctrl.rx', 'calf_twist_02_r.rx')

    ####### legTwist PB transform

    mc.select(legTwist_r_jnt_rist)
    thighT_r_01_PB = mc.createNode('pairBlend', n='thigh_twist_01_r_PB')
    mc.setAttr(thighT_r_01_PB + '.weight', 0.4)
    mc.connectAttr('thigh_r_ctrl.rx', thighT_r_01_PB + '.inRotateX2')
    mc.connectAttr(thighT_r_01_PB + '.outRotateX', 'thigh_twist_01_r.rx', f=True)

    thighT_r_02_PB = mc.createNode('pairBlend', n='thigh_twist_02_r_PB')
    mc.setAttr(thighT_r_02_PB + '.weight', 0.8)
    mc.connectAttr('thigh_r_ctrl.rx', thighT_r_02_PB + '.inRotateX2')
    mc.connectAttr(thighT_r_02_PB + '.outRotateX', 'thigh_twist_02_r.rx', f=True)

    calfT_r_01_PB = mc.createNode('pairBlend', n='calf_twist_01_r_PB')
    mc.setAttr(calfT_r_01_PB + '.weight', -0.4)
    mc.connectAttr('foot_r_ctrl.rz', calfT_r_01_PB + '.inRotateX2')
    mc.connectAttr(calfT_r_01_PB + '.outRotateX', 'calf_twist_01_r.rx', f=True)

    calfT_r_02_PB = mc.createNode('pairBlend', n='calf_twist_02_r_PB')
    mc.setAttr(calfT_r_02_PB + '.weight', -0.8)
    mc.connectAttr('foot_r_ctrl.rz', calfT_r_02_PB + '.inRotateX2')
    mc.connectAttr(calfT_r_02_PB + '.outRotateX', 'calf_twist_02_r.rx', f=True)

    mc.select(d=True)

    bipedGrp = mc.group(n='biped_controls', em=True)
    mc.parent(armsGrp, legGrp, neckHeadGrp, spineGrp, bipedGrp), mc.select(d=True)
    mc.parent(armsGrp, neckHeadGrp, 'spine_03_ctrl'), mc.parent(legGrp, 'pelvis_ctrl')
    mc.parent('thigh_r', 'thigh_l', 'pelvis'), mc.parent('neck', 'clavicle_l', 'clavicle_r', 'spine_03'), mc.select(d=True)
    print('Biped_FK_completed')

#######################################################################
#
#
#                           IK System
#
#
#######################################################################

######################################################### spine IK transform #############################################################

def spine_IK_transform(*args):

    mc.ikHandle(n='spine_ik', sj='pelvis', ee='spine_03', sol='ikSplineSolver')

    spine_jnt_list = ['pelvis', 'spine_01', 'spine_02', 'spine_03']

    cv_list = ['curve1.cv[0]', 'curve1.cv[1:2]', 'curve1.cv[3]']
    for each in cv_list:
        mc.cluster(each)
    mc.select(d=True)

    clusters = ['cluster1Handle', 'cluster2Handle', 'cluster3Handle']
    for each in clusters:
        mc.rename(each, 'spine_cl')

    clustersNodes = ['spine_cl', 'spine_cl1', 'spine_cl2']
    for each in clustersNodes:
        cluster_ctrl = mc.circle(nr=(0, 1, 0), c=(0, 0, 0), r=5, n=each + '_ctrl', ch=False)
        cluster_grp = mc.group(n= each + '_ctrlSpace', em=True)
        cluster_masterGrp = mc.group(n= each + '_master_ctrSpace', em=True)
        mc.parent(cluster_ctrl, cluster_grp)
        mc.parent(cluster_grp, cluster_masterGrp)
        mc.delete(mc.parentConstraint(each, cluster_masterGrp, mo=False))
    mc.select(d=True)

    spine_ctrl_list = ['spine_cl_ctrl', 'spine_cl1_ctrl', 'spine_cl2_ctrl']
    for item in spine_ctrl_list:
        itemColor(item, 17)

    # parent the cluster under the controllers
    mc.parent('spine_cl', 'spine_cl_ctrl'), mc.parent('spine_cl1', 'spine_cl1_ctrl'), mc.parent('spine_cl2', 'spine_cl2_ctrl')
    mc.select(d=True)

    # advance twist controls setup
    mc.setAttr("spine_ik.dTwistControlEnable", 1)
    mc.setAttr("spine_ik.dWorldUpType", 4)
    mc.setAttr("spine_ik.dForwardAxis", 0)
    mc.setAttr("spine_ik.dWorldUpAxis", 3)
    mc.setAttr("spine_ik.dTwistValueType", 1)
    mc.setAttr('spine_ik.dWorldUpVectorZ', 1)
    mc.setAttr('spine_ik.dWorldUpVectorEndZ', 1)
    mc.setAttr('spine_ik.dWorldUpVectorY', 0)
    mc.setAttr('spine_ik.dWorldUpVectorEndY', 0)
    mc.connectAttr('spine_cl2_ctrl.worldMatrix', 'spine_ik.dWorldUpMatrixEnd')
    mc.connectAttr('spine_cl_ctrl.worldMatrix', 'spine_ik.dWorldUpMatrix')

    # S&S
    spine_arcLength_MD = mc.createNode('multiplyDivide', n='spine_arcLength_MD')
    mc.setAttr(spine_arcLength_MD + '.operation', 2)
    spine_arcLength_div_MD = mc.createNode('multiplyDivide', n='spine_arcLength_div_MD')
    mc.setAttr(spine_arcLength_div_MD + '.operation', 2)
    crvInfo = mc.createNode('curveInfo', n='spine_crvInfo')
    mc.connectAttr('curveShape1.worldSpace', crvInfo + '.inputCurve', f=True)
    arcLengh_data = mc.getAttr(crvInfo + '.arcLength')
    mc.setAttr(spine_arcLength_MD + '.input2X', arcLengh_data)
    mc.connectAttr(crvInfo + '.arcLength', spine_arcLength_MD + '.input1X', f=True)
    mc.connectAttr(spine_arcLength_MD + '.outputX', spine_arcLength_div_MD + '.input1X', f=True)

    for spineJnt in (spine_jnt_list):
        mc.connectAttr(spine_arcLength_div_MD + '.outputX', spineJnt + '.sx')

    # COG control
    cog_ctrl = mc.circle(nr=(0, 1, 0), r=20, n='cog_ctrl', ch=False)
    cog_ctrlSpace = mc.group(cog_ctrl, n='cog_ctrlSpace')
    cog_ctrlSpaceMaster = mc.group(cog_ctrlSpace, n='cog_masterSpace')
    mc.delete(mc.parentConstraint('pelvis', cog_ctrlSpaceMaster))
    mc.setAttr(cog_ctrlSpaceMaster + '.rx', 0), mc.setAttr(cog_ctrlSpaceMaster + '.ry', 0), mc.setAttr(cog_ctrlSpaceMaster + '.rz', 0)

    # clean
    spineIK_grp = mc.group(n='spine_IK_controls', em=True)
    mc.parent('spine_cl_master_ctrSpace', 'spine_cl1_master_ctrSpace', 'spine_cl2_master_ctrSpace', cog_ctrl), mc.parent(cog_ctrlSpaceMaster, spineIK_grp)
    mc.select(d=True)
    for i in clustersNodes:
        mc.setAttr(i + '.v', 0)
    mc.setAttr('spine_ik.v', 0)

######################################################### arm IK transform ################################################################

