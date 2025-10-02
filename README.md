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
- **Database**: MongoDB
- **Authentication**: JWT
- **API Documentation**: Swagger UI
- **Containerization**: Docker

## 📦 Prerequisites

- Node.js (v18+)
- Python (3.10+)
- MongoDB Atlas
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

5. Start the backend server:
   ```bash
   uvicorn app.main:app --reload
   ```

   The API will be available at `http://localhost:8000`
   
   Access Swagger documentation at `http://localhost:8000/docs`

### Admin Management

#### 1. Create a New Admin User

Use the `create_admin.py` script to create a new admin user:

```bash
# From the backend directory
python scripts/create_admin.py
```

You'll be prompted to enter:
- Admin email
- Admin name
- Password

#### 2. Promote Existing User to Admin

Use the `promote_user.py` script to promote an existing user to admin:

```bash
# From the backend directory
python scripts/promote_user.py
```

You'll be prompted to enter either:
- User's email address
- User's ObjectId

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

## 🐳 Docker Setup

### Build the Docker Image

1. From the project root, build the backend image:
   ```bash
   docker build -t task-management-backend .
   ```

2. Run the container (make sure you have a .env file in the project root):
   ```bash
   docker run -p 8000:8000 --env-file .env task-management-backend
   ```

   - The API will be available at `http://localhost:8000`
   - Swagger UI: `http://localhost:8000/docs`

## 🚀 Deployment

This application is deployed using:
- **Backend**: Hosted on Azure Container Apps
- **Frontend**: Deployed on Vercel
- **Database**: MongoDB Atlas (Cloud)

### Live Demo
- **Frontend**: [Live Demo](https://primetrade-backend-internship.vercel.app)
- **API Documentation**: [Swagger UI](https://task-backend.wonderfulmushroom-7d76aaa2.westus2.azurecontainerapps.io/docs)

## 🔒 Environment Variables

### Backend (.env)

```
# MongoDB Atlas
MONGO_URI=your_mongodb_atlas_connection_string

# JWT
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS
FRONTEND_URL=http://localhost:5173

# App
ENVIRONMENT=development
DEBUG=True
```

### Frontend (.env)
```
VITE_API_URL=http://localhost:8000/api/v1
```

## 🔒 Environment Variables

### Backend

```
# Database
MONGO_URI=your_mongodb_atlas_connection_string

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
