from rest_framework import viewsets
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

class ListingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Listings to be viewed, created, updated, or deleted.

    - GET: List or retrieve Listings.
    - POST: Create a new Listing.
    - PUT/PATCH: Update an existing Listing.
    - DELETE: Remove a Listing.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Bookings to be viewed, created, updated, or deleted.

    - GET: List or retrieve Bookings.
    - POST: Create a new Booking.
    - PUT/PATCH: Update an existing Booking.
    - DELETE: Remove a Booking.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer