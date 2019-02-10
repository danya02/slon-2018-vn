import bpy
import os
from bpy.app.handlers import persistent

@persistent
def do_render(dummy):
    bpy.data.scenes['Scene'].render.resolution_percentage=75
    bpy.data.scenes['Scene'].frame_start = 0
    bpy.data.scenes['Scene'].frame_end = bpy.data.scenes['Scene'].frame_start
    bpy.data.scenes['Scene'].render.alpha_mode = 'TRANSPARENT'

    bpy.ops.render.render(write_still=True)
    bpy.ops.wm.quit_blender()
bpy.app.handlers.load_post.append(do_render)
