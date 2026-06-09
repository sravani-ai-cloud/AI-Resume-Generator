# AI Resume Generator

An AI-powered Resume Generator built using FastAPI, Gemini AI, JWT Authentication, and Docker.

## Features

* User Authentication using JWT Tokens
* Resume Generation using Gemini AI
* Resume Review Agent
* ATS Optimization Agent
* Profile Analysis Agent
* FastAPI REST APIs
* Dockerized Deployment
* Environment Variable Management using .env
* Modular Multi-Agent Architecture

## Tech Stack

* Python
* FastAPI
* Gemini AI
* JWT Authentication
* Docker
* Uvicorn
* REST APIs

## Project Architecture

User Request

↓

JWT Authentication

↓

Profile Analyzer Agent

↓

Resume Writer Agent

↓

ATS Optimizer Agent

↓

Resume Reviewer Agent

↓

Generated Resume Response

## API Endpoints

### Login

POST /login

Request:

```json
{
  "username": "admin",
  "password": "password123"
}
```

### Generate Resume

POST /generate-resume

Headers:

```text
Authorization: Bearer <token>
```

Request:

```json
{
  "name": "Sravani Koriginja",
  "experience": 5,
  "skills": ["Python", "AWS", "FastAPI"]
}
```

## Docker

Build Image

```bash
docker build -t resume-generator .
```

Run Container

```bash
docker run -d -p 8000:8000 resume-generator
```

## Future Enhancements

* React Frontend
* Database Integration
* CI/CD Pipeline
* Kubernetes Deployment
* Multi-User Support
* Resume PDF Export

## Author

Sravani Koriginja

