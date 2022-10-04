#!/usr/bin/python3

# Author: newadministrator a.k.a e.victor	#
# Date: 09/2020 							#
# What: DoItDir&File Toolkit  				#
# Lang: Python								#
# Disclaimer: You need python3.+			#

import platform, os, sys, shutil, time

yoursystemis = platform.system()

print("Your System is: "+yoursystemis+".\n")

if yoursystemis == "Windows":
    
    path = (os.environ['USERPROFILE'])

    mknow = ('\DoItDir&FileTool')

    path0 = (path+mknow)
        
    try:
        if not os.path.exists(path0):
            os.mkdir(path0)
            
        else:
            print ("\nAn error was identified, the required folder already exists, exiting ...!")
            sys.exit()
    
    except OSError:
        print ("Creation of the directory %s failed" % path0 + "\n")
    
    else:
        print ("\nSuccessfully created the directory %s " % path0 + "\n")
        
        Done = shutil.move("DIDeFT.py", path0)
               
        sayit = os.popen('reg query "HKEY_CURRENT_USER\Environment" /v "Path"').read()

        said0 = sayit.replace('HKEY_CURRENT_USER\Environment\n','').replace('    ','').replace('PathREG_SZ','').replace('\n','')

        stras = str(said0)

        ok = path0
        
        wwhr = ('reg add "HKEY_CURRENT_USER\Environment" /v "Path" /d '+"\""+stras+ok+";"+"\""+" /f") 
        
        if wwhr:
            os.system(wwhr)
            print("\n\n                   [WARNING]\n\n       Please, restart your Explorer.exe.\nYou may need to sign out and sign in again with your user.\n\n[ [ Required to link '.py' to the environment variables. ] ]")
            
        else:
            print("Error")
        
elif yoursystemis == "Linux" or yoursystemis == "Darwin":
    
    path0 = ("/usr/bin/")
    
    os.chmod('DIDeFT.py', 0o755)
    
    os.system('mv DIDeF.py DIDeF')
        
    Done = shutil.move("DIDeF", path0)
    
else:
    print('\nUnknown System!'+' Unknown System!'+' Unknown System!'+' Unknown System!'+' Unknown System!')
    sys.exit()

if Done:
    print("\n\nFinished!")
    time.sleep(3)
    
    

