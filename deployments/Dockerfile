FROM python:3.11-slim

WORKDIR /app

# Copy and build requirements first such that it will be cached and any changes
# in the code won't trigger the library installs everytime
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src .
COPY data/sample_problems.json sample_problems.json

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
