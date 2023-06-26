from parking_api.settings import ROOT_DIR

bind = "0.0.0.0:8000"  # Set the IP address and port to bind Gunicorn to
workers = 4  # Number of worker processes
timeout = 120  # Request timeout in seconds
static_root = str(ROOT_DIR / "staticfiles")
