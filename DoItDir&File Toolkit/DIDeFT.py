#!/usr/bin/python3

# Author: newadministrator a.k.a e.victor									    */
# Date: 09/2020 															    */
# What: DoItDir&File Toolkit  											        */
# Lang: Python															        */
# Disclaimer: You need python3.+                                                */
# Version: 1.1b                                                                 */

import os
import sys
import time
import hashlib
import itertools

def comco():

    os.system('cls||clear')
    
    print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
    print('This program has many functions, for example:')
    print('')
    print('. List of file(s) / (sub)directory(ies) with or without MD5;')
    print('')
    print('. List of MD5 from file(s) / (sub)directory(ies);')
    print('')
    print('. Check for duplicate(s) and unique(s) between files;')
    print('')
    print('. Replacement(s) in the file using a file as base;')
    print('')
    
    time.sleep(5.5)
    
    os.system('cls||clear')
    
    print('\n########################\n# DoItDir&File Toolkit #\n########################\n')   
    print('')
    print('Choose the option you want:\n')
    #print('1  - Check for duplicate(s) and unique(s) between files; \n2  - Replacement(s) in a file with wordlist; \n3  - List of file(s) with path; \n4  - List of MD5 of the file(s); \n5  - List of file(s) with (sub)directory(ies) + MD5; \n6  - List of (sub)directory(ies); \n7  - List of MD5 from (sub)directory(ies)*;  \n8  - List of (sub)directory(ies) + MD5*; \n9  - List of file(s) without path; \n10 - List of file(s) without path but with MD5;   \n11 - List of line(s) with same argument;   \n12 - Delete file(s) using wordlist;\n------------------------------------------------------------------\n')
    print('1  - Check for duplicate(s) and unique(s) between files; \n2  - Replacement(s) in a file with wordlist; \n3  - List of file(s) with path; \n4  - List of MD5 of the file(s); \n5  - List of file(s) with (sub)directory(ies) + MD5; \n6  - List of (sub)directory(ies); \n7  - List of file(s) without path(s); \n8  - List of file(s) without path but with MD5;   \n9  - List of line(s) with same argument;   \n10 - Delete file(s) using wordlist;\n------------------------------------------------------------------\n')
    #print('* -> string;\n\n')
    aescolha = input('Press the option: ')

    if aescolha == '1':
    
        #Check duplicate and unique line \/
        def aaa():
        
            os.system('cls||clear')
            
            print ('Starting the system . .. ...  .')
            
            time.sleep(1.5)
            os.system('cls||clear')
                        
            def aaa1():
            
                print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
            
                print('                                     \nThis system checks for unique(s) line(s) or\n duplicate(s) between 2 files.')
            
                print('\n\nWhat\'s the first file? (e.g: /home/xxx/arc1.txt): ')
                chocho = input()
                lock = os.path.isfile(chocho)
                
                if not lock:
                    os.system('cls||clear')
                    print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                    print('Invalid | the first file wasn\'t found, restarting . ..')
                    
                    time.sleep(2.5)
                    os.system('cls||clear')
                    
                    aaa1()
            
                if not chocho:
                
                    os.system('cls||clear')
                    
                    aaa1()
                
                def aaa2():
                
                    
                    print('\nWhat\'s the second file? (e.g: /home/xxx/arc2.txt): ')
                    
                    chocha = input()
                    
                    locka = os.path.isfile(chocha)
                    
                    if not locka:
                    
                        os.system('cls||clear')
                        
                        print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                        
                        print('Invalid | the second file wasn\'t found, restarting . ..')
                                              
                        time.sleep(2.5)
                        
                        os.system('cls||clear')
                        
                        print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                        
                        aaa2()
                        
                    if not chocha:

                        os.system('cls||clear')
                        aaa2()                        

                    if chocho == chocha:
                        
                        os.system('cls||clear')
                        print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                        print('\n\n"Same" files;')
                        print('\nThe system will be restarted, wait . .. .')
                        
                        time.sleep(5.5)
                        os.system('cls||clear')
                        
                        aaa1()
                        
                    a1 = open(chocho,'r')
                    a2 = open(chocha,'r')

                    textoA = a1.read()
                    textoB = a2.read()

                    textoA_words = textoA.split()
                    textoB_words = textoB.split()

                    igual = set(textoA_words).difference(set(textoB_words))
                    igual2 = set(textoB_words).difference(set(textoA_words))
                    igual3 = set(textoA_words).intersection(set(textoB_words))

                    if not igual:
                    
                        if not igual2:
                        
                            vale = '0'
                            os.system('cls||clear')
                        
                            print('\n########################\n# DoItDir&File Toolkit #\n########################\n')                            
                            print ('')
                            print ("UNIQUE(S) in 1° file:",chocho,'=',vale,end='.\n--')
                            print ("\nUNIQUE(S) in 2° file:",chocha,'=',vale,end='.\n--')
                            print ("\nDUPLICATE(S):", igual3,end='.')
                            print ('\n')
                            print ('\n_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/')
                            print('\nDo you want to do a new task, return to the main menu or exit?\n')
                            print('1 - New task\n2 - Main menu\n3 - Exit\n4 - Save the result\n')
                            nova = input('Press: ')
                        
                            if nova == '1':
                            
                                os.system('cls||clear')
                                
                                print('Ok! Wait . ..')
                                
                                time.sleep(1.5)
                                os.system('cls||clear')
                                
                                aaa()
                                
                            elif nova == '2' or nova == 'menu' or nova == 'Menu' or nova == 'm' or nova == 'M':
                            
                                os.system('cls||clear')
                                
                                print('Ok! Wait . ..')
                                
                                time.sleep(1.5)
                                os.system('cls||clear')
                                
                                comco()
                               
                                
                            elif nova == '3' or nova == 'exit' or nova == 'Exit' or nova == 'e' or nova == 'E':
                            
                                print('\n\nExiting..')
                                time.sleep(1.5)
                                os.system('cls||clear')
                                sys.exit()
                                
                            elif nova == '4' or nova == 'o' or nova == 's' or nova == 'S' or nova == 'save' or nova == 'Save':
                            
                                print('\nWhat will be the file name (e.g: /path/efinal.txt | efinal.txt): ')
                                leei = input()
                                                              
                                with open(leei, 'w', encoding='utf-8') as f:
                                    f.write('UNIQUE(S) in 1° file: '+chocho+' = '+vale+'\nUNIQUE(S) in 2° file: '+chocha+' = '+vale+"\nDUPLICATE(S): "+ str(igual3))
                                f.close()
                                print('\nFile created in: ',leei)
                                time.sleep(1.5)
                                
                                print('\nThe default is to return to the main menu!')
                                time.sleep(4.0)
                                comco()                                
                                
                    if not igual:
                        
                        vale = '0'
                        os.system('cls||clear')
                    
                        print('\n########################\n# DoItDir&File Toolkit #\n########################\n')                            
                        print ('')
                        print ("UNIQUE(S) in 1° file:",chocho,'=',vale,end='.\n--')
                        print ("\nUNIQUE(S) in 2° file:",chocha,'=',igual2,end='.\n--')
                        print ("\nDUPLICATE(S):", igual3,end='.')
                        print ('\n')
                        print ('\n_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/')
                        print('\nDo you want to do a new task, return to the main menu or exit?\n')
                        print('1 - New task\n2 - Main menu\n3 - Exit\n4 - Save the result\n')
                        nova = input('Press: ')
                    
                        if nova == '1':
                        
                            os.system('cls||clear')
                            
                            print('Ok! Wait . ..')
                            
                            time.sleep(1.5)
                            os.system('cls||clear')
                            
                            aaa()
                            
                        elif nova == '2' or nova == 'menu' or nova == 'Menu' or nova == 'm' or nova == 'M':
                        
                            os.system('cls||clear')
                            
                            print('Ok! Wait . ..')
                            
                            time.sleep(1.5)
                            os.system('cls||clear')
                            
                            comco()
                           
                            
                        elif nova == '3' or nova == 'exit' or nova == 'Exit' or nova == 'e' or nova == 'E':
                        
                            print('\n\nExiting..')
                            time.sleep(2.5)
                            os.system('cls||clear')
                            sys.exit()

                        elif nova == '4' or nova == 'o' or nova == 's' or nova == 'S' or nova == 'save' or nova == 'Save':
                        
                            print('\nWhat will be the file name (e.g: /path/efinal.txt | efinal.txt): ')
                            leei = input()
                                                          
                            with open(leei, 'w', encoding='utf-8') as f:
                                f.write('UNIQUE(S) in 1° file: '+chocho+' = '+vale+'\nUNIQUE(S) in 2° file: '+chocha+' = '+str(igual2)+"\nDUPLICATE(S): "+ str(igual3))
                            f.close()
                            print('\nFile created in: ',leei)
                            time.sleep(1.5)
                            
                            print('\nThe default is to return to the main menu!')
                            time.sleep(4.0)
                            comco()                            
                    
                    if not igual2:
                        
                        vale = '0'
                        os.system('cls||clear')
                    
                        print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                        print ('')
                        print ("UNIQUE(S) in 1° file:",chocho,'=',igual,end='.\n--')
                        print ("\nUNIQUE(S) in 2° file:",chocha,'=',vale,end='.\n--')
                        print ("\nDUPLICATE(S):", igual3,end='.')
                        print ('\n')
                        print ('\n_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/')
                        print('\nDo you want to do a new task, return to the main menu or exit?\n')
                        print('1 - New task\n2 - Main menu\n3 - Exit\n4 - Save the result\n')
                        nova = input('Press: ')
                    
                        if nova == '1':
                        
                            os.system('cls||clear')
                            
                            print('Ok! Wait . ..')
                            
                            time.sleep(1.5)
                            os.system('cls||clear')
                            
                            aaa()
                            
                        elif nova == '2' or nova == 'menu' or nova == 'Menu' or nova == 'm' or nova == 'M':
                        
                            os.system('cls||clear')
                            
                            print('Ok! Wait . ..')
                            
                            time.sleep(1.5)
                            os.system('cls||clear')
                            
                            comco()
                           
                            
                        elif nova == '3' or nova == 'exit' or nova == 'Exit' or nova == 'e' or nova == 'E':
                        
                            print('\n\nExiting..')
                            time.sleep(2.5)
                            os.system('cls||clear')
                            sys.exit()

                        elif nova == '4' or nova == 'o' or nova == 's' or nova == 'S' or nova == 'save' or nova == 'Save':
                        
                            print('\nWhat will be the file name (e.g: /path/efinal.txt | efinal.txt): ')
                            leei = input()
                                                          
                            with open(leei, 'w', encoding='utf-8') as f:
                                f.write('UNIQUE(S) in 1° file: '+chocho+' = '+str(igual)+'\nUNIQUE(S) in 2° file: '+chocha+' = '+vale+"\nDUPLICATE(S): "+ str(igual3))
                            f.close()
                            print('\nFile created in: ',leei)
                            time.sleep(1.5)
                            
                            print('\nThe default is to return to the main menu!')
                            time.sleep(4.0)
                            comco()
                    
                    if not igual3:
                        
                        vale = '0'
                        os.system('cls||clear')
                    
                        print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                        print ('')
                        print ("UNIQUE(S) in 1° file:",chocho,'=',igual,end='.\n--')
                        print ("\nUNIQUE(S) in 2° file:",chocha,'=',igual2,end='.\n--')
                        print ("\nDUPLICATE(S):", vale,end='.')
                        print ('\n')
                        print ('\n_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/')
                        print('\nDo you want to do a new task, return to the main menu or exit?\n')
                        print('1 - New task\n2 - Main menu\n3 - Exit\n4 - Save the result\n')
                        nova = input('Press: ')
                    
                        if nova == '1':
                        
                            os.system('cls||clear')
                            
                            print('Ok! Wait . ..')
                            
                            time.sleep(1.5)
                            os.system('cls||clear')
                            
                            aaa()
                            
                        elif nova == '2' or nova == 'menu' or nova == 'Menu' or nova == 'm' or nova == 'M':
                        
                            os.system('cls||clear')
                            
                            print('Ok! Wait . ..')
                            
                            time.sleep(1.5)
                            os.system('cls||clear')
                            
                            comco()
                           
                            
                        elif nova == '3' or nova == 'exit' or nova == 'Exit' or nova == 'e' or nova == 'E':
                        
                            print('\n\nExiting..')
                            time.sleep(2.5)
                            os.system('cls||clear')
                            sys.exit()     

                        elif nova == '4' or nova == 'o' or nova == 's' or nova == 'S' or nova == 'save' or nova == 'Save':
                        
                            print('\nWhat will be the file name (e.g: /path/efinal.txt | efinal.txt): ')
                            leei = input()
                                                          
                            with open(leei, 'w', encoding='utf-8') as f:
                                f.write('UNIQUE(S) in 1° file: '+chocho+' = '+str(igual)+'\nUNIQUE(S) in 2° file: '+chocha+' = '+str(igual2)+"\nDUPLICATE(S): "+ vale)
                            f.close()
                            print('\nFile created in: ',leei)
                            time.sleep(1.5)
                            
                            print('\nThe default is to return to the main menu!')
                            time.sleep(4.0)
                            comco()                            
                    
                    
                    else:
                                               
                        os.system('cls||clear')
                        
                        print ('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                        print ('')
                        print ("UNIQUE(S) in 1° file:",chocho,'=',igual,end='.\n--')
                        print ("\nUNIQUE(S) in 2° file:",chocha,'=',igual2,end='.\n--')
                        print ("\nDUPLICATE(S):", igual3,end='.')
                        print ('\n')
                        print ('\n_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/')
                        print ('\nDo you want to do a new task, return to the main menu or exit?\n')
                        print ('1 - New task\n2 - Main menu\n3 - Exit\n4 - Save the result\n')
                        nova = input('Press: ')
                    
                        if nova == '1':
                        
                            os.system('cls||clear')
                            
                            print('Ok! Wait . ..')
                            
                            time.sleep(1.5)
                            os.system('cls||clear')
                            
                            aaa()
                            
                        elif nova == '2' or nova == 'menu' or nova == 'Menu' or nova == 'm' or nova == 'M':
                        
                            os.system('cls||clear')
                            
                            print('Ok! Wait . ..')
                            
                            time.sleep(1.5)
                            os.system('cls||clear')
                            
                            comco()
                           
                            
                        elif nova == '3' or nova == 'exit' or nova == 'Exit' or nova == 'e' or nova == 'E':
                        
                            print('\n\nExiting..')
                            time.sleep(2.5)
                            os.system('cls||clear')
                            sys.exit()
                            
                        elif nova == '4' or nova == 'o' or nova == 's' or nova == 'S' or nova == 'save' or nova == 'Save':
                        
                            print('\nWhat will be the file name (e.g: /path/efinal.txt | efinal.txt): ')
                            leei = input()
                                                          
                            with open(leei, 'w', encoding='utf-8') as f:
                                f.write('UNIQUE(S) in 1° file: '+chocho+' = '+str(igual)+'\nUNIQUE(S) in 2° file: '+chocha+' = '+str(igual2)+"\nDUPLICATE(S): "+ str(igual3))
                            f.close()
                            print('\nFile created in: ',leei)
                            time.sleep(1.5)
                            
                            print('\nThe default is to return to the main menu!')
                            time.sleep(4.0)
                            comco()
                        
                aaa2()        
            aaa1()    
        aaa()
        #Check duplicate and unique line /\
        
    elif aescolha == '2':
    
        #Replace with wordlist \/
        def bbb():
        
            os.system('cls||clear')
            
            print ('Starting the system . .. ...  .')
            
            time.sleep(1.5)
            
            os.system('cls||clear')
            
            def bbb1():
                global x
                
                os.system('cls||clear')
                
                print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
            
                print('                             \nThis system does text(s) replacement(s) using wordlist as base.')
                
                print('\n\nWhat\'s the file that will be changed? (main) (e.g. /path/arc1.txt ou arc1.txt)')
                lha = input()
                za = os.path.isfile(lha)
                
                if not za:
                    
                    os.system('cls||clear')
                    
                    print('Invalid | not found, the system is restarting . ..')
                    
                    time.sleep(2.5)
                    os.system('cls||clear')
                    
                    bbb1()

                a1 = open(lha, 'r', encoding='utf-8')

                x = a1.read()
                a1.close()    
                
                def bbb2():
                    global x
                                                   
                    print('\nWhat\'s the file with wordlist? (e.g. /path/arc2.txt ou arc2.txt)')
                    vla = input()
                    zb = os.path.isfile(vla)
                    
                    if not zb:
                        
                        os.system('cls||clear')
                        
                        print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                        print('Invalid | not found, the system is restarting . ..')
                        
                        time.sleep(2.5)
                        os.system('cls||clear')
                        
                        print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                        
                        bbb2()
                    
                    print('\nReplace with? ( n_l = new line | (space) = blank | ... ): ')    
                    mudap = input() 

                    print('\nWhat will be the file name to be created? (e.g. /path/final.txt ou final.txt)\n(DO NOT CHOOSE A (FILE) NAME THAT ALREADY EXISTS!):')
                    gtr = input() 
                     
                    with open(vla,"r",encoding='utf-8') as arc:
                        
                        palavchas = []
                        
                        for line in arc:
                            
                            palavchas.append(line)
                            l1 = [nv for nv in itertools.chain.from_iterable(nv.split('\n') for nv in palavchas)]
                            l1 = ("\n".join(palavchas)).split("\n")
                            new_line = list(filter(None, l1))

                    tags = new_line
                    arc.close()
                    
                    if mudap == 'n_l':    
                        for tag in tags:
                            
                            x = x.replace(tag, '\n')
                    
                    else:
                        for tag in tags:
                            
                            x = x.replace(tag, mudap)

                    with open('tmp.txt', 'a', encoding='utf-8') as f:
                        
                        for item in x:
                        
                            f.write(item)
                            
                    f.close()
                          
                    t = open('tmp.txt', 'r+', encoding='utf-8')
                    t2 = open(gtr, 'a', encoding='utf-8')
                    isso = ("".join(line for line in t if not line.isspace()))
                    t2.write(isso)  
                    t2.close()
                    t.close()

                    if os.path.exists("tmp.txt"):
                    
                        os.remove("tmp.txt")
                        os.system('cls||clear')
                        
                        print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                        print('File generated!')
                        
                        time.sleep(2.5)
                        os.system('cls||clear')
                        
                        print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                        print('You can find it at:', gtr)
                        
                        time.sleep(2.5)
                        os.system('cls||clear')
                        
                        vale = '0'
                        print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                        print ('\n_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/')
                        print('\nDo you want to do a new task, return to the main menu or exit?\n')
                        print('1 - New task\n2 - Main menu\n3 - Exit\n')
                        nova = input('Press: ')
                    
                        if nova == '1':
                        
                            os.system('cls||clear')
                            
                            print('Ok! Wait . ..')
                            
                            time.sleep(1.5)
                            os.system('cls||clear')
                            
                            bbb()
                            
                        elif nova == '2' or nova == 'menu' or nova == 'Menu' or nova == 'm' or nova == 'M':
                        
                            os.system('cls||clear')
                            
                            print('Ok! Wait . ..')
                            
                            time.sleep(1.5)
                            os.system('cls||clear')
                            
                            comco()
                           
                            
                        elif nova == '3' or nova == 'exit' or nova == 'Exit' or nova == 'e' or nova == 'E':
                        
                            print('\n\nExiting..')
                            time.sleep(2.5)
                            os.system('cls||clear')
                            sys.exit()
                            
                bbb2()       
            bbb1()    
        bbb()      
        #Replace with wordlist /\ 
        
    elif aescolha == '3':
    
        #Only file list \/
        def ccc():
        
            os.system('cls||clear')
            
            print ('Starting the system . .. ...  .')
            
            time.sleep(1.5)
            
            os.system('cls||clear')
            
            def ccc1():
                
                print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                print('                                        \nThis system can do the list of file(s) using\ndirectory(ies) and subdirectory(ies) as base.')
                
                time.sleep(5.5)

                print('\nSet the directory/folder (e.g. /path/directory):')
                sa = input()
                diga = os.path.isdir(sa)
                
                if not diga:
                    
                    os.system('cls||clear')
                    
                    print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                    print('It\'s not a directory!')
                    
                    time.sleep(2.5)
                    os.system('cls||clear')
                    
                    print('Restarting .. .')
                    time.sleep(1.5)
                    ccc1()
                               
                print('\nSet the file name that will be generated (e.g. /path/directory/dump.txt or dump.txt):')
                ss = input()
                
                def ccc2(*tudo):
                    
                    if tudo:
                        
                        for item in tudo:
                            
                            for p, _, files in os.walk(os.path.abspath(item)):
                                
                                with open(ss, "a", encoding='UTF-8') as f:
                                    
                                    for file in files:
                                        
                                        quebra = (os.path.join(p, file))
                                        quebra2 = hashlib.md5(quebra.encode())
                                        
                                        if quebra2 == file:
                                            continue
                                        
                                        else:
                                            
                                            f.write(quebra+'\n')
                                f.close()
                    else:
                    
                        print('\nFile was successfully generated!')
                        
                        time.sleep(2.5)
                        os.system('cls||clear')
                        
                        vale = '0'
                        
                        print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                        print ('\n_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/')
                        print('\nDo you want to do a new task, return to the main menu or exit?\n')
                        print('1 - New task\n2 - Main menu\n3 - Exit\n')
                        nova = input('Press: ')
                    
                        if nova == '1':
                        
                            os.system('cls||clear')
                            
                            print('Ok! Wait . ..')
                            
                            time.sleep(1.5)
                            os.system('cls||clear')
                            
                            ccc()
                            
                        elif nova == '2' or nova == 'menu' or nova == 'Menu' or nova == 'm' or nova == 'M':
                        
                            os.system('cls||clear')
                            
                            print('Ok! Wait . ..')
                            
                            time.sleep(1.5)
                            os.system('cls||clear')
                            
                            comco()
                           
                            
                        elif nova == '3' or nova == 'exit' or nova == 'Exit' or nova == 'e' or nova == 'E':
                        
                            print('\n\nExiting..')
                            time.sleep(2.5)
                            os.system('cls||clear')
                            sys.exit()         
                        
                ccc2(sa)
                ccc2()
            ccc1()    
        ccc()
        #Only file list /\
        
    elif aescolha == '4':
    
        #Only MD5 from file \/
        def ddd():
        
            os.system('cls||clear')
            
            print ('Starting the system . .. ...  .')
            
            time.sleep(1.5)
            os.system('cls||clear')
                     
            def ddd1():
            
                print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                print('                                        \nThis system can do a list of hash(es) in MD5 of file(s)\n  using directory(ies) e subdirectory(ies) as base.')
                
                time.sleep(5.5)

                print('\n\nSet the directory/folder (e.g. /path/directory):')
                sa = input()
                diga = os.path.isdir(sa)
                
                if not diga:
                    
                    os.system('cls||clear')
                    
                    print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                    
                    print('It\'s not a directory!')
                    
                    time.sleep(2.5)
                    os.system('cls||clear')
                    
                    print('Restarting .. .')
                    
                    time.sleep(1.5)
                    os.system('cls||clear')
                    
                    ddd1()
                    
                print('\nSet the file name that will be generated (e.g. /path/directory/dump.txt or dump.txt):')
                ss = input()
                
                def ddd2(*tudo, bsize=2**20):
                                                           
                    if tudo:

                        for item in tudo:
                        
                            for p, _, files in os.walk(os.path.abspath(item)):
                            
                                for file in files:
                                                      
                                    file_path = (os.path.join(p, file))
                                    
                                    with open(file_path, "rb") as f:
                                        
                                        h4r = hashlib.md5()

                                        while True:
                                        
                                            d2t = f.read(bsize)
                                            
                                            if not d2t:
                                            
                                                break
                                            
                                            h4r.update(d2t)
                                            
                                            okap = h4r.hexdigest()
                                        
                                        with open(ss, "a", encoding='UTF-8') as faca:
                                            
                                            faca.write(okap+'\n')
                                        
                                        faca.close()                                            
                                                
                                    f.close()
                                
                    else:
                    
                        print('\nFile was successfully generated!')
                        
                        time.sleep(2.5)
                        os.system('cls||clear')
                        
                        vale = '0'
                        
                        print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                        print ('\n_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/')
                        print('\nDo you want to do a new task, return to the main menu or exit?\n')
                        print('1 - New task\n2 - Main menu\n3 - Exit\n')
                        nova = input('Press: ')
                    
                        if nova == '1':
                        
                            os.system('cls||clear')
                            
                            print('Ok! Wait . ..')
                            
                            time.sleep(1.5)
                            os.system('cls||clear')
                            
                            ddd1()
                            
                        elif nova == '2' or nova == 'menu' or nova == 'Menu' or nova == 'm' or nova == 'M':
                        
                            os.system('cls||clear')
                            
                            print('Ok! Wait . ..')
                            
                            time.sleep(1.5)
                            os.system('cls||clear')
                            
                            comco()
                           
                            
                        elif nova == '3' or nova == 'exit' or nova == 'Exit' or nova == 'e' or nova == 'E':
                        
                            print('\n\nExiting..')
                            time.sleep(2.5)
                            os.system('cls||clear')
                            sys.exit()                     
                        
                ddd2(sa)
                ddd2()
            ddd1()    
        ddd()
        #Only MD5 from files /\
        
    elif aescolha == '5':

        #List of files (with directory n' sub) and MD5 \/
        def eee():
        
            os.system('cls||clear')
            
            print ('Starting the system . .. ...  .')
            
            time.sleep(2.0)
            os.system('cls||clear')
            
            
            def eee1():
                    
                os.system('cls||clear')
                
                print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                print('                                        \nThis system can do the list of file(s) with your path(s) and your\nhash(es) in MD5 using directory(ies) and subdirectory(ies) as base.')
                
                time.sleep(8.5)
                
                print('\n\nSet the directory (folder) (e.g. /path/directory):')
                sa = input()
                diga = os.path.isdir(sa)
                
                if not diga:
                    
                    os.system('cls||clear')
                    
                    print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                    print('It\'s not a directory!')
                    
                    time.sleep(2.5)
                    os.system('cls||clear')
                    
                    print('Restarting .. .')
                    
                    time.sleep(1.5)
                    os.system('cls||clear')
                    
                    eee1()
                    
                print('\nSet the file name that will be generated (e.g. /path/directory/dump.txt or dump.txt): ')
                ss = input()
                
                def eee2(*tudo, bsize=2**20):
                
                    if tudo:

                        for item in tudo:
                        
                            for p, _, files in os.walk(os.path.abspath(item)):
                            
                                for file in files:
                                                      
                                    file_path = (os.path.join(p, file))
                                    
                                    with open(file_path, "rb") as f:
                                        
                                        h4r = hashlib.md5()

                                        while True:
                                        
                                            d2t = f.read(bsize)
                                            
                                            if not d2t:
                                            
                                                break
                                            
                                            h4r.update(d2t)
                                            
                                            okap = h4r.hexdigest()
                                        
                                        with open(ss, "a", encoding='UTF-8') as faca:
                                            
                                            faca.write(file_path+' = '+okap+'\n')
                                        
                                        faca.close()                                            
                                                
                                    f.close()
                    else:
                       
                        print('\nFile was successfully generated!')
                        
                        time.sleep(4.5)
                        os.system('cls||clear')
                        
                        vale = '0'
                        os.system('cls||clear')
                        print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                        print ('\n_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/')
                        print('\nDo you want to do a new task, return to the main menu or exit?\n')
                        print('1 - New task\n2 - Main menu\n3 - Exit\n')
                        nova = input('Press: ')
                    
                        if nova == '1':
                        
                            os.system('cls||clear')
                            
                            print('Ok! Wait . ..')
                            
                            time.sleep(1.5)
                            os.system('cls||clear')
                            
                            eee1()
                            
                        elif nova == '2' or nova == 'menu' or nova == 'Menu' or nova == 'm' or nova == 'M':
                        
                            os.system('cls||clear')
                            
                            print('Ok! Wait . ..')
                            
                            time.sleep(1.5)
                            os.system('cls||clear')
                            
                            comco()
                           
                            
                        elif nova == '3' or nova == 'exit' or nova == 'Exit' or nova == 'e' or nova == 'E':
                        
                            print('\n\nExiting..')
                            time.sleep(2.5)
                            os.system('cls||clear')
                            sys.exit()           
                        
                eee2(sa)
                eee2()
            eee1()    
        eee()
        #List of files (with directory n' sub) and MD5 /\

    elif aescolha == '6':

        # Only directory list n' sub \/
        def fff():
            
            os.system('cls||clear')
            
            print ('Starting the system . .. ...  .')
                      
            time.sleep(2.0)
            os.system('cls||clear')
            
            def fff1():
                
                print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                print('                             \nThis system can do a list of directory(ies) and\nsubdirectory(ies) using a main directory as base.')
                print('\n\nWhat\'s the directory (main)? (e.g. /path/directory): ')
                nada = input()
                diga = os.path.isdir(nada)
                
                if not diga:
                
                    os.system('cls||clear')
                    
                    print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                    print('It\'s not a directory!')
                    time.sleep(1.8)
                    
                    os.system('cls||clear')
                    
                    print('Restarting .. .')
                    
                    time.sleep(1.8)
                    
                    os.system('cls||clear')
                    
                    fff1()
                

                print('\nWhat will be the name of the file generated? (e.g. /path/result.txt ou result.txt): ')
                nada2 = input()
                
                for root,dirs,_ in os.walk(nada):
                
                    with open(nada2, "a", encoding='UTF-8') as f:
                    
                        for file in dirs:
                        
                            quebra = (os.path.join(root,file))
                            quebra2 = hashlib.md5(quebra.encode())
                            
                            if quebra2 == file:
                            
                                continue
                                
                            else:
                            
                                f.write(quebra+'\n')
                    f.close()
                    
                else:
                
                    print('\nFile was successfully generated!')
                    
                    time.sleep(2.5)                    
                    
                    vale = '0'
                    os.system('cls||clear')
                    
                    print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                    print ('\n_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/')
                    print('\nDo you want to do a new task, return to the main menu or exit?\n')
                    print('1 - New task\n2 - Main menu\n3 - Exit\n')
                    nova = input('Press: ')
                
                    if nova == '1':
                    
                        os.system('cls||clear')
                        
                        print('Ok! Wait . ..')
                        
                        time.sleep(1.5)
                        os.system('cls||clear')
                        
                        fff1()
                        
                    elif nova == '2' or nova == 'menu' or nova == 'Menu' or nova == 'm' or nova == 'M':
                    
                        os.system('cls||clear')
                        
                        print('Ok! Wait . ..')
                        
                        time.sleep(1.5)
                        os.system('cls||clear')
                        
                        comco()
                       
                        
                    elif nova == '3' or nova == 'exit' or nova == 'Exit' or nova == 'e' or nova == 'E':
                    
                        print('\n\nExiting..')
                        time.sleep(2.5)
                        os.system('cls||clear')
                        sys.exit()
            fff1()        
        fff()
        #Only directory list n' sub /\
    
    # elif aescolha == '7':

        # Only MD5 from directory n' sub \/
        # def ggg():
        
            # os.system('cls||clear')           
            
            # print ('Starting the system . .. ...  .')

            # time.sleep(2.0)
            # os.system('cls||clear')
            
            # def ggg1():
                
                # print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                # print('                             \nThis system can do a list of hash(es) in MD5 of directory(ies),\n       subdirectory(ies) using a main directory as base.*\n(*) - string;')
                
                # print('\n\nWhat\'s the directory (main)? (e.g. /path/directory): ')
                # nada = input()
                # diga = os.path.isdir(nada)
                
                # if not diga:
                
                    # print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                    # print('It\'s not a directory!')
                    
                    # time.sleep(1.5)
                    # os.system('cls||clear')
                    
                    # print('Restarting .. .')
                    
                    # time.sleep(1.5)
                    
                    # ggg1()
                
                # print('\nWhat will be the name of the file generated? (e.g. /path/result.txt ou result.txt): ') 
                # nada2 = input()
                
                # for root,dirs,_ in os.walk(nada):
                
                    # with open(nada2, "a", encoding='UTF-8') as f:
                    
                        # for file in dirs:
                        
                            # quebra = (os.path.join(root,file))
                            # quebra2 = hashlib.md5(quebra.encode())
                            
                            # if quebra2 == file:
                            
                                # continue
                                
                            # else:
                            
                                # f.write(quebra2.hexdigest()+'\n')
                    # f.close()
                
                # else:
                    
                    # print('\nFile was successfully generated!')
                    
                    # time.sleep(2.5)
                    
                    # vale = '0'
                    # os.system('cls||clear')
                    # print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                    # print ('\n_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/')
                    # print('\nDo you want to do a new task, return to the main menu or exit?\n')
                    # print('1 - New task\n2 - Main menu\n3 - Exit\n')
                    # nova = input('Press: ')
                
                    # if nova == '1':
                    
                        # os.system('cls||clear')
                        
                        # print('Ok! Wait . ..')
                        
                        # time.sleep(1.5)
                        # os.system('cls||clear')
                        
                        # ggg1()
                        
                    # elif nova == '2' or nova == 'menu' or nova == 'Menu' or nova == 'm' or nova == 'M':
                    
                        # os.system('cls||clear')
                        
                        # print('Ok! Wait . ..')
                        
                        # time.sleep(1.5)
                        # os.system('cls||clear')
                        
                        # comco()
                       
                        
                    # elif nova == '3' or nova == 'exit' or nova == 'Exit' or nova == 'e' or nova == 'E':
                    
                        # print('\n\nExiting..')
                        # time.sleep(2.5)
                        # os.system('cls||clear')
                        # sys.exit()
            # ggg1()    
        # ggg()
        #Only MD5 from directory n' sub /\   

    # elif aescolha == '8':

            #Directory, sub n' MD5 \/
        # def hhh():
        
            # os.system('cls||clear')
            
            # print ('Starting the system . .. ...  .')

            # time.sleep(2.0)
            # os.system('cls||clear')
            
            # def hhh1():
                
                # os.system('cls||clear')
                # print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                # print('                             \nThis system can make a list of directory(ies), subdirectory(ies) and\n with your hash(es) in MD5 using a main directory as base.*\n(*) - string;')
            
                # print('\n\nWhat\'s the directory (main)? (e.g. /path/directory)')
                # nada = input()
                # diga = os.path.isdir(nada)
            
                # if not diga:
                
                    # print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                    # print('It\'s not a directory!')
                    
                    # time.sleep(1.5)
                    # os.system('cls||clear')
                    
                    # print('Restarting .. .')
                    
                    # time.sleep(1.5)
                    
                    # hhh1()
                
                # print('\nWhat will be the name of the file generated? (e.g. /path/result.txt ou result.txt)')
                # nada2 = input()
               # if nada:#
                # for root,dirs,_ in os.walk(nada):
                
                    # with open(nada2, "a", encoding='UTF-8') as f:
                    
                        # for file in dirs:
                        
                            # quebra = (os.path.join(root,file))
                            # quebra2 = hashlib.md5(quebra.encode())
                            
                            # if quebra2 == file:
                            
                                # continue
                                
                            # else:
                            
                                # f.write(quebra+' = '+quebra2.hexdigest()+'\n')
                    # f.close()
                    
                # else:
                
                    # print('\nFile was successfully generated!')
                    
                    # time.sleep(2.5)
                    # vale = '0'
                    # os.system('cls||clear')
                    
                    # print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                    # print ('\n_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/')
                    # print('\nDo you want to do a new task, return to the main menu or exit?\n')
                    # print('1 - New task\n2 - Main menu\n3 - Exit\n')
                    # nova = input('Press: ')
                
                    # if nova == '1':
                    
                        # os.system('cls||clear')
                        
                        # print('Ok! Wait . ..')
                        
                        # time.sleep(1.5)
                        # os.system('cls||clear')
                        
                        # hhh1()
                        
                    # elif nova == '2' or nova == 'menu' or nova == 'Menu' or nova == 'm' or nova == 'M':
                    
                        # os.system('cls||clear')
                        
                        # print('Ok! Wait . ..')
                        
                        # time.sleep(1.5)
                        # os.system('cls||clear')
                        
                        # comco()
                       
                        
                    # elif nova == '3' or nova == 'exit' or nova == 'Exit' or nova == 'e' or nova == 'E':
                    
                        # print('\n\nExiting..')
                        # time.sleep(2.5)
                        # os.system('cls||clear')
                        # sys.exit() 
            # hhh1()        
        # hhh()
        #Directory, sub n' MD5 /\
    
    elif aescolha == '7':
    # elif aescolha == '9':
        # file list with directory
        def iii():
            
            os.system('cls||clear')
            
            print ('Starting the system . .. ...  .')
            
            time.sleep(2.0)
            os.system('cls||clear')
            
            
            def iii1():
                    
                os.system('cls||clear')
                
                print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                print('                                        \nThis system can do a list of file(s) (without your path(s) and without\n hash(es) in MD5) using directory(ies) and subdirectory(ies) as base.')
                
                time.sleep(8.5)
                
                print('\n\nSet the directory (folder) (e.g. /path/directory):')
                sa = input()
                diga = os.path.isdir(sa)
                
                if not diga:
                    
                    os.system('cls||clear')
                    
                    print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                    print('It\'s not a directory!')
                    
                    time.sleep(2.5)
                    os.system('cls||clear')
                    
                    print('Restarting .. .')
                    
                    time.sleep(1.5)
                    os.system('cls||clear')
                    
                    iii1()
                    
                print('\nSet the file name that will be generated (e.g. /path/directory/dump.txt or dump.txt): ')
                ss = input()
                
                def iii2(*tudo):
                
                    if tudo:
                    
                        for item in tudo:
                        
                            for p, _, files in os.walk(os.path.abspath(item)):
                            
                                with open(ss, "a", encoding='UTF-8') as f:
                                
                                    for file in files:
                                        
                                        quebra = (os.path.join(file))
                                        
                                        if quebra != file:
                                        
                                            continue
                                            
                                        else:
                                        
                                            f.write(quebra+'\n')
                                f.close()
                    else:
                       
                        print('\nFile was successfully generated!')
                        
                        time.sleep(4.5)
                        os.system('cls||clear')
                        
                        vale = '0'
                        os.system('cls||clear')
                        print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                        print ('\n_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/')
                        print('\nDo you want to do a new task, return to the main menu or exit?\n')
                        print('1 - New task\n2 - Main menu\n3 - Exit\n')
                        nova = input('Press: ')
                    
                        if nova == '1':
                        
                            os.system('cls||clear')
                            
                            print('Ok! Wait . ..')
                            
                            time.sleep(1.5)
                            os.system('cls||clear')
                            
                            iii1()
                            
                        elif nova == '2' or nova == 'menu' or nova == 'Menu' or nova == 'm' or nova == 'M':
                        
                            os.system('cls||clear')
                            
                            print('Ok! Wait . ..')
                            
                            time.sleep(1.5)
                            os.system('cls||clear')
                            
                            comco()
                           
                            
                        elif nova == '3' or nova == 'exit' or nova == 'Exit' or nova == 'e' or nova == 'E':
                        
                            print('\n\nExiting..')
                            time.sleep(2.5)
                            os.system('cls||clear')
                            sys.exit()           
                        
                iii2(sa)
                iii2()
            iii1()    
        iii()
        # file list with directory
        
    # elif aescolha == '10':
    elif aescolha == '8':
        # file list and hashes only
        def jjj():
        
            os.system('cls||clear')
            
            print ('Starting the system . .. ...  .')
            
            time.sleep(2.0)
            os.system('cls||clear')
            
            
            def jjj1():
                    
                os.system('cls||clear')
                
                print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                print('                                        \nThis system can do a list of file(s) (without your path(s)), but with your\n   hash(es) in MD5 using directory(ies) and subdirectory(ies) as base.')
                
                time.sleep(4.5)
                
                print('\n\nSet the directory (folder) (e.g. /path/directory):')
                sa = input()
                diga = os.path.isdir(sa)
                
                if not diga:
                    
                    os.system('cls||clear')
                    
                    print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                    print('It\'s not a directory!')
                    
                    time.sleep(2.5)
                    os.system('cls||clear')
                    
                    print('Restarting .. .')
                    
                    time.sleep(1.5)
                    os.system('cls||clear')
                    
                    jjj1()
                    
                print('\nSet the file name that will be generated (e.g. /path/directory/dump.txt or dump.txt): ')
                ss = input()
                
                def jjj2(*tudo, bsize=2**20):
                
                    if tudo:

                        for item in tudo:
                        
                            for p, _, files in os.walk(os.path.abspath(item)):
                            
                                for file in files:
                                                      
                                    file_path = (os.path.join(p, file))
                                    
                                    with open(file_path, "rb") as f:
                                        
                                        h4r = hashlib.md5()

                                        while True:
                                        
                                            d2t = f.read(bsize)
                                            
                                            if not d2t:
                                            
                                                break
                                            
                                            h4r.update(d2t)
                                            
                                            okap = h4r.hexdigest()
                                        
                                        with open(ss, "a", encoding='UTF-8') as faca:
                                            
                                            faca.write(file+' = '+okap+'\n')
                                        
                                        faca.close()                                            
                                                
                                    f.close()
                    else:
                       
                        print('\nFile was successfully generated!')
                        
                        time.sleep(4.5)
                        os.system('cls||clear')
                        
                        vale = '0'
                        os.system('cls||clear')
                        print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                        print ('\n_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/')
                        print('\nDo you want to do a new task, return to the main menu or exit?\n')
                        print('1 - New task\n2 - Main menu\n3 - Exit\n')
                        nova = input('Press: ')
                    
                        if nova == '1':
                        
                            os.system('cls||clear')
                            
                            print('Ok! Wait . ..')
                            
                            time.sleep(1.5)
                            os.system('cls||clear')
                            
                            jjj1()
                            
                        elif nova == '2' or nova == 'menu' or nova == 'Menu' or nova == 'm' or nova == 'M':
                        
                            os.system('cls||clear')
                            
                            print('Ok! Wait . ..')
                            
                            time.sleep(1.5)
                            os.system('cls||clear')
                            
                            comco()
                           
                            
                        elif nova == '3' or nova == 'exit' or nova == 'Exit' or nova == 'e' or nova == 'E':
                        
                            print('\n\nExiting..')
                            time.sleep(2.5)
                            os.system('cls||clear')
                            sys.exit()           
                        
                jjj2(sa)
                jjj2()
            jjj1()    
        jjj()
        # file list and hashes only
        
    # if aescolha == '11':
    if aescolha == '9':
        # Line list using keywords
        def kkk():
            os.system('cls||clear')
            
            print ('Starting the system . .. ...  .')
            
            time.sleep(2.0)
            os.system('cls||clear')
            
            
            def kkk1():
                    
                os.system('cls||clear')
                
                print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                print('                                        \nThis system can do a list of line(s) that \n     contain(s) specific keyword(s).')
                
                time.sleep(4.5)
                
                print('\n\nWhat\'s the base file? (e.g. /path/exa.txt | exa.txt):')
                valorize = input()
                diga = os.path.isfile(valorize)
                
                if not diga:
                    
                    os.system('cls||clear')
                    
                    print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                    print('It\'s not a file | not found!')
                    
                    time.sleep(2.5)
                    os.system('cls||clear')
                    
                    print('Restarting .. .')
                    
                    time.sleep(1.5)
                    os.system('cls||clear')
                    
                    kkk1()
                
                def kkk2(*tudo):
                
                    if tudo:

                        print ('\nList only if it contains?:')
        
                        querocafe = input()
                        
                        print ('\nSave where? (e.g. /path/text.txt | text.txt) :')
                        
                        aquio = input()
                        
                        with open(valorize) as f:
                        
                            for num, line in enumerate(f, 1):
                            
                                if querocafe in line:
                                
                                    with open(aquio, 'a', encoding='utf-8') as n:
                                    
                                        n.write(line)
                                        
                                    n.close()
                                    
                        f.close()
                        
                    else:
                       
                        print('\nFile was successfully generated!')
                        
                        time.sleep(4.5)
                        os.system('cls||clear')
                        
                        vale = '0'
                        os.system('cls||clear')
                        print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                        print ('\n_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/')
                        print('\nDo you want to do a new task, return to the main menu or exit?\n')
                        print('1 - New task\n2 - Main menu\n3 - Exit\n')
                        nova = input('Press: ')
                    
                        if nova == '1':
                        
                            os.system('cls||clear')
                            
                            print('Ok! Wait . ..')
                            
                            time.sleep(1.5)
                            os.system('cls||clear')
                            
                            kkk1()
                            
                        elif nova == '2' or nova == 'menu' or nova == 'Menu' or nova == 'm' or nova == 'M':
                        
                            os.system('cls||clear')
                            
                            print('Ok! Wait . ..')
                            
                            time.sleep(1.5)
                            os.system('cls||clear')
                            
                            comco()
                           
                            
                        elif nova == '3' or nova == 'exit' or nova == 'Exit' or nova == 'e' or nova == 'E':
                        
                            print('\n\nExiting..')
                            time.sleep(2.5)
                            os.system('cls||clear')
                            sys.exit()           
                        
                kkk2(valorize)
                kkk2()
            kkk1()         
        kkk()
        # Line list using keywords
        
    # if aescolha == '12':
    if aescolha == '10':
        #Delete files using a file(wordlist)
        def lll():
        
            os.system('cls||clear')
            
            print ('Starting the system . .. ...  .')
            
            time.sleep(2.0)
            os.system('cls||clear')
            
            
            def lll1():
                    
                os.system('cls||clear')
                
                print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                print('                                        \nThis system can delete file(s) using a wordlist as base.')
                
                time.sleep(8.5)
                
                print('\n\nWhat\'s the wordlist file with the path(s) to be deleted?:')
                valorize = input()
                
                print('')
                
                diga = os.path.isfile(valorize)
                
                if not diga:
                    
                    os.system('cls||clear')
                    
                    print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                    print('It\'s not a file | not found!')
                    
                    time.sleep(2.5)
                    os.system('cls||clear')
                    
                    print('Restarting .. .')
                    
                    time.sleep(1.5)
                    os.system('cls||clear')
                    
                    lll1()
                
                def lll2(*tudo):
                
                    if tudo:

                        with open(valorize, 'r+', encoding='utf-8') as faz:
                                    
                            for lixe in faz:

                                lines = [line.rstrip('\n') for line in lixe]
                                
                                convert = (''.join(lines))
                                
                                if os.path.isfile(convert):
                                    
                                    os.remove(convert)
                                    
                                    print('Deleted: '+convert)
                                    
                                else:
                                
                                    print('Doesn\'t exist or has already been deleted!')

                        faz.close()
                        
                    else:
                       
                        print('\nExecuted!')
                        
                        time.sleep(8.5)
                        os.system('cls||clear')
                        
                        vale = '0'
                        os.system('cls||clear')
                        print('\n########################\n# DoItDir&File Toolkit #\n########################\n')
                        print ('\n_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/')
                        print('\nDo you want to do a new task, return to the main menu or exit?\n')
                        print('1 - New task\n2 - Main menu\n3 - Exit\n')
                        nova = input('Press: ')
                    
                        if nova == '1':
                        
                            os.system('cls||clear')
                            
                            print('Ok! Wait . ..')
                            
                            time.sleep(1.5)
                            os.system('cls||clear')
                            
                            lll1()
                            
                        elif nova == '2' or nova == 'menu' or nova == 'Menu' or nova == 'm' or nova == 'M':
                        
                            os.system('cls||clear')
                            
                            print('Ok! Wait . ..')
                            
                            time.sleep(1.5)
                            os.system('cls||clear')
                            
                            comco()
                           
                            
                        elif nova == '3' or nova == 'exit' or nova == 'Exit' or nova == 'e' or nova == 'E':
                        
                            print('\n\nExiting..')
                            time.sleep(2.5)
                            os.system('cls||clear')
                            sys.exit()           
                        
                lll2(valorize)
                lll2()
            lll1()                
        lll()
        #Delete files using a file(wordlist)
        
    else:
        os.system('cls||clear')
        sys.exit()
    
comco()
