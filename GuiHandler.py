import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Image Asciifier', width=850, height=500)

# define varibles
imageFilePath = "No file loaded"

# local varibles


def FileDialogCallback(sender, appData):
    imageFilePath = appData["file_path_name"]

with dpg.file_dialog(directory_selector=False, show=False, callback=FileDialogCallback, id="filePicker01", width=700, height=400, label="Select an Image"):
    dpg.add_file_extension("Supported image fileds (*.jpg){.jpg,jpeg}", color=(0, 255, 255, 255))

with dpg.window(label="Image Asciifier", tag="MainWindow"):

    dpg.add_separator()
    dpg.add_text(imageFilePath)
    dpg.add_button(label="Select Image File", callback=lambda: dpg.show_item("filePicker01"))

def InitGUI():
    dpg.set_primary_window("MainWindow", True)

    dpg.setup_dearpygui()

    dpg.show_viewport()
    dpg.start_dearpygui()

def CloseGUI():
    dpg.destroy_context()

if __name__ == "__main__":
    InitGUI()
    CloseGUI()