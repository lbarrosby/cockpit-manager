import boto3

def listar_funcoes_lambda(profile_name='cockpit'):
    session = boto3.Session(profile_name=profile_name)
    lambda_client = session.client('lambda')
    response = lambda_client.list_functions()
    funcoes_details = []
    for funcao in response['Functions']:
        funcao_details = {
            'Nome da função': funcao['FunctionName'],
            'ARN da função': funcao['FunctionArn'],
            'Última modificação': funcao['LastModified']
        }
        funcoes_details.append(funcao_details)
    return funcoes_details


funcoes = listar_funcoes_lambda()
for funcao in funcoes:
    print(funcao)
