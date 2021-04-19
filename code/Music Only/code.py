"""Modified CircuitPython Essentials Audio Out MP3 Example"""
import audiocore
import board
import time
import audiobusio
import digitalio

from audiomp3 import MP3Decoder

mp3 = open("still-alive.mp3", "rb")
decoder = MP3Decoder(mp3)
audio = audiobusio.I2SOut(board.GP10, board.GP11, board.GP9)

audio.play(decoder)

while audio.playing:
    pass
    time.sleep(0.1)
