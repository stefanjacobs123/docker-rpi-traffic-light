FROM hypriot/rpi-python

RUN apt-get update && \
    apt-get install -y gcc python-smbus build-essential python-dev && \
    pip install RPi.GPIO

COPY Adafruit_Python_MCP3008 /opt/gpio-spi/Adafruit_Python_MCP3008
COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]
