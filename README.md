# analyzing-data-aws-lambda

Sample code to use an [Amazon EFS](https://aws.amazon.com/efs/) file system to manage data science dependencies (NumPy, SciPy, scikit-learn, pandas, Matplotlib, Jupyter, papermill) for AWS Lambda functions.

## Installing the dependencies on EFS

The functions use the `python3.13` runtime and load packages from `/mnt/DataScience/lib` (`PYTHONPATH`). Packages with native code (NumPy, SciPy, pandas, ...) must be built for the same Python version and architecture as the function (x86_64, the default in this template), so install them from an environment matching the Lambda runtime (for example an EC2 instance or container using the `public.ecr.aws/lambda/python:3.13` image) with the EFS access point mounted:

```
pip install -r requirements.txt --target /mnt/DataScience/lib --upgrade
```

If you previously installed the packages for an older Python version (e.g. 3.8), remove them and reinstall: they are not compatible with Python 3.13.

## Matplotlib image

The `/mi` endpoint uploads the generated image to the output bucket (without public ACLs, which are disabled by default on new buckets) and redirects to a presigned URL valid for one hour (`URL_EXPIRATION` environment variable, in seconds).
