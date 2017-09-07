#!/bin/bash

#raspivid -o - -t 0 -hf -w 600 -h 400 -fps 30 |cvlc -v stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8554}' :demux=h264

raspivid -o - -t 0 -n -w 600 -h 400 -fps 30 | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/}' :demux=h264

