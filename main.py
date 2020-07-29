from machine import Pin
import time

# ピンの設定
io12 = Pin(2, Pin.OUT)

while True:
    io12.value(1)
    time.sleep(0.5)
    io12.value(0)
    time.sleep(0.5)
