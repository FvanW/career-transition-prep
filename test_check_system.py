import pytest
from unittest.mock import patch, MagicMock
from datetime import date
import check_system

@patch('check_system.date')
@patch('check_system.platform')
@patch('check_system.shutil')
def test_get_system_status_output(mock_shutil, mock_platform, mock_date, capsys):
    mock_date.today.return_value = date(2026, 1, 1)
    mock_platform.system.return_value = "Linux"
    mock_platform.release.return_value = "5.15.0-100-generic"
    mock_platform.python_version.return_value = "3.12.3"
    # total, used, free
    mock_shutil.disk_usage.return_value = (500 * (2**30), 100 * (2**30), 400 * (2**30))

    check_system.get_system_status()

    captured = capsys.readouterr()
    stdout = captured.out

    assert "Date:           2026-01-01" in stdout
    assert "OS:             Linux 5.15.0-100-generic" in stdout
    assert "Python Version: 3.12.3" in stdout
    assert "Disk Space:     400 GB free of 500 GB" in stdout
