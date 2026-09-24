import os
import shutil
import platform
from datetime import date

def get_system_status():
    print("=========================================")
    print("   CAREER TRANSITION PREP - ENV CHECK   ")
    print("=========================================")
    print(f"Date:           {date.today()}")
    print(f"OS:             {platform.system()} {platform.release()}")
    print(f"Python Version: {platform.python_version()}")

    # Check Disk Space
    total, _, free = shutil.disk_usage("/")
    print(f"Disk Space:     {free // (2**30)} GB free of {total // (2**30)} GB")

    # Training Environment Info
    print("")
    print("--- TRAINING ENVIRONMENT ---")
    print("Target Role:    Cloud Engineer / Cybersecurity Analyst")
    print("Current Phase:  Phase 1 - VSF Scholarship (2026)")
    print("Active Courses: AWS Cloud Technical Essentials | CS50P | CS50x")
    print("Lab Setup:      WSL2 Ubuntu 24.04 on Windows 11")

    # Environment Health
    print("")
    print("--- ENVIRONMENT STATUS ---")
    python_ok = platform.python_version().startswith("3")
    disk_ok = free // (2**30) > 10
    print(f"Python 3:       {'[OK]' if python_ok else '[FAIL]'}")
    print(f"Disk Space:     {'[OK]' if disk_ok else '[LOW]'}")

    print("")
    print("[SUCCESS] Environment fully operational. Stay consistent.")
    print("=========================================")

if __name__ == "__main__":
    get_system_status()
