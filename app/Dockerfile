FROM python:3.12.0-slim-bookworm

COPY . /app/
WORKDIR /app/

RUN apt-get update \
    && apt-get install libpq-dev gcc -y \
    && pip install -r requirements.txt

ENV STREAMLIT_SERVER_PORT=80

CMD ["streamlit", "run", "home.py"]
