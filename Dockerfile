FROM python:3.10-slim-buster
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY req.txt req.txt
RUN pip install -r req.txt

COPY . .

RUN pip install gunicorn

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "run.wsgi:application"]


# docker run -p 8080:8080 <image_id>