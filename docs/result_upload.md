## Inspection result upload ##

The disk inspection is now capable of returning the inspection result in two different ways: http response body (classic) or blob upload.

The method of how the inspection result is returned is determined by an input parameter on the POST request: `blobsasurl`

__Sample input__

If `blobsasurl` is supplied as follows, the service will use the given blob SAS Url to upload the result file. 

For example:

`curl -X POST -k "https://127.0.0.1:8080/eb8482c8-adbd-46fa-a0d5-0ad694eae404/diagnostic/foo/bar/abcd" --data-urlencode "timeout=30" --data-urlencode "saskey=sv=2017-04-17&some_sas_token" --data-urlencode "blobsasurl=https://myaccount.blob.core.windows.net/mycontainer/output.zip?sp=some_sas_token"`

If the 'blobsasurl' parameter is not supplied on the POST request, the service will return the inspection result zip file in the Http response as it had before.

For example:

`curl -X POST -k "https://127.0.0.1:8080/eb8482c8-adbd-46fa-a0d5-0ad694eae404/diagnostic/foo/bar/abcd" --data-urlencode "timeout=30" --data-urlencode "saskey=sv=2017-04-17&some_sas_token" -o output.zip`
