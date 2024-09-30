import sys
from scanner import scan_file
from monitor import start_monitoring
from database import create_database, add_signature, list_signatures, delete_signature

# Main entry point for the antivirus tool
if __name__ == "__main__":
    create_database()  # Ensure the database exists
    
    while True:
        print("\n1. Manual File Scan")
        print("2. Start Real-Time Monitoring")
        print("3. Add Malware Signature to Database")
        print("4. List Malware Signatures")
        print("5. Delete Malware Signature from Database")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            file_path = input("Enter the file path to scan: ")
            scan_file(file_path)
        
        elif choice == "2":
            directory_to_watch = input("Enter the directory to monitor: ")
            start_monitoring(directory_to_watch)
        
        elif choice == "3":
            name = input("Enter malware name: ")
            md5_hash = input("Enter MD5 hash of malware: ")
            add_signature(name, md5_hash)
        
        elif choice == "4":
            signatures = list_signatures()
            if signatures:
                print("Malware Signatures:")
                for sig in signatures:
                    print(f"ID: {sig[0]}, Name: {sig[1]}, MD5 Hash: {sig[2]}")
            else:
                print("No signatures found.")
        
        elif choice == "5":
            md5_hash = input("Enter MD5 hash of malware to delete: ")
            delete_signature(md5_hash)
        
        elif choice == "6":
            sys.exit()
        
        else:
            print("Invalid option, try again.")
