# main.py
from ast import Lambda
from cProfile import label
from email.policy import default
import ImageProcesser
import dearpygui.dearpygui as dpg

import imageio.v3 as imageio

dpg.create_context()
dpg.create_viewport(title='Image Asciifier', width=850, height=500)

# local varibles
imageFilePath = "No file selected"
characterWidth = 4
characterHeight = 10

defaultGreyRamp = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1\{\}[]?-_+~<>i!lI;:,\"^`'. "

cancel = False

ImageProcesser.greyRamp = defaultGreyRamp

def FileDialogCallback(sender, appData):
    global imageFilePath
    imageFilePath = appData["file_path_name"]
    dpg.set_value("FileNameDisplay", imageFilePath)

def ProgressCallback(progress, max):
    dpg.set_value("ProgressBar", progress / max)

    if (cancel):
        dpg.configure_item("ProgressModal", show=False)

    return cancel

def Generate():
    global cancel
    cancel = False

    dpg.set_value("ProgressBar", 0)
    dpg.configure_item("ProgressModal", show=True)

    characterWidth = dpg.get_value("CharWidth")
    characterHeight = dpg.get_value("CharHeight")

    image = imageio.imread(imageFilePath)
    ascii = ImageProcesser.GenerateAscii(image, characterWidth, characterHeight, ProgressCallback)

    dpg.configure_item("ProgressModal", show=False)

    print("\n", ascii)

def CancelCallback():
    cancel = True

def GreyrampCallback(sender, data):
    ImageProcesser.greyRamp = data

with dpg.file_dialog(directory_selector=False, show=False, callback=FileDialogCallback, id="filePicker01", width=700, height=400, label="Select an Image"):
    dpg.add_file_extension("Supported image fileds (*.jpg){.jpg,jpeg}", color=(0, 255, 255, 255))

with dpg.window(label="Image Asciifier", tag="MainWindow"):
    dpg.add_text("Options")
    dpg.add_input_int(label="Character Width", max_value=12, min_value= 1, default_value=4, tag="CharWidth")
    dpg.add_input_int(label="Character Height", max_value=20, min_value= 1, default_value=10, tag="CharHeight")

    dpg.add_spacer()

    dpg.add_combo(label="Greyramp", items=[
            "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1\{\}[]?-_+~<>i!lI;:,\"^`'. ",
            "▮▼●cɵ*v<>^`\"'~."
        ],
        default_value=defaultGreyRamp,
         callback=GreyrampCallback)

    dpg.add_separator()
    dpg.add_text(default_value="No file selected", tag="FileNameDisplay")
    dpg.add_button(label="Select Image File", callback=lambda: dpg.show_item("filePicker01"))

    dpg.add_separator()

    dpg.add_button(label="Generate", callback=Generate, tag="GenerateButton")

    with dpg.popup("GenerateButton", modal=True, tag="ProgressModal", min_size=(300, 100)):
            dpg.add_progress_bar(tag="ProgressBar")
            dpg.add_button(label="Cancel Generation", callback=CancelCallback)


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
