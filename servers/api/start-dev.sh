clear
echo "Starting Development Server..."
gunicorn routes:api --bind localhost:5000 --workers=4 --access-logfile - --worker-class "egg:meinheld#gunicorn_worker"
