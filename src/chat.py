from search import search_prompt
from langchain_openai import ChatOpenAI

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough

PROMPT_TEMPLATE = """
CONTEXTO:
{contexto}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.

EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
Pergunta: "Qual é a capital da França?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Quantos clientes temos em 2024?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Você acha isso bom ou ruim?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

PERGUNTA DO USUÁRIO:
{pergunta}

RESPONDA A "PERGUNTA DO USUÁRIO"
"""

def main():

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    prompt = PromptTemplate(
        input_variables=["contexto", "pergunta"],
        template=PROMPT_TEMPLATE
    )

    print("\n")
    print("="*70)
    print("Faça perguntas sobre a lista de empresas inseridas no banco de dados")
    print("Digite 'sair' para encerrar o chat.")
    print("="*70)
    print("\n")

    while True:
        user_question = input("Pergunta: ").strip()

        if user_question.lower() == "sair":
            print("Chat encerrado.")
            break

        if not user_question:
            continue

        context = search_prompt(user_question)

        if not context:
            print("Não foi possível obter contexto para a pergunta.")
            continue

        response = llm.invoke(prompt.format(contexto=context, pergunta=user_question))

        print(f"Resposta: {response.content}\n")

if __name__ == "__main__":
    main()