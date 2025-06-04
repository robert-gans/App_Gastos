
import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd
import os
import yaml
from yaml.loader import SafeLoader

# Carrega credenciais do arquivo YAML
with open("users.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

name, authentication_status, username = authenticator.login("Login", "sidebar")

if authentication_status:
    authenticator.logout("Logout", "sidebar")
    st.success(f"Bem-vindo(a), {name}!")

    filename = f"gastos_{username}.csv"
    if not os.path.exists(filename):
        df = pd.DataFrame(columns=["Data", "Descrição", "Categoria", "Valor"])
        df.to_csv(filename, index=False)
    else:
        df = pd.read_csv(filename)

    with st.form("novo_gasto"):
        data = st.date_input("Data")
        descricao = st.text_input("Descrição")
        categoria = st.selectbox("Categoria", ["Alimentação", "Transporte", "Lazer", "Outros"])
        valor = st.number_input("Valor (R$)", min_value=0.0, step=0.01)
        enviar = st.form_submit_button("Adicionar")

        if enviar:
            novo = pd.DataFrame([[data, descricao, categoria, valor]], columns=df.columns)
            df = pd.concat([df, novo], ignore_index=True)
            df.to_csv(filename, index=False)
            st.success("Gasto adicionado com sucesso!")

    st.subheader("🧾 Gastos Registrados")
    st.dataframe(df)

elif authentication_status is False:
    st.error("Usuário ou senha incorretos")
elif authentication_status is None:
    st.warning("Digite seu login para continuar.")
