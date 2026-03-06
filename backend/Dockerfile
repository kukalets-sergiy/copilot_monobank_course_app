# Dockerfile for the backend

FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy pyproject.toml and install dependencies
COPY backend/pyproject.toml ./
RUN pip install poetry && poetry install --no-dev

# Copy the rest of the app
COPY backend/ .

# Command to run the application
CMD ["uvicorn", "main:app"]
