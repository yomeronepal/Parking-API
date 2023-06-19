from rest_framework.views import exception_handler
from rest_framework import status
from rest_framework.response import Response


class CustomException(Exception):
    """Base  Exception"""


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is None and isinstance(exc, (ValueError, CustomException)):
        response = Response(
            {"message": str(exc)},
            status=status.HTTP_400_BAD_REQUEST,
        )

    return response
