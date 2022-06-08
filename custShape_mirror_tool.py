'''
CustShape_mirror tool_v01
Create mirror custumization on AF / AM rigs - AGS project
Andres Mauricio Trejos M
Aka -> MaurofreeCG - Rigger
'''

import maya.cmds as mc

#############################################################################################################################################################################################
###############################################################                                  Create loc                                 #################################################

leftBones_list = ['LeftUpLeg', 'LeftUpperlegHelper', 'LeftButtock', 'LeftUpperlegHelperUp', 'LeftUpperlegHelperDn', 'LeftLeg', 'LeftLowerleg', 'LeftLegRoll', 'LeftBreast',
                  'LeftShoulder', 'LeftArm', 'LeftUpperarm', 'LeftShoulderarmHelper_01', 'LeftArmRoll', 'LeftShoulderarmHelper_02', 'LeftForeArm', 'LeftLowerarm', 'LeftForeArmRoll', 'LeftWristHelper',
                  'LeftHipExpandLeft', 'LeftHand']

leftBones_loc_list = ['LeftUpLeg_locCust', 'LeftUpperlegHelper_locCust', 'LeftButtock_locCust', 'LeftUpperlegHelperUp_locCust', 'LeftUpperlegHelperDn_locCust', 'LeftLeg_locCust', 'LeftLowerleg_locCust',
                      'LeftLegRoll_locCust', 'LeftBreast_locCust', 'LeftShoulder_locCust', 'LeftArm_locCust', 'LeftUpperarm_locCust', 'LeftShoulderarmHelper_01_locCust', 'LeftArmRoll_locCust', 'LeftShoulderarmHelper_02_locCust',
                      'LeftForeArm_locCust', 'LeftLowerarm_locCust', 'LeftForeArmRoll_locCust',  'LeftWristHelper_locCust', 'LeftHipExpandLeft_locCust', 'LeftHand_locCust']

rightBones_list = ['RightUpLeg', 'RightUpperlegHelper', 'RightButtock', 'RightUpperlegHelperUp', 'RightUpperlegHelperDn', 'RightLeg', 'RightLowerleg',
                    'RightLegRoll', 'RightBreast', 'RightShoulder', 'RightArm', 'RightUpperarm', 'RightShoulderarmHelper_01', 'RightArmRoll', 'RightShoulderarmHelper_02',
                    'RightForeArm', 'RightLowerarm', 'RightForeArmRoll',  'RightWristHelper', 'RightHipExpandRight', 'RightHand']

centerBones_list = ['Hips_ExpandFront', 'HipsExpandBack', 'SpineScale', 'Spine1Scale', 'Spine2Scale', 'HipsExpand']

for i in leftBones_list:
    loc = mc.spaceLocator(n=i + '_locCust')
    locSpace = mc.group(loc, n=i + '_locCustSpace')
    mc.delete(mc.parentConstraint(i, loc, mo=False))


for j, item in enumerate(leftBones_loc_list):
    mc.parentConstraint(leftBones_list[j], item, mo=True)
    mc.connectAttr(leftBones_list[j] + '.s', item + '.s')

mc.select('*_locCustSpace')
locSpaceSel = mc.ls(sl=True)
mc.select(d=True)
locSpaceGRP = mc.group(n='locSpace_grp', em=True)
mc.parent(locSpaceSel, 'locSpace_grp')
mc.select(d=True)

print('locator constrained')

#############################################################################################################################################################################################
###############################################################        Bake locators and delete constrainst                                 #################################################

startF = mc.playbackOptions(q=True, minTime=True)
print(startF)
endF = mc.playbackOptions(q=True, maxTime=True)
print(endF)
mc.bakeResults(leftBones_loc_list, t=(startF, endF), sm=True)
########################################################################################################################################
##################################################### delete constraints ###############################################################
mc.select('*_locCust_parentConstraint1')
loc_pCon = mc.ls(sl=True)
mc.delete(loc_pCon)

#############################################################################################################################################################################################
###############################################################        Mirror control // connect to right side and bake                     #################################################

mc.select(locSpaceGRP)
mc.scale(-1, 1, 1)

# connect Left locator to right grp
for r, item in enumerate(rightBones_list):
    mc.pointConstraint(leftBones_loc_list[r], item, mo=True)
    mc.orientConstraint(leftBones_loc_list[r], item, mo=True)
    mc.connectAttr(leftBones_loc_list[r] + '.s', item + '.s', f=True)

#############################################################################################################################################################################################
###############################################################        Bake locators and delete constrainst final                           #################################################

startF = mc.playbackOptions(q=True, minTime=True)
print(startF)
endF = mc.playbackOptions(q=True, maxTime=True)
print(endF)
mc.bakeResults(rightBones_list, centerBones_list, t=(startF, endF), sm=True)
mc.delete(locSpaceGRP)

print(' - CUSTOM SHAPE MIRROR DONE // BAKE ALL BONES WITH TRANSFORMS IS COMPLETED - ')
