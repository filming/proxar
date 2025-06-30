import logging

from .storage import StorageHandler

logger = logging.getLogger(__name__)


class FetchHandler:
    """Manages the operations of fetching proxies from various sources."""

    def __init__(self, storage_handler: StorageHandler) -> None:
        """Initialize the FetchHandler instance.

        Args:
            storage_handler: A handler for storage operations.
        """
        self.storage_handler = storage_handler

        logger.debug("FetchHandler has been initialized.")
