import streamlit as st
import numpy as np

# Coeficientes del modelo ajustado sin interacción
b0 = 0.4974
b_ldl = -0.0147
b_estat = -0.4649
b_edad = -0.0076
b_dm = 0.5161
b_ci = -0.3076

st.set_page_config(page_title="LDL-C <55 mg/dl risk calculator")
st.title("Estimation for ACS patients treated without PCSK9 inhibitors")

st.markdown("Required variables")

# Entradas del usuario
ldl = st.slider("LDL (mg/dL)", min_value=50, max_value=200, value=100)
estatinas = st.radio("¿On-treatment with statins?", [0, 1], format_func=lambda x: "Yes" if x else "No")
edad = st.slider("Age", min_value=18, max_value=100, value=60)
dm = st.radio("¿Diabetes mellitus?", [0, 1], format_func=lambda x: "Yes" if x else "No")
ci = st.radio("¿Previous coronary heart disease?", [0, 1], format_func=lambda x: "Yes" if x else "No")

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
st.subheader("Result")
st.metric("Estimated probability of LDL-C <55 mg/dl with statins plus ezetimibe", f"{prob*100:.1f}%")
