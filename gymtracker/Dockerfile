FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN mkdir -p staticfiles && \
    python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "gymtracker.wsgi:application", "--bind", "0.0.0.0:8000"]
