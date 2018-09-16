import os
import subprocess
root = os.getcwd()
opengl_render = True # TODO: get from argv
for i in os.walk('.'):
    print('entering',i[0])
    os.chdir(i[0])
    for j in i[2]:
        if j.endswith('.blend'):
            print('rendering',j)
            subprocess.call([f'blender','-P', root+"/render"+("_opengl" if opengl_render else "")+".py", j])
    print('exiting',i[0])
    os.chdir(root)

for i in os.popen('find').read().split('\n'):
    if i.endswith('.png'):
        j=i.split('/')[1:]
        os.popen('cp "'+i+'" "'+' '.join(j)+'"').read()

