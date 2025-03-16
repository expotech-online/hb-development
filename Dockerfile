# Use the official Python image as a base
FROM python:3.12

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
# Set the working directory
WORKDIR /app

# Copy the project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Set environment variable to define STATIC_ROOT
#ENV DJANGO_STATIC_ROOT=/app/staticfiles

# Run collectstatic with the environment variable
#RUN python manage.py collectstatic --noinput --settings=myapp.settings

RUN apt-get update && apt-get install -y default-mysql-client
# Expose port 8000 for Django
EXPOSE 8000


# Start the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
