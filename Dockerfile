FROM python:3.11
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN useradd -rm -d /code -s /bin/bash -g root -G sudo -u 1001 ubuntu

COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

WORKDIR /code

COPY . /code

USER ubuntu

EXPOSE 8000

CMD bash -c 'echo "Waiting for mysql..." && sleep 40 && alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 8000'