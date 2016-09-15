FROM hypriot/rpi-python

# Change workdir to root folder. Base image's root dir is '/data'.
# When installing python packages, this messes it up.
WORKDIR /

RUN apt-get update && \
    apt-get install -y gcc python-smbus build-essential python-dev && \
    pip install RPi.GPIO

COPY entrypoint.sh /entrypoint.sh
COPY trigger-relay.py /trigger-relay.py

RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]
