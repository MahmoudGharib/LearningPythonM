
import os
#clear screen 
os.system ('cls')
# import d4Module.py to access the list of variables 
import d4Moudule
# import d4Lists 
import d4Lists

d4Lists.dirty_dozen.append("Manga")
d4Lists.dirty_dozen.extend(["a7a", "fash5", "bdan tneen"])
print(f'the new fruit lst is {d4Lists.dirty_dozen}')
dirtyLen = len ( d4Lists.dirty_dozen )
print (f' lenth of dity dozen is {dirtyLen}')




print ("")