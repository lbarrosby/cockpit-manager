import boto3

def listar_filas_sqs(profile_name='cockpit'):
    session = boto3.Session(profile_name=profile_name)
    sqs_client = session.client('sqs')
    response = sqs_client.list_queues()
    queues_details = []
    for url in response.get('QueueUrls', []):
        queue_name = url.split('/')[-1]  
        queue_details = {
            'Nome da fila': queue_name,
            'URL da fila': url
        }
        queues_details.append(queue_details)
    return queues_details


filas = listar_filas_sqs()
for fila in filas:
    print(fila)
