import logging


def setup_logger(log_file="task_manager.log"):
    """Set up and return a logger."""
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    return logging.getLogger("TaskManager")
