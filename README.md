# Attendance Log Service

Microservice ini bertanggung jawab untuk mencatat waktu kehadiran (Check-in/Check-out) menggunakan User ID. Dirancang untuk berjalan di perangkat dengan resource terbatas (STB) menggunakan Docker dan SQLite.

## Teknologi
- **Language:** Python 3.9
- **Framework:** FastAPI
- **Database:** SQLite
- **Deployment:** Docker Container

## Cara Menjalankan (Docker)
1. Build image: `docker build -t log-service .`
2. Run container: `docker run -d -p 8000:8000 -v $(pwd)/data:/app/data log-service`

## API Documentation
Akses Swagger UI di: `http://[IP_STB]:8000/docs`