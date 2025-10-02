# Task Management API

A secure, scalable RESTful API for task management with JWT authentication and role-based access control.

## 🚀 Features

- **Authentication**
  - JWT-based authentication
  - Role-based access control (User & Admin)
  - Secure password hashing with bcrypt
  - Token refresh mechanism

- **Task Management**
  - CRUD operations for tasks
  - Task assignment
  - Status tracking
  - Filtering and pagination

- **API Features**
  - RESTful design
  - Input validation with Pydantic
  - Comprehensive error handling
  - Request/response logging
  - Rate limiting
  - CORS enabled

- **Documentation**
  - Interactive API documentation with Swagger UI
  - ReDoc documentation
  - API versioning

## 🛠️ Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Migrations**: Alembic
- **Authentication**: JWT
- **Validation**: Pydantic
- **Testing**: Pytest
- **Containerization**: Docker

## 📦 Prerequisites

- Python 3.10+
- PostgreSQL 14+
- pip (Python package manager)
- virtualenv (recommended)
- Docker (optional)

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/task-management-api.git
cd task-management-api/backend
```

### 2. Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the backend directory:

```bash
cp .env.example .env
```

Update the `.env` file with your configuration:

```
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/taskdb
TEST_DATABASE_URL=postgresql://user:password@localhost:5432/test_taskdb

# JWT
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# CORS
FRONTEND_URL=http://localhost:5173

# App
ENVIRONMENT=development
DEBUG=True
```

### 5. Set up the database

1. Create a new PostgreSQL database:
   ```bash
   createdb taskdb
   ```

2. Run migrations:
   ```bash
   alembic upgrade head
   ```

### 6. Run the application

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## 📚 API Documentation

### Interactive Documentation

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Available Endpoints

#### Authentication

- `POST /api/v1/auth/register` - Register a new user
- `POST /api/v1/auth/login` - Login and get access token
- `POST /api/v1/auth/refresh` - Refresh access token
- `POST /api/v1/auth/logout` - Logout and invalidate token

#### Users

- `GET /api/v1/users/me` - Get current user profile
- `PATCH /api/v1/users/me` - Update current user profile
- `GET /api/v1/users/` - List all users (Admin only)
- `GET /api/v1/users/{user_id}` - Get user by ID (Admin only)
- `PATCH /api/v1/users/{user_id}` - Update user (Admin only)
- `DELETE /api/v1/users/{user_id}` - Delete user (Admin only)

#### Tasks

- `GET /api/v1/tasks/` - List all tasks (with filters)
- `POST /api/v1/tasks/` - Create a new task
- `GET /api/v1/tasks/{task_id}` - Get task by ID
- `PATCH /api/v1/tasks/{task_id}` - Update task
- `DELETE /api/v1/tasks/{task_id}` - Delete task

## 🧪 Testing

1. Create a test database:
   ```bash
   createdb test_taskdb
   ```

2. Run tests:
   ```bash
   pytest -v
   ```

## 🐳 Docker Setup

1. Build and run the application:
   ```bash
   docker-compose up --build
   ```

2. The API will be available at `http://localhost:8000`

## 🔒 Security

- Password hashing with bcrypt
- JWT token-based authentication
- CORS enabled for frontend URL
- Input validation and sanitization
- Rate limiting
- Security headers

## 📊 Database Schema

### Users Table
- id (UUID, PK)
- email (String, unique, not null)
- hashed_password (String, not null)
- full_name (String)
- is_active (Boolean, default=True)
- is_superuser (Boolean, default=False)
- created_at (DateTime)
- updated_at (DateTime)

### Tasks Table
- id (UUID, PK)
- title (String, not null)
- description (Text)
- status (Enum: pending, in_progress, completed)
- priority (Enum: low, medium, high)
- due_date (DateTime)
- created_by (UUID, FK to users.id)
- assigned_to (UUID, FK to users.id, nullable)
- created_at (DateTime)
- updated_at (DateTime)

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Built with FastAPI and ❤️
</p>
