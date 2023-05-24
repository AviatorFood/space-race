yes_or_no = 0
current_roll = 0
previous_roll = 0

def on_button_pressed_ab():
    global previous_roll, yes_or_no
    previous_roll = 0
    if 4 <= previous_roll:
        yes_or_no = randint(0, 8)
    if 4 > previous_roll:
        yes_or_no = randint(0, 5)
    if 2 < yes_or_no:
        basic.show_string("YES")
        basic.clear_screen()
    else:
        basic.show_string("NO")
        basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_gesture_shake():
    global current_roll
    current_roll = randint(0, 6)
    basic.show_number(current_roll + 1)
    basic.pause(5000)
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    global previous_roll
    previous_roll += 1
    basic.show_number(previous_roll)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_a():
    global previous_roll
    previous_roll += -1
    basic.show_number(previous_roll)
input.on_button_pressed(Button.A, on_button_pressed_a)

basic.show_string("SPACE RACE")
previous_roll = 0