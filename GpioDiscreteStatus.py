#!/usr/bin/python

import os
import time
import argparse
import RPi.GPIO as GPIO

parser = argparse.ArgumentParser(description='Return the status of a GPIO line.')
parser.add_argument('--mode', nargs=1, help='pull \'up\' or pull \'down\' line mode, default \'up\'', choices=['up', 'down'], default='up')
parser.add_argument('--pin', nargs=1, type=int, help='GPIO pin number to retrieve status from', required=True)
parser.add_argument('--debounce', help='Enable debounce logic', action='store_true')

args = parser.parse_args()

num_checks = 1

if args.debounce:
    num_checks = 5

if args.mode == 'up':
    pull_up_down = GPIO.PUD_UP
else:
    pull_up_down = GPIO.PUD_DOWN

# This is going to let us use the BCM pin numbers.

GPIO.setmode(GPIO.BCM)

GPIO.setup(args.pin, GPIO.IN, pull_up_down=pull_up_down)

checks = []

for check in range(num_checks):
    checks.append(GPIO.input(args.pin[0]))
    if check > 0:
        time.sleep(0.25)

# Report whichever state had the majority
state = sum(checks) > (num_checks / 2)

print state


