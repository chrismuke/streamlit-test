FROM python:3.12-slim
WORKDIR /app
RUN pip install --no-cache-dir streamlit
COPY app.py .
EXPOSE 8501
HEALTHCHECK CMD curl -sf http://localhost:8501/_stcore/health || exit 1
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.headless=true", "--server.address=0.0.0.0"]
