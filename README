# Parking Reservations API

This is a simple API for handling customers' all-day parking reservations at a car park.

## Requirements

- Python (version 3.6 or above)
- Django (version 3.2 or above)
- Django REST framework (version 3.12 or above)

## Installation

1. Clone the repository:
   git clone <repository-url>
2. Navigate to the project directory:
   cd parking_api
3. Set up a virtual environment (optional but recommended):
   python3 -m venv env
   source env/bin/activate # for Linux/macOS
   env\Scripts\activate # for Windows

4. Install the dependencies:

- pip install -r requirements.txt

## Usage

1. Set up the database:
   python manage.py makemigrations
   python manage.py migrate

2. Start the development server:
   python manage.py runserver

3. Access the API endpoints using the following URLs:

- `POST /api/bookings/` to make a booking
- `GET /api/bookings/?date=<booking_date>` to get bookings for a specific date

For example, you can make a booking using the following command:

```python
import requests

headers = {
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
}

json_data = {
    'name': 'Alice',
    'license_plate': 'ABC123',
    'booking_date': '2022-06-01',
}

response = requests.post('http://localhost:8000/api/bookings/', headers=headers, json=json_data)
```

## Running Tests

1. Run the unit tests:
   python manage.py test bookings.tests

## Assumptions and Design Decisions

- Customers can only make one booking per day to ensure fairness and availability for other customers.
- Bookings must be made at least 24 hours in advance to allow sufficient time for preparation.
- The API assumes a car park with four bays numbered from 1 to 4 inclusively.

## Limitations and Trade-offs

- The API does not handle concurrency and may encounter issues if multiple requests try to book the same bay simultaneously.
- The API does not have user authentication and authorization mechanisms.
- The API does not provide real-time updates or notifications for booking availability.

## Contributing

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.
