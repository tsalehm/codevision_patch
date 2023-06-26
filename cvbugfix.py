import os, subprocess, configparser
from colorama import init,Fore,Style


def process(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    output = subprocess.check_output(call).decode()
    last_line = output.strip().split('\r\n')[-1]

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

init()
print(Style.BRIGHT+Fore.YELLOW+"\n            CodeVision Bugfix            \n\n\n\n\n")
print(Style.RESET_ALL+Fore.CYAN+"view in github: https://github.com/tsalehm/codevision_patch")
print(Style.RESET_ALL+"\n\n"+"for the white page bug, use UI fixer (fixes UI without removing settings)\nfor any other UI problem, use UI reset (UI settings will be reset)\nand if your problem is not related to UI, try resetting all settings\n\n\n"+Fore.LIGHTMAGENTA_EX+"1 --> UI fixer\n2 --> UI reset\n3 --> reset all settings\nthen press \"Enter\" :\n\n")


paths=["C:\ProgramData\HP InfoTech\CodeVisionAVR"]
if os.path.exists(os.path.expandvars("$localappdata\google")):
   paths.append(os.path.expandvars("$localappdata\VirtualStore\ProgramData\HP InfoTech\CodeVisionAVR")) 
   
   
while 1:
   how = input()
      
   if how=='1':   
      try:
         for path in paths:
            if os.path.exists(os.path.join(path,"cvdocking.ini")): 
               os.remove(os.path.join(path,"cvdocking.ini"))
            if os.path.exists(os.path.join(path,"cvtoolbars.ini")):
               inifix(path)
      except Exception as e:
         print(Style.RESET_ALL+Fore.RED+"\n\nshoot! i can't do it! please open an issue in github about this and report this error:\n\n"+Style.RESET_ALL+Fore.WHITE+str(e))
      else:
         print(Style.RESET_ALL+Fore.GREEN+"\n\nUI settings fixed successfully. if it didn't work, try using next option and please! open an issue in github about this","green")
      finally:
         input(Style.RESET_ALL+"\n\npress \"Enter\" to exit")
         exit()

   elif how=='2':   
      try:
         for path in paths:
            if os.path.exists(os.path.join(path,"cvdocking.ini")): 
               os.remove(os.path.join(path,"cvdocking.ini"))
            if os.path.exists(os.path.join(path,"cvtoolbars.ini")):
               os.remove(os.path.join(path,"cvtoolbars.ini"))
      except:
         print(Style.RESET_ALL+Fore.RED+"\n\nshoot! i can't do it! please open an issue in github about this and report this error:\n\n"+Style.RESET_ALL+Fore.WHITE+str(e))
      else:
         print(Style.RESET_ALL+Fore.GREEN+"\n\nUI settings were reset successfully. if it didn't work, try using next option and please! open an issue in github about this","green")
      finally:
         input(Style.RESET_ALL+"\n\npress \"Enter\" to exit")
         exit()


   elif how=='3':   
      try:
         for path in paths:
            if os.path.exists(os.path.join(path,"cvdocking.ini")): 
               os.remove(os.path.join(path,"cvdocking.ini"))
            if os.path.exists(os.path.join(path,"cvtoolbars.ini")):
               os.remove(os.path.join(path,"cvtoolbars.ini"))
            if os.path.exists(os.path.join(path,"cvavr.ini")):
               os.remove(os.path.join(path,"cvavr.ini"))
      except:
         print(Style.RESET_ALL+Fore.RED+"\n\nshoot! i can't do it! please open an issue in github about this and report this error:\n\n"+Style.RESET_ALL+Fore.WHITE+str(e))
      else:
         print(Style.RESET_ALL+Fore.GREEN+"\n\nALL settings were reset successfully. if it didn't work, please! open an issue in github about this","green")
      finally:
         input(Style.RESET_ALL+"\n\npress \"Enter\" to exit")
         exit()

   else :
      print(Style.RESET_ALL+"\nplease enter '1' or '2' or '3' :\n\n")
