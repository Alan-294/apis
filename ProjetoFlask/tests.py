import unittest
from flask import request  # Import do Flask (caso esteja usando)
import requests  # Biblioteca para requisições HTTP
from Turma import *

class TestProduct(unittest.TestCase):
    # def test001(self):
    #     self.assertTrue(True)

# 10 testes 
    

    # Teste 001: Verificar se a rota /turma está funcionando
    def teste001(self):
        r = requests.get('http://127.0.0.1:5000/turma')
        if r.status_code == 200:
            self.assertTrue(True)
        else:
            self.fail("Erro na url")
        
    # teste 002: verificar se estar retornando um valor json.

    def teste002(self):
        r = requests.get('http://127.0.0.1:5000/turma')
        if r.headers['Content-Type'] == 'application/json':
            self.assertTrue(True)
        else:
            self.fail("Erro no tipo de retorno")
        

    # teste 003: GeT com id - Validar se estar retornando turma com uma id valida

    def teste003(self):
        r = requests.get('http://127.0.0.1:5000/turma?id=2000') 
        dados = r.json()
        self.assertEqual(dados['turma']['id'], 2000, "Erro ID não encontrado")

        
    # teste 004: GET com id - Validar se estar retornando turma com um id especifico que não existe
    def teste004(self):    
        r = requests.get('http://127.0.0.1:5000/turma?id=-1')
        dados = r.json()
        if self.assertEqual(dados['code'], 404): 
            self.assertTrue(True)

    # teste 005: POST - Validar se está adicionando uma turma
    def teste005(self):
        r = requests.post('http://127.0.0.1:5000/turma?nome=ads2&turno=noite&professor_id=3000')
        dados = r.json()     
        id = dados['turma_adicionada']['id']['id']
        print(id)
        r2 = requests.get(f'http://127.0.0.1:5000/turma?id={id}')
        dados2 = r2.json()
        self.assertEqual(dados2['turma']['id'], id, "Erro ao adicionar turma")

   


if __name__ == '__main__':
    unittest.main()