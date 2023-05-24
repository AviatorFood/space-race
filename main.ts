input.onButtonPressed(Button.A, function () {
    previous_roll += -1
    basic.showNumber(previous_roll)
})
input.onButtonPressed(Button.AB, function () {
    previous_roll = 0
    if (4 <= previous_roll) {
        yes_or_no = randint(0, 8)
    }
    if (4 > previous_roll) {
        yes_or_no = randint(0, 5)
    }
    if (2 < yes_or_no) {
        basic.showString("YES")
        basic.clearScreen()
    } else {
        basic.showString("NO")
        basic.clearScreen()
    }
})
input.onButtonPressed(Button.B, function () {
    previous_roll += 1
    basic.showNumber(previous_roll)
})
input.onGesture(Gesture.Shake, function () {
    current_roll = randint(0, 6)
    basic.showNumber(current_roll + 1)
    basic.pause(5000)
    basic.clearScreen()
})
let current_roll = 0
let yes_or_no = 0
let previous_roll = 0
basic.showString("SPACE RACE")
previous_roll = 0
