# Maintenance Tracker API

A simple Django REST API to track preventive maintenance of machines based on operating hours.

---

## Project Overview

This project models machines and their maintenance schedules by tracking total operating hours and last service hours. It calculates maintenance status dynamically to inform when machines require servicing.

- **MachineType**: Defines machine categories and their maintenance interval in operating hours.  
- **Machine**: Represents a physical machine with accumulated runtime and last maintenance info.  
- Computed status (`OK`, `DUE`, `OVERDUE`) based on usage and interval.

The API supports full CRUD for both machine types and machines, exposing real-time maintenance status without storing redundant fields.

---

## Features

- Create, read, update, and delete machine types  
- Create, read, update, and delete machines  
- Real-time maintenance status calculation  
- Hours remaining and overdue hours metrics  
- Simple, clean REST API using Django REST Framework

---

## Installation

1. **Clone the repo**

```bash
git clone https://github.com/omar-aljalam/maintenance.git
cd maintenance

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run migrations**
```bash
python manage.py migrate
```

5. **Run the server**
```bash
python manage.py runserver
```

6. **Access the API**
Open your browser and navigate to `http://localhost:8000/api/machines/` to view the list of machines.

---

## API Endpoints

- `GET /api/machines/`: List all machines
- `POST /api/machines/`: Create a new machine
- `GET /api/machines/{id}/`: Retrieve a specific machine
- `PUT /api/machines/{id}/`: Update a specific machine
- `DELETE /api/machines/{id}/`: Delete a specific machine

---

## Example Usage

### Create a new machine
```bash
POST /api/machines/
{
    "name": "Machine 1",
    "machine_type": 1,
    "total_operating_hours": 100,
    "last_service_hours": 50
}
```

### Get machine status
```bash
GET /api/machines/{id}/
{
    "name": "Machine 1",
    "machine_type": 1,
    "total_operating_hours": 100,
    "last_service_hours": 50,
    "status": "OK",
    "hours_remaining": 50,
    "overdue_hours": 0
}
```