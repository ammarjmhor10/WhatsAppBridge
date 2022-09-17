# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10-slim


# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED True

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install python-dotenv
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app
COPY ./app /app

EXPOSE 8080
# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers


# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
