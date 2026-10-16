import pytest
from unittest.mock import patch, MagicMock
from datetime import date
from check_system import get_system_status

@patch("check_system.date")
@patch("check_system.platform")
@patch("check_system.shutil")
def test_get_system_status_happy_path(mock_shutil, mock_platform, mock_date, capsys):
    mock_date.today.return_value = date(2026, 1, 1)

    mock_platform.python_version.return_value = "3.12.3"
    mock_platform.system.return_value = "Linux"
    mock_platform.release.return_value = "5.15.0-1040-aws"

    # disk_usage returns (total, used, free)
    # Give 20GB free space
    mock_shutil.disk_usage.return_value = (50 * (2**30), 30 * (2**30), 20 * (2**30))

    get_system_status()

    captured = capsys.readouterr()
    output = captured.out

    assert "Date:           2026-01-01" in output
    assert "OS:             Linux 5.15.0-1040-aws" in output
    assert "Python Version: 3.12.3" in output
    assert "Disk Space:     20 GB free of 50 GB" in output

    assert "Python 3:       [OK]" in output
    assert "Disk Space:     [OK]" in output

@patch("check_system.date")
@patch("check_system.platform")
@patch("check_system.shutil")
def test_get_system_status_error_cases(mock_shutil, mock_platform, mock_date, capsys):
    mock_date.today.return_value = date(2026, 1, 1)

    mock_platform.python_version.return_value = "2.7.18"
    mock_platform.system.return_value = "Linux"
    mock_platform.release.return_value = "5.15.0"

    # disk_usage returns (total, used, free)
    # Give exactly 10GB free space
    mock_shutil.disk_usage.return_value = (50 * (2**30), 40 * (2**30), 10 * (2**30))

    get_system_status()

    captured = capsys.readouterr()
    output = captured.out

    assert "Python Version: 2.7.18" in output
    assert "Disk Space:     10 GB free of 50 GB" in output

    assert "Python 3:       [FAIL]" in output
    assert "Disk Space:     [LOW]" in output
