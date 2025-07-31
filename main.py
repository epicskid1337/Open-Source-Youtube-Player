import dearpygui.dearpygui as dpg
import video
import findvideo
import time
import discordrpc
import threading
import globals

rpc = discordrpc.RPC(app_id=1400552010792571053)
rpc.set_activity()

def startthreadforyt(): # dude i have no idea on how to handle this
    threading.Thread(target=findvideo.youtube).start()
def dcrpc(): #kill me
    rpc.run()

dpg.create_context()
dpg.create_viewport(title='youtube', width=600, height=400)

dpg.setup_dearpygui()

def checkbox(sender):
    globals.vidOrSong = dpg.get_value(sender)

with dpg.window(label="youtube", no_title_bar=True, no_resize=True, no_move=True, width=600, height=400):
    dpg.add_text("Underneath there is a button that will open a chrome window containing youtube.")
    dpg.add_button(label="Open youtube", callback=startthreadforyt)
    dpg.add_checkbox(label="Video Or song? (On = Video, vice versa you get it)", default_value=globals.vidOrSong, callback=checkbox)
    dpg.add_text("Open the video url you want, logging in is optional.")


threading.Thread(target=dcrpc).start()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
