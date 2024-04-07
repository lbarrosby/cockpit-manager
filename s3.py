import boto3

def listar_buckets_s3(profile_name='cockpit'):
    session = boto3.Session(profile_name=profile_name)
    s3_client = session.client('s3')
    response = s3_client.list_buckets()
    buckets_details = []
    for bucket in response['Buckets']:
        bucket_details = {
            'Nome do bucket': bucket['Name'],
            'Data de criação': bucket['CreationDate']
        }
        buckets_details.append(bucket_details)
    return buckets_details


buckets = listar_buckets_s3()
for bucket in buckets:
    print(bucket)
