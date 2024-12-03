import dearpygui.dearpygui as dpg
import keyboard
from screeninfo import get_monitors
import os 
from pathlib import Path
import re

monitor = get_monitors()[0]
screen_width = monitor.width

dpg.create_context()
dpg.create_viewport(title="Live Update",width=315,height=550,x_pos=screen_width-300,y_pos=10,always_on_top=True,resizable=False)
dpg.setup_dearpygui()


def tab_window_display(sender,app_data,user_data):
    windows = [debug_console_window,window_manager_window,meta_data_window]
    for window in windows:
        if user_data == window:
            dpg.show_item(window)
        else:
            dpg.hide_item(window)
        

def run_script():
    print("inserted")

    file_name = dpg.get_value(insert_file)


    for path in Path('C:/').rglob(file_name):  # Use '/' on Linux/macOS or 'C:/' on Windows
            #print(path)
            full_path = path.resolve()
    
    print(full_path)

    try:
        
        
        try:
            os.system(f"py {full_path}")
        except:
            try:
                os.system(f"python3 {full_path}")
            except:
                print("Unable to find file...")
    except:
        print("Unable to find file...")
        
"""
for path in Path('C:/').rglob(""):  # Use '/' on Linux/macOS or 'C:/' on Windows
    print(path)

os.system(f"py C:/Users/ztdnz/Documents/Capstone-Project-2024/xzplore/xzplore.py")

"""
def kill():
    file_name = dpg.get_value(insert_file)
    for path in Path("C:/").rglob(file_name):
        full_path = path 

    #os.system(f"taskkill /PID {full_path} /F ")
    
with dpg.window(label="main_window",tag="main_window"):
    status = dpg.add_text(f"Status: Inactive")
    dpg.add_separator()
    dpg.add_spacer(height=5)
    with dpg.group(horizontal=True):
        insert_file = dpg.add_input_text(width=200,hint="Insert file name",default_value="Photon_precesion.py")
        with dpg.tooltip(insert_file): 
            with dpg.group():
                dpg.add_text("Ex: 'Filename.py'")
                dpg.add_text("Ex: 'Users/Documents/Filename.py'")
        dpg.add_button(label="Insert",callback=run_script)
    dpg.add_spacer(height=2)
    dpg.add_text("File Name:")
    dpg.add_text("Path:")    
    with dpg.group():
        dpg.add_text(f"Runtime: {None}")
    dpg.add_button(label="Kill Program",callback=kill)
    dpg.add_spacer(height=5)
    dpg.add_separator()
    dpg.add_text("1. Insert your file name into the textbox above.",wrap=270)
    dpg.add_text("2. File will only be executed if accompanied by .py || Ex: Filename.py",wrap=270)
    dpg.add_text("3. If file unable to be executed check for spelling errors or specify the full path of file",wrap=270) 
    dpg.add_separator()
    with dpg.tab_bar():
        dpg.add_tab_button(label="Debug Console",user_data="debug_console_window",callback=tab_window_display)
        dpg.add_tab_button(label="Window Manager",user_data="window_manager_window",callback=tab_window_display)
        dpg.add_tab_button(label="Metadata",user_data="metadata_window",callback=tab_window_display)

    with dpg.child_window(height=85,show=True,tag="debug_console_window") as debug_console_window:
        dpg.add_text("Debug Console")
        dpg.add_input_text(height=45,width=265,multiline=True,enabled=False)
    
    with dpg.child_window(height=175,show=False,tag="window_manager_window") as window_manager_window:
        pass
    
    with dpg.child_window(height=85,show=False,tag="metadata_window") as meta_data_window:
        dpg.add_text("metadata")
        

dpg.set_primary_window("main_window",True)
dpg.show_viewport()

runtime = 0 
# below replaces, start_dearpygui()
while dpg.is_dearpygui_running():

    runtime += 1 

    def on_key_pressed(event):
        return event.name
    
    keyboard.on_press(on_key_pressed)

    #print(runtime)
    if runtime > 100:
        print(" ")
        #print("killing task")
        
        os.system('tasklist | findstr python.exe > output.txt')

        with open('output.txt', 'r') as read_file:
            result = read_file.read()
            section = re.split("K", result)

        #print(result)
        
  
        print(section)

        for i in range(len(section)-1):

            with dpg.group(horizontal=True,parent="window_manager_window"):
                dpg.add_text(f"{section[i]}",parent="window_manager_window")
                dpg.add_button(label="Terminate file",callback=lambda:print("program closed"),parent="window_manager_window")
  

       # print(os.getpid())
   
        #os.system(f"taskkill /PID Python.exe")
        
        runtime = 0
    
    #os.system("tasklist | findstr python")
       
    
        
   

 


    # Register a global key press event listener

    # insert here any code you would like to run in the render loop
    # you can manually stop by using stop_dearpygui()
    
    dpg.render_dearpygui_frame()

dpg.destroy_context()