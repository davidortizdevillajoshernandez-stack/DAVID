
# 1. Defino st
import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Salud 3º ESO", page_icon="🏥")

# Título y Descripción
st.title("% Calculadora de Descuentos %")
st.markdown("Bienvenido. Introduce tus datos para calcular tu precio de final.")
st.write("---") # Línea separadora

# 2. Entrada de Datos (Barra Lateral)
st.sidebar.header("Tus Datos")
precio_original = st.sidebar.number_input("Tu precio en (€) ", min_value=0, max_value=10000000000000, value=60)
descuento = st.sidebar.slider("Tu descuento (%)", 0, 100)

# 3. Botón de Cálculo y Lógica
if st.button("Calcular ahora"):
   
    # Fórmula Matemática:
    ahorro = precio_original * (descuento / 100)
    precio_final = precio_original - ahorro
   
    # 4. Mostrar Resultado con Diseño
    col1, col2 = st.columns(2)
   
    with col1:
        # Usamos metric para que el número se vea grande
        st.metric(label="tu precio_final es:", value=f"{precio_final:.2f}")
