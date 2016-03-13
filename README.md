# Dockerized traffic light app running on a Raspberry Pi

This repo contains the source codes, Dockerfile and docker-compose.yml for a traffic light app explained in [this blog post](http://blog.hypriot.com/post/traffic-light/).

## Setup your Raspberry Pi

Flash HypriotOS and customize WiFi

```
flash --hostname tl --password YOUR-WIFI-PSK --ssid YOUR-WIFI-SSID https://downloads.hypriot.com/hypriot-rpi-20160306-192317.img.zip
```

Prepare HypriotOS for Docker machine

```
function getip() { (traceroute $1 2>&1 | head -n 1 | cut -d\( -f 2 | cut -d\) -f 1) }

ssh-keygen -R $(getip tl.local)
ssh-copy-id -oStrictHostKeyChecking=no -oCheckHostIP=no root@$(getip tl.local)
ssh root@tl.local sed -i \'s/ID=raspbian/ID=debian/g\' /etc/os-release
```

## Create a Docker machine

```
docker-machine create -d generic --engine-storage-driver=overlay --generic-ip-address=$(getip tl.local) tl
```

## Build the app

```
eval $(docker-machine env tl)
docker build -t pedestrian-crossing .
```

## Connect LEDs

![gpio](http://pi4j.com/images/gpio-control-example-large.png)

## Run the app

```
docker run --rm --cap-add SYS_RAWIO --device /dev/mem pedestrian-crossing
```

or even simpler with docker-compose

```
docker-compose up -d
```


## Turn off your Pi

```
docker-machine ssh tl shutdown
```
