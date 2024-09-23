# cybulde-prepare-data

Process raw data stored with DVC using a distributed dask cluster.

The following steps outide this code are nessary in order to run the code:

- Create AWS user with programmetic access
- Give the use S3 and secret manager permissions (policies)
- Create a bucket in S3 (bucket - dvc-test-svw, folder - datasets). (use another repo to version and store data on in this folder on s3 using dvc)
- configure the AWS CLI with the user keys using `aws configure`
- create personal github token
- store the personal github token in aws secrets manager.

With all these preparation steps the code is running correctly. 
