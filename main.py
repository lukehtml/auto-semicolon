import keyboard as kb

def on_enter(e):
    kb.press_and_release("enter")
    kb.press_and_release("backspace")
    kb.press_and_release(";")
    kb.press_and_release("enter")

kb.on_press_key("enter", on_enter, suppress=True)
kb.wait()