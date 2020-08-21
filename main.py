from machine import Pin, ADC, I2C
import machine
import time
import i2c_lcd


def rainbow():
    rgbColour = [0, 0, 0]

    while True:
        for x in range(0, 255, 1):
            disp.color(x, 0, 0)

        for x in range(0, 255, 1):
            disp.color(0, x, 0)

        for x in range(0, 255, 1):
            disp.color(0, 0, x)


# ピンの設定
blue = Pin(2, Pin.OUT)
yellow = Pin(12, Pin.OUT)
green = Pin(13, Pin.OUT)
red = Pin(14, Pin.OUT)
# buz = Pin(27, Pin.OUT)
# adc = ADC(Pin(34))          # ADC ピンの ADC オブジェクトを作成
# adc.atten(ADC.ATTN_6DB)
# print(adc.read())
print('done')
# i2c = I2C(Pin(22), Pin(21), freq=400000)
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
print(isinstance(i2c, I2C))
disp = i2c_lcd.Display(i2c)

i2c.scan()
disp.color(10, 100, 100)
disp.home()
disp.write('Hello World')

rainbow()
# while True:
# blue.on()
# time.sleep(2)
# blue.off()
# time.sleep(2)
