# !/bin/bash

# Docker Container
CONTAINERREPO="azlinux/azdis"
CONTAINERTAG="1.0"
CONTAINERNAME="$CONTAINERREPO:$CONTAINERTAG"
CONTAINERHOSTNAME="logext-testagents.trafficmanager.net"

# Disk Inspector Service
SERVICENAME="AzureDiskInspectSvc_US"
SERVICEVOLUMENAME="AzureDiskInspectSvcSSLVolume"

# SSL 
SSL_PATH="$HOME/azdis_ssl"
SSL_PRIVATE_KEY="$SSL_PATH/azdis_private.rsa"
SSL_PUBLIC_KEY="$SSL_PATH/azdis_public.crt"

# Miscellaneous
LOG_FILE="/var/log/azureDiskInspectSvc.log"
