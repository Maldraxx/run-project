FROM python:3.10-slim-buster
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY req.txt req.txt
RUN pip install -r req.txt

COPY . .

CMD [ "python", "manage.py", "runserver", "0.0.0.0:${PORT:-8080}" ]

# docker run -p 8080:8080 <image_id>