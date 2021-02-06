#!/bin/bash
docker rmi rp2:latest
docker build . -t rp2
