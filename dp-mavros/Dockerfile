FROM ros:noetic
MAINTAINER Jes Jepsen <jegj@mmmi.sdu.dk>

RUN apt update && apt install -y \
	ros-noetic-mavros

WORKDIR /
RUN wget https://raw.githubusercontent.com/mavlink/mavros/master/mavros/scripts/install_geographiclib_datasets.sh
RUN chmod +x install_geographiclib_datasets.sh
RUN ./install_geographiclib_datasets.sh

COPY scripts/ /scripts/
