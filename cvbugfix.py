import os
from re import L
import subprocess
import colorama
from termcolor import *
import configparser

colorama.init()
def process(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call).decode()
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())

def inifix(path):
   cvc = configparser.ConfigParser()
   cvc.read(path+"\cvtoolbars.ini")

   cvc.set("MainFrm.dxBarManager1.Bar0","Visible",'1')

   cvc.set("MainFrm.dxBarManager1.Bar1","DockedTop",'25')
   cvc.set("MainFrm.dxBarManager1.Bar1","Visible",'1')

   cvc.set("MainFrm.dxBarManager1.Bar2","DockedLeft",'372')
   cvc.set("MainFrm.dxBarManager1.Bar2","DockedTop",'25')
   cvc.set("MainFrm.dxBarManager1.Bar2","Visible",'1')

   cvc.set("MainFrm.dxBarManager1.Bar3","DockedTop",'81')
   cvc.set("MainFrm.dxBarManager1.Bar3","Visible",'1')

   cvc.set("MainFrm.dxBarManager1.Bar4","DockedTop",'53')
   cvc.set("MainFrm.dxBarManager1.Bar4","Visible",'1')

   cvc.set("MainFrm.dxBarManager1.Bar5","DockedLeft",'166')
   cvc.set("MainFrm.dxBarManager1.Bar5","DockedTop",'53')
   cvc.set("MainFrm.dxBarManager1.Bar5","Visible",'1')

   cvc.set("MainFrm.dxBarManager1.Bar6","DockedLeft",'573')
   cvc.set("MainFrm.dxBarManager1.Bar6","DockedTop",'53')
   cvc.set("MainFrm.dxBarManager1.Bar6","Visible",'1')

   cvc.set("MainFrm.dxBarManager1.Bar7","DockedLeft",'739')
   cvc.set("MainFrm.dxBarManager1.Bar7","DockedTop",'53')
   cvc.set("MainFrm.dxBarManager1.Bar7","Visible",'1')

   cvc.set("MainFrm.dxBarManager1.Bar7","DockedLeft",'881')
   cvc.set("MainFrm.dxBarManager1.Bar7","DockedTop",'53')
   cvc.set("MainFrm.dxBarManager1.Bar7","Visible",'1')

   with open(path+"\cvtoolbars.ini",'wt') as cvtoolbar :
      cvc.write(cvtoolbar,False)

   

if process("cvavr.exe"):
   os.system("taskkill /IM cvavr.exe")
   os.system("cls")



cprint("\n\n\n\n\n            CodeVision Bugfix            \n","yellow",attrs=["bold"])
cprint("  made by tsalehm","cyan")
print("\n\n"+"  for the white page bug, use UI fixer (fixes UI without removing settings)\n  for any other UI problem, use UI reset (UI settings will be reset) \n  and if your problem is not related to UI, try resetting all settings\n\n\n"+"  1 --> UI fixer\n  2 --> UI reset\n  3 --> reset all settings\n  then press \"Enter\" :\n\n")


while 1:
   how = input("  ")

   if how=='1':   
      try:
         inifix() 
         os.remove("C:\ProgramData\HP InfoTech\CodeVisionAVR\cvdocking.ini")
      except:

         cprint("\n\n  there is nothing to change! if the bug is not fixed, msg : @tsalehm in telegeam","red")
      else:
         cprint("\n\n  UI settings fixed successfully","green")
      finally:
         if bool(input("\n\n   press \"Enter\" to exit")):
            quit()


   elif how=='2':

      try: 
         if os.path.exists("C:\ProgramData\HP InfoTech\CodeVisionAVR\cvdocking.ini"):
            os.remove("C:\ProgramData\HP InfoTech\CodeVisionAVR\cvdocking.ini")
         os.remove("C:\ProgramData\HP InfoTech\CodeVisionAVR\cvtoolbars.ini")
#         os.remove("C:\ProgramData\HP InfoTech\CodeVisionAVR\cvavr.ini")
      except:
         cprint("\n\n  UI settings were already reset. if didn't work, try resetting all settings","red")
      else: 
         cprint("\n\n  UI settings reset successfully","green")
      finally:
         if input("\n\n   press \"Enter\" to exit")!='5':
            quit()

   elif how=='3':

      try: 
         if os.path.exists("C:\ProgramData\HP InfoTech\CodeVisionAVR\cvdocking.ini"):
            os.remove("C:\ProgramData\HP InfoTech\CodeVisionAVR\cvdocking.ini")
         if os.path.exists("C:\ProgramData\HP InfoTech\CodeVisionAVR\cvtoolbars.ini"):
            os.remove("C:\ProgramData\HP InfoTech\CodeVisionAVR\cvtoolbars.ini")
         os.remove("C:\ProgramData\HP InfoTech\CodeVisionAVR\cvavr.ini")
      except:
         cprint("\n\n  settings are reset before. if the bug is still remaining, try re-installing CodeVisin","red")
      else: 
         cprint("\n\n  all settings were reset successfully","green")
      finally:
         if input("\n\n   press \"Enter\" to exit")!='5':
            quit()


   else :
      print("\n  please enter '1' or '2' or '3' :\n\n")
