web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker wsgi:app --bind=0.0.0.0:${PORT:-8000}
