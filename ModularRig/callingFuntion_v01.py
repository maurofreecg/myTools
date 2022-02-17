import pymel.core as pm
import importlib
import utility as ut
import hierarchyJntTempletes as hierarchyJntTempletes
importlib.reload(ut)
importlib.reload(hierarchyJntTempletes)
myHJntTemp = hierarchyJntTempletes.myHierarchyJntTempletes()

######################################## window
def windowRig():
    window_name = 'modularRig_v001'
    window_width = 300
    bgcLabelColor = (.1,.1,.1)

    if (pm.window(window_name, q=True, ex=True)):
        pm.deleteUI(window_name)
    window = pm.window(window_name, w=300, h=200, bgc=(0.13, 0.13, .13))
    pm.window(window_name, edit=True, width=300, height=400)

    ################################# neck
    colMain = pm.columnLayout("MainColumn", h=50, bgc=(.13, .13, .13))
    imgColumn = pm.columnLayout(h=40, bgc=(.15, .15, .15))
    pm.rowColumnLayout(nc=3, w=window_width, h=30)
    pm.text(l='Neck Rig', w=window_width/3, bgc=(.3,.3,.3))
    neckTemp_buttom = pm.button(l='Neck Templete', w=window_width/3, bgc=(.3,.3,.4))
    neckBuild_buttom = pm.button(l='Neck Build', w=window_width/3, bgc=(.3,.3,.4))

    ############################### spine
    pm.setParent(colMain)
    pm.separator(w=300, h=20)
    pm.rowColumnLayout(nc=4, w=window_width, h=40)
    pm.text(l='Spine Rig', w=window_width/3, bgc=(.3,.3,.3))
    spineTemp_buttom = pm.button(l='Spine Templete', w=window_width/3, bgc=(.3,.3,.4))
    spineBuildIK_buttom = pm.button(l='Spine IK', w=window_width/6, bgc=(.3,.3,.4))
    spineBuildFK_buttom = pm.button(l='Spine FK', w=window_width/6, bgc=(.3,.3,.4))

    ############################### arm
    pm.setParent(colMain)
    pm.separator(w=300, h=20)
    pm.rowColumnLayout(nc=4, w=window_width, h=40)
    pm.text(l='Arm Rig', w=window_width/3, bgc=(.3,.3,.3))
    armTemp_buttom = pm.button(l='Arm Templete', w=window_width/3, bgc=(.3,.3,.4))
    armBuildIK_buttom = pm.button(l='Arm IK', w=window_width/6, bgc=(.3,.3,.4))
    armBuildFK_buttom = pm.button(l='Arm FK', w=window_width/6, bgc=(.3,.3,.4))

    ############################### leg
    pm.setParent(colMain)
    pm.separator(w=300, h=20)
    pm.rowColumnLayout(nc=3, w=window_width, h=40)
    pm.text(l='Leg Rig', w=window_width/3, bgc=(.3,.3,.3))
    legTemp_buttom = pm.button(l='Leg Templete', w=window_width/3, bgc=(.3,.3,.4))
    legBuildFK_buttom = pm.button(l='Leg Build', w=window_width/3, bgc=(.3,.3,.4))

    ############################### biped
    pm.setParent(colMain)
    pm.separator(w=300, h=20)
    pm.rowColumnLayout(nc=3, w=window_width, h=40)
    pm.text(l='Biped Rig', w=window_width/3, bgc=(.3,.3,.3))
    bipedTemp_buttom = pm.button(l='Biped Templete', w=window_width/3, bgc=(.3,.3,.4))
    bipedBuild_buttom = pm.button(l='Biped Build', w=window_width/3, bgc=(.3,.3,.4))

    ############################## note
    pm.setParent(colMain)
    pm.text(l='--- The idea is create our own Modular Rig for future projects --')
    pm.text(l='                  --- I hope you like this progress --')
    pm.separator(w=300, h=20)
    pm.text(l='             --- With love - Rigging team --', w=window_width, bgc=(.3,.3,.3), h=30)

    ######################### calling functions
    ### neck head
    neckTemp_buttom.setCommand(myHJntTemp.neckHeadT)
    neckBuild_buttom.setCommand(ut.neck_FK_transform)
    ### spine
    spineTemp_buttom.setCommand(myHJntTemp.spineT)
    spineBuildIK_buttom.setCommand(ut.spine_IK_transform)
    spineBuildFK_buttom.setCommand(ut.spine_FK_transfomr)
    ### arm
    armTemp_buttom.setCommand(myHJntTemp.armT)
    armBuildIK_buttom.setCommand(ut.arm_fingers_IK_transform)
    armBuildFK_buttom.setCommand(ut.arm_fingers_FK_transform)
    ### leg
    legTemp_buttom.setCommand(myHJntTemp.legT)
    legBuildFK_buttom.setCommand(ut.leg_FK_Transform)
    ### biped
    bipedTemp_buttom.setCommand(myHJntTemp.bipedT)
    bipedBuild_buttom.setCommand(ut.biped_FK_transform)

    pm.showWindow(window_name)