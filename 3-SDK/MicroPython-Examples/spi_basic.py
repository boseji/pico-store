from machine import Pin, SPI;P=Pin
from utime import sleep_ms

# GP19 = MOSI = SPI0_TX  => SI  Pin W25Qxx Flash
# GP18 = SCK  = SPI0_SCK => SCK Pin W25Qxx Flash
# GP16 = MISO = SPI0_RX  => SO  Pin W25Qxx Flash
# GP17 = SS   = SPI0_CSn => CE# Pin W25Qxx Flash
spi = SPI(0,baudrate=100000,sck=P(18),mosi=P(19),miso=P(16))
ssp = P(17, P.OUT); ss = ssp.value; ss(1)

# Mark The Beginning
print("Starting SPI Demo W25Qxx Flash IC")
# 1
print('Manufacturer ID (2bytes): ', end='')
ss(0)
spi.write(b'\x90\x00\x00\x00')
b = spi.read(2)
ss(1)
# Should be 0xEF to indicate Winbond
print("".join(['{:02X}'.format(i) for i in b]))
# 2
print('Unique ID (8bytes): ', end='')
ss(0)
spi.write(b'\x4B\x00\x00\x00\x00')
b = spi.read(8)
ss(1)
print("".join(['{:02X}'.format(i) for i in b]))

