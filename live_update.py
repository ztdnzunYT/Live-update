import dearpygui.dearpygui as dpg
import keyboard
from screeninfo import get_monitors
import os 
from pathlib import Path

monitor = get_monitors()[0]
screen_width = monitor.width

dpg.create_context()
dpg.create_viewport(title="Live Update",width=300,x_pos=screen_width-300,y_pos=10, height=350,always_on_top=True,resizable=False)
dpg.setup_dearpygui()

def run_script():
    file_name = dpg.get_value(file)

    try:
        for path in Path('C:/').rglob(file_name):  # Use '/' on Linux/macOS or 'C:/' on Windows
            print(path)
            full_path = path
        
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





with dpg.window(label="main_window",tag="main_window"):
    status = dpg.add_text(f"Status: Inactive")
    dpg.add_separator()
    dpg.add_spacer(height=5)
    with dpg.group(horizontal=True):
        file = dpg.add_input_text(width=200,hint="Insert file name")
        with dpg.tooltip(file): 
            with dpg.group():
                dpg.add_text("Ex: 'Filename.py'")
                dpg.add_text("Ex: 'Users/Documents/Filename.py'")
        dpg.add_button(label="Insert",callback=run_script)
    dpg.add_spacer(height=2)
    dpg.add_text("File Name:")
    dpg.add_text("Path:")    
    with dpg.group():
        dpg.add_text(f"Runtime: {None}")
    dpg.add_spacer(height=5)
    dpg.add_separator()
    dpg.add_text("1. Insert your file name into the textbox above.",wrap=270)
    dpg.add_text("2. File will only be executed if accompanied by .py || Ex: Filename.py",wrap=270)
    dpg.add_text("3. If file unable to be executed check for spelling errors or specify the full path of file",wrap=270)

dpg.set_primary_window("main_window",True)
dpg.show_viewport()

# below replaces, start_dearpygui()
while dpg.is_dearpygui_running():

    def on_key_pressed(event):
        return event.name
    
    keyboard.on_press(on_key_pressed)

    
   




    # Register a global key press event listener

    # insert here any code you would like to run in the render loop
    # you can manually stop by using stop_dearpygui()
    
    dpg.render_dearpygui_frame()

dpg.destroy_context()