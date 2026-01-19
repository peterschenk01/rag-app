import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def setup_logging(
    level: int = logging.INFO,
    log_file: str = "rag_system.log",
) -> None:
    """Configure root logger once at application startup."""

    root = logging.getLogger()
    root.setLevel(level)

    if root.handlers:
        return

    formatter = logging.Formatter(LOG_FORMAT, DATE_FORMAT)

    file_handler = RotatingFileHandler(
        LOG_DIR / log_file,
        maxBytes=5_000_000,
        backupCount=5,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    root.addHandler(file_handler)
