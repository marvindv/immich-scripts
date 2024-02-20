import logging

from rich.logging import RichHandler

_FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=_FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)
log = logging.getLogger("immich-scripts")
