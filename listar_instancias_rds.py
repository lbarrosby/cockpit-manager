import boto3

def listar_instancias_rds(profile_name='cockpit'):
    session = boto3.Session(profile_name=profile_name)
    rds_client = session.client('rds')
    response = rds_client.describe_db_instances()
    instances_details = []
    for instance in response.get('DBInstances', []):
        instance_details = {
            'ID da instância': instance['DBInstanceIdentifier'],
            'Motor do banco de dados': instance['Engine'],
            'Status': instance['DBInstanceStatus'],
            'Endpoint': instance.get('Endpoint', {}).get('Address', 'N/A'),
            'Porta': instance.get('Endpoint', {}).get('Port', 'N/A')
        }
        instances_details.append(instance_details)
    return instances_details


instances = listar_instancias_rds()
for instance in instances:
    print(instance)
