FROM python:3.10.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY .env /app/

COPY . /app/

EXPOSE 8083

CMD ["python", "manage.py", "runserver", "0.0.0.0:8083"]
