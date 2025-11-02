import logging # Python’s built-in library for creating and managing logs.
import os # used for file and path operations (like making directories).
from datetime import datetime # used to generate timestamps (so each log file gets a unique name).

# Creates a unique log file name based on the current date and time.
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Builds a path to where the log file will be stored.
#     os.getcwd() → current working directory (the folder where your script runs).
#     "logs" → name of the folder where all logs will be saved.
#     LOG_FILE → the timestamped filename created above.
logs_path = os.path.join(os.getcwd(), "logs")

# This line tries to create a folder at the path stored in logs_path.
os.makedirs(logs_path,exist_ok=True)

# Joins the logs directory path with the log file name, giving the complete file path where logs will be saved.
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
