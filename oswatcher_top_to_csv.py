# -*- coding: utf-8 -*-
"""
More information on how to install oswatcher tool.
https://www.2daygeek.com/oswbb-how-to-install-and-configure-oswatcher-black-box-for-system-diagnostics/

"""

#OWSTOP file path
OSWATCHER_TOP_FILE = './test.dat'
FILE_TO_WRITE = './output.csv'

CURRENT = None

parts = []

replacements =[
    #find -> replace
    (' ',''),
    ('%us',''),
    ('%sy',''),
    ('%ni',''),
    ('%id',''),
    ('%wa',''),
    ('%hi',''),
    ('%si',''),
    ('%st',''),
    ('%total',''),
    ('%used',''),
    ('%free',''),
    ('%buffers',''),
    ('%cached',''),
    ('%running',''),
    ('%sleeping',''),
    ('%stopped',''),
    ('%zombie','')
    ]


#Iterate through the oswtop file and extract time & system stats.
with open(OSWATCHER_TOP_FILE,'r') as f:
    for line in f:
        if line.startwith('zzz'):
            CURRENT = [(line.replace('zzz ***','')).strip()]
            parts.append(CURRENT)
        elif CURRENT is not None:
            if 'load average:' in line:
                linestr = line[line.find('load average:')]
                for target, replacement in replacements:
                    linestr = linestr.replace(target, replacement)
                CURRENT.append((linestr.replace('loadaverage:','')).strip())
                #print(current)
            if line.startwith('Cpu(s):'):
                for target, replacement in replacements:
                    linestr = linestr.replace(target, replacement)
                CURRENT.append((linestr.replace('Cpu(s):','')).strip())
            if line.startwith('Mem:'):
                for target, replacement in replacements:
                    linestr = linestr.replace(target, replacement)
                CURRENT.append((linestr.replace('Mem:','')).strip())
            if line.startwith('Swap:'):
                for target, replacement in replacements:
                    linestr = linestr.replace(target, replacement)
                CURRENT.append((linestr.replace('Swap:','')).strip())
            if line.startwith('Tasks:'):
                for target, replacement in replacements:
                    linestr = linestr.replace(target, replacement)
                CURRENT.append((linestr.replace('Tasks:','')).strip())


#Save extracted data to the file
with open(FILE_TO_WRITE,'w+') as f:
    f.write("time,1MinLoad,5MinLoad,15MinLoad,Task-Total,Task-run,Tasks-sleep,Task-stop,Task-zombie,%us,%sy,%ni,%id,%wa,%hi,%si,%st,Mem-total,Mem-used,Mem-free,Mem-buffer,Swp-total,Swp-used,Swp-free,Swp-cached\n")
    f.write('\n'.join((','.join(part) for part in parts)))