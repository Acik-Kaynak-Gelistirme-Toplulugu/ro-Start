import logging
import os
import sys
from logging.handlers import RotatingFileHandler
from platformdirs import user_log_dir

def setup_logging(app_name="ro-start"):
    """
    Sets up logging to both console and a rotating file in the user's log directory.
    Linux: ~/.local/state/ro-start/logs/ or ~/.cache/...
    macOS: ~/Library/Logs/ro-start/
    """
    
    # Determine log directory
    log_dir = user_log_dir(app_name, ensure_exists=True)
    log_file = os.path.join(log_dir, f"{app_name}.log")
    
    # Create handlers
    
    # 1. Console Handler (stdout)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)
    
    # 2. File Handler (Rotating) - Max 5MB, keep last 3 backups
    file_handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=3)
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)
    
    # Root Logger Config
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)
    
    logging.info(f"Logging initialized. Log file: {log_file}")
    
    return log_file
