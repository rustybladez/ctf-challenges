#!/bin/bash

socat TCP-LISTEN:10001,fork,reuseaddr EXEC:./service.py
