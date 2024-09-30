from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from scanner import scan_file
import time

# Event handler for real-time monitoring
class RealTimeEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print(f"File modified: {event.src_path}")
            scan_file(event.src_path)

# Start watching the directory for changes
def start_monitoring(path):
    event_handler = RealTimeEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
