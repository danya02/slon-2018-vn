import os
import subprocess
import pygame
import sys
root = os.getcwd()
opengl_render = 'opengl' in sys.argv
for i in os.walk('.'):
    print('entering',i[0])
    os.chdir(i[0])
    for j in i[2]:
        if j.endswith('.blend'):
            print('rendering',j)
            if opengl_render:
                subprocess.call([f'blender','-P', root+"/render"+("_opengl" if opengl_render else "")+".py", j])
            else:
                subprocess.call(['blender', '--background', j, '--render-output','//'+j.split('.')[0].split('/')[-1]+'$$TEMP_PART####','--render-frame', '1'])
                for x in os.listdir('.'):
                    if '$$' in x:
                        xnew = x.split('$$')[0]+'.png'
                        subprocess.call(['mv',x,xnew])
    print('exiting',i[0])
    os.chdir(root)

if not opengl_render:
    exit()
pygame.init()
pygame.display.set_mode((10,10))

for i in os.popen('find').read().split('\n'):
    if i.endswith('0000.png'):
        os.rename(i,i.replace('0000.png',''))
for i in os.popen('find').read().split('\n'):
    if i.endswith('.png'):
        print(i)
        j=i.split('/')[1:]
        s = pygame.image.load(i)
        d = pygame.Surface(s.get_size(),pygame.SRCALPHA, 32)
        d=d.convert_alpha()
        for x in range(s.get_width()):
            for y in range(s.get_height()):
                c = s.get_at((x,y))
                if not (c.r==c.b==255 and c.g==0):
                    d.set_at((x,y),c)
                else:
                    d.set_at((x,y),pygame.Color(0,0,0,0))
        pygame.image.save(d,i)

pygame.quit()
