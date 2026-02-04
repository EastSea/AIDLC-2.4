# Table Order API (Unit 1)

Backend API for the Table Order Service built with FastAPI, SQLAlchemy, and PostgreSQL.

## Setup

### 1. Install Dependencies

```bash
cd api
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Environment Variables

Create a `.env` file in the `api` directory:

```env
DATABASE_URL=postgresql://tableorder:tableorder123@localhost:5432/tableorder
REDIS_URL=redis://localhost:6379
SECRET_KEY=your-secret-key-change-in-production
```

### 3. Database Migration

```bash
# Initialize database (first time only)
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

### 4. Run the Server

```bash
uvicorn app.main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

### Customer API (`/api/customer/*`)

- `POST /api/customer/auth/login` - Table login
- `GET /api/customer/categories` - Get categories
- `GET /api/customer/menus` - Get menus (query: category_id, serving_size)
- `GET /api/customer/menus/{id}` - Get menu detail
- `GET /api/customer/menus/{id}/image` - Get menu image
- `POST /api/customer/orders` - Create order
- `GET /api/customer/orders` - Get orders (query: session_id)
- `GET /api/customer/orders/{id}` - Get order detail
- `POST /api/customer/staff-call` - Call staff

### Admin API (`/api/admin/*`)

- `POST /api/admin/auth/login` - Admin login
- `POST /api/admin/auth/logout` - Admin logout
- `GET /api/admin/orders` - Get orders (query: table_id)
- `GET /api/admin/orders/{id}` - Get order detail
- `PATCH /api/admin/orders/{id}/status` - Update order status
- `DELETE /api/admin/orders/{id}` - Delete order
- `GET /api/admin/tables` - Get tables
- `GET /api/admin/tables/{id}` - Get table detail
- `POST /api/admin/tables/{id}/complete` - Complete table session
- `GET /api/admin/menus` - Get menus
- `GET /api/admin/staff-calls` - Get staff calls (query: acknowledged)
- `PATCH /api/admin/staff-calls/{id}/acknowledge` - Acknowledge staff call

## Project Structure

```
api/
├── alembic/              # Database migrations
├── app/
│   ├── models/          # SQLAlchemy models
│   ├── schemas/         # Pydantic schemas
│   ├── services/        # Business logic
│   ├── routers/         # API endpoints
│   │   ├── customer/    # Customer endpoints
│   │   └── admin/       # Admin endpoints
│   ├── auth.py          # Authentication utilities
│   ├── config.py        # Configuration
│   ├── database.py      # Database connection
│   ├── dependencies.py  # FastAPI dependencies
│   ├── redis.py         # Redis client
│   └── main.py          # FastAPI application
├── requirements.txt     # Python dependencies
└── alembic.ini         # Alembic configuration
```

## Development

### Database Migrations

```bash
# Create a new migration
alembic revision --autogenerate -m "Description"

# Apply migrations
alembic upgrade head

# Rollback migration
alembic downgrade -1
```

### Testing

```bash
pytest
```

## Notes

- All endpoints (except login) require JWT authentication via Bearer token
- Customer endpoints use table authentication
- Admin endpoints use admin authentication
- Mock data structure matches the mock server on port 8001
