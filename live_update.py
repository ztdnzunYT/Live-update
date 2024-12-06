import dearpygui.dearpygui as dpg
import keyboard
from screeninfo import get_monitors
import os 
from pathlib import Path
import re
import time
from multiprocessing import Process

monitor = get_monitors()[0]
screen_width = monitor.width
start_time = time.time()
live_update_pid = os.getpid()
running_pid_numbers_list = []
current_running_pid_numbers_list = [] 


dpg.create_context()
dpg.create_viewport(title="Live Update",width=315,height=550,x_pos=screen_width-300,y_pos=10,always_on_top=True,resizable=True)
dpg.setup_dearpygui()

def run_script():
    print("running script")
    global start_time, running_pid_numbers_list, num_pids, file_name, full_path

    running_pid_numbers_list.clear()

    try:
        
        dpg.show_item(search_loading_indicator)
        dpg.configure_item(insert_file_text,enabled=False)
        dpg.set_value(debug_console,value="")
    
    
        for pid_info in get_pids():
            split_pid = pid_info.split()
            if len(split_pid) > 0 :
                running_pid_numbers_list.append(split_pid[1])


        num_pids = len(running_pid_numbers_list)
        
        file_name = dpg.get_value(insert_file_text)
 
        for path in Path('C:/').rglob(file_name):  # Use '/' on Linux/macOS or 'C:/' on Windows
            
            split_path = str(path)
            full_path = path.resolve()
        
        py_path = split_path.split("\\")
        subfolder_num = len(py_path)-1

        print(py_path[subfolder_num][-3:])
        print(click_wait_time)

        if py_path[subfolder_num][-3:] == ".py":

            try:
                dpg.set_value(debug_console,value=f"Running file on path: \n{full_path}")
                dpg.set_value(display_py_file,value=dpg.get_value(insert_file_text))
                dpg.set_value(display_path,value=full_path)
                dpg.show_item(active_status)
                dpg.hide_item(inactive_status)
                start_time = time.time()
                dpg.hide_item(search_loading_indicator)
                dpg.show_item(active_loading_indicator)
                global status
                status = "Active"
                os.system(f"start py {full_path}")
            except:
                try:
                    os.system(f"start python3 {full_path}")
                except:
                    print("No file found")
                    reset()
        else:
            print("non .py")
            reset()
    except:
        print("Exception")
        reset()



        

"""
for path in Path('C:/').rglob(""):  # Use '/' on Linux/macOS or 'C:/' on Windows
    print(path)

os.system(f"py C:/Users/ztdnz/Documents/Capstone-Project-2024/xzplore/xzplore.py")

"""

def kill():
    #reset()
    print("kill button")
    #file_name = dpg.get_value(insert_file_text)
    '''
    for path in Path("C:/").rglob(file_name):
        full_path = path '''

    #os.system(f"taskkill /PID {full_path} /F ")

   

def reset():
    print("Program reset")
    global status
    status = "Inactive"
    dpg.set_value(debug_console,value="Unable to find .py file...")
    #dpg.set_value(insert_file_text,value="")
    dpg.set_value(display_py_file,value="")
    dpg.set_value(display_path,value="")
    dpg.show_item(inactive_status)
    dpg.hide_item(active_status)
    dpg.set_value(file_runtime,value="")
    dpg.hide_item(active_loading_indicator)
    dpg.hide_item(search_loading_indicator)
    dpg.configure_item(insert_file_text,enabled=True)

def on_key_pressed(event):
    global click_wait_time, click_start_time
    click_wait_time = 0
    click_start_time = time.time()    

def get_pids():
    os.system('tasklist | findstr python.exe > output.txt')

    with open('output.txt', 'r') as read_file:
        result = read_file.read()
        section = re.split("K", result)
    
    return section

def tab_window_display(sender,app_data,user_data):
    windows = [debug_console_window,window_manager_window,meta_data_window]
    for window in windows:
        dpg.hide_item(window)

    dpg.show_item(user_data)

def add_pid_console():
    global loop_time

    if loop_time > 100:

        pid_list = get_pids()

        for i in range(len(pid_list)-1):

            with dpg.group(horizontal=True,parent="window_manager_window"):
                dpg.add_text(f"{pid_list[i]}",parent="window_manager_window")
                dpg.add_button(label="Terminate file",callback=lambda:print("program closed"),parent="window_manager_window")
        #print(os.getpid())
        #os.system(f"taskkill /PID Python.exe")
        loop_time = 0
























        
with dpg.window(label="main_window",tag="main_window"):
    with dpg.group(horizontal=True):
        dpg.add_text("Status:")
        status = None
        inactive_status = dpg.add_text(f"Inactive",color=(240,230,14))
        active_status = dpg.add_text(f"Active  ",color=(0,255,0),show=False)
        dpg.add_spacer(width=50) 
        dpg.add_text("Auto Run")
        auto_run = dpg.add_checkbox(default_value=True)
        with dpg.tooltip(auto_run):
            dpg.add_text("Disables live update \nauto run when unchecked")
        active_loading_indicator = dpg.add_loading_indicator(style=1,radius=1,color=(0, 255, 0),show=False)
        search_loading_indicator = dpg.add_loading_indicator(style=1,radius=1,color=(0, 150, 200),show=False)
        
        
    dpg.add_separator()
    dpg.add_spacer(height=5)
    with dpg.group(horizontal=True):
        insert_file_text = dpg.add_input_text(width=200,hint="Insert file name",default_value="",tag="insert_file_text")

        with dpg.tooltip(insert_file_text): 
            with dpg.group():
                dpg.add_text("Ex: 'Filename.py'")
                dpg.add_text("Ex: 'Users/Documents/Filename.py'")
        dpg.add_button(label="Insert",callback=run_script)
    dpg.add_spacer(height=2)
    with dpg.group(horizontal=True):
        dpg.add_text("File Name:")
        display_py_file = dpg.add_text()
    with dpg.group(horizontal=True):
        dpg.add_text("Path:")  
        display_path = dpg.add_text(wrap=230)

    with dpg.group(horizontal=True):
        dpg.add_text("Runtime:")
        file_runtime = dpg.add_text()

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
        debug_console = dpg.add_input_text(height=45,width=265,multiline=True,enabled=False)
    
    with dpg.child_window(height=175,show=False,tag="window_manager_window") as window_manager_window:
        dpg.add_text("Current Console")
        pass

    with dpg.child_window(height=85,show=False,tag="metadata_window") as meta_data_window:
        dpg.add_text("metadata")
        
dpg.set_primary_window("main_window",True)
dpg.show_viewport()

loop_time = 0
click_start_time = time.time()
click_wait_time = 0 
file_inserted = False


while dpg.is_dearpygui_running():

    runtime = round(time.time() - start_time)
    click_wait_time = round(time.time() - click_start_time)

   
        
    keyboard.on_press(on_key_pressed)

    if status == "Active":
        dpg.set_value(file_runtime,f"{runtime} seconds")
        print(click_wait_time)

        if click_wait_time > 3:
            #print("Refresh",click_wait_time)
            try:
                os.system(f"taskkill /PID {insert_file_pid_number} /F")
                print("taskkileld")
                
                

            except:
                pass
            
            
            for pid_info in get_pids():
                split_pid = pid_info.split()
                if len(split_pid) > 0 :
                    current_running_pid_numbers_list.append(split_pid[1])
            
            for pid in running_pid_numbers_list:
                if pid in current_running_pid_numbers_list:
                    current_running_pid_numbers_list.remove(pid)
                    

            click_start_time = time.time()

            print()
            print(running_pid_numbers_list)
            print(current_running_pid_numbers_list)

            try:
                insert_file_pid_number = current_running_pid_numbers_list[0]
                print(insert_file_pid_number)
            except:
                pass
        
            print(dpg.get_value(insert_file_text))


        loop_time +=1

        #print(runtime)
        add_pid_console()
        current_running_pid_numbers_list.clear()

    
   # os.system("tasklist | findstr python")
 


    dpg.render_dearpygui_frame()
dpg.destroy_context()