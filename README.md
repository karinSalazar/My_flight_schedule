# 🛫 Optimización de Vuelos con Streamlit + OpenAI

Este proyecto utiliza algoritmos genéticos para optimizar vuelos y proporciona análisis con modelos de lenguaje GPT. Empaquetado para ejecución local o despliegue en la nube.

## 🚀 Cómo usar

```bash
# 1. Clonar y entrar al proyecto
git clone https://github.com/tu_usuario/flight-ai
cd flight-ai

# 2. Ejecutar en Docker
docker-compose up --build
```

## 📦 Estructura
- `app.py`: interfaz principal con Streamlit
- `optimizer.py`: lógica de optimización genética
- `gpt_analysis.py`: interpretación con IA generativa
- `Dockerfile` + `docker-compose.yml`: despliegue portable