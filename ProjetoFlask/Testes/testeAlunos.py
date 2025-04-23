import unittest
from flask import request  # Import do Flask (caso esteja usando)
import requests  # Biblioteca para requisições HTTP
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from config import BASE_URL

class TestProduct(unittest.TestCase):
    def test001(self):
        self.assertTrue(True)

# 7 testes 

    # Teste 001: Verificar se a rota /alunos está funcionando!
    def teste001(self):
        r = requests.get(f'{BASE_URL}/api/alunos')
        self.assertEqual(r.status_code, 200, "Erro na URL")
        
        try:
            dados = r.json()  
            return dados
        except requests.exceptions.JSONDecodeError:
            self.fail("Erro: resposta não é um JSON válido")

        
    # teste 002: verificar se estar retornando um valor json.

    def teste002(self):
        r = requests.get(f'{BASE_URL}/api/alunos')
        if r.headers['Content-Type'] == 'application/json':
            self.assertTrue(True)
            
        else:
            self.fail("Erro no tipo de retorno")
        

    # teste 003: GeT com id - Validar se estar retornando alunos com uma id valida

    def teste003(self):
        r = requests.get(f'{BASE_URL}/api/alunos/1') 
        
        try:
            dados = r.json()
            if 'id' in dados:
                self.assertEqual(dados['id'], 1, "Erro ID não encontrado")
            else:
                self.fail("Resposta não contém 'id'")
        except requests.exceptions.JSONDecodeError:
            self.fail("Erro: resposta não é um JSON válido")
        
        
    # teste 004: GET com id - Validar se estar retornando alunos com um id especifico que não existe
    def teste004(self):    
        r = requests.get(f'{BASE_URL}/api/alunos/1008')
        
        
        try:
            dados = r.json()
   
            self.assertTrue('mensagem' in dados, "Resposta não contém mensagem de erro esperada")
        except requests.exceptions.JSONDecodeError:
            self.fail("Erro: resposta não é um JSON válido")

           


    # teste 005: POST - Validar se está adicionando um aluno corretamente
    def teste005(self):
        novo_aluno = {
            "nome": "Jailson",
            "idade": 21,
            "turma_id": 1,
            "nota_primeiro_semestre": 9,
            "nota_segundo_semestre": 10
        }

        r = requests.post(f'{BASE_URL}/api/alunos', json=novo_aluno)

        if r.status_code != 201:
            self.fail(f"Erro ao adicionar aluno. Status: {r.status_code}, Resposta: {r.text}")

        try:
            dados = r.json()  
        except requests.exceptions.JSONDecodeError:
            self.fail("Erro: resposta não é um JSON válido")
            
        id = dados.get("id")

        if not id:
            self.fail("Erro: ID do aluno não retornado corretamente")

        # Verifica se os dados do aluno batem com os enviados
        r2 = requests.get(f'{BASE_URL}/api/alunos/{id}')
        
        if r2.status_code != 200:
            self.fail(f"Erro ao buscar aluno recém-criado. Status: {r2.status_code}, Resposta: {r2.text}")

        dados2 = r2.json()

        self.assertEqual(dados2['id'], id, "Erro: ID não confere")
        self.assertEqual(dados2['nome'], novo_aluno['nome'], "Erro: Nome não confere")
        self.assertEqual(dados2['idade'], novo_aluno['idade'], "Erro: Idade não confere")
        self.assertEqual(dados2['turma_id'], novo_aluno['turma_id'], "Erro: Turma não confere")
        self.assertIn("media_final", dados, "Erro: Média final não retornada")

        return dados2
    
    
    def teste006(self):
        dados2 = self.teste005() 
        aluno_id = dados2['id']
        
        r = requests.put(f'{BASE_URL}/api/alunos/{aluno_id}',
                        json={'nome': 'Gohan',
                            'data_nascimento': '31-10-2003',
                            'nota_primeiro_semestre': 4,
                            'nota_segundo_semestre': 5,
                            "turma_id": 1,
                            "media_final": 4.5})

        
        dados3 = self.teste001()
        print("dados3:", dados3)  

        if dados3 is None:
            self.fail("Erro: teste001() não retornou dados válidos")
        
        
        if isinstance(dados3, list): 
            for listaalunos in dados3:
                if listaalunos['id'] == dados2['id']: 
                    self.assertEqual(listaalunos['nome'], 'Jailson', "Erro ao editar aluno")
                    break
            else:
                self.fail("Erro: Aluno não encontrado na lista após edição")
        else:
            self.fail("Erro: dados3 não contém uma lista de alunos")



    # teste 007: DELETE - Validar se está excluindo uma alunos
    def teste007(self):
    
                            
        novo_aluno = self.teste005()
        id_aluno = novo_aluno["id"]

        requests.delete(f"{BASE_URL}/api/alunos/{id_aluno}")

        r2 = requests.get(f"{BASE_URL}/api/alunos/{id_aluno}")
        self.assertEqual(r2.status_code, 404, "Erro: Aluno ainda existe após deleção")

                


if __name__ == '__main__':
    unittest.main()
