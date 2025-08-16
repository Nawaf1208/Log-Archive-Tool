#!/usr/bin/env python3
import os
import sys
import tarfile
from datetime import datetime

def archive_logs(log_dir):
    # Check if directory exists
    if not os.path.isdir(log_dir):
        print(f"Error: {log_dir} is not a valid directory.")
        sys.exit(1)

    # Create archive directory
    archive_dir = "archives"
    os.makedirs(archive_dir, exist_ok=True)

    # Create timestamped archive name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_name = f"logs_archive_{timestamp}.tar.gz"
    archive_path = os.path.join(archive_dir, archive_name)

    # Compress logs into tar.gz
    with tarfile.open(archive_path, "w:gz") as tar:
        tar.add(log_dir, arcname=os.path.basename(log_dir))

    # Log the operation
    log_file = os.path.join(archive_dir, "archive_log.txt")
    with open(log_file, "a") as f:
        f.write(f"{datetime.now()} - Archived {log_dir} -> {archive_name}\n")

    print(f"✅ Logs archived successfully: {archive_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: log-archive <log-directory>")
        sys.exit(1)

    log_dir = sys.argv[1]
    archive_logs(log_dir)
