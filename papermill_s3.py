import papermill as pm
import jupyter
import sys
import os
import json
import boto3
from urllib.parse import unquote_plus

import os

OUTPUT_BUCKET = os.environ['OUTPUT_BUCKET']

sys.path.append("/opt/bin")
sys.path.append("/opt/python")
os.environ["IPYTHONDIR"]='/tmp/ipythondir'

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    
    result = { "output_notebooks": [] }

    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = unquote_plus(record['s3']['object']['key'])
        
        print("bucket = {}".format(bucket))
        print("key = {}".format(key))
        
        input_notebook = 's3://{}/{}'.format(bucket, key)
        output_notebook = 's3://{}/{}'.format(OUTPUT_BUCKET, key)
        
        print("input_notebook = {}".format(input_notebook))
        print("output_notebook = {}".format(output_notebook))
        
        response = s3_client.head_object(
            Bucket=bucket,
            Key=key
        )
        parameters = response['Metadata']
        
        # Convert values to int
        for key, value in parameters.items(): 
            try: 
                parameters[key] = int(value)
            except ValueError:
                pass

        print("parameters = {}".format(parameters))

        pm.execute_notebook(
           input_notebook,
           output_notebook,
           parameters = parameters
        )
        
        result["output_notebooks"].append(output_notebook)

    print("result = {}".format(result))

    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
