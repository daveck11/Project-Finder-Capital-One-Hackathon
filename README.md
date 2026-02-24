# Project Finder - Capital One Hackathon

## Overview

Project Finder is a web application designed to help students and professionals discover and join hackathon projects. It solves the problem of fragmented project discovery by aggregating projects from multiple platforms into a single, searchable interface.

## Problem Statement

Finding hackathon projects is difficult because:
- Projects are scattered across different platforms (Devpost, Hackathon.io, etc.)
- Discoverability is poor - hard to find projects matching your skills
- No centralized place to see what projects are available

## Solution

Project Finder provides:
- **Aggregated Project Listings**: Pulls projects from multiple sources
- **Advanced Search & Filtering**: Find projects by skills, technologies, and more
- **Project Details**: View complete project information including requirements and goals
- **Team Formation**: Connect with other participants to build your team

## Features

### For Participants
- **Discover Projects**: Browse and search through a comprehensive list of hackathon projects
- **Filter by Skills**: Find projects that match your technical skills (e.g., Python, React, AI)
- **View Project Details**: See project requirements, goals, and technologies used
- **Join Projects**: Express interest in joining a project and connect with the team
- **Team Building**: Find other participants with complementary skills to form a team

### For Organizers (Future Scope)
- **Project Submission**: Easily submit your hackathon project to the platform
- **Project Management**: Track participants interested in your project
- **Team Management**: Organize your project team and communicate with members

## Technology Stack

### Frontend
- **Framework**: React 19 with TypeScript
- **Styling**: Tailwind CSS v4
- **State Management**: TanStack Query (React Query)
- **UI Components**: Custom components with Tailwind

### Backend
- **Framework**: FastAPI
- **Language**: Python 3.13
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Authentication**: JWT (JSON Web Tokens)
- **Background Tasks**: Celery with Redis

### Infrastructure
- **Containerization**: Docker
- **Container Orchestration**: Docker Compose
- **Deployment**: Render (Cloud Platform)

## Project Structure

```
project-finder/
├── backend/                  # FastAPI backend application
│   ├── app/
│   │   ├── api/              # API endpoints
│   │   ├── core/             # Core configuration and utilities
│   │   ├── db/               # Database models and session management
│   │   ├── schemas/          # Pydantic request/response models
│   │   ├── services/         # Business logic and service layer
│   │   └── main.py           # Application entry point
│   ├── requirements.txt      # Python dependencies
│   └── Dockerfile            # Backend Docker configuration
├── frontend/                 # React frontend application
│   ├── src/
│   │   ├── components/       # Reusable UI components
│   │   ├── pages/            # Page components
│   │   ├── services/         # API service layer
│   │   ├── store/            # State management
│   │   └── App.tsx           # Main application component
│   ├── package.json          # Frontend dependencies
│   └── Dockerfile            # Frontend Docker configuration
├── docker-compose.yml        # Multi-container Docker setup
├── .env.example              # Environment variable template
└── README.md                 # Project documentation
```

## Getting Started

### Prerequisites
- Docker Desktop installed and running
- Node.js 18+ (for frontend development)
- Python 3.13+ (for backend development)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd project-finder
   ```

2. **Start the application**
   ```bash
   docker-compose up --build
   ```

   This will start:
   - Backend API on `http://localhost:8000`
   - Frontend on `http://localhost:3000`
   - PostgreSQL database on `http://localhost:5432`
   - Redis on `http://localhost:6379`

### Development

#### Backend Development
```bash
# Navigate to backend directory
cd backend

# Install dependencies
pip install -r requirements.txt

# Run the development server
uvicorn app.main:app --reload
```

#### Frontend Development
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Run the development server
npm run dev
```

## API Documentation

### Authentication
- **Login**: `POST /api/auth/login`
- **Register**: `POST /api/auth/register`
- **Refresh Token**: `POST /api/auth/refresh`

### Projects
- **List Projects**: `GET /api/projects`
- **Get Project**: `GET /api/projects/{project_id}`
- **Create Project**: `POST /api/projects` (requires authentication)
- **Update Project**: `PUT /api/projects/{project_id}` (requires authentication)
- **Delete Project**: `DELETE /api/projects/{project_id}` (requires authentication)

### Search
- **Search Projects**: `GET /api/projects/search?q={query}`

### Skills
- **List Skills**: `GET /api/skills`

### Users
- **Get Current User**: `GET /api/users/me` (requires authentication)
- **Update Profile**: `PUT /api/users/me` (requires authentication)

## Environment Variables

Create a `.env` file in the root directory based on `.env.example`:

```env
# Database Configuration
DATABASE_URL=postgresql://user:password@db:5432/project_finder

# JWT Configuration
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Redis Configuration
REDIS_URL=redis://redis:6379/0

# Celery Configuration
CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0
```

## Deployment

### Render Deployment

1. **Create a Render account**
   - Go to [render.com](https://render.com)
   - Sign up or log in

2. **Deploy the Backend**
   - Click "New" -> "Web Service"
   - Connect your GitHub repository
   - Settings:
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `uvicorn app.main:app --host [IP_ADDRESS] --port $PORT`
     - **Environment**: Python
     - **Region**: Choose your preferred region
   - Add environment variables (see `.env.example`)
   - Click "Create Web Service"

3. **Deploy the Frontend**
   - Click "New" -> "Web Service"
   - Connect your GitHub repository
   - Settings:
     - **Build Command**: `npm install && npm run build`
     - **Start Command**: `npm run start`
     - **Environment**: Node
     - **Region**: Choose your preferred region
   - Add environment variables:
     - `VITE_API_URL=https://your-backend-url.onrender.com/api`
   - Click "Create Web Service"

4. **Configure CORS**
   - In your backend settings, go to "Environment"
   - Add `https://your-frontend-url.onrender.com` to the `ALLOWED_ORIGINS` variable

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Capital One for hosting the hackathon
- All the open-source libraries