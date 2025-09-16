FROM python:3.11

WORKDIR /app
RUN mkdir /app/logs
COPY . /app
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip freeze

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload", "--reload-dir", "/app"]
