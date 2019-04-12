# !/bin/bash

# Docker Container
CONTAINERREPO="azlinux/azdis"
CONTAINERTAG="1.1"
CONTAINERNAME="$CONTAINERREPO:$CONTAINERTAG"
CONTAINERHOSTNAME="logext-testagents.trafficmanager.net"
CONTAINERREGISTRY="iidbuildimagestest.azurecr.io"

# Disk Inspector Service
SERVICENAME="AzureDiskInspectSvc_US"
SERVICEVOLUMENAME="AzureDiskInspectSvcSSLVolume"

# SSL 
SSL_PATH="$HOME/azdis_ssl"
SSL_PRIVATE_KEY="$SSL_PATH/azdis_private.rsa"
SSL_PUBLIC_KEY="$SSL_PATH/azdis_public.crt"

# Miscellaneous
LOG_FILE="/var/log/azureDiskInspectSvc.log"
CREDSCANSERVICEVOLUMENAME="CredScanSvc"

# TODO: replace this with envionment specific AppInsights instrumentation key
APPINSIGHTS_KEY='00000000-0000-0000-00000000000000000'