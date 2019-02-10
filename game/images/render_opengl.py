# from https://blender.stackexchange.com/a/2575/61091
import bpy
import sys
import os
from bpy.app.handlers import persistent

@persistent
def do_render_opengl(dummy):
    bpy.data.scenes['Scene'].render.use_antialiasing=False
    bpy.data.scenes['Scene'].render.resolution_percentage=75
    bpy.data.scenes['Scene'].frame_start = 0
    bpy.data.scenes['Scene'].frame_end = bpy.data.scenes['Scene'].frame_start
    bpy.data.scenes['Scene'].render.alpha_mode = 'TRANSPARENT'
    # from https://blender.stackexchange.com/a/17746/61091
    area = next(area for area in bpy.context.screen.areas if area.type == 'VIEW_3D')
    space = next(space for space in area.spaces if space.type == 'VIEW_3D')
    space.viewport_shade = 'MATERIAL'
    bpy.ops.render.opengl(animation=True, view_context=True)
    bpy.ops.wm.quit_blender()

bpy.app.handlers.load_post.append(do_render_opengl)
