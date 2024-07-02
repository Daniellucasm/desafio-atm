# Desafio Técnico Morada.ai: Caixa Eletrônico API
Esta API simula o funcionamento de um caixa eletrônico. Ela recebe um valor de saque desejado e retorna a quantidade de cédulas de cada valor necessárias para compor esse saque, utilizando a menor quantidade de cédulas possível. As cédulas consideradas são: 100, 50, 20, 10, 5 e 2.

## Desafios 
O principal desafio foi implementar o código em Python, pois é uma linguagem que comecei a estudar há pouco tempo, para realizar algumas implementações para a empresa atual em que trabalho como estagiário, com o objetivo de automatizar alguns processos que envolvem planilhas de Excel.

## Instrução de execução

### Pré-requisitos
- **Python 3.12.4** (ou versão mais recente)
- **Flask** (biblioteca Python para construção de APIs)

### Passos para Configuração e Execução
1. **Instalar a Biblioteca Flask**:
   - Execute o seguinte comando para instalar a biblioteca Flask:
     ```bash
     pip install Flask
     ```
2. **Obter o Código-Fonte**:
   - Faça um clone deste repositório ou baixe o arquivo .zip e extraia-o em seu computador:
   - Navegue até o diretório onde o código foi clonado ou extraído.
3. **Iniciar o Servidor Flask**:
   - No diretório contendo o arquivo `atm.py`, execute o comando abaixo para iniciar o servidor Flask:
     ```bash
     python atm.py
     ```
   - O servidor Flask estará rodando em `http://localhost:5000`.
4. **Testar o Endpoint**:
   - Com o servidor em execução, você pode testar o endpoint usando o comando cURL abaixo:
     ```bash
     curl -X POST -H "Content-Type: application/json" -d "{\"valor\": 380}" http://localhost:5000/api/saque
     ```
5. Por fim, para realizar executar os testes unitários basta realizar o comando abaixo, em que irá fornecer uma saída detalhada dos testes.
  ```bash
  python -m unittest -v test_atm.py
  ```
## Estrutura do Projeto
- **`atm.py`**: Contém a implementação da API Flask e a lógica para calcular a quantidade mínima de cédulas necessárias para um valor de saque.
- **`test_atm.py`**: Contém testes unitários para validar a lógica de cálculo de cédulas e o comportamento da API.


