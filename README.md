### まず

#### 環境

- pip で `esptool` と `adafruit-ampy` を入れる
- esp32 を使う場合、cp210x driver を入れる

#### コマンド

- `esptool.py chip_id` でポート確認
- `ampr -p COM3 ls` でボードの中を見る (COM3 は上で確認したポート)
- `ampr -p COM3 -b 115200 put main.py` で書き込む
- `ampr -p COM3 -b 115200 rm main.py` で消せる
