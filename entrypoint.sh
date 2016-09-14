#!/bin/bash

cd /opt/gpio-spi/Adafruit_Python_MCP3008/

sudo python setup.py install

cd /opt/gpio-spi/Adafruit_Python_MCP3008/examples

sudo python simpletest.py
