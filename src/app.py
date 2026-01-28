import json
import pandas as pd
import requests
import streamlit as st
# ---------- CONFIGURAÇÃO ----------

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "tinyllama"



# ===== CARREGAR DADOS =====
perfil = json.load(open("./data/perfil_investidor.json"))
transacoes = pd.read_csv("./data/transacoes.csv")
historico = pd.read_csv("./data/historico_atendimento.csv")
produtos = json.load(open("./data/produtos_financeiros.json"))

# ===== MONTAR CONTEXTO =====
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_financeiro']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ===== SYSTEM PROMPT =====
SYSTEM_PROMPT = """
Você é um agente financeiro inteligente, amigável e didático, especializado em educação financeira para autônomos e MEIs.

OBJETIVO:
Ajudar o usuário a organizar suas finanças pessoais e profissionais, tomar decisões mais conscientes e aprender conceitos financeiros de forma simples, prática e contextualizada.

REGRAS:
1. Sempre baseie suas respostas nos dados fornecidos do cliente.
2. Nunca invente informações financeiras ou valores.
3. Não recomende investimentos específicos; explique como funcionam.
4. Use linguagem simples, como se estivesse explicando para um amigo.
5. Se não souber algo, diga claramente que não tem essa informação, mas explique o conceito.
6. Use dados financeiros para dar exemplos personalizados.
7. Responda de forma clara, direta e com no máximo 3 parágrafos.
8. Mantenha sempre um tom respeitoso, educativo e motivador.
"""
# ---------- CHAMAR OLLAMA ----------

def perguntar(msg):
    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}

Pergunta: {msg}
"""
    try:
        r = requests.post(
            OLLAMA_URL,
            json={
                "model": MODELO,
                "prompt": prompt,
                "stream": False
            },
            timeout=180
        )

        st.write("🔎 Resposta bruta do Ollama:")
        st.write(r.json())

        return r.json().get("response", "Resposta vazia do modelo.")

    except Exception as e:
        return f"Erro ao conectar com o Ollama: {e}"



# ========== INTERFACE ==========

# ========== INTERFACE ==========

st.title("🎓 MEI, Seu Educador Finaceiro")

# Inicializa histórico
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Olá! 👋 Sou o Edu, seu educador financeiro. Como posso te ajudar hoje?"
        }
    ]

# Renderiza histórico (ESSA PARTE FAZ A JANELA APARECER)
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Input do chat
if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    # Mensagem do usuário
    st.session_state.messages.append(
        {"role": "user", "content": pergunta}
    )
    st.chat_message("user").write(pergunta)

    # Resposta do assistente
    with st.spinner("Pensando..."):
        resposta = perguntar(pergunta)

    st.session_state.messages.append(
        {"role": "assistant", "content": resposta}
    )
    st.chat_message("assistant").write(resposta)
