# Gunakan image python slim agar hemat storage (cocok untuk STB)
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements dan install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy seluruh source code
COPY . .

# Expose port (Misalnya 8000)
EXPOSE 8000

# Command untuk menjalankan aplikasi
# host 0.0.0.0 agar bisa diakses dari luar STB (network public)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]