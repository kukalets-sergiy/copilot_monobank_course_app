FROM python:3.9-slim

COPY pyproject.toml .

RUN pip install build

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]