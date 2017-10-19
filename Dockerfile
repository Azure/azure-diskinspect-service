# This file creates a container that runs nginx and a libguestfs python web service
# The libguestfs service provides a way to extract log files from a SAS uri of an
# Azure blob as a zip archive.
 
FROM ubuntu:16.04

# package dependencies
RUN echo "deb http://archive.ubuntu.com/ubuntu/ trusty main universe" >> /etc/apt/sources.list
RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    build-essential \
    autoconf \
    git \
    nginx \
    python3-pip \
 && DEBIAN_FRONTEND=noninteractive apt-get build-dep -y \
    libguestfs

# patched libguestfs
WORKDIR /
RUN git clone https://github.com/amitchat/libguestfs.git
WORKDIR /libguestfs
RUN ./autogen.sh \
 && make ; rm -f po-docs/podfiles; make -C po-docs update-po 
RUN make

# extractor service
RUN rm -v /etc/nginx/nginx.conf
COPY conf/nginx.conf /etc/nginx/
COPY pyServer/* /azureDiskInspectSvc/
COPY pyServer/manifests/ /etc/azdis/

# Redirect python3 as default 
RUN ln -s -f /usr/bin/python3 /usr/bin/python

# Install AppInsights 
RUN pip3 install applicationinsights

# Expose port 8080 for nginx
EXPOSE 8080

# Start the nginx service
CMD service nginx start && python /azureDiskInspectSvc/main.py



