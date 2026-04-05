import os
import sys
import time

#  ____ ___ ____ _____ ___  _   _ 
# |  _ \_ _/ ___|_   _/ _ \| \ | |
# |_) | |\___ \ | || | | |  \| |
# |  __/| | ___) || || |_| | |\  |
# |_|  |___|____/ |_| \___/|_| \_|                                
# made by classiccatlinux
# 1.2_stable - foss - 4/3/2026

# == basic ==
def clear():
    if sys.platform == "win32":
        os.system('cls')
    else:
        os.system('clear')
        
def wait(wt):
    time.sleep(wt)
    
def stop3(): 
    print("exiting...")
    wait(3)
    clear()
    exit()

def cmd(c):
    os.system(c)

ms = lambda x: time.sleep(x / 1000)


    


