# Ingestão e busca semântica com LangChain e Postgres

## Introdução

Esta aplicação como objetivo fazer a ingestão de dados de um pdf em um banco de dados 
de vetor e fazer busca semântica sobre o conteúdo do pdf.

## Pré-requisitos

- Python
- Bibliotecas LangChain
- Docker & Docker Compose
- PostgreSQL + pgVector

## Configuração do Ambiente

Para configurar o ambiente e instalar as dependências do projeto, siga os passos abaixo:

1. **Criar e ativar um ambiente virtual (`venv`):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

2. **Instalar as dependências:**

   **Opção A - A partir do `requirements.txt`:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar as variáveis de ambiente:**

   - Duplique o arquivo `.env.example` e renomeie para `.env`
   - Abra o arquivo `.env` e substitua os valores pelas suas chaves de API reais, dados do banco de dados e o caminho do pdf que deseja fazer a ingestão de dados.


## Ingestão de Dados

1. Inicialize o banco de dados
```bash
docker-compose up
```

2. Na raiz do projeto, execute somente uma vez o arquivo `ingest.py`
```bash
python src/ingest.py
```

## Execução do chat

- Para iniciar o chat execute `python src/chat.py`
- Faça perguntas relacionadas ao contexto das empresas do PDF
- Quando quiser sair do chat digite `sair`


## Encerramento
- Quando finalizar a execução do programa finalize os containers docker e desative a máquina virtual do Python

```
docker compose down
deactivate
```