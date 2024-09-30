import logging

# Configure logging
logging.basicConfig(filename='antivirus.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Log messages
def log_message(message):
    logging.info(message)
