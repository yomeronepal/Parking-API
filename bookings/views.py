from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from django.utils import timezone
from bookings.models import Booking
from rest_framework.views import APIView
from bookings.utils.orm import BookingORM

# Create your views here.


class BookingView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        # Get customer details from request payload
        booking = BookingORM(request.data)
        booking.check_booking()

        # Create a new booking instance
        booking.create_booking()

        return Response(
            {"message": "Booking successful.", "bay": booking.get_bay()}, status=201
        )

    def get(self, request, *args, **kwargs):
        # Get booking date from request parameters
        booking_date = request.GET.get("date")

        # Get all bookings for the requested date
        bookings = Booking.objects.filter(booking_date=booking_date)
        bookings = BookingORM(request.GET).get_booking()

        return Response(bookings, status=200)
