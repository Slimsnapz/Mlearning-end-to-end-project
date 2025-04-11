import logging
import os
from datetime import datetime

# Correctly format the log file name by closing the f-string before appending ".log"
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create a directory called "logs" in the current working directory
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Define the full path for the log file within the logs directory
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging module to write to the specified file with a defined format
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

