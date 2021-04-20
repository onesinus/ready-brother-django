FROM python:3.9.2-slim-buster

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ENV "Production"

RUN pip install --upgrade pip

COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

CMD ["gunicorn", "--bind", "0.0.0.0:80", "--workers", "3", "ocommerce.wsgi:application"]
