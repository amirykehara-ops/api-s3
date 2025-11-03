import boto3
import base64
import json

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        bucket_name = body['bucket_name']
        directorio = body['directorio']
        file_name = body['file_name']
        base64_data = body['file_data']

        s3 = boto3.resource('s3')
        object_key = f"{directorio}/{file_name}"

        s3.Object(bucket_name, object_key).put(Body=base64.b64decode(base64_data))

        return {
            'statusCode': 200,
            'body': json.dumps({
                'mensaje': f'Archivo {file_name} subido a {bucket_name}/{directorio}/ correctamente'
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
