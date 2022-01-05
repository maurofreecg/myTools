import maya.cmds as mc
import pymel.core as pm

selO = mc.ls(sl=True)

for i in (selO):
    grp = mc.group(n= i + '_ctrlSpace', em=True)
    crv = mc.circle( n= i + '_ctrl', ch=False)
    mc.parent(crv, grp)
    mc.delete(mc.parentConstraint(i, grp, mo=False))
    pm.connectAttr(('%s.r'%crv[0]), ('%s.r'%i))
    pm.connectAttr(('%s.s'%crv[0]), ('%s.s'%i))
    multM = mc.createNode('multMatrix', n= i + '_MM')
    decM = mc.createNode('decomposeMatrix', n= i + '_DM')
    pm.connectAttr(multM + '.matrixSum', decM + '.inputMatrix')
    pm.connectAttr(('%s.worldMatrix[0]'%crv[0]), ('%s.matrixIn[0]'%multM), f=True)
    pm.connectAttr(str(i) + '.parentInverseMatrix[0]', multM + '.matrixIn[1]', f=True)
    pm.connectAttr(decM + '.outputTranslate', i + '.t')