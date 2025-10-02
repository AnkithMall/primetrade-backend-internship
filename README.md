# Secure Task Management System

A full-stack application featuring secure authentication, role-based access control, and task management capabilities.

## 🚀 Features

- **User Authentication**
  - Secure JWT-based authentication
  - Role-based access control (User & Admin)
  - Password hashing with bcrypt

- **Task Management**
  - Create, Read, Update, Delete tasks
  - Task assignment and status tracking
  - Search and filter functionality

- **API**
  - RESTful API design
  - API versioning
  - Input validation and sanitization
  - Comprehensive error handling
  - Swagger API documentation

- **Frontend**
  - Responsive React.js interface
  - Protected routes
  - Form validation
  - Real-time feedback

## 🛠️ Tech Stack

- **Backend**: Python (FastAPI)
- **Frontend**: React.js with TypeScript
- **Database**: PostgreSQL
- **Authentication**: JWT
- **API Documentation**: Swagger UI
- **Containerization**: Docker

## 📦 Prerequisites

- Node.js (v18+)
- Python (3.10+)
- PostgreSQL (v14+)
- Docker (optional)

## 🚀 Quick Start

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Update the .env file with your configuration
   ```

5. Run database migrations:
   ```bash
   alembic upgrade head
   ```

6. Start the backend server:
   ```bash
   uvicorn app.main:app --reload
   ```

   The API will be available at `http://localhost:8000`
   
   Access Swagger documentation at `http://localhost:8000/docs`

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Update the .env file with your API URL
   ```

4. Start the development server:
   ```bash
   npm run dev
   ```

   The frontend will be available at `http://localhost:5173`

## 🐳 Docker Setup (Optional)

1. Build and run the application:
   ```bash
   docker-compose up --build
   ```

2. Access the application:
   - Frontend: `http://localhost:3000`
   - Backend API: `http://localhost:8000`
   - Swagger UI: `http://localhost:8000/docs`

## 🔒 Environment Variables

### Backend

```
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/taskdb

# JWT
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS
FRONTEND_URL=http://localhost:5173
```

### Frontend

```
VITE_API_URL=http://localhost:8000/api/v1
```

## 📚 API Documentation

Comprehensive API documentation is available through Swagger UI:
- Development: `http://localhost:8000/docs`
- Production: `https://your-api-url.com/docs`

## 🧪 Testing

### Backend Tests

```bash
pytest
```

### Frontend Tests

```bash
npm test
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- FastAPI for the amazing backend framework
- React.js for the frontend library
- All open-source contributors

---

<p align="center">
  Made with ❤️ for Primetrade.ai
</p>
