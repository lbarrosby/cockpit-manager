import boto3

def listar_instancias_ec2(profile_name='cockpit'):
    try:
        session = boto3.Session(profile_name=profile_name)
        ec2_client = session.client('ec2')
        response = ec2_client.describe_instances()
        instances_details = []
        for reservation in response.get('Reservations', []):
            for instance in reservation.get('Instances', []):
                instance_details = {
                    'ID da instância': instance['InstanceId'],
                    'Tipo da instância': instance['InstanceType'],
                    'Estado da instância': instance['State']['Name'],
                    'IP público': instance.get('PublicIpAddress', 'N/A'),
                    'IP privado': instance.get('PrivateIpAddress', 'N/A'),
                    'Tags': instance.get('Tags', 'N/A')
                }
                instances_details.append(instance_details)
        return instances_details
    except Exception as e:
        print(f"Ocorreu um erro ao listar as instâncias EC2: {e}")
        return []

def test_listar_instancias_ec2():
    class MockSession:
        def client(self, service):
            return MockClient()

    class MockClient:
        def describe_instances(self):
            return {
                'Reservations': [
                    {
                        'Instances': [
                            {
                                'InstanceId': 'i-1234567890abcdef0',
                                'InstanceType': 't2.micro',
                                'State': {'Name': 'running'},
                                'PublicIpAddress': '1.2.3.4',
                                'PrivateIpAddress': '10.0.0.1',
                                'Tags': [{'Key': 'Name', 'Value': 'Teste'}]
                            }
                        ]
                    }
                ]
            }

    boto3.Session = MockSession

    instances = listar_instancias_ec2()
    assert len(instances) == 1
    assert instances[0]['ID da instância'] == 'i-1234567890abcdef0'
    assert instances[0]['Tipo da instância'] == 't2.micro'
    assert instances[0]['Estado da instância'] == 'running'
    assert instances[0]['IP público'] == '1.2.3.4'
    assert instances[0]['IP privado'] == '10.0.0.1'
    assert instances[0]['Tags'] == [{'Key': 'Name', 'Value': 'Teste'}]

test_listar_instancias_ec2()
