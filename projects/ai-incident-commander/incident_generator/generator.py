import random
from datetime import datetime

SEVERITIES = ["LOW", "MEDIUM", "HIGH"]
SERVICES = ["auth-service", "payment-api", "inventory-service"]

ERRORS = [
    "Database connection timeout",
    "Null pointer exception",
    "Service unavailable",
    "Authentication failed",
    "High memory usage detected"
]

def generate_incident():
    """
    Generates a simulated production incident.
    """
    return {
        "service": random.choice(SERVICES),
        "severity": random.choice(SEVERITIES),
        "error": random.choice(ERRORS),
        "timestamp": datetime.utcnow().isoformat()
    }
