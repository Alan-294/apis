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

           

    def teste005(self):
        novo_aluno = {
            "nome": "Jailson",
            "idade": 21,
            "turma_id": 1,
            "nota_primeiro_semestre": 9,
            "nota_segundo_semestre": 10
        }

        # Debugging: Print the URL being called
        print(f"POST URL: {BASE_URL}/api/alunos/alunos")

        # Envia POST para a API
        r = requests.post(f'{BASE_URL}/api/alunos/alunos', json=novo_aluno)

        # Verifica status de resposta
        self.assertEqual(r.status_code, 201, f"Esperado status 201, mas veio {r.status_code}: {r.text}")

        try:
            dados = r.json()
        except requests.exceptions.JSONDecodeError:
            self.fail("Erro: resposta não é um JSON válido")

        # Confere se todos os campos estão no JSON de retorno
        for campo in ["id", "nome", "idade", "turma_id", "media_final"]:
            self.assertIn(campo, dados, f"Campo '{campo}' não encontrado na resposta")

        # Verifica se os valores retornados batem com os enviados
        self.assertEqual(dados["nome"], novo_aluno["nome"], "Nome não confere")
        self.assertEqual(dados["idade"], novo_aluno["idade"], "Idade não confere")
        self.assertEqual(dados["turma_id"], novo_aluno["turma_id"], "Turma ID não confere")

        # Confere se a média foi calculada corretamente
        media_esperada = (novo_aluno["nota_primeiro_semestre"] + novo_aluno["nota_segundo_semestre"]) / 2
        self.assertAlmostEqual(dados["media_final"], media_esperada, places=2, msg="Média final incorreta")

        return dados

    
   
    
    def teste006(self):
        # Create a new student to update
        dados2 = self.teste005() 
        aluno_id = dados2['id']

        # Update the student's name and other details
        r = requests.put(f'{BASE_URL}/api/alunos/{aluno_id}',
                        json={
                            'nome': 'Gohan',
                            'idade': 21,
                            'turma_id': 1,
                            'nota_primeiro_semestre': 4,
                            'nota_segundo_semestre': 5
                        })

        # Verify the response status code
        self.assertEqual(r.status_code, 200, f"Esperado status 200, mas veio {r.status_code}: {r.text}")

        # Fetch the updated student
        r = requests.get(f'{BASE_URL}/api/alunos/{aluno_id}')
        self.assertEqual(r.status_code, 200, f"Esperado status 200, mas veio {r.status_code}: {r.text}")

        try:
            dados3 = r.json()
        except requests.exceptions.JSONDecodeError:
            self.fail("Erro: resposta não é um JSON válido")

        # Verify the updated fields
        self.assertEqual(dados3['nome'], 'Gohan', "Erro ao editar aluno")
        self.assertEqual(dados3['nota_primeiro_semestre'], 4, "Erro ao editar nota do primeiro semestre")
        self.assertEqual(dados3['nota_segundo_semestre'], 5, "Erro ao editar nota do segundo semestre")
        self.assertAlmostEqual(dados3['media_final'], 4.5, places=2, msg="Erro ao calcular média final")

    # teste 007: DELETE - Validar se está excluindo uma alunos
    def teste007(self):                  
        novo_aluno = self.teste005()
        id_aluno = novo_aluno["id"]

        requests.delete(f"{BASE_URL}/api/alunos/{id_aluno}")

        r2 = requests.get(f"{BASE_URL}/api/alunos/{id_aluno}")
        self.assertEqual(r2.status_code, 404, "Erro: Aluno ainda existe após deleção")

            


if __name__ == '__main__':
    unittest.main()
