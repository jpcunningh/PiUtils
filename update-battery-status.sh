#!/bin/bash

notlow=$(~/src/PiUtils/GpioDiscreteStatus.py --pin 18 --debounce)

if [ $notlow = "False" ]; then
  echo True > monitor/low-battery.json
else
  echo False > monitor/low-battery.json
fi

