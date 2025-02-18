# introducao-api-sabor-express


         Início
           |
           v
+----------------------------------+
| Importa requests e json         |
+----------------------------------+
           |
           v
+----------------------------------+
| Define a URL da API             |
+----------------------------------+
           |
           v
+----------------------------------+
| Faz a requisição GET na API     |
+----------------------------------+
           |
           v
+----------------------------------+
| Verifica se resposta.status_code|
| é 200 (sucesso)                 |
+----------------------------------+
       /       \
     (Sim)     (Não)
      |          |
      v          v
+----------------------------------+
| Inicializa dicionário vazio      |
| dados_restaurante = {}           |
+----------------------------------+
      |      
      v      
+----------------------------------+
| Percorre os itens do JSON       |
+----------------------------------+
      |      
      v      
+-----------------------------------------------+
| Verifica se o nome do restaurante já existe  |
| no dicionário                                |
+-----------------------------------------------+
       /       \
     (Sim)     (Não)
      |          |
      v          v
+------------------+   +--------------------------------+
| Adiciona item à  |   | Cria nova entrada no dict    |
| lista existente  |   | e adiciona item              |
+------------------+   +--------------------------------+
           |
           v
+----------------------------------+
| Percorre todos os restaurantes  |
| para salvar os arquivos JSON    |
+----------------------------------+
           |
           v
+----------------------------------+
| Cria e escreve o arquivo JSON   |
| para cada restaurante           |
+----------------------------------+
           |
           v
+----------------------------------+
| Exibe mensagem de sucesso       |
+----------------------------------+
           |
           v
          Fim
