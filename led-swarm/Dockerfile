FROM hypriot/rpi-python

RUN apt-get update && \
    apt-get install -y gcc && \
    pip install RPi.GPIO

CMD ["python", "blinking.py"]

COPY blinking.py /data
