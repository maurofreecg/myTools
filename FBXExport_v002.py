# Original writer scripter by Truong Cg Artist
# Modify by MauroFreeCG - FBXExport_v002


import maya.cmds as cmds
import pymel.core as pm
import maya.mel as mel
import os
import maya.OpenMaya as OpenMaya

mainBodyMesh = None
mainBodyMeshTF = "main_body_mesh_tf"
geoGrp = "geo_grp"
geoGrpTF = "geo_grp_tf"
deformSystemGrp = "deform_system_grp"
deformSystemGrpTF = "deform_system_grp_tf"
asVer = 0.0
trsUI_ID = "FBX_animation_baking"
bakeBoxValue = False
fbxPath = "fbx_save_path"
ikJointsList = []

# checks if there are unsaved changes, if yes, saves the scene first
def saveScene():
    fileState = cmds.file(q=True, modified=True)
    if fileState:
        cmds.SaveScene()
        print('Scene saved.')

# load fbx plugin if not loaded yet
def checkFBX():
    try:
        cmds.loadPlugin("fbxmaya")
    except:
        print("Failed to load fbx plugin!")

def chooseDeformSystemGrp():
    global deformSystemGrp
    cmds.select('root', 'GEO')

def find_most_influential_jnt(bodySkin, closestVert):
    # queries all joints influencing the current vertex with value above given threshold
    influences = cmds.skinPercent(bodySkin, closestVert, q=True, ignoreBelow=0.2, t=None)
    print(influences)
    inf_values_dict = {}
    for systemJnt in influences:
        inf_values_dict[systemJnt] = cmds.skinPercent(bodySkin, closestVert, q=True, t=systemJnt)

    sorted_inf_values = sorted(list(inf_values_dict.items()), key=lambda x: x[-1], reverse=True)
    # returns a list of tuples of each joint and its influence value
    # sorted by the influence value (key to sort is the result of lambda function: x[-1]: value of each key in dict)
    print(sorted_inf_values)
    # get the first item in the list
    most_influential_jnt = sorted_inf_values[0][0] # index 2 times to get the system joint name
    return most_influential_jnt

def BakeAll():
    startF = cmds.playbackOptions(q=True, minTime=True)
    print(startF)
    endF = cmds.playbackOptions(q=True, maxTime=True)
    print(endF)
    cmds.bakeResults(deformSystemGrp, hierarchy="below", simulation=True, sampleBy=1, t=(startF,endF))
    deformSystemJointList = cmds.listRelatives("DeformationSystem", allDescendents=True, type="joint")
    for j in deformSystemJointList:
        cmds.delete(j, cn=True)

def BakeIKJoints():
    global ikJointsList
    if not ikJointsList:
        raise Exception("ik Joint list is empty")
    # bake the joints
    startF = cmds.playbackOptions(q=True, minTime=True)
    print(startF)
    endF = cmds.playbackOptions(q=True, maxTime=True)
    print(endF)
    cmds.bakeResults(ikJointsList, simulation=True, sampleBy=1, t=(startF,endF))
    # delete the parent constraint (constraint is not needed after baking)
    cmds.delete(ikJointsList, cn=True)
    print("Done IK Joints baking")

def getFilePath():
    global fbxPath
    filepath = cmds.file(q=True, sn=True)
    folderPath = os.path.dirname(filepath)
    filename = os.path.basename(filepath)
    raw_name, extension = os.path.splitext(filename)
    fbxName = raw_name + ".fbx"
    fbxPath = (os.path.join(folderPath, fbxName)).replace(os.sep, '/')
    return fbxPath

def checkBoxOn():
    global bakeBoxValue
    bakeBoxValue = True
    print(bakeBoxValue)
    return bakeBoxValue

def checkBoxOff():
    global bakeBoxValue
    bakeBoxValue = False
    print(bakeBoxValue)
    return bakeBoxValue

def exportFBX():
    # select DeformationSystem & Geometry group
    global deformSystemGrp
    global geoGrp
    global bakeBoxValue
    global fbxPath
    #cmds.select([deformSystemGrp, geoGrp], replace=True)

    mel.eval("FBXExportSmoothingGroups -v true")
    mel.eval("FBXExportHardEdges -v false")
    mel.eval("FBXExportTangents -v false")
    mel.eval("FBXExportSmoothMesh -v true")
    mel.eval("FBXExportInstances -v false")
    mel.eval("FBXExportReferencedAssetsContent -v false")

    # Animation
    if bakeBoxValue:
        mel.eval("FBXExportBakeComplexAnimation -v true")
        mel.eval("FBXExportBakeComplexStep -v 1")
    else:
        mel.eval("FBXExportBakeComplexAnimation -v false")

    mel.eval("FBXExportUseSceneName -v false")
    mel.eval("FBXExportQuaternion -v euler")
    mel.eval("FBXExportShapes -v true")
    mel.eval("FBXExportSkins -v true")

    # Constraints
    mel.eval("FBXExportConstraints -v false")
    # Cameras
    mel.eval("FBXExportCameras -v false")
    # Lights
    mel.eval("FBXExportLights -v false")
    # Embed Media
    mel.eval("FBXExportEmbeddedTextures -v false")
    # Connections
    mel.eval("FBXExportInputConnections -v false")
    # Axis Conversion
    mel.eval("FBXExportUpAxis y")

    getFilePath()

    # Export!
    mel.eval('FBXExport -f "{0}" -s'.format(fbxPath))

def show_UI(winID):
    if cmds.window(winID, exists=True):
        cmds.deleteUI(winID)
    cmds.window(winID)
    create_UI(winID)
    cmds.showWindow(winID)

def create_UI(winID):
    cmds.window(winID, e=True, width=250)

    # Create the tabLayout
    tabControls = cmds.tabLayout()

    # Preparing tab
    tab1Layout = cmds.columnLayout()
    cmds.button(label="Save Scene", width=250, command='saveScene()')
    cmds.button(label="Check FBX Plugin", width=250, command='checkFBX()')
    cmds.text(label="\nSelect GEO // root\n")
    cmds.button(label="GEO // root - Selected", width=250, command='chooseDeformSystemGrp()')
    
    # We need to go back one to the tabLayout (the parent) to add the next tab layout.
    cmds.setParent('..')

   
    # Bake tab
    tab5Layout = cmds.columnLayout()
    cmds.text(label="\nExporting!\n")
    bakeBox = cmds.checkBox(label='Bake While Exporting - Recommended', value=False, onCommand='checkBoxOn()', offCommand='checkBoxOff()')
    cmds.button(label="Export FBX*", width=250, command='exportFBX()')
    cmds.text(label="* Check your Maya file folder for the FBX file\n", align="left")
    cmds.setParent('..')

    # Create appropriate labels for the tabs
    cmds.tabLayout(tabControls, edit=True, tabLabel=(
    (tab1Layout, "Pre"),  
    (tab5Layout, "Bake")))

show_UI(trsUI_ID)

def show_UI(winID):
    if cmds.window(winID, exists=True):
        cmds.deleteUI(winID)
    cmds.window(winID)
    create_UI(winID)
    cmds.showWindow(winID)

def create_UI(winID):
    cmds.window(winID, e=True, width=250)

    # Create the tabLayout
    tabControls = cmds.tabLayout()

    # Preparing tab
    tab1Layout = cmds.columnLayout()
    cmds.button(label="Save Scene", width=250, command='saveScene()')
    cmds.button(label="Check FBX Plugin", width=250, command='checkFBX()')
    cmds.text(label="\nSelect GEO // root\n")
    cmds.button(label="GEO // root Selected", width=250, command='chooseDeformSystemGrp()')
    # We need to go back one to the tabLayout (the parent) to add the next tab layout.
    cmds.setParent('..')

    # Bake tab
    tab5Layout = cmds.columnLayout()
    bakeBox = cmds.checkBox(label='Bake While Exporting', value=False, onCommand='checkBoxOn()', offCommand='checkBoxOff()')
    cmds.button(label="Export FBX*", width=250, command='exportFBX()')
    cmds.text(label="* Check your Maya file folder for the FBX file\n", align="left")
    cmds.setParent('..')

    # Create appropriate labels for the tabs
    cmds.tabLayout(tabControls, edit=True, tabLabel=(
    (tab1Layout, "Pre"),  
    (tab5Layout, "Bake")))

show_UI(trsUI_ID)
