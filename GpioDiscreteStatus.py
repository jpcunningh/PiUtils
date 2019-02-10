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
print args

if args.debounce:
    print 'Debounce not implemented'

if args.mode == 'up':
    pull_up_down = GPIO.PUD_UP
else:
    pull_up_down = GPIO.PUD_DOWN

# This is going to let us use the BCM pin numbers.  The number on JuiceBox
# Zero is labeled
# according to BCM.  See https://pinout.xyz/ for more details on pinouts.

GPIO.setmode(GPIO.BCM)

GPIO.setup(args.pin, GPIO.IN, pull_up_down=pull_up_down)

state = GPIO.input(args.pin)

print state


