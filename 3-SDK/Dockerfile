FROM ubuntu:latest as builder
# Source Machine

MAINTAINER boseji@boseji.com
LABEL "author"="boseji" "Date"="2021-02-05" stage=builder

# Environment Variables
ENV TZ=Asia/Kolkata \
	LIBUSB_INCLUDE_DIR="/usr/include/libusb-1.0" \
	PICO_SDK_PATH=/pico/micropython/lib/pico-sdk

# Set Timezone Data
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Get Dependencies
RUN apt-get update && apt-get -y install \
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
	make && cp build/firmware.uf2 /pico/rp2-pico-micropython.uf2

# Build picotool
RUN git clone https://github.com/raspberrypi/picotool.git && \
    cd picotool && mkdir build && cd build && cmake .. && make && \
    cp picotool /usr/bin && cd ../.. && \
    rm -rf picotool && cp /usr/bin/picotool .

# Actual Machine
FROM ubuntu:latest as production

MAINTAINER boseji@boseji.com
LABEL "author"="boseji" "Date"="2021-02-05" stage=builder

# Environment Variables
ENV TZ=Asia/Kolkata \
	PICO_SDK_PATH=/pico/micropython/lib/pico-sdk \
	LANG=en_US.utf8

# Get Dependencies
RUN \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
    apt-get update && apt-get -y install \
    build-essential wget nano git python3 python3-pip curl vim sudo \
    cmake gcc-arm-none-eabi libnewlib-arm-none-eabi && \
    rm -rf /var/lib/apt/lists/* 

# Working Directory
COPY --from=builder /pico /pico
WORKDIR /pico


