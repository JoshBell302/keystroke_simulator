from pynput.keyboard import Key, Controller

keyboard_controller = Controller()

lambda_key_inputs = {
    "Key.esc": lambda: (keyboard_controller.press(Key.esc), keyboard_controller.release(Key.esc)),
    "Key.f1": lambda: (keyboard_controller.press(Key.f1), keyboard_controller.release(Key.f1)),
    "Key.f2": lambda: (keyboard_controller.press(Key.f2), keyboard_controller.release(Key.f2)),
    "Key.f3": lambda: (keyboard_controller.press(Key.f3), keyboard_controller.release(Key.f3)),
    "Key.f4": lambda: (keyboard_controller.press(Key.f4), keyboard_controller.release(Key.f4)),
    "Key.f5": lambda: (keyboard_controller.press(Key.f5), keyboard_controller.release(Key.f5)),
    "Key.f6": lambda: (keyboard_controller.press(Key.f6), keyboard_controller.release(Key.f6)),
    "Key.f7": lambda: (keyboard_controller.press(Key.f7), keyboard_controller.release(Key.f7)),
    "Key.f8": lambda: (keyboard_controller.press(Key.f8), keyboard_controller.release(Key.f8)),
    "Key.f9": lambda: (keyboard_controller.press(Key.f9), keyboard_controller.release(Key.f9)),
    "Key.f10": lambda: (keyboard_controller.press(Key.f10), keyboard_controller.release(Key.f10)),
    "Key.f11": lambda: (keyboard_controller.press(Key.f11), keyboard_controller.release(Key.f11)),
    "Key.f12": lambda: (keyboard_controller.press(Key.f12), keyboard_controller.release(Key.f12)),
    "Key.print_screen": lambda: (keyboard_controller.press(Key.print_screen), keyboard_controller.release(Key.print_screen)),
    "Key.scroll_lock ": lambda: (keyboard_controller.press(Key.scroll_lock ), keyboard_controller.release(Key.scroll_lock )),
    "Key.backspace": lambda: (keyboard_controller.press(Key.backspace), keyboard_controller.release(Key.backspace)),
    "Key.tab": lambda: (keyboard_controller.press(Key.tab), keyboard_controller.release(Key.tab)),
    "Key.caps_lock": lambda: (keyboard_controller.press(Key.caps_lock), keyboard_controller.release(Key.caps_lock)),
    "Key.enter": lambda: (keyboard_controller.press(Key.enter), keyboard_controller.release(Key.enter)),
    "Key.shift": lambda: (keyboard_controller.press(Key.shift), keyboard_controller.release(Key.shift)),
    "Key.shift_r": lambda: (keyboard_controller.press(Key.shift_r), keyboard_controller.release(Key.shift_r)),
    "Key.ctrl_l": lambda: (keyboard_controller.press(Key.ctrl_l), keyboard_controller.release(Key.ctrl_l)),
    "Key.cmd": lambda: (keyboard_controller.press(Key.cmd), keyboard_controller.release(Key.cmd)),
    "Key.alt_l": lambda: (keyboard_controller.press(Key.alt_l), keyboard_controller.release(Key.alt_l)),
    "Key.space": lambda: (keyboard_controller.press(Key.space), keyboard_controller.release(Key.space)),
    "Key.alt_gr": lambda: (keyboard_controller.press(Key.alt_gr), keyboard_controller.release(Key.alt_gr)),
    "Key.ctrl_r": lambda: (keyboard_controller.press(Key.ctrl_r), keyboard_controller.release(Key.ctrl_r)),
    "Key.insert": lambda: (keyboard_controller.press(Key.insert), keyboard_controller.release(Key.insert)),
    "Key.delete": lambda: (keyboard_controller.press(Key.delete), keyboard_controller.release(Key.delete)),
    "Key.page_up": lambda: (keyboard_controller.press(Key.page_up), keyboard_controller.release(Key.page_up)),
    "Key.page_down": lambda: (keyboard_controller.press(Key.page_down), keyboard_controller.release(Key.page_down)),
    "Key.num_lock": lambda: (keyboard_controller.press(Key.num_lock), keyboard_controller.release(Key.num_lock)),
    "Key.home": lambda: (keyboard_controller.press(Key.home), keyboard_controller.release(Key.home)),
    "Key.left": lambda: (keyboard_controller.press(Key.left), keyboard_controller.release(Key.left)),
    "Key.up": lambda: (keyboard_controller.press(Key.up), keyboard_controller.release(Key.up)),
    "Key.down": lambda: (keyboard_controller.press(Key.down), keyboard_controller.release(Key.down)),
    "Key.right": lambda: (keyboard_controller.press(Key.right), keyboard_controller.release(Key.right))
}