import boto3

def listar_clusters_eks(profile_name='cockpit'):
    session = boto3.Session(profile_name=profile_name)
    eks_client = session.client('eks')
    response = eks_client.list_clusters()
    clusters_details = []
    for cluster_name in response.get('clusters', []):
        cluster_details = {
            'Nome do cluster': cluster_name,
        }
        clusters_details.append(cluster_details)
    return clusters_details

# Exemplo de uso
clusters = listar_clusters_eks()
for cluster in clusters:
    print(cluster)
