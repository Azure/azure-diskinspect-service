# Azure Disk Inspect Service
The Azure Disk Inspect Service is intended to be a service that allows customers, support or third party personnel with privileged access to access an Azure OS Disk for log and configuration files without provisioning a VM and attaching a copy of the disk in order to probe the contents. It is a fast and secure way to retrieve well known contents of an OS disk by the user to aid in system failure diagnosis.

## Building (Local):

To build the docker container, ensure you have installed docker.io
	apt-get install docker.io
from the azure-diskinspect-service folder and then,
	./build.sh
	
## Building (Remote ACS):

You can also choose to directly build on an Azure Container Service by setting up Docker Port Forwarding. To do this you will need to copy the ssh private key for the ACS deployed into 
	~./id_rsa 
Ensure the id_rsa has sufficient permissions
	chmod 400 ~./id_rsa
	
Next, setup port forwarding:
	nohup ssh -L 2375:localhost:2375 -N user@host.com -p 2200 &
	
This will expose the port 2375 on your localhost to map to 2375 on the docker swarm. You can specify any port on the localhost that you desire if you intend to use multiple service mappings. 

Next, export the port forwarding rule for Docker.
	export DOCKER_HOST=:2375

Now, run:
	docker ps
to ensure that you are now connected to the remote docker swarm.

Follow the local build steps as documented before, but note that the docker container is now built on the remote machine.

## Deploying:

First ensure the SSL certificates for the NGINX server are available and placed at:
	~/azdis_ssl/

Assuming you have built the docker container, you can deploy it by running from your source folder:
	./scripts/run.sh
this sets up a server named "AzureDiskInspectService_US" by default.

Run:
	docker ps
to verify the service is running.

## Logs:

To look at realtime logs generated from the service run:
	./scripts/checklog.sh

To copy the logs over for examination on the host:
  ./scripts/getlogs.sh
