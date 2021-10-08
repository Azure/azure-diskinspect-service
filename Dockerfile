# This file creates a container that runs nginx and a libguestfs python web service
# The libguestfs service provides a way to extract log files from a SAS uri of an
# Azure blob as a zip archive.
 
FROM ubuntu:18.04

# package dependencies
COPY conf/sources.list /etc/apt/sources.list
RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get upgrade -y \
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
    wget \
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

# Remove old version and install latest golang version
RUN DEBIAN_FRONTEND=noninteractive apt-get remove -y \
    golang-go \
    --auto-remove golang-go
RUN rm -rf /usr/local/go
RUN wget -qO- https://golang.org/dl/go1.17.2.linux-amd64.tar.gz | tar -xzv -C /usr/local
ENV PATH $PATH:/usr/local/go/bin

# extractor service
RUN rm -v /etc/nginx/nginx.conf
COPY conf/nginx.conf /etc/nginx/
COPY pyServer/* /azureDiskInspectSvc/
COPY pyServer/manifests/ /etc/azdis/

# Redirect python3 as default 
RUN ln -s -f /usr/bin/python3 /usr/bin/python

# Install AppInsights 
RUN pip3 install azure-storage-blob==12.8.1
RUN pip3 install applicationinsights==0.11.9

# Expose port 8080 for nginx
EXPOSE 8080

#Setup docker entrypoint and start the nginx service
COPY ./entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]


# Set the locale
ENV LANG=C.UTF-8
ENV LANGUAGE=C.UTF-8
ENV LC_ALL=C.UTF-8

