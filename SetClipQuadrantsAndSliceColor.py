from paraview.simple import *

# Get all sources in the pipeline
sources = GetSources()

# Get the active render view
render_view = GetActiveViewOrCreate('RenderView')

# Iterate through all sources
for source_name, source in sources.items():
    # Check if the source name starts with "ClipQuadrant" or "Slice"
    if source_name.startswith("ClipQuadrant") or source_name.startswith("Slice"):
        # Find the source
        clip = FindSource(source_name)
        if clip is None:
            continue  # Skip if the source is not found
        
        # Get the input of the source (parent glyph)
        parent_glyph = clip.Input
        
        # Access the display properties of the parent glyph
        glyph_display = GetDisplayProperties(parent_glyph, view=render_view)
        if glyph_display is not None:
            glyph_color = glyph_display.DiffuseColor  # Get the color of the parent glyph

            # Set the color of the Clip or Slice filter's display properties
            clip_display = GetDisplayProperties(clip, view=render_view)
            if clip_display is not None:
                clip_display.DiffuseColor = glyph_color

        # Ensure the pipeline updates for the source
        clip.UpdatePipeline()

# Render the updated scene
Render()
