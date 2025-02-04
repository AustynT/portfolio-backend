FROM python:alpine

ENV PYTHONUNBUFFERED=1
ENV WORKDIR=/app

WORKDIR $WORKDIR


RUN apk update && apk add --no-cache \
  gcc \
  musl-dev \
  postgresql-dev  

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn","app.main:app","--host","0.0.0.0", "--port", "8000"]

