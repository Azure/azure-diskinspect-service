#!/bin/bash 
###########################################################################################
# This script pulls the CA bundle from the host wireserver, parses it,                    #
# and installs them in the Ubuntu CA bundle for the specialized clouds                    #
# where CA bundle is completely different from normal production clouds.                  #
# Recommended execution method                                                            #
# is cloud-init or VM custom-data for execution at provisioning time                      #
#                                                                                         #
# NOTES:                                                                                  #
# Many Linux applications use their own CA bundle instead of the system one.              #
# If you are still seeing TLS certificate validation errors, ensure that                  #
# you have also copied these certificates to the calling application's CA Bundle          #
# or identify the environment setting to direct it to use the system CA bundle            #
# Example: export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt for python/az cli #
#                                                                                         #
# This script must be run as root or else calls to the wireserver will time out           #
#                                                                                         #
# This script will run in a container, but does require sed so that must be installed     #
###########################################################################################
echo "Cloud Environment: $CLOUD"
if [ "$CLOUD" == "USNat" ]; then
    mkdir -p /root/AzureCACertificates
    # http://168.63.129.16 is a constant for the host's wireserver endpoint
    certs=$(curl "http://168.63.129.16/machine?comp=acmspackage&type=cacertificates&ext=json")
    IFS_backup=$IFS
    IFS=$'\r\n'
    certNames=($(echo $certs | grep -oP '(?<=Name\": \")[^\"]*'))
    certBodies=($(echo $certs | grep -oP '(?<=CertBody\": \")[^\"]*'))
    for i in ${!certBodies[@]}; do
        echo ${certBodies[$i]}  | sed 's/\\r\\n/\n/g' | sed 's/\\//g' > "/root/AzureCACertificates/$(echo ${certNames[$i]} | sed 's/.cer/.crt/g')"
    done
    IFS=$IFS_backup

    cp /root/AzureCACertificates/*.crt /usr/local/share/ca-certificates/
    update-ca-certificates

    # This copies the updated bundle to the location used by OpenSSL which is commonly used
    cp /etc/ssl/certs/ca-certificates.crt /usr/lib/ssl/cert.pem

    # This section creates a cron job to poll for refreshed CA certs daily
    # It can be removed if not needed or desired
    #action=${1:-init}
    #if [ $action == "ca-refresh" ]
    #then
    #    exit
    #fi

    #(crontab -l ; echo "0 19 * * * $0 ca-refresh") | crontab -
fi

# Start the nginx service
service nginx start && python /azureDiskInspectSvc/main.py