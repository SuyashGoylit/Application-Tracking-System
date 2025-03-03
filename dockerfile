# Use the official Python image as the base
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Manually install NC
RUN apt-get update && apt-get install -y netcat-traditional postgresql-client && rm -rf /var/lib/apt/lists/*

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Django runs on
EXPOSE 8000

# Run migrations and start Django server
CMD ["sh", "-c", "python manage.py migrate && python manage.py loaddata candidate.json && python manage.py runserver 0.0.0.0:8000"]
