import keyboard as kb

paused = False

def on_enter(e):
    if paused:
        return
    kb.press_and_release("enter")
    kb.press_and_release("backspace")
    kb.press_and_release(";")
    kb.press_and_release("enter")

def pause(e):
    global paused
    paused = not paused
    print("Paused XD" if paused else "Unpaused :D")

kb.on_press_key("enter", on_enter, suppress=True)
kb.on_press_key("right shift", pause)

kb.wait()
