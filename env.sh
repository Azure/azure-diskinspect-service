# !/bin/bash

# Docker Container
CONTAINERREPO="azlinux/azdiskinspectsvc"
CONTAINERTAG="1.0"
CONTAINERNAME="$CONTAINERREPO:$CONTAINERTAG"
CONTAINERHOSTNAME="logext-testagents.trafficmanager.net"

# Disk Inspector Service
SERVICENAME="AzureDiskInspectorSvc_US"
SERVICEVOLUMENAME="AzureDiskInspectorSvcSSLVolume"

# SSL 
SSL_PATH="$HOME/logext_ssl"
SSL_PRIVATE_KEY="$SSL_PATH/logext_private.rsa"
SSL_PUBLIC_KEY="$SSL_PATH/logext_public.crt"

# Miscellaneous
LOG_FILE="/var/log/azureDiskInspectorSvc.log"
