FROM python:3.10

WORKDIR /backend

COPY requirements.txt backend/requirements.txt

RUN pip install -r backend/requirements.txt

COPY . /backend

EXPOSE 8000

ENV PYTHONPATH "${PYTHONPATH}:/backend"


CMD ["gunicorn", "--forwarded-allow-ips", "*", "backend.main:app", "--workers", "8", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
