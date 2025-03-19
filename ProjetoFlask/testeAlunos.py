import unittest
from flask import request  # Import do Flask (caso esteja usando)
import requests  # Biblioteca para requisições HTTP
from alunos import *

class TestProduct(unittest.TestCase):
    def test001(self):
        self.assertTrue(True)

# 10 testes 
    

    # Teste 001: Verificar se a rota /alunos está funcionando!
    def teste001(self):

        r = requests.get('http://127.0.0.1:5000/api/alunos')
        self.assertEqual(r.status_code, 200, "Erro na URL")

        
    # teste 002: verificar se estar retornando um valor json.

    def teste002(self):
        r = requests.get('http://127.0.0.1:5000/api/alunos')
        if r.headers['Content-Type'] == 'application/json':
            self.assertTrue(True)
        else:
            self.fail("Erro no tipo de retorno")
        

    # teste 003: GeT com id - Validar se estar retornando alunos com uma id valida

    def teste003(self):
        r = requests.get('http://127.0.0.1:5000/api/alunos/1009') 
        print("Resposta JSON:", r.text)  
        
        try:
            dados = r.json()
            if 'id' in dados:
                self.assertEqual(dados['id'], 1009, "Erro ID não encontrado")
            else:
                self.fail("Resposta não contém 'id'")
        except requests.exceptions.JSONDecodeError:
            self.fail("Erro: resposta não é um JSON válido")
        
        
    # teste 004: GET com id - Validar se estar retornando alunos com um id especifico que não existe
    def teste004(self):    
        r = requests.get('http://127.0.0.1:5000/api/alunos/1011')
        print("[Teste 4]Resposta JSON:", r.text)  
        
        try:
            dados = r.json()
            self.assertEqual(r.status_code, 404)  
            if 'erro' in dados:
                self.assertTrue(True)
            else:
                self.fail("Resposta não contém mensagem de erro esperada")
        except requests.exceptions.JSONDecodeError:
            self.fail("Erro: resposta não é um JSON válido")


    # teste 005: POST - Validar se está adicionando uma alunos
    def teste005(self):
        r = requests.post('http://127.0.0.1:5000/api/alunos/', json={"nome":"Jailson",
                                                                 "data_nascimento" :"2003-03-05",
                                                                 "nota_primeiro_semestre":9,
                                                                 "turma_id":6}
                          )
    
        dados = r.json()     
        id = dados.get("alunos_adicionada", {}).get("aluno", {}).get("id")
        if not id:
            self.fail("Erro: ID do aluno não retornado corretamente")

        r2 = requests.get(f'http://127.0.0.1:5000/api/alunos/{id}')
            
            
        dados2 = r2.json()
        self.assertEqual(dados2['aluno']['id'], id, "Erro ao adicionar aluno")
        return dados2
    
    # teste 006: PUT - Validar se está editando uma alunos
    def teste006(self):
        dados2 = self.teste005()
        #print(dados2)
        
        r = requests.put(f'http://127.0.0.1:5000/api/alunos/1009',
                         json={'nome': 'Gohan',
                               'data-nascimento':'31-10-2003',
                               'nota_primeiro_semestre':4,
                               'nota_segundo_semestre':5,
                               "turma_id": 6,
                               "media_final": 4.5,})

        dados3 = self.teste001()
        #print(dados3) 
        
        for listaalunos in dados3['alunos']:

            if listaalunos['id'] == dados2['alunos']['id']:
                #print(listaalunos)
                self.assertEqual(listaalunos['nome'], 'Nome(alterado)', "Erro ao editar aluno")


    # teste 007: DELETE - Validar se está excluindo uma alunos
    def teste007(self):
    
                            
                            
        novo_aluno = self.teste005()
        id_novo_aluno = novo_aluno["alunos"]["id"]

        # Excluir aluno
        requests.delete(f"http://127.0.0.1:5000/api/alunos/{id_novo_aluno}")

        # Verificar se aluno ainda existe
        r2 = requests.get(f"http://127.0.0.1:5000/api/alunos/{id_novo_aluno}")
        self.assertEqual(r2.status_code, 404, "Erro: Aluno ainda existe após deleção")

                


if __name__ == '__main__':
    unittest.main()
