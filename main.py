from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
        Endipoint que exibe a mensagem "Hello World"
    '''
    return {"Hello": "World"}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str=Query(None)):
    '''
        Endpoint que retorna o cardápio de um restaurante específico ou de todos os restaurantes
    '''
    url= 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

    resposta = requests.get(url)


    if resposta.status_code == 200:
        dados_json = resposta.json()
        if restaurante is None:
            return {'Dados' : dados_json}
        
        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    "item": item['Item'],
                    "preco": item['price'],
                    "descricao": item['description']
                })
        return {'Restaurante' : restaurante, 'Cardapio' : dados_restaurante}       
    else:
        return {'Erro':f'{resposta.statu_code} - {resposta.reason}'}