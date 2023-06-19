from django.utils import timezone
from bookings.models import Booking


class BookingORM:
    def __init__(self, data):
        self.data = data
        self.bay = None

    def check_existing_bay(self, booking_date):
        # Find a free bay for the booking
        for i in range(1, 5):
            if not Booking.objects.filter(
                booking_date=booking_date, bay_number=i
            ).exists():
                self.bay = i
                return self.bay
        return None

    def get_bay(self):
        return self.bay

    def check_booking(self) -> dict:
        customer_name = self.data.get("name")
        license_plate = self.data.get("license_plate")
        booking_date = self.data.get("booking_date")

        # Check if customer has already made a booking for today
        today = timezone.now().date()
        if Booking.objects.filter(
            customer_name=customer_name,
            booking_date=booking_date,
        ).exists():
            raise ValueError("You have already made a booking for today.")

        # Check if the booking is at least 24 hours in advance
        if booking_date <= str(today):
            raise ValueError("Booking must be made at least 24 hours in advance.")
        bay = self.check_existing_bay(booking_date)
        # If no free bay is available, return an error message
        if bay is None:
            raise ValueError("No free bays available for the requested date.")

    def create_booking(self) -> None:
        booking = Booking(
            customer_name=self.data.get("name"),
            license_plate=self.data.get("license_plate"),
            booking_date=self.data.get("booking_date"),
            bay_number=self.bay,
        )
        booking.save()

    def get_booking(self):
        bookings = Booking.objects.filter(booking_date=self.data.get("date"))
        if not bookings:
            raise ValueError("No bookings found for the requested date.")

        booking_data = {
            booking.customer_name: booking.bay_number for booking in bookings
        }
        return booking_data
