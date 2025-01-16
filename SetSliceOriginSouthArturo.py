#### Import the simple module from the paraview
from paraview.simple import *
import pandas as pd

#### Disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()


# Define the range for the z-axis values
x_coordinate = -2400.31601210717
y_coordinate = 4787.662482685926
z_axis_values = range(30410, 30430, 10)
# Define the normal vector for the slices
normal_vector = [0.3, 0.49, -1.0]




# Loop through the z-axis values
for z_value in z_axis_values:

        # Iterate over all slices from Slice1 to Slice22
    for j in range(1, 50):
        slice_name = f'Slice{j}'
        slice_source = FindSource(slice_name)
        if slice_source:
            slice_source.SliceType.Origin = [x_coordinate, y_coordinate, z_value]
            slice_source.SliceType.Normal = normal_vector
        else:
            print(f"Warning: Source {slice_name} not found.")


    # Get the active view
renderView1 = GetActiveViewOrCreate('RenderView')

    # Update the view to ensure updated data information
renderView1.Update()


