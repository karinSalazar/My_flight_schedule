FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install streamlit openai
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]