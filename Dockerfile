FROM hypriot/rpi-python

RUN apt-get update && \
    apt-get install -y gcc python-smbus && \
    pip install RPi.GPIO

CMD ["python", "pedestrian-crossing.py"]

COPY pedestrian-crossing.py /data
