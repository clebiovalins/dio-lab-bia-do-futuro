import json
import pandas
import requests
import streamlit as st

# ====================== Configuração ========================
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "glm-5.3:cloud"
# =============== CARREGAR DADOS =================
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv') 
historico = pd.read_csv('./data/historico_atendimento.csv')
produto = json.load(open('./dataprodutos_financeiros.json'))

# ====================== Montar Contexto =====================
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']}, anos, perfil {perfil{'perfil_investidor'}}
OBJETIVO: {perfil{'objetivo_principal'}}
PATRIMONIO: R$ {perfil{'patrimonio_total'}} | RESERVA: R$ {perfil{'reserva_emergencia_atual'}}

TRANSACOES RECENTES:
{transacoes.to_string(index=False)}

ATEDIMENTO ANTERIORES: 
{historico.to_string(index=False)}

PRODUTOS DISPONIVEIS:
{json.dumps(produtos, index=2, ensure_ascii=False)}
"""

# =================== System Prompt ==================
SYSTEM_PROMPT = """Voce e o MR. Valins, um educador financeiro amigavel e didatico.

OBJETIVO:
Ensinar conceitos de finanças pessoais de forma simples, usando os dados do cliente como exemplos pratico. 

REGRAS:
- Nunca recomende investimentos especificos, apenas explique como funcionam;
- Jamais responda a perguntas fora do tema ensino de finanças pessoais.
  Quando ocorrer, responda lembrando o seu papel de educador financeiro;
- Use os dados fornecidos para dar exemplos personalizados;
- Linguagem simples, como se explicasse para um amigo;
- Se não souber algo, admita: "Não tenho essa informação, mas posso explicar...";
- Sempre pergunte se o cliente entedeu;
- Responda de forma sucinta e direta ,com no maximo 3 paragrafos.
""" 

# =========================== Chamar Ollama =============================
def perguntar(msg):
    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}



r = requests.post(OLLAMA_URL, json= {"model": MODELO, "prompt": prompt, "stream": False})
return r.json()['response']


# ==================== INTERFACE ============================
st.title(" MR. Valins,  Seu Educador Finaceiro")
if pergunta := st.chat_input("Sua Dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta)) 
