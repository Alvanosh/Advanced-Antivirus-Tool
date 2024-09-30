import logging
import hashlib
import yara
from database import check_hash_in_database

# Configure logging
logging.basicConfig(filename='antivirus.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Load YARA rules
rule_file = "yara_rules/example_rule.yar"
rules = yara.compile(filepath=rule_file)

# Function to calculate MD5 hash of a file
def calculate_md5(file_path):
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as file:
            for chunk in iter(lambda: file.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception as e:
        logging.error(f"Error calculating MD5 for {file_path}: {e}")
        return None

# Scan file using YARA rules
def scan_with_yara(file_path):
    try:
        matches = rules.match(file_path)
        if matches:
            logging.info(f"YARA detected malware in {file_path}: {matches}")
            return True
        return False
    except Exception as e:
        logging.error(f"Error scanning with YARA for {file_path}: {e}")
        return False

# Full file scan, check with MD5 hash and YARA
def scan_file(file_path):
    print(f"Scanning file: {file_path}")
    
    # Step 1: MD5 Hash check
    file_md5 = calculate_md5(file_path)
    if file_md5 and check_hash_in_database(file_md5):
        print(f"File {file_path} flagged as malware by MD5.")
        logging.info(f"File {file_path} flagged as malware by MD5.")
        return True
    
    # Step 2: YARA rule check
    if scan_with_yara(file_path):
        print(f"File {file_path} flagged by YARA rules.")
        logging.info(f"File {file_path} flagged by YARA rules.")
        return True
    
    print(f"File {file_path} is clean.")
    logging.info(f"File {file_path} is clean.")
    return False
