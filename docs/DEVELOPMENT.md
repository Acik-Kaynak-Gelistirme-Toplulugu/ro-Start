# Development Guide

## Getting Started

### Prerequisites

- Python 3.9+
- Node.js 18+
- Git

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start.git
cd ro-start

# Run installation script
chmod +x scripts/install.sh
./scripts/install.sh
```

Or manually:

```bash
# Backend setup
python3 -m venv venv
source venv/bin/activate
pip install -e .
pip install pytest ruff black  # Dev dependencies

# Frontend setup
cd frontend
npm install
npm run build
cd ..
```

## Development Workflow

### Running in Development Mode

```bash
# Terminal 1: Run backend
source venv/bin/activate
python3 backend/main.py

# Terminal 2: Frontend development (optional)
cd frontend
npm run dev
```

### Code Quality

Before committing, ensure code quality:

```bash
# Python
ruff check .
black .

# Frontend
cd frontend
npm run lint
npm run format
```

### Install Git Hooks

```bash
# Install pre-commit hook
cp scripts/pre-commit .git/hooks/
chmod +x .git/hooks/pre-commit
```

## Project Structure

```
ro-start/
├── backend/              # Python backend
│   ├── core/            # Core utilities
│   ├── ui/              # UI pages
│   └── main.py          # Entry point
├── frontend/            # React frontend
│   ├── components/      # React components
│   ├── config/          # Frontend config
│   └── dist/            # Built files
├── assets/              # Static assets
│   └── locales/         # Translation files
├── configs/             # App configuration
├── scripts/             # Build/install scripts
├── tests/               # Test files
│   ├── backend/         # Python tests
│   └── frontend/        # React tests
└── docs/                # Documentation
```

## Testing

### Backend Tests

```bash
# Run all tests
pytest tests/backend/

# Run specific test
pytest tests/backend/test_sys_info.py

# With coverage
pytest --cov=backend tests/backend/
```

### Frontend Tests

```bash
cd frontend
npm test
```

## Building

### Development Build

```bash
cd frontend
npm run build
```

### Production Build

```bash
./scripts/build.sh
```

This creates:

- Python wheel in `dist/`
- Frontend bundle in `frontend/dist/`

## Adding Features

### 1. Backend Feature

```python
# backend/core/my_feature.py
def my_function():
    """New feature implementation"""
    pass
```

### 2. Frontend Component

```typescript
// frontend/components/MyComponent.tsx
export function MyComponent() {
  return <div>My Component</div>;
}
```

### 3. Add Tests

```python
# tests/backend/test_my_feature.py
def test_my_function():
    assert my_function() == expected_result
```

### 4. Update i18n

```json
// assets/locales/en_US.json
{
  "my_feature": {
    "title": "My Feature"
  }
}
```

## Debugging

### Backend Debugging

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Frontend Debugging

Open DevTools in the application:

- Linux: `Ctrl+Shift+I`
- macOS: `Cmd+Option+I`

## Common Issues

### Import Errors

If you get import errors, ensure:

1. Virtual environment is activated
2. Package is installed in editable mode: `pip install -e .`

### Frontend Not Loading

1. Check if frontend is built: `ls frontend/dist/`
2. Rebuild: `cd frontend && npm run build`

### Permission Errors

System operations require `pkexec`. Ensure it's installed:

```bash
which pkexec
```

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for contribution guidelines.
