import unittest
from atm import calcular_cedulas
from flask import Flask, jsonify, request

class TestATM(unittest.TestCase):
    # Teste para verificar a correta distribuição das cédulas para um valor de saque
    def test_calcular_cedulas(self):
        resultado = calcular_cedulas(380)
        esperado = {
            "100": 3,
            "50": 1,
            "20": 1,
            "10": 1,
            "5": 0,
            "2": 0
        }
        self.assertEqual(resultado, esperado)
    
    # Teste para verificar a resposta quando o valor não pode ser atendido com as cédulas disponíveis
    def test_valor_nao_atendido(self):
        with self.assertRaises(ValueError) as context:
            calcular_cedulas(3)
        self.assertTrue("O valor de saque não pode ser atendido com as cédulas disponíveis!" in str(context.exception))

    # Teste para verificar a resposta para valores negativos
    def test_valor_negativo(self):
        with self.assertRaises(ValueError) as context:
            calcular_cedulas(-50)
        self.assertTrue("O valor de saque deve ser um número inteiro positivo!" in str(context.exception))
    
    # Teste para verificar a resposta para valores não numéricos
    def test_valor_nao_numerico(self):
        app = Flask(__name__)

        @app.route('/api/saque', methods=['POST'])
        def saque():
            dados = request.get_json()
            valor = dados.get('valor')
            
            if not isinstance(valor, int) or valor <= 0:
                return jsonify({'error': 'Valor de saque deve ser um número inteiro positivo!'}), 400
            
            try:
                resultado = calcular_cedulas(valor)
                return jsonify(resultado)
            except ValueError as e:
                return jsonify({'error': str(e)}), 400

        # Cria um cliente de teste para enviar a requisição ao endpoint
        with app.test_client() as client:
            response = client.post('/api/saque', json={'valor': 'cinquenta'})
            self.assertEqual(response.status_code, 400)
            self.assertIn('Valor de saque deve ser um número inteiro positivo!', response.get_json()['error'])

if __name__ == '__main__':
    unittest.main()