FROM python:3.10-slim-buster
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY req.txt req.txt
RUN pip install -r req.txt

ENV PORT 8080
ENV HOST 0.0.0.0

COPY . .

CMD [ "python", "./run/manage.py", "runserver", "0.0.0.0:$PORT" ]

# docker run -p 8080:8080 <image_id>