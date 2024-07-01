from flask import Flask, request, jsonify
from collections import OrderedDict

app = Flask(__name__)

# Função para calcular a quantidade mínima de cédulas necessárias
def calcular_cedulas(valor):
    # Verifica se o valor é um número inteiro positivo
    if valor <= 0:
        raise ValueError("O valor de saque deve ser um número inteiro positivo!")

    # Lista das cédulas disponíveis
    cedulas = [100, 50, 20, 10, 5, 2]
    # Inicializa o dicionário de resultado com todas as cédulas como 0
    resultado = {str(cedula): 0 for cedula in cedulas}
    
    # Calcula a quantidade de cada cédula necessária
    for cedula in cedulas:
        quantidade, valor = divmod(valor, cedula)
        resultado[str(cedula)] = quantidade
    
    # Se ainda restar valor, significa que não pode ser atendido com as cédulas disponíveis
    if valor != 0:
        raise ValueError("O valor de saque não pode ser atendido com as cédulas disponíveis!")
    
    # Ordena o resultado em ordem decrescente de denominação das cédulas
    resultado_ordenado = OrderedDict(sorted(resultado.items(), key=lambda x: int(x[0]), reverse=True))
    
    return resultado_ordenado

# Endpoint para saque
@app.route('/api/saque', methods=['POST'])
def saque():
    dados = request.get_json()
    valor = dados.get('valor')
    
    # Validar a entrada: deve ser um número inteiro positivo
    if not isinstance(valor, int) or valor <= 0:
        return jsonify({'error': 'Valor de saque deve ser um número inteiro positivo!'}), 400
    
    try:
        # Calcula a quantidade de cédulas e retorna o resultado
        resultado = calcular_cedulas(valor)
        return jsonify(resultado)
    except ValueError as e:
        # Retorna uma mensagem de erro se não for possível atender o valor solicitado
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)