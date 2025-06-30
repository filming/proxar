import logging
from pathlib import Path

import platformdirs

logger = logging.getLogger(__name__)


class StorageHandler:
    """Handle persistent, asynchronous storage of proxies in a JSON file."""

    def __init__(self, storage_dir: str | Path | None) -> None:
        """Initializes the StorageHandler instance.

        Args:
            storage_dir: The directory path to store the proxies.json file. If None,
                an OS-specific user data directory is used.
        """
        # Set a flag to track unsaved proxies.
        self._dirty: bool = False

        # Set storage dir path and ensure its existence
        if storage_dir is None:
            self.storage_dir_path = Path(platformdirs.user_data_dir("proxar"))
            logger.debug(
                "No storage directory provided. Using default path: %s",
                self.storage_dir_path,
            )
        else:
            self.storage_dir_path = Path(storage_dir)
            logger.debug("Using provided storage directory: %s", self.storage_dir_path)

        self.storage_dir_path.mkdir(parents=True, exist_ok=True)
        self.json_file_path = self.storage_dir_path / "proxies.json"
