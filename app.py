import streamlit as st
from optimizer import run_optimization
from gpt_analysis import analyze_results

st.title("✈️ Optimización de Vuelos con IA Generativa")
if st.button("Ejecutar optimización"):
    result = run_optimization()
    st.success("Optimización completada.")
    st.write(result)
    st.subheader("📊 Análisis con IA")
    st.write(analyze_results(result))