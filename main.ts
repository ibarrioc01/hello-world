radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 0) {
        basic.showNumber(0)
    }
})
// Crea el canal 12 cuando se pulsa el botón A
input.onButtonPressed(Button.A, function () {
    radio.setGroup(12)
    radio.sendString("IRENE")
})
input.onButtonPressed(Button.AB, function () {
    radio.setGroup(0)
})
radio.onReceivedString(function (receivedString) {
    if (receivedString == "SERGIO") {
        basic.showString("OK")
        music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    }
})
input.onButtonPressed(Button.B, function () {
    radio.setGroup(6)
})
input.onLogoEvent(TouchButtonEvent.Touched, function () {
    music.play(music.tonePlayable(175, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    basic.clearScreen()
})
