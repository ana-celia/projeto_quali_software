import requests

BASE_URL = 'http://localhost:8000/amazon_api/'

def get_clientes():
    response = requests.get(BASE_URL + 'clientes/')
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Exemplo de uso
if __name__ == '__main__':

    # Obter todos os clientes
    clientes = get_clientes()
    for cliente in clientes:
        print('Cliente:', cliente)