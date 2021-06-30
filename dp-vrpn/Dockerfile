FROM ros:melodic
MAINTAINER Jes Jepsen <jegj@mmmi.sdu.dk>

RUN apt update && apt install -y \
	ros-melodic-vrpn-client-ros \
	net-tools 

COPY scripts/ /scripts/
