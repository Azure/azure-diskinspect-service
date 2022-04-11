#!/bin/bash
# This is a replication of script to list/install all the packages required in dockerbuild.
# This script/packages downloaded from it are not used for actual docker build,
# only purplose of the scripts to allow Component Governance to scan all the packages

echo "**********Copy source repositories list to apt.**********"
cp conf/sources.list /etc/apt/sources.list

echo "**********Install debian apt packages.**********"
apt-get update \
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

echo "**********Install Credential Scanner dependencies.**********"
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
echo "deb http://download.mono-project.com/repo/ubuntu bionic main" | tee /etc/apt/sources.list.d/mono-official.list
apt-get update && apt-get install -y mono-complete

echo "**********Clone forked libguesfs repo and build.**********"
git clone https://github.com/chintanrp/libguestfs.git
cd libguestfs
./autogen.sh --disable-gobject --disable-golang \
&& make ; rm -f po-docs/podfiles; make -C po-docs update-po
make

echo "**********Install python libraries.**********"
pip3 install azure-storage-blob==12.8.1
pip3 install applicationinsights==0.11.9
pip3 install python-json-logger


