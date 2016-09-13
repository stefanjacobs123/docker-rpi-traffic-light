FROM hypriot/rpi-python

RUN apt-get update && \
    apt-get install -y gcc python-smbus && \
    pip install RPi.GPIO

COPY Adafruit_Python_MCP3008 /opt/gpio-spi/Adafruit_Python_MCP3008
COPY entrypoint.sh /entrypoint.sh

#RUN cd /opt/gpio-spi/Adafruit_Python_MCP3008

#WORKDIR /opt/gpio-spi/Adafruit_Python_MCP3008

#RUN 'cd /opt/gpio-spi/Adafruit_Python_MCP3008 ; python setup.py install'

WORKDIR /
RUN python /opt/gpio-spi/Adafruit_Python_MCP3008/setup.py install

#WORKDIR /

RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]
