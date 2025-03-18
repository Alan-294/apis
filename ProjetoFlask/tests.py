import unittest
from flask import request  # Import do Flask (caso esteja usando)
import requests  # Biblioteca para requisições HTTP
from Turma import *

class TestProduct(unittest.TestCase):
    def test001(self):
        self.assertTrue(True)

                    ########################
                    #### Teste Turmas #####
                    ########################

    # Teste 001: Verificar se a rota /turma está funcionando
    def teste001(self):
        r = requests.get('http://127.0.0.1:5000/turma')
        if r.status_code == 200:
            self.assertTrue(True)
        else:
            self.fail("Erro na url")
        return r.json()
        
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
        r2 = requests.get(f'http://127.0.0.1:5000/turma?id={id}')
        dados2 = r2.json()
        self.assertEqual(dados2['turma']['id'], id, "Erro ao adicionar turma")
        return dados2
    
    # teste 006: PUT - Validar se está editando uma turma
    def teste006(self):
        dados2 = self.teste005()
        
        r = requests.put(f'http://127.0.0.1:5000/turma?id={dados2['turma']['id']}&nome=Nome(alterado)&turno=Noite&professor_id=13')

        dados3 = self.teste001()
        
        for listaTurmas in dados3['turmas']:

            if listaTurmas['id'] == dados2['turma']['id']:
                self.assertEqual(listaTurmas['nome'], 'Nome(alterado)', "Erro ao editar turma")


    # teste 007: DELETE - Validar se está excluindo uma turma
    def teste007(self):
        novaTurma = self.teste005()
        listaTurmas = self.teste001()
        
        for turma in listaTurmas['turmas']:
            if turma['id'] == novaTurma['turma']['id']:
                dodos = requests.delete(f"http://127.0.0.1:5000/turma?id={turma['id']}")
                break

        listaTurmas = self.teste001()

        if novaTurma['turma']['id'] not in [t['id'] for t in listaTurmas['turmas']]: 
            self.assertTrue(True)
        else:
            self.fail("Erro ao excluir turma")
        


if __name__ == '__main__':
    unittest.main()
    