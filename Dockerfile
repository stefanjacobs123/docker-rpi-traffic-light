FROM hypriot/rpi-python

RUN apt-get update && \
    apt-get install -y gcc python-smbus && \
    pip install RPi.GPIO

COPY Adafruit_Python_MCP3008 /opt/gpio-spi

RUN cd Adafruit_Python_MCP3008

RUN python setup.py install

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]
