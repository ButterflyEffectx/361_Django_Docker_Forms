# Django Application with Docker

This is a Django project containerized using Docker. The project includes a user registration page (`/userRegistration/`) and is structured with multiple directories. This guide will walk you through setting up, running, and contributing to the project.

## Table of Contents
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation Steps](#installation-steps)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

```bash
firstproject/
├── formsDemo/
│   └── formsApp/
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── tests.py
│       ├── views.py
│       └── manage.py       # Main entry point for Django server
├── Dockerfile              # Docker configuration
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```
Clone This Project
```bash
git clone https://github.com/ButterflyEffectx/361_Django_Docker_Forms.git
```
Next step cd to your repo
```bash
cd 361_Django_Docker_Forms
```
build your image from dockerfile
```bash
docker build -t your-docker-username/django-app .
```
Follow this step to test the project 👇🏻
```bash
docker run -p 8000:8000 your-docker-username/django-app
```
```bash
http://localhost:8000/userRegistration/
```

# Last step
## Push your image to Docker hub
```bash
docker push your-docker-username/django-app .
```
