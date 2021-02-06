# SDK Directory

This directory stores the Software, source code and tools for for [**Raspberry Pi Pico rev3** board](https://www.raspberrypi.org/documentation/pico/getting-started/)

## Contents

### Raspberry Pi Pico Rev3

- [Getting Started Guide for Pico](getting-started-with-pico.pdf)
- [C/C++ SDK Guide](raspberry-pi-pico-c-sdk.pdf)
- [C/C++ SDK Release v1.0.1](pico-sdk-1.0.1.zip)
- [C/C++ SDK Examples Release v1.0.1](pico-examples-sdk-1.0.1.zip)
- [Blinky Firmware for Onboard LED (`GP25`)](blink.uf2)
- [`picoprobe` Firmware for Debugging other Pico boards](picoprobe.uf2)
- [Flash Resetting Firmware](flash_nuke.uf2)
- [Linux x64 Build of `picotool`](picotool) done under *Ubuntu 20.04 LTS*.
  - SHA256 : `23c84451587d843bebca68cf00d7e3bce7d86380ab1fa01663135e6fe713072d`
- [MicroPython SDK Documentation](raspberry-pi-pico-python-sdk.pdf)
- MicroPython Firmware :
  - First Release - [`pico_micropython_20210121`](pico_micropython_20210121.uf2)
  - Latest Release - [`rp2-pico-20210205-unstable-v1.14-9-g9dedcf122`](rp2-pico-20210205-unstable-v1.14-9-g9dedcf122.uf2)
  - Dockerfile Build - [`rp2-pico-micropython`](rp2-pico-micropython.uf2)

### Important Repository Links

- Official C/C++ SDK : 
  - https://github.com/raspberrypi/pico-sdk
- Official C/C++ SDK Examples : 
  - https://github.com/raspberrypi/pico-examples
- `picotool` Repository : 
  - https://github.com/raspberrypi/picotool
- `picoprobe` Firmware Repository : 
  - https://github.com/raspberrypi/picoprobe
- Flash Resetting Firmware Repository : 
  - https://github.com/raspberrypi/pico-examples/blob/master/flash/nuke/nuke.c
- Official C/C++ SDK Project generator : 
  - https://github.com/raspberrypi/pico-project-generator
- Official MicroPython Fork : 
  - https://github.com/raspberrypi/micropython
- Official MicroPython Examples : 
  - https://github.com/raspberrypi/pico-micropython-examples
- MicroPython Release Link for Firmware for RP2 or Pico Rev 3 board : 
  - https://micropython.org/download/rp2-pico/

### `picoprobe` Pinout

| Pico Pin | Debug Pin|
|----------|----------|
| GP25 (built-in)    | Nil |
| GP2 | SWCLK |
| GP3 | SWDIO |
| GP4(uart1) | UART_TX|
| GP5(uart1) | UART_RX|
| GND | GND |

## Dockerfile to build MicroPython using C/C++ SDK and `picotool` for Linux

This docker file would use the `/pico` directory to do all
download and built actions. 

```dockerfile
FROM ubuntu:latest
MAINTAINER boseji@boseji.com
LABEL "author"="boseji" "Date"="2021-02-05"

# Environment Variables
ENV TZ=Asia/Kolkata \
	LIBUSB_INCLUDE_DIR="/usr/include/libusb-1.0" \
	PICO_SDK_PATH=/pico/micropython/lib/pico-sdk

# Set Timezone Data
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Get Dependencies
RUN echo "  # --> Getting Dependencies" && \
    apt-get update && apt-get -y install \
    build-essential wget nano git python3 python3-pip \
    cmake gcc-arm-none-eabi libnewlib-arm-none-eabi \
    libusb-1.0-0-dev pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Working Directory
WORKDIR /pico

# Build micropython Firmware
RUN git clone -b pico https://github.com/raspberrypi/micropython.git && \
	cd micropython && \
	git submodule update --init -- lib/pico-sdk && \
	cd lib/pico-sdk && \
	git submodule update --init && \
	cd ../.. && \
	make -C mpy-cross && \
	cd ports/rp2 && \
	make && \
    cp build/firmware.uf2 /pico/rp2-pico-micropython.uf2

# Build picotool
RUN git clone https://github.com/raspberrypi/picotool.git && \
    cd picotool && \
    mkdir build && \
    cd build && \
    cmake .. && 
    make && \
    cp picotool ../.. 

```

Build Instructions:

```shell
docker build . -t rp2
```

Container Execution:

```shell
docker container run --rm -it -v "$(pwd)":/download rp2:latest bash
```

This command would open a `root` prompt into the image and mount the
current directory under `/download` location in the container.
Then one can use `cp` commands to copy out the built *MicroPython* Uf2 image.

This same container can also be used for building MicroPython again bu
updating the repositories.