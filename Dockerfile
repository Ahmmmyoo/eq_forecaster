FROM python:3.9-slim

COPY . /app

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

ENV PYTHONPATH="/app"

CMD ["streamlit", "run", "src/client/pages/overview.py"]
