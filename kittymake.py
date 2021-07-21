import os
file=open("kittymake.kme",'r')
s=file.read()
cmds=s.split('\n')
for cmd in cmds:

        if cmd[:2]==('cd') :
                os.chdir(cmd[3:])
                continue
        elif cmd[:2]==(r'//') :
                continue
        else: 
                os.system(cmd)
    

file.close()
