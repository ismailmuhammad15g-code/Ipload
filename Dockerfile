FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY bot.py .
COPY .env.example .env

# Create directory for database
RUN mkdir -p /app/data

# Set environment variable for bot token (can be overridden)
ENV BOT_TOKEN=7933653463:AAEQ7wrD-XH4p6SOSLpXfHo36PmW77AOKAo

# Run the bot
CMD ["python", "bot.py"]
