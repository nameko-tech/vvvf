from machine import Pin, ADC, I2C, PWM
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
# disp.write('a')
# disp.move(0, 1)# disp.write('hello!')


adc = ADC(Pin(32))          # ADC ピンの ADC オブジェクトを作成
adc.read()                  # 0.0v - 1.0v 範囲を 0-4095 の値で読込み

adc.atten(ADC.ATTN_11DB)    # 11dBの入力減衰率を設定(電圧範囲はおよそ 0.0v - 3.6v)
# adc.width(ADC.WIDTH_9BIT)   # 9ビットの戻り値を設定(戻り値の範囲 0-511)


pwm0 = PWM(Pin(4))      # ピンから PWM オブジェクトを作成
# pwm0.freq()             # 現在の周波数を取得
pwm0.freq(1000)         # 周波数を設定
# pwm0.duty()             # 現在のデューティ比を取得
pwm0.duty(200)          # デューティ比を設定
# pwm0.deinit()           # PWM を無効化

# pwm2 = PWM(Pin(2), freq=20000, duty=512) # 作成と設定を一度に実行

while(True):
    num = adc.read()                  # 新しく設定された減衰率と戻り値幅を使って値を読込み
    disp.write('      ')
    disp.home()
    disp.write(str(num//40) + ' km/h')
    # print(str(num))
    pwm0.freq(num//40)
    time.sleep(0.03)


# rainbow()
# while True:
# blue.on()
# time.sleep(2)
# blue.off()
# time.sleep(2)
