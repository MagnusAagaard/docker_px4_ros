FROM ros:noetic
MAINTAINER Jes Jepsen <jegj@mmmi.sdu.dk>

RUN apt update && apt install -y \
	ros-noetic-mavros


RUN python3 --version

COPY scripts/ /scripts/
