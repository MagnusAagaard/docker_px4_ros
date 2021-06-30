FROM ros:noetic
MAINTAINER Jes Jepsen <jegj@mmmi.sdu.dk>

RUN apt update && apt install -y \
	ros-noetic-mavros \
	python3-pip \
	libxml2-dev \
	libxslt-dev \
	python3-lxml

RUN pip3 install pymavlink --upgrade
RUN pip3 install pyserial

COPY scripts/ /scripts/
