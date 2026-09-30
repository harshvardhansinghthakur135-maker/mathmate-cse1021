"""Simple activity logger (non-functional requirement: logging / monitoring).

Appends one line per event to logs/mathmate.log. Logging must never crash the
program, so any file problem is ignored.
"""
import os
from datetime import datetime

LOG_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "logs", "mathmate.log")


def log_event(level, message):
    """Write 'timestamp | LEVEL | message' to the log file."""
    line = f"{datetime.now():%Y-%m-%d %H:%M:%S} | {level} | {message}\n"
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as log_file:
            log_file.write(line)
    except OSError:
        pass  # logging is optional; never stop the program because of it
