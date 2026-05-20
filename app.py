import streamlit as st


st.set_page_config(page_title="Orcamento de PC", layout="centered")

st.title("Calculadora de Orcamento para PC")
st.subheader("Monte o computador dos seus sonhos, Mister Andre!")
st.write("---")


def pedir_valor(nome_da_peca):
    valor = st.number_input(f"Valor da {nome_da_peca} (R$):", min_value=0.0, step=50.0)
    return valor

st.write("### Digite o valor de cada componente:")


placa_mae    = pedir_valor("Placa-mae")
ram          = pedir_valor("Memoria RAM")
processador  = pedir_valor("Processador")
gpu          = pedir_valor("Placa de video")
ssd          = pedir_valor("Armazenamento SSD/HDD")
fonte        = pedir_valor("Fonte de alimentacao")
gabinete     = pedir_valor("Gabinete")
cooler       = pedir_valor("Cooler")
monitor      = pedir_valor("Monitor")
perifericos  = pedir_valor("Teclado e mouse")
sistema      = pedir_valor("Sistema operacional")
outros       = pedir_valor("Outros perifericos")

st.write("---")

total = placa_mae + ram + processador + gpu + ssd + fonte + gabinete + cooler + monitor + perifericos + sistema + outros

st.write("### Resumo do Orcamento")
st.metric(label="VALOR TOTAL DO PC", value=f"R$ {total}")

if st.button("Finalizar Orcamento"):
    st.success(f"Mister Andre, o orcamento ficou em R$ {total}! Pronto para montar!")
    st.balloons()
