import streamlit as st

st.title('Simulação de conta bancária 💵')
st.write('### Bem-vindo, Mister André!')

# Mantém o saldo na memória do navegador
if 'saldo' not in st.session_state:
    st.session_state.saldo = 1000.0

# Menu de opções simples
opcao = st.radio(
    'Escolha uma operação:',
    ['Consultar saldo', 'Efetuar saque', 'Encerrar operação']
)

# 1 - CONSULTAR SALDO
if opcao == 'Consultar saldo':
    st.write(f"Mister André, seu Saldo atual é de: **R$ {st.session_state.saldo:.2f}** 💰")

# 2 - EFETUAR SAQUE
elif opcao == 'Efetuar saque':
    valor_saque = st.number_input("Digite o valor do saque:", min_value=0.0, step=10.0)
    
    if st.button('Confirmar Saque'):
        if valor_saque <= 0:
            st.write("Mister André, valor inválido para saque 😔")
        elif valor_saque > st.session_state.saldo:
            st.write("Mister André, saldo insuficiente 😔")
        else:
            st.session_state.saldo -= valor_saque
            st.write(f"Saque de R$ {valor_saque:.2f} realizado com sucesso! 💰")
            st.write(f"Saldo atualizado: **R$ {st.session_state.saldo:.2f}**")

# 3 - ENCERRAR OPERAÇÃO
elif opcao == 'Encerrar operação':
    st.write(f"Sistema finalizado. Saldo final: **R$ {st.session_state.saldo:.2f}** 💰")

