import winreg as wrg
import PySimpleGUI as sg
import sys
from pathlib import Path

root = Path(sys.executable).anchor
pathtocmd = root + "WINDOWS\system32\cmd.exe"

def CreateShortCut(shortcutname, path):
    location = wrg.HKEY_CLASSES_ROOT
    main_path = wrg.OpenKeyEx(location, r"DIRECTORY\\BACKGROUND\\SHELL\\")
    #---------------------------------------------------------------------#
    shortcut_key = wrg.CreateKey(main_path, "" + str(shortcutname))
    #---------------------------------------------------------------------#
    wrg.SetValueEx(shortcut_key, "", 0, wrg.REG_SZ, "" + str(shortcutname))               
    wrg.SetValueEx(shortcut_key, "Icon", 0, wrg.REG_SZ, "" + str(path))
    #---------------------------------------------------------------------#
    command_key = wrg.CreateKey(shortcut_key, "command")
    #---------------------------------------------------------------------#
    wrg.SetValueEx(command_key, "", 0 , wrg.REG_SZ,  "\"" + str(path) + "\"")
    #---------------------------------------------------------------------#
    #Closing keys after use
    if command_key: wrg.CloseKey(command_key)
    if shortcut_key: wrg.CloseKey(shortcut_key)


def DeleteShortCut(shortcutname):
    location = wrg.HKEY_CLASSES_ROOT
    main_path = wrg.OpenKeyEx(location, r"DIRECTORY\\BACKGROUND\\SHELL\\")
    #---------------------------------------------------------------------#
    shortcut_to_delete = wrg.CreateKey(main_path, "" + str(shortcutname))
    #---------------------------------------------------------------------#
    try: 
        delete_key = wrg.DeleteKey(shortcut_to_delete, "command")
    except WindowsError:
        a = 0
    
    try: 
        delete_key = wrg.DeleteKey(shortcut_to_delete, "")
    except WindowsError:
        a = 1
    


layout = [[sg.Text("C0NS0LE : STATUS", key="status")], [sg.Button("Add Console")], [sg.Button("Remove Console")]]
sg.theme("BlueMono")

window = sg.Window("ShortCut",layout,icon=pathtocmd, size=(220,110))

# Create an event loop
while True:
    event, values = window.read()
  
    if event == "Add Console":
        CreateShortCut("C0NS0L" , pathtocmd)
        window["status"].update("C0NS0LE: ACTIVATED",text_color = "LightGreen")
    if event == "Remove Console":
        DeleteShortCut("C0NS0L")
        window["status"].update("C0NS0LE: DEACTIVATED", text_color = "Red")
    if event == sg.WIN_CLOSED:
        break

window.close()










