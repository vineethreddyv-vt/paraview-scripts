from paraview.simple import *
# Disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Define the range for the x-axis values
x_coordinate = -2400.31601210717
y_coordinate = 4787.662482685926
z_axis_values = range(29700, 30570, 250)

# Define the normal vector for the slices
normal_vector = [0.3, 0.49, -1.0]

# Find all slices and save screenshots
for i, z_value in enumerate(z_axis_values, start=1):
    # Update the origin coordinates for the slices
    origin_coordinates = [x_coordinate, y_coordinate, z_value]

    # Iterate over all slices from Slice1 to Slice22
    for j in range(1, 50):
        slice_name = f'Slice{j}'
        slice_source = FindSource(slice_name)
        if slice_source:
            slice_source.SliceType.Origin = origin_coordinates
            slice_source.SliceType.Normal = normal_vector
        else:
            print(f"Warning: Source {slice_name} not found.")

    # Get active view
    renderView1 = GetActiveViewOrCreate('RenderView')


    # Reset camera (optional multiple resets if needed for proper alignment)
    renderView1.ResetCamera()

    z_rel_value = 30570 - z_value

    # Save screenshot with a filename that reflects the current x-axis value
    screenshot_filename = f'/projects/caserm/South Arturo/Data/Slices/{z_rel_value}_aucuas.png'
    SaveScreenshot(screenshot_filename, renderView1, ImageResolution=[1100, 1100])
    

    # Optional: Print confirmation for each screenshot saved
    print(f"Saved screenshot: {screenshot_filename}")

# Optionally render all views (uncomment the following line if needed)
# RenderAllViews()
