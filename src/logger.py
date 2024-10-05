import logging
import os
from datetime import datetime

# Define log file name using current date and time
log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# Define path for logs directory
logs_path = os.path.join(os.getcwd(), "logs")
# Create the logs directory if it doesn't exist
os.makedirs(logs_path, exist_ok=True)

# Full path to the log file
log_file_path = os.path.join(logs_path, log_file)

# Configure logging to output to the log file
logging.basicConfig(
    filename=log_file_path,
    filemode='w',  # Overwrite the log file each time
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO  # Set to INFO to capture informational and error messages
)

# Log that the logging configuration is set up
logging.info("Logging is set up and ready to capture events")
