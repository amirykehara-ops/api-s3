import boto3
import json

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        bucket_name = body['bucket_name']
        directorio = body['directorio']

        s3 = boto3.client('s3')
        s3.put_object(Bucket=bucket_name, Key=f"{directorio}/")
        
        return {
            'statusCode': 200,
            'body': json.dumps({'mensaje': f'Directorio {directorio}/ creado en el bucket {bucket_name}'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
