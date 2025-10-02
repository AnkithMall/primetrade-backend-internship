# Task Management Dashboard

A responsive React.js frontend for the Task Management System, featuring secure authentication and an intuitive user interface.

## 🚀 Features

- **Authentication**
  - User registration and login
  - Protected routes based on user roles
  - JWT token management
  - Auto-logout on token expiration

- **Task Management**
  - Create, view, update, and delete tasks
  - Task filtering and sorting
  - Responsive design for all devices
  - Real-time updates

- **User Interface**
  - Clean, modern design
  - Loading states and error handling
  - Form validation
  - Toast notifications

## 🛠️ Tech Stack

- **Framework**: React 18
- **Language**: TypeScript
- **Build Tool**: Vite
- **State Management**: React Query
- **UI Library**: Shadcn UI
- **Form Handling**: React Hook Form
- **Routing**: React Router DOM
- **HTTP Client**: Axios
- **Styling**: Tailwind CSS
- **Icons**: Lucide React
- **Testing**: Jest + React Testing Library

## 📦 Prerequisites

- Node.js (v18+)
- npm (v9+) or yarn (1.22+)
- Backend API (see [Backend README](../backend/README.md))

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/task-management-system.git
cd task-management-system/frontend
```

### 2. Install dependencies

```bash
npm install
# or
yarn install
```

### 3. Configure environment variables

Create a `.env` file in the frontend directory:

```bash
cp .env.example .env
```

Update the `.env` file with your configuration:

```
VITE_API_URL=http://localhost:8000/api/v1
VITE_APP_NAME=Task Management
VITE_APP_VERSION=1.0.0
VITE_APP_ENV=development
```

### 4. Start the development server

```bash
npm run dev
# or
yarn dev
```

The application will be available at `http://localhost:5173`

## 🏗️ Project Structure

```
frontend/
├── public/               # Static files
├── src/
│   ├── assets/           # Images, fonts, etc.
│   ├── components/       # Reusable UI components
│   │   ├── ui/           # Shadcn UI components
│   │   ├── layout/       # Layout components
│   │   └── shared/       # Shared components
│   ├── config/           # App configuration
│   ├── contexts/         # React contexts
│   ├── hooks/            # Custom React hooks
│   ├── lib/              # Utility functions
│   ├── pages/            # Page components
│   │   ├── auth/         # Authentication pages
│   │   ├── dashboard/    # Dashboard pages
│   │   └── tasks/        # Task management pages
│   ├── services/         # API services
│   ├── store/            # State management
│   ├── types/            # TypeScript type definitions
│   ├── App.tsx           # Main App component
│   └── main.tsx          # Entry point
├── .env.example          # Environment variables example
├── .eslintrc.js          # ESLint configuration
├── .prettierrc           # Prettier configuration
├── index.html            # HTML template
├── package.json          # Dependencies and scripts
├── tailwind.config.js    # Tailwind CSS configuration
└── tsconfig.json         # TypeScript configuration
```

## 🔧 Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint
- `npm run format` - Format code with Prettier
- `npm run test` - Run tests
- `npm run test:coverage` - Run tests with coverage
- `npm run test:watch` - Run tests in watch mode

## 🧪 Testing

### Run tests

```bash
npm test
# or
yarn test
```

### Run tests with coverage

```bash
npm run test:coverage
# or
yarn test:coverage
```

## 🐳 Docker Setup

1. Build the Docker image:
   ```bash
   docker build -t task-management-frontend .
   ```

2. Run the container:
   ```bash
   docker run -p 3000:80 task-management-frontend
   ```

   The application will be available at `http://localhost:3000`

## 🌐 Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `VITE_API_URL` | Base URL for API requests | `http://localhost:8000/api/v1` |
| `VITE_APP_NAME` | Application name | `Task Management` |
| `VITE_APP_VERSION` | Application version | `1.0.0` |
| `VITE_APP_ENV` | Application environment | `development` |

## 🔒 Security

- JWT token storage in HTTP-only cookies
- CSRF protection
- Input sanitization
- Rate limiting (handled by backend)
- Secure headers
- Environment variable validation

## 🎨 UI Components

This project uses [Shadcn UI](https://ui.shadcn.com/), a collection of reusable components built with Radix UI and Tailwind CSS.

### Available Components

- Button
- Input
- Form
- Card
- Dialog
- Dropdown Menu
- Navigation Menu
- Table
- Toast
- Tooltip
- And more...

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
  Built with React, TypeScript, and ❤️
</p>
  {
    files: ['**/*.{ts,tsx}'],
    extends: [
      // Other configs...

      // Remove tseslint.configs.recommended and replace with this
      tseslint.configs.recommendedTypeChecked,
      // Alternatively, use this for stricter rules
      tseslint.configs.strictTypeChecked,
      // Optionally, add this for stylistic rules
      tseslint.configs.stylisticTypeChecked,

      // Other configs...
    ],
    languageOptions: {
      parserOptions: {
        project: ['./tsconfig.node.json', './tsconfig.app.json'],
        tsconfigRootDir: import.meta.dirname,
      },
      // other options...
    },
  },
])
```

You can also install [eslint-plugin-react-x](https://github.com/Rel1cx/eslint-react/tree/main/packages/plugins/eslint-plugin-react-x) and [eslint-plugin-react-dom](https://github.com/Rel1cx/eslint-react/tree/main/packages/plugins/eslint-plugin-react-dom) for React-specific lint rules:

```js
// eslint.config.js
import reactX from 'eslint-plugin-react-x'
import reactDom from 'eslint-plugin-react-dom'

export default defineConfig([
  globalIgnores(['dist']),
  {
    files: ['**/*.{ts,tsx}'],
    extends: [
      // Other configs...
      // Enable lint rules for React
      reactX.configs['recommended-typescript'],
      // Enable lint rules for React DOM
      reactDom.configs.recommended,
    ],
    languageOptions: {
      parserOptions: {
        project: ['./tsconfig.node.json', './tsconfig.app.json'],
        tsconfigRootDir: import.meta.dirname,
      },
      // other options...
    },
  },
])
```
