from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from bookings.models import Booking


class BookingsViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.booking_url = reverse("bookings")

    def test_successful_booking(self):
        # Make a successful booking
        response = self.client.post(
            self.booking_url,
            {
                "name": "Alice",
                "license_plate": "ABC123",
                "booking_date": str(timezone.now().date() + timezone.timedelta(days=1)),
            },
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"message": "Booking successful.", "bay": 1})

    def test_duplicate_booking(self):
        # Create a booking for today
        Booking.objects.create(
            customer_name="Alice",
            license_plate="ABC123",
            booking_date=timezone.now().date(),
            bay_number=1,
        )

        # Try to make another booking for today (should fail)
        response = self.client.post(
            self.booking_url,
            {
                "name": "Alice",
                "license_plate": "DEF456",
                "booking_date": str(timezone.now().date()),
            },
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(), {"message": "You have already made a booking for today."}
        )

    def test_booking_with_invalid_date(self):
        # Try to make a booking with an invalid date (less than 24 hours in advance)
        response = self.client.post(
            self.booking_url,
            {
                "name": "Alice",
                "license_plate": "GHI789",
                "booking_date": str(
                    timezone.now().date() + timezone.timedelta(hours=12)
                ),
            },
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(),
            {"message": "Booking must be made at least 24 hours in advance."},
        )

    def test_no_available_bays(self):
        # Create bookings for all bays on a specific date
        booking_date = timezone.now().date() + timezone.timedelta(days=1)
        for bay_number in range(1, 5):
            Booking.objects.create(
                customer_name=f"Customer{bay_number}",
                license_plate=f"ABC{bay_number}",
                booking_date=booking_date,
                bay_number=bay_number,
            )

        # Try to make a booking for the same date (no available bays)
        response = self.client.post(
            self.booking_url,
            {
                "name": "Alice",
                "license_plate": "JKL012",
                "booking_date": str(booking_date),
            },
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(),
            {"message": "No free bays available for the requested date."},
        )

    def test_get_bookings(self):
        # Create bookings for a specific date
        booking_date = timezone.now().date()
        Booking.objects.create(
            customer_name="Alice",
            license_plate="ABC123",
            booking_date=booking_date,
            bay_number=1,
        )
        Booking.objects.create(
            customer_name="Bob",
            license_plate="DEF456",
            booking_date=booking_date,
            bay_number=2,
        )

        # Get bookings for the specific date
        response = self.client.get(self.booking_url, {"date": str(booking_date)})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"Alice": 1, "Bob": 2})

    def test_get_bookings_no_results(self):
        # Get bookings for a date with no bookings
        response = self.client.get(self.booking_url, {"date": "2022-06-01"})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(), {"message": "No bookings found for the requested date."}
        )
