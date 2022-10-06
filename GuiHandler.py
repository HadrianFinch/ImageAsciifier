import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Image Asciifier', width=1000, height=800)

def FileDialogCallback(sender, app_data):
    print('OK was clicked.')
    print("Sender: ", sender)
    print("App Data: ", app_data)

with dpg.file_dialog(directory_selector=False, show=False, callback=FileDialogCallback, id="filePicker01"):
    dpg.add_file_extension("Supported image fileds (*.jpg){.jpg,jpeg}", color=(0, 255, 255, 255))

with dpg.window(label="Example Window", tag="MainWindow"):
    dpg.add_text("Hello, world")
    dpg.add_button(label="Save")
    dpg.add_input_text(label="string", default_value="Quick brown fox")
    dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

    dpg.add_button(label="Select Image File", callback=lambda: dpg.show_item("filePicker01"))

dpg.set_primary_window("MainWindow", True)

dpg.setup_dearpygui()

dpg.show_viewport()
dpg.start_dearpygui()

dpg.destroy_context()