# trace generated using paraview version 5.9.1

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
slice2 = FindSource('Slice2')

# set active source
SetActiveSource(slice2)



z_val = -800
k = 400


while z_val < k:

    # toggle 3D widget visibility (only when running from the GUI)
    Show3DWidgets(proxy=slice2.SliceType)

    # get color transfer function/color map for 'gold'
    goldLUT = GetColorTransferFunction('gold')
    goldLUT.RGBPoints = [0.013683000000000006, 0.0, 0.0, 1.90933e-05, 0.024387165578653745, 0.128363, 0.0636265, 0.0, 0.04346516443474919, 0.193795, 0.111057, 0.0, 0.07746817535841417, 0.25976, 0.15987, 0.0, 0.1380712723483029, 0.328546, 0.210589, 0.0, 0.2460839713815286, 0.399726, 0.26332, 0.0, 0.43859464710473006, 0.472969, 0.318261, 0.0, 0.7817057868051048, 0.546245, 0.375827, 0.0, 1.3932352917914927, 0.61745, 0.436719, 0.0, 2.4831635630469204, 0.685545, 0.501113, 0.0, 4.42573419359095, 0.749578, 0.568799, 0.0, 7.887971394154209, 0.80962, 0.6394, 0.0, 14.058705288966078, 0.865572, 0.712699, 0.10257, 25.05689926177251, 0.917709, 0.787569, 0.233665, 44.65882855985476, 0.966914, 0.863138, 0.369608, 79.59528222158067, 1.0, 0.939405, 0.496104, 136.83000000000007, 0.999225, 1.0, 0.612275]
    goldLUT.UseLogScale = 1
    goldLUT.ColorSpace = 'Lab'
    goldLUT.ScalarRangeInitialized = 1.0

    # get opacity transfer function/opacity map for 'gold'
    goldPWF = GetOpacityTransferFunction('gold')
    goldPWF.Points = [0.0, 0.0, 0.5, 0.0, 136.83, 1.0, 0.5, 0.0]
    goldPWF.ScalarRangeInitialized = 1

    # find source
    slice1 = FindSource('Slice1')

    # set active source
    SetActiveSource(slice1)

    # toggle 3D widget visibility (only when running from the GUI)
    Hide3DWidgets(proxy=slice2.SliceType)

    # toggle 3D widget visibility (only when running from the GUI)
    Show3DWidgets(proxy=slice1.SliceType)

    # find source
    tableToPoints1 = FindSource('TableToPoints1')

    # find source
    glyph1 = FindSource('Glyph1')

    # find source
    glyph6 = FindSource('Glyph6')

    # find source
    slice3 = FindSource('Slice3')

    # find source
    slice5 = FindSource('Slice5')

    # Properties modified on slice1.SliceType
    slice1.SliceType.Origin = [1876282.55, 3920581.55, z_val]

    # find source
    slice6 = FindSource('Slice6')

    # find source
    slice10 = FindSource('Slice10')

    # find source
    slice11 = FindSource('Slice11')

    # find source
    slice4 = FindSource('Slice4')

    # find source
    slice8 = FindSource('Slice8')

    # find source
    slice7 = FindSource('Slice7')

    # find source
    slice9 = FindSource('Slice9')

    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')

    # update the view to ensure updated data information
    renderView1.Update()

    # set active source
    SetActiveSource(slice2)

    # toggle 3D widget visibility (only when running from the GUI)
    Hide3DWidgets(proxy=slice1.SliceType)

    # toggle 3D widget visibility (only when running from the GUI)
    Show3DWidgets(proxy=slice2.SliceType)

    # Properties modified on slice2.SliceType
    slice2.SliceType.Origin = [1876282.55, 3920581.55, z_val]

    # update the view to ensure updated data information
    renderView1.Update()

    # set active source
    SetActiveSource(slice3)

    # toggle 3D widget visibility (only when running from the GUI)
    Hide3DWidgets(proxy=slice2.SliceType)

    # get color transfer function/color map for 'silver'
    silverLUT = GetColorTransferFunction('silver')
    silverLUT.RGBPoints = [0.005665000200000002, 0.0, 0.0, 0.0, 56.650002000000015, 1.0, 1.0, 1.0]
    silverLUT.UseLogScale = 1
    silverLUT.ColorSpace = 'RGB'
    silverLUT.NanColor = [1.0, 0.0, 0.0]
    silverLUT.ScalarRangeInitialized = 1.0

    # get opacity transfer function/opacity map for 'silver'
    silverPWF = GetOpacityTransferFunction('silver')
    silverPWF.Points = [0.0, 0.0, 0.5, 0.0, 56.650002, 1.0, 0.5, 0.0]
    silverPWF.ScalarRangeInitialized = 1

    # Properties modified on slice3.SliceType
    slice3.SliceType.Origin = [1876282.55, 3920581.55, z_val]

    # update the view to ensure updated data information
    renderView1.Update()

    # set active source
    SetActiveSource(slice4)

    # get color transfer function/color map for 'hg_ind'
    hg_indLUT = GetColorTransferFunction('hg_ind')
    hg_indLUT.RGBPoints = [0.0001, 0.101961, 0.101961, 0.101961, 0.0001782323986935575, 0.227451, 0.227451, 0.227451, 0.0003176678794405924, 0.359939, 0.359939, 0.359939, 0.0005661896888689036, 0.502653, 0.502653, 0.502653, 0.001009133463626637, 0.631373, 0.631373, 0.631373, 0.0017986027782411318, 0.749865, 0.749865, 0.749865, 0.003205692874628136, 0.843368, 0.843368, 0.843368, 0.005713583305198183, 0.926105, 0.926105, 0.926105, 0.01018348330798678, 0.999846, 0.997232, 0.995694, 0.018150302512949662, 0.994925, 0.908651, 0.857901, 0.032349719538967196, 0.982468, 0.800692, 0.706113, 0.05765768110493971, 0.960323, 0.66782, 0.536332, 0.10276466806441617, 0.894579, 0.503806, 0.399769, 0.18316077640764122, 0.81707, 0.33218, 0.281046, 0.3264518452570826, 0.728489, 0.155017, 0.197386, 0.5818429543810791, 0.576932, 0.055363, 0.14925, 1.0002441406250007, 0.403922, 0.0, 0.121569]
    hg_indLUT.UseLogScale = 1
    hg_indLUT.ColorSpace = 'Lab'
    hg_indLUT.ScalarRangeInitialized = 1.0

    # get opacity transfer function/opacity map for 'hg_ind'
    hg_indPWF = GetOpacityTransferFunction('hg_ind')
    hg_indPWF.Points = [0.0, 0.0, 0.5, 0.0, 1.000244140625, 1.0, 0.5, 0.0]
    hg_indPWF.ScalarRangeInitialized = 1

    # Properties modified on slice4.SliceType
    slice4.SliceType.Origin = [1876282.55, 3920581.55, z_val]

    # update the view to ensure updated data information
    renderView1.Update()

    # set active source
    SetActiveSource(slice5)

    # get color transfer function/color map for 'true_thick'
    true_thickLUT = GetColorTransferFunction('true_thick')
    true_thickLUT.RGBPoints = [0.0, 1.0, 1.0, 0.999967, 0.7058819999999987, 0.948461, 0.922603, 0.994449, 1.458821999999999, 0.89724, 0.838454, 0.994093, 2.2117619999999993, 0.850914, 0.752618, 0.992396, 2.964707999999996, 0.805017, 0.667956, 0.977626, 3.717647999999999, 0.74891, 0.590906, 0.93976, 4.4705879999999985, 0.688373, 0.517374, 0.895694, 5.223527999999998, 0.629381, 0.445284, 0.8448, 5.97647058, 0.567456, 0.380459, 0.778091, 6.729413999999998, 0.498202, 0.320012, 0.705799, 7.482353999999997, 0.431136, 0.260776, 0.637195, 8.235293999999996, 0.363211, 0.209286, 0.55306, 8.988233999999991, 0.296699, 0.163027, 0.461278, 9.741173999999999, 0.231446, 0.123339, 0.360511, 10.494119999999997, 0.167794, 0.0889224, 0.254953, 11.247059999999994, 0.100579, 0.0593111, 0.145666, 11.999999999999995, 4.264e-08, 0.0, 6.20844e-07]
    true_thickLUT.ColorSpace = 'Lab'
    true_thickLUT.ScalarRangeInitialized = 1.0

    # get opacity transfer function/opacity map for 'true_thick'
    true_thickPWF = GetOpacityTransferFunction('true_thick')
    true_thickPWF.Points = [0.0, 0.0, 0.5, 0.0, 12.0, 1.0, 0.5, 0.0]
    true_thickPWF.ScalarRangeInitialized = 1

    # Properties modified on slice5.SliceType
    slice5.SliceType.Origin = [1876282.55, 3920581.55, z_val]

    # update the view to ensure updated data information
    renderView1.Update()

    # set active source
    SetActiveSource(slice6)

    # get color transfer function/color map for 'DistanceToAndesiteCentroid'
    distanceToAndesiteCentroidLUT = GetColorTransferFunction('DistanceToAndesiteCentroid')
    distanceToAndesiteCentroidLUT.RGBPoints = [10.309238587288435, 0.054902, 0.109804, 0.121569, 53.47582042020929, 0.07451, 0.172549, 0.180392, 96.64240225313014, 0.086275, 0.231373, 0.219608, 139.80898408605097, 0.094118, 0.278431, 0.25098, 182.97556591897185, 0.109804, 0.34902, 0.278431, 226.14214775189268, 0.113725, 0.4, 0.278431, 269.30872958481353, 0.117647, 0.45098, 0.270588, 312.47531141773436, 0.117647, 0.490196, 0.243137, 355.64189325065524, 0.113725, 0.521569, 0.203922, 398.80847508357607, 0.109804, 0.54902, 0.152941, 441.97505691649695, 0.082353, 0.588235, 0.082353, 485.14163874941784, 0.109804, 0.631373, 0.05098, 528.3082205823385, 0.211765, 0.678431, 0.082353, 571.4748024152595, 0.317647, 0.721569, 0.113725, 614.6413842481803, 0.431373, 0.760784, 0.160784, 657.8079660811012, 0.556863, 0.8, 0.239216, 700.9745479140221, 0.666667, 0.839216, 0.294118, 744.1411297469429, 0.784314, 0.878431, 0.396078, 787.3077115798637, 0.886275, 0.921569, 0.533333, 830.4742934127845, 0.960784, 0.94902, 0.670588, 873.6408752457054, 1.0, 0.984314, 0.901961]
    distanceToAndesiteCentroidLUT.ColorSpace = 'Lab'
    distanceToAndesiteCentroidLUT.NanColor = [0.25, 0.0, 0.0]
    distanceToAndesiteCentroidLUT.ScalarRangeInitialized = 1.0

    # get opacity transfer function/opacity map for 'DistanceToAndesiteCentroid'
    distanceToAndesiteCentroidPWF = GetOpacityTransferFunction('DistanceToAndesiteCentroid')
    distanceToAndesiteCentroidPWF.Points = [10.309238587288435, 0.0, 0.5, 0.0, 873.6408752457054, 1.0, 0.5, 0.0]
    distanceToAndesiteCentroidPWF.ScalarRangeInitialized = 1

    # Properties modified on slice6.SliceType
    slice6.SliceType.Origin = [1876282.55, 3920581.55, z_val]

    # update the view to ensure updated data information
    renderView1.Update()

    # set active source
    SetActiveSource(slice7)

    # toggle 3D widget visibility (only when running from the GUI)
    Show3DWidgets(proxy=slice7.SliceType)

    # get color transfer function/color map for 'DistanceToCoreshedCentroid'
    distanceToCoreshedCentroidLUT = GetColorTransferFunction('DistanceToCoreshedCentroid')
    distanceToCoreshedCentroidLUT.RGBPoints = [67.68242183172354, 0.0, 0.0, 0.0, 114.62311292880847, 0.117562, 0.0291202, 0.175876, 161.5638040258934, 0.178368, 0.0458476, 0.285454, 208.50486918219497, 0.237731, 0.0680173, 0.387717, 255.44556027927985, 0.300877, 0.0956291, 0.484802, 302.38625137636484, 0.370929, 0.136858, 0.554985, 349.3269424734497, 0.449033, 0.189273, 0.58863, 396.26763357053466, 0.529971, 0.245796, 0.598587, 443.20853788137305, 0.609914, 0.300643, 0.610244, 490.14938982392124, 0.697079, 0.351286, 0.616371, 537.0900809210061, 0.785858, 0.401991, 0.617376, 584.030772018091, 0.862517, 0.45745, 0.64463, 630.9714631151761, 0.91359, 0.525462, 0.705336, 677.9125282714775, 0.932583, 0.61064, 0.767412, 724.8532193685625, 0.922478, 0.706966, 0.817522, 771.7939104656474, 0.901302, 0.803071, 0.856311, 815.8008551265666, 0.887571, 0.887591, 0.887549]
    distanceToCoreshedCentroidLUT.ColorSpace = 'Lab'
    distanceToCoreshedCentroidLUT.ScalarRangeInitialized = 1.0

    # get opacity transfer function/opacity map for 'DistanceToCoreshedCentroid'
    distanceToCoreshedCentroidPWF = GetOpacityTransferFunction('DistanceToCoreshedCentroid')
    distanceToCoreshedCentroidPWF.Points = [67.68242183172354, 0.0, 0.5, 0.0, 815.8008551265666, 1.0, 0.5, 0.0]
    distanceToCoreshedCentroidPWF.ScalarRangeInitialized = 1

    # Properties modified on slice7.SliceType
    slice7.SliceType.Origin = [1876282.55, 3920581.55, z_val]

    # update the view to ensure updated data information
    renderView1.Update()

    # set active source
    SetActiveSource(slice8)

    # toggle 3D widget visibility (only when running from the GUI)
    Hide3DWidgets(proxy=slice7.SliceType)

    # toggle 3D widget visibility (only when running from the GUI)
    Show3DWidgets(proxy=slice8.SliceType)

    # get color transfer function/color map for 'DistanceToCabexCentroid'
    distanceToCabexCentroidLUT = GetColorTransferFunction('DistanceToCabexCentroid')
    distanceToCabexCentroidLUT.RGBPoints = [20.506668403378196, 4.05298e-07, 0.0, 5.9012e-06, 73.14973969793196, 0.0207526, 0.0740933, 0.18093, 125.79281099248574, 0.0, 0.121033, 0.30343, 178.43630178716938, 0.0, 0.166892, 0.416095, 231.07937308172316, 0.0, 0.216768, 0.524796, 283.72244437627694, 0.0164769, 0.275471, 0.608585, 336.3655156708307, 0.0544527, 0.344824, 0.659267, 389.0085869653845, 0.0880643, 0.419118, 0.688675, 441.65189737501225, 0.127938, 0.492556, 0.720256, 494.2951490546219, 0.149476, 0.566946, 0.756918, 546.9382203491756, 0.188961, 0.641333, 0.792122, 599.5812916437295, 0.245482, 0.715336, 0.827609, 652.2243629382833, 0.329216, 0.786235, 0.874761, 704.8678537329669, 0.453558, 0.852803, 0.918466, 757.5109250275207, 0.626281, 0.910493, 0.954, 810.1539963220745, 0.82257, 0.958709, 0.980146, 859.5069280982348, 1.0, 1.0, 0.999989]
    distanceToCabexCentroidLUT.ColorSpace = 'Lab'
    distanceToCabexCentroidLUT.ScalarRangeInitialized = 1.0

    # get opacity transfer function/opacity map for 'DistanceToCabexCentroid'
    distanceToCabexCentroidPWF = GetOpacityTransferFunction('DistanceToCabexCentroid')
    distanceToCabexCentroidPWF.Points = [20.506668403378196, 0.0, 0.5, 0.0, 859.5069280982348, 1.0, 0.5, 0.0]
    distanceToCabexCentroidPWF.ScalarRangeInitialized = 1

    # Properties modified on slice8.SliceType
    slice8.SliceType.Origin = [1876282.55, 3920581.55, z_val]

    # update the view to ensure updated data information
    renderView1.Update()

    # set active source
    SetActiveSource(slice9)

    # toggle 3D widget visibility (only when running from the GUI)
    Hide3DWidgets(proxy=slice8.SliceType)

    # Properties modified on slice9.SliceType
    slice9.SliceType.Origin = [1876282.55, 3920581.55, z_val]

    # update the view to ensure updated data information
    renderView1.Update()

    # set active source
    SetActiveSource(slice10)

    # Properties modified on slice10.SliceType
    slice10.SliceType.Origin = [1876282.55, 3920581.55, z_val]

    # update the view to ensure updated data information
    renderView1.Update()

    # set active source
    SetActiveSource(slice11)

    # Properties modified on slice11.SliceType
    slice11.SliceType.Origin = [1876282.55, 3920581.55, z_val]

    #Update position for slice 12 to 21
    # set origins for slices 12 to 21
    for i in range(12, 22):
        slice_name = 'Slice' + str(i)
        slice_source = FindSource(slice_name)
        slice_source.SliceType.Origin = [1876282.55, 3920581.55, z_val]

    # update the view to ensure updated data information
    renderView1.Update()

    # get layout
    layout1 = GetLayout()

    # layout/tab size in pixels
    layout1.SetSize(1228, 560)

    # current camera placement for renderView1
    renderView1.InteractionMode = '2D'
    renderView1.CameraPosition = [1876282.55, 3920581.55, -3613.553861851266]
    renderView1.CameraFocalPoint = [1876282.55, 3920581.55, -185.25]
    renderView1.CameraViewUp = [1.0, 0.0, 0.0]
    renderView1.CameraParallelScale = 887.3103318456289

    # save screenshot
    SaveScreenshot('/home/vineethreddyv/ondemand/data/caserm/FinalSlices/10Inc/Z-axis/FinalSlice'+ str(z_val)[-4:] + 'm.png', renderView1, ImageResolution=[900, 1228])

    #================================================================
    # addendum: following script captures some of the application
    # state to faithfully reproduce the visualization during playback
    #================================================================

    #--------------------------------
    # saving layout sizes for layouts

    # layout/tab size in pixels
    layout1.SetSize(1221, 561)

    #-----------------------------------
    # saving camera placements for views

    # current camera placement for renderView1
    renderView1.InteractionMode = '2D'
    renderView1.CameraPosition = [1876282.55, 3920581.55, -3613.553861851266]
    renderView1.CameraFocalPoint = [1876282.55, 3920581.55, -185.25]
    renderView1.CameraViewUp = [1.0, 0.0, 0.0]
    renderView1.CameraParallelScale = 887.3103318456289

    #--------------------------------------------
    # uncomment the following to render all views
    # RenderAllViews()
    # alternatively, if you want to write images, you can use SaveScreenshot(...).

    z_val += 10