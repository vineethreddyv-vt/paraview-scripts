# trace generated using paraview version 5.9.1

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# set the origin coordinates
origin_coordinates = [1876282.55, 3920581.55, 300]

# find all sources from Slice1 to Slice22 and set their origin
for i in range(1, 23):
    slice_name = 'Slice' + str(i)
    slice_source = FindSource(slice_name)
    if slice_source:
        slice_source.SliceType.Origin = origin_coordinates
    else:
        print(f"Warning: Source {slice_name} not found.")

