# Tableau Migration App

## Overview
The Tableau Migration App is a FastAPI application designed to facilitate the migration of Tableau dashboards from one location to another. It provides a simple API to accept migration requests, validate the input, and simulate the migration process.

## Features
- Accepts dashboard migration requests via a POST API endpoint.
- Validates input parameters including dashboard name, source path, and destination path.
- Simulates the migration process and returns appropriate responses.

## Project Structure
```
tableau-migration-app/
├── requirements.txt
├── README.md
└── src/
    ├── main.py
    ├──__init__.py
    ├── api/
    │   ├── __init__.py
    │   └── endpoints.py
    ├── models/
    │   ├── __init__.py
    │   └── migration.py
    ├── services/
    │   ├── __init__.py
    │   └── migration_service.py
    └── types/
        └── __init__.py
```

## Installation
To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd tableau-migration-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the FastAPI application, execute the following command:
```
uvicorn src.main:app --reload
```

Once the application is running, you can access the API documentation at `http://127.0.0.1:8000/docs`.

## API Endpoint
### POST /migrate
This endpoint accepts a JSON payload with the following structure:
```json
{
  "dashboard_name": "string",
  "source_path": "string",
  "destination_path": "string"
}
```

#### Example Request
```json
{
  "dashboard_name": "Sales Dashboard",
  "source_path": "/path/to/source",
  "destination_path": "/path/to/destination"
}
```

#### Response
- **200 OK**: Migration simulated successfully.
- **400 Bad Request**: Validation errors or missing fields.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.