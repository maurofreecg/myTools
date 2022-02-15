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

    ##################################################### gear control ###########################################################
    def gear_ctrl(self, name='gear', itemColor=8):
        gearCtrl = mc.curve(d=True, p=((1.724336, 7.352745, 3.448672), (1.724336, 5.973276, 3.448672), (4.310841, 4.479957, 3.448672), (5.505496, 5.169692, 3.448672), (7.229832, 2.183053, 3.448672),
                                       (6.035176, 1.493319, 3.448672), (6.035176, -1.493319, 3.448672), (7.229832, -2.183053, 3.448672), (5.505496, -5.169692, 3.448672), (4.310841, -4.479957, 3.448672),
                                       (1.724336, -5.973276, 3.448672), (1.724336, -7.352745, 3.448672), (-1.724337, -7.352745, 3.448672), (-1.724337, -5.973276, 3.448672), (-4.310841, -4.479957, 3.448672),
                                       (-5.505496, -5.169692, 3.448672), (-7.229832, -2.183054, 3.448672), (-6.035176, -1.49332, 3.448672), (-6.035176, 1.493318, 3.448672), (-7.229832, 2.183052, 3.448672),
                                       (-5.505496, 5.16969, 3.448672), (-4.310841, 4.479956, 3.448672), (-1.724337, 5.973276, 3.448672), (-1.724337, 7.352745, 3.448672), (1.724336, 7.352745, 3.448672)), n=name + '_ctrl')
        gearCtrlSpace = mc.group(em=True, n=name + '_ctrlSpace')
        print(gearCtrl)
        gearCtrlSpaceMaster = mc.group(em=True, n=name + '_ctrlSpaceMaster')
        mc.parent(gearCtrl, gearCtrlSpace), mc.parent(gearCtrlSpace, gearCtrlSpaceMaster)
        mc.select(d=True)

    ############################################### line cross control ############################################################
    def lineCross_ctrl(self, name='lineCross', itemColor=8):
        lineCrossCtrl = mc.curve(d=True, p=((0, 6, 0), (0, -6, 0), (0, 0, 0), (0, 0, 6), (0, 0, -6), (0, 0, 0), (-6, 0, 0), (6, 0, 0)), n=name + '_ctrl')
        lineCrossCtrlSpace = mc.group(em=True, n=name + '_ctrlSPace')
        print(lineCrossCtrl)
        lineCrossCtrlSpaceMaster = mc.group(em=True, n=name + '_ctrlSpaceMaster')
        mc.parent(lineCrossCtrl, lineCrossCtrlSpace), mc.parent(lineCrossCtrlSpace, lineCrossCtrlSpaceMaster)
        mc.select(d=True)

    #################################################### diamondLow control #####################################################
    def diamondLow_ctrl(self, name='diamondLow', itemColor=8):
        diamondLowCtrl = mc.curve(d=True, p=((0, 6.092856, 0.473397), (0, 6.092856, 0.473397), (0, 6.092856, -0.473397), (6.092856, 0, -0.473397), (6.092856, 0, 0.473397), (0, 6.092856, 0.473397),
                                             (-6.092856, 0, 0.473397), (-6.092856, 0, -0.473397), (0, 6.092856, -0.473397), (6.092856, 0, -0.473397), (0, -6.092856, -0.473397), (0, -6.092856, 0.473397),
                                             (6.092856, 0, 0.473397), (6.092856, 0, -0.473397), (0, -6.092856, -0.473397), (-6.092856, 0, -0.473397), (-6.092856, 0, 0.473397), (0, -6.092856, 0.473397),
                                             (0, -6.092856, -0.473397)), n=name + '_ctrl')
        diamondLowCtrlSpace = mc.group(em=True, n=name + '_ctrlSpace')
        print(diamondLowCtrl)
        diamondLowCtrlSpaceMaster = mc.group(em=True, n=name + '_ctrlSpaceMaster')
        mc.parent(diamondLowCtrl, diamondLowCtrlSpace), mc.parent(diamondLowCtrlSpace, diamondLowCtrlSpaceMaster)
        mc.select(d=True)

    ################################################ diamondMid control #########################################################
    def diamondMid_ctrl(self, name='diamondMid', itemColor=8):
        diamondMidCtrl = mc.curve(d=True, p=((0, 0, 6.86093), (0, 6.86093, 0), (6.86093, 0, 0), (0, 0, 6.86093), (0, -6.86093, 0), (6.86093, 0, 0), (0, 6.86093, 0), (0, 0, -6.86093), (6.86093, 0, 0), (0, -6.86093, 0),
                                             (0, 0, -6.86093), (0, 6.86093, 0), (-6.86093, 0, 0), (0, 0, -6.86093), (0, -6.86093, 0), (-6.86093, 0, 0), (0, 6.86093, 0), (0, 0, 6.86093), (-6.86093, 0, 0), (0, -6.86093, 0),
                                             (0, 0, 6.86093)), n=name + '_ctrl')
        diamondMidCtrlSpace = mc.group(em=True, n=name + '_ctrlSpace')
        print(diamondMidCtrl)
        diamondMidCtrlSpaceMaster = mc.group(em=True, n=name + '_ctrlSpaceMaster')
        mc.parent(diamondMidCtrl, diamondMidCtrlSpace), mc.parent(diamondMidCtrlSpace, diamondMidCtrlSpaceMaster)
        mc.select(d=True)


myCtrl = myControls()

