import requests
import json

url= 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

resposta = requests.get(url)


if resposta.status_code == 200:
    dados_json = resposta.json()
    dados_restaurante = {}
    
    for item in dados_json:
        nome_do_restaurante = item['Company']
        
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []
            
        dados_restaurante[nome_do_restaurante].append({
            "item": item['Item'],
            "preco": item['price'],
            "descricao": item['description']
        })
else:
    print('Erro ao acessar a API')
    
    
for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivos = f'{nome_do_restaurante}.json'
    with open(nome_do_arquivos, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4)
        print(f'Arquivo {nome_do_arquivos} criado com sucesso!')
