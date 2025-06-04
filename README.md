
# 💸 Controle de Gastos com Autenticação – App em Streamlit

Aplicação web desenvolvida com **Python + Streamlit**, que permite ao usuário:
- Fazer login de forma segura (com autenticação personalizada)
- Registrar seus gastos diários com categoria, valor e data
- Visualizar um extrato interativo com todos os lançamentos

🔐 Cada usuário acessa **apenas seus próprios dados**, armazenados em arquivos separados automaticamente.

---

## 🚀 Funcionalidades
- Login e logout com controle de sessão (via `streamlit-authenticator`)
- Cadastro de gastos com categorias
- Armazenamento local por usuário (`gastos_nome.csv`)
- Visualização de gastos em tabela interativa
- Pronto para deploy na **Streamlit Cloud**

---

## 🛠️ Tecnologias utilizadas
- Python 3.x
- Streamlit
- Streamlit Authenticator
- Pandas
- YAML

---

## 📦 Como rodar localmente

```bash
# Clone o repositório
git clone https://github.com/seuusuario/controle-gastos-streamlit.git
cd controle-gastos-streamlit

# Instale as dependências
pip install -r requirements.txt

# Rode o app
streamlit run app.py
```

---

## 🌐 Deploy na Streamlit Cloud

1. Suba este repositório para o GitHub
2. Vá em: [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Clique em **"New app"** e conecte ao repositório
4. Aponte para `app.py` e publique!
