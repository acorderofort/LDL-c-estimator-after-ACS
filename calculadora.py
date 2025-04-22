import streamlit as st
import numpy as np

# Coeficientes del modelo ajustado sin interacción
b0 = 0.4974
b_ldl = -0.0147
b_estat = -0.4649
b_edad = -0.0076
b_dm = 0.5161
b_ci = -0.3076

st.set_page_config(page_title="Calculadora de Riesgo LDL < 55")
st.title("Calculadora de Riesgo: LDL < 55 mg/dL")

st.markdown("Ingrese los datos del paciente para estimar la probabilidad de lograr LDL < 55.")

# Entradas del usuario
ldl = st.slider("LDL (mg/dL)", min_value=50, max_value=200, value=100)
estatinas = st.radio("¿El paciente está tomando estatinas?", [0, 1], format_func=lambda x: "Sí" if x else "No")
edad = st.slider("Edad", min_value=18, max_value=100, value=60)
dm = st.radio("¿El paciente tiene diabetes mellitus?", [0, 1], format_func=lambda x: "Sí" if x else "No")
ci = st.radio("¿Antecedente de cardiopatía isquémica?", [0, 1], format_func=lambda x: "Sí" if x else "No")

# Cálculo del logit y probabilidad
logit = (
    b0 +
    b_ldl * ldl +
    b_estat * estatinas +
    b_edad * edad +
    b_dm * dm +
    b_ci * ci
)
prob = 1 / (1 + np.exp(-logit))

# Resultado
st.subheader("Resultado")
st.metric("Probabilidad estimada de LDL < 55", f"{prob*100:.1f}%")
