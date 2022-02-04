import maya.cmds as mc

#######################################################################
#
#
#                           Controls
#
#
#######################################################################

class myControls():
    def __init__(self, name='text', itemColor=8, isFkCtrl=True):
        self.name = name
        self.itemColor = itemColor
        self.isFkCtrl = isFkCtrl
        self.shape = None

    ################################################ square control ########################################################
    def square_ctrl(self, name='square', itemColor=8):
        squareCtrl = mc.curve(d=True, p=((4.364857, 4.364857, 4.364857), (4.364857, -4.364857, 4.364857), (4.364857, -4.364857, -4.364857),
                                          (4.364857, 4.364857, -4.364857),(4.364857, 4.364857, 4.364857), (-4.364857, 4.364857, 4.364857), (-4.364857, -4.364857, 4.364857),
                                          (4.364857, -4.364857, 4.364857),(4.364857, 4.364857, 4.364857), (4.364857, 4.364857, -4.364857), (-4.364857, 4.364857, -4.364857),
                                          (-4.364857, 4.364857, 4.364857),(-4.364857, -4.364857, 4.364857), (-4.364857, -4.364857, -4.364857), (-4.364857, 4.364857, -4.364857),
                                          (4.364857, 4.364857, -4.364857),(4.364857, -4.364857, -4.364857), (-4.364857, -4.364857, -4.364857)), n=name + '_ctrl')
        squareCtrlSpace = mc.group(em=True, n=name + '_ctrlSpace')
        print(squareCtrl)
        squareCtrlSpaceMaster = mc.group(em=True, n=name + '_ctrlSpaceMaster')
        mc.parent(squareCtrl, squareCtrlSpace), mc.parent(squareCtrlSpace, squareCtrlSpaceMaster)
        mc.select(d=True)

    ######################################################## cone control ######################################################
    def cone_ctrl(self, name='cone', itemColor=8):
        coneCtrl = mc.curve(d=True, p=((1.540524, 0.153401, 0), (0, 3.234449, 0), (0.476048, 0.153401, -1.465125), (-1.24631, 0.153401, -0.905497), (0, 3.234449, 0), (-1.24631, 0.153401, 0.905497),
                                       (0.476048, 0.153401, 1.465125), (0, 3.234449, 0), (-1.24631, 0.153401, 0.905497), (0.476048, 0.153401, 1.465125), (1.540524, 0.153401, 0), (0.476048, 0.153401, -1.465125),
                                       (-1.24631, 0.153401, -0.905497), (-1.24631, 0.153401, 0.905497)), n=name + '_ctrl')
        coneCtrlSpace = mc.group(em=True, n=name + '_ctrlSpace')
        print(coneCtrl)
        coneCtrlSpaceMaster = mc.group(em=True, n=name + '_ctrlSpaceMaster')
        mc.parent(coneCtrl, coneCtrlSpace), mc.parent(coneCtrlSpace, coneCtrlSpaceMaster)
        mc.select(d=True)

    ################################################### rectangle control ##########################################################
    def rectangle_ctrl(self, name='rectangle', itemColor=8):
        rectangleCtrl = mc.curve(d=True, p=((7.235142, 6.870199, 11.285807), (7.235142, 6.870199, -11.285807), (7.235142, -6.870199, -11.285807), (7.235142, -6.870199, 11.285807), (7.235142, 6.870199, 11.285807),
                                            (-3.602244, 9.883969, 16.236584), (-3.602244, -9.883969, 16.236584), (-3.602244, -9.883969, -16.236584), (-3.602244, 9.883969, -16.236584), (7.235142, 6.870199, -11.285807),
                                            (7.235142, 6.870199, 11.285807), (-3.602244, 9.883969, 16.236584), (-3.602244, 9.883969, -16.236584), (-3.602244, -9.883969, -16.236584), (7.235142, -6.870199, -11.285807),
                                            (7.235142, -6.870199, 11.285807), (-3.602244, -9.883969, 16.236584), (-3.602244, -9.883969, -16.236584)), n=name + '_ctrl')
        rectangleCtrlSpace = mc.group(em=True, n=name + '_ctrlSpace')
        print(rectangleCtrl)
        rectangleCtrlSpaceMaster = mc.group(em=True, n=name + '_ctrlSpaceMaster')
        mc.parent(rectangleCtrl, rectangleCtrlSpace), mc.parent(rectangleCtrlSpace, rectangleCtrlSpaceMaster)
        mc.select(d=True)


myCtrl = myControls()
