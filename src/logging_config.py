import logging
from pathlib import Path


def ensure_logs_dir() -> Path:
    root = Path(__file__).resolve().parents[1]
    logs_dir = root / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)
    return logs_dir


def get_logger(name: str, level=logging.INFO) -> logging.Logger:
    logs_dir = ensure_logs_dir()
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid adding multiple handlers in interactive runs
    if logger.handlers:
        return logger

    fmt = logging.Formatter("%(asctime)s %(levelname)-8s %(name)s: %(message)s", "%Y-%m-%d %H:%M:%S")

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(fmt)
    logger.addHandler(ch)

    # File handler per module name
    fh = logging.FileHandler(logs_dir / f"{name}.log", encoding="utf-8")
    fh.setLevel(level)
    fh.setFormatter(fmt)
    logger.addHandler(fh)

    return logger
