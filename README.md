# Multi-Tech Test Repository

This repository is designed for testing the DevOps Agent system with realistic build failures.

## Structure

- `backend/` - Flask API (Python)
- `frontend/` - React app (JavaScript)
- `docker/` - Dockerfiles
- `.github/workflows/` - CI/CD pipelines
- `config/` - Configuration files

## Intentional Bugs for Testing

This repo contains several intentional bugs that can be enabled/disabled:

### 1. Python Import Error
**File:** `backend/app.py`
**Trigger:** Uncomment the `json.dumps()` line
**Expected Fix:** Add `import json` at top

### 2. Python Syntax Error
**File:** `backend/app.py`
**Trigger:** Uncomment the `def calculate_total(items)` function
**Expected Fix:** Add `:` after function definition

### 3. Missing Package
**File:** `backend/requirements.txt`
**Trigger:** Uncomment `nonexistent-package==0.1.0`
**Expected Fix:** Remove that line

### 4. Deprecated Package
**File:** `backend/requirements.txt`
**Trigger:** Uncomment `pkg-resources==0.0.0`
**Expected Fix:** Remove that line

### 5. Version Conflict
**File:** `frontend/package.json`
**Bug:** Already present - React 18 with React Router 5
**Expected Fix:** Update react-router-dom to 6.x

### 6. ESLint Errors
**File:** `frontend/app.js`
**Trigger:** Uncomment the useState/useEffect code without imports
**Expected Fix:** Add React imports

## Running Tests

### Backend
```bash
cd backend
pip install -r requirements.txt
pytest tests/
```

### Frontend
```bash
cd frontend
npm install
npm run lint
```

## Environment Variables

Required for production:
- `DATABASE_URL` - PostgreSQL connection string
- `SECRET_KEY` - Flask secret key
- `NODE_ENV` - Node environment (development/production)

## License

MIT