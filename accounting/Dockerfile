# Use the official Python image
FROM python:3.10.1-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the accounting app
COPY accounting/ /app/accounting/

# Copy the project files
COPY news_website/ /app/news_website/
COPY manage.py /app/

# Expose the port
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
