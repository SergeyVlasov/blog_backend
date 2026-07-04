FROM python:3.12
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN chmod +x /app/entrypoint.sh
CMD ["sh", "/app/entrypoint.sh"]
