#!/usr/bin/python3.4

# Author: newadministrator a.k.a e.victor	#
# Date: 09/2020 							#
# What: DoItDir&File Toolkit  				#
# Lang: Python								#
# Disclaimer: You need python3.+			#

import platform, os, sys, shutil

yoursystemis = platform.system()

print("Your System is: "+yoursystemis+".\n")

if yoursystemis == "Windows":

    path = (os.environ['USERPROFILE'])

    mknow = ('\DoItDir&FileTool')

    path0 = (path+mknow)
    
    paqt = (path0+";")
    
    get11 = os.popen('reg query "HKEY_CURRENT_USER\Environment" /v "Path"').read()
  
    said0 = get11.replace('HKEY_CURRENT_USER\Environment\n','').replace('    ','').replace('PathREG_SZ','').replace('\n','').replace(paqt,'')
   
    stras = str(said0)
    
    wwhr = ('reg add "HKEY_CURRENT_USER\Environment" /v "Path" /d '+"\""+stras+"\""+" /f")
    
    if wwhr:
        os.system(wwhr)
        done = shutil.rmtree(path0)
        
    else:
        print("Error")
    
elif yoursystemis == "Linux" or yoursystemis == "Darwin":
    
    path0 = ("/usr/bin/DIDeFT")
    
    done = os.remove(path0)
    
else:
    print('\nUnknown System!'+' Unknown System!'+' Unknown System!'+' Unknown System!'+' Unknown System!')
    sys.exit()

if done:
    print("\nFinished!")
