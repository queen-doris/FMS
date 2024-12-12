# Fleet Management System with fastAPI

## Overview
The **Fleet Management System** is a RESTful API built with FastAPI to manage vehicle data efficiently. The system enables CRUD (Create, Read, Update, Delete) operations on vehicles and leverages a PostgreSQL database for data persistence. This project serves as a foundational backend for fleet management solutions.

---

## Features
- **Add Vehicles**: Register new vehicles with details such as registration number, model, and owner.
- **View Vehicles**: Retrieve a list of all registered vehicles or details of a specific vehicle.
- **Update Vehicle Information**: Modify details of existing vehicles.
- **Delete Vehicles**: Remove vehicles from the database.
- **Database Integration**: Powered by PostgreSQL and SQLAlchemy.

---

## Prerequisites
Ensure you have the following installed:

- Python 3.10+
- PostgreSQL (configured and running locally)

---

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/queen-doris/Fleet_management_system_fastAPI.git
```

### 2. Install Dependencies
Install the required Python libraries from the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 3. Configure the Database
Ensure your PostgreSQL server is running and a database named `fleet_db` exists. Update the `DATABASE_URL` in `database.py` if necessary:

```python
DATABASE_URL = "postgresql://<username>:<password>@localhost:5432/fleet_db"
```

### 4. Run Database Migrations
Automatically create tables in the database:
```bash
python main.py
```

### 5. Start the Application
Run the FastAPI server using Uvicorn:
```bash
uvicorn app.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

### 6. Access the API Documentation
FastAPI automatically generates interactive API documentation. Access it at:
- Swagger UI: `http://127.0.0.1:8000/docs`

---

## Project Structure
```
.
├── app
│   ├── __init__.py
│   ├── crud.py         # Business logic for CRUD operations
│   ├── database.py     # Database connection and session handling
│   ├── models.py       # SQLAlchemy models
│   ├── routers
│   │   ├── __init__.py
│   │   └── fleet.py    # API routes for vehicle operations
│   └── schemas.py      # Pydantic models for validation
├── main.py             # Application entry point
├── requirements.txt    # List of project dependencies
└── README.md           # Project documentation
```

---

## API Endpoints

### Base URL
`http://127.0.0.1:8000`

### Endpoints

#### Root Endpoint
- **GET** `/`
  - Response: `{ "message": "Welcome to Fleet Management System!" }`

#### Vehicles
- **GET** `/vehicles/`
  - Fetch a list of vehicles. Supports optional query parameters:
    - `skip`: Number of records to skip (default: `0`)
    - `limit`: Number of records to fetch (default: `10`)
- **GET** `/vehicles/{vehicle_id}`
  - Retrieve details of a specific vehicle by ID.
  - Response: Details of the vehicle or a 404 error if not found.
- **POST** `/vehicles/`
  - Add a new vehicle.
  - Request Body: Vehicle details (e.g., registration number, model, owner).
- **PUT** `/vehicles/{vehicle_id}`
  - Update details of an existing vehicle by ID.
  - Request Body: Updated vehicle details.
  - Response: Updated vehicle details or a 404 error if not found.
- **DELETE** `/vehicles/{vehicle_id}`
  - Remove a vehicle by ID.
  - Response: Deleted vehicle details or a 404 error if not found.

---

## Example Payloads

### Create Vehicle (POST `/vehicles/`)
```json
{
  "registration_number": "ABC123",
  "model": "Toyota Prius",
  "owner": "John Doe"
}
```

### Update Vehicle (PUT `/vehicles/{vehicle_id}`)
```json
{
  "registration_number": "XYZ789",
  "model": "Honda Accord",
  "owner": "Jane Doe"
}
```

---

## Dependencies
The following Python libraries are used in this project:

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Uvicorn](https://www.uvicorn.org/)
- [Psycopg2](https://pypi.org/project/psycopg2/)

---

## Author
Developed by Queen.

