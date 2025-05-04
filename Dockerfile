# Use uma imagem base com Python pré-instalado
FROM python:3.13-slim
# Informações sobre a imagem
LABEL version="1.0"
LABEL description="This is a sample image"

# Define o diretório de trabalho dentro do container
WORKDIR /apis

# Copia o arquivo de dependências para o container
COPY requirements.txt .

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código para o container
COPY . .

# Expõe a porta 5000 para acesso externo
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "ProjetoFlask/app.py"]