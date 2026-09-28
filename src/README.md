# Passo a Passo de Execução

## Setup do ollama

```bash
# 1. Instalar ollama (ollama.com)
# 2. Baixar um modelo leve
ollama pull gpt-oss
# 3. Testar se funciona ollama run gpt-oss "olá!" 

Esta pasta contém o código do seu agente financeiro.

## Estrutura Sugerida

```
## Código Completo
Todo o código-fonte está no arqyuivo 'app.py'.

## Como Rodar 
```bash
# 1. Instalar dependencias
pip install streamlit pandas requests
# 2.Garantir que ollama esta rodano
ollama serve

# 3. Rodar o app
streamlit run .\src\app.py



src/
├── app.py              # Aplicação principal (Streamlit/Gradio)

```

## Exemplo de requirements.txt

```
streamlit
openai
python-dotenv
```

## Como Rodar

```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar a aplicação
streamlit run app.py
```
## Evidencia de Execução 
<img width="1358" height="764" alt="image" src="https://github.com/user-attachments/assets/892aa3da-e1df-4b5c-84ef-e4249b2ba5dc" />
