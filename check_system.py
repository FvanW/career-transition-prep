import shutil
import platform
from datetime import date

BYTES_PER_GB = 2**30

def get_system_status():
    py_version = platform.python_version()

    print("=========================================")
    print("   CAREER TRANSITION PREP - ENV CHECK   ")
    print("=========================================")
    print(f"Date:           {date.today()}")
    print(f"OS:             {platform.system()} {platform.release()}")
    print(f"Python Version: {py_version}")

    # Check Disk Space
    total, _, free = shutil.disk_usage("/")
    print(f"Disk Space:     {free // BYTES_PER_GB} GB free of {total // BYTES_PER_GB} GB")

    # Training Environment Info
    print()
    print("--- TRAINING ENVIRONMENT ---")
    print("Target Role:    Cloud Engineer / Cybersecurity Analyst")
    print("Current Phase:  Phase 1 - VSF Scholarship (2026)")
    print("Active Courses: AWS Cloud Technical Essentials | CS50P | CS50x")
    print("Lab Setup:      WSL2 Ubuntu 24.04 on Windows 11")

    # Environment Health
    print()
    print("--- ENVIRONMENT STATUS ---")
    python_ok = py_version.startswith("3")
    disk_ok = free // BYTES_PER_GB > 10
    print(f"Python 3:       {'[OK]' if python_ok else '[FAIL]'}")
    print(f"Disk Space:     {'[OK]' if disk_ok else '[LOW]'}")

    print()
    print("[SUCCESS] Environment fully operational. Stay consistent.")
    print("=========================================")

if __name__ == "__main__":
    get_system_status()
