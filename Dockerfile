# This file creates a container that runs nginx and a libguestfs python web service
# The libguestfs service provides a way to extract log files from a SAS uri of an
# Azure blob as a zip archive.
 
FROM ubuntu:18.04

# package dependencies
COPY conf/sources.list /etc/apt/sources.list
RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    build-essential \
    autoconf \
    git \
    nginx \
    libjansson-dev \
    ocaml \
    libhivex-ocaml \
    libhivex-ocaml-dev \
    python3-pip \
    libssl-dev \
 && DEBIAN_FRONTEND=noninteractive apt-get build-dep -y \
    libguestfs

# Install Credential Scanner dependencies
WORKDIR /
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
RUN echo "deb http://download.mono-project.com/repo/ubuntu bionic main" | tee /etc/apt/sources.list.d/mono-official.list
RUN apt-get update && apt-get install -y mono-complete

# patched libguestfs
WORKDIR /
RUN git clone https://github.com/chintanrp/libguestfs.git
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
RUN pip3 install azure-storage-blob
RUN pip3 install applicationinsights

# Expose port 8080 for nginx
EXPOSE 8080

# Start the nginx service
CMD service nginx start && python /azureDiskInspectSvc/main.py



