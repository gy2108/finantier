FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY encrypt/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
CMD python encrypt.py