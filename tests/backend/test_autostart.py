"""
Tests for autostart functionality
"""
import pytest
import os
from backend.core.autostart import get_autostart_file_path, is_autostart_enabled, set_autostart


def test_get_autostart_file_path():
    """Test autostart file path generation"""
    path = get_autostart_file_path()
    assert path is not None
    assert path.endswith("ro-start.desktop")
    assert ".config/autostart" in path


def test_autostart_operations():
    """Test autostart enable/disable operations"""
    # Clean up before test
    path = get_autostart_file_path()
    if os.path.exists(path):
        os.remove(path)
    
    # Test initial state
    assert not is_autostart_enabled()
    
    # Test enable
    result = set_autostart(True)
    assert result is True
    assert is_autostart_enabled()
    
    # Test disable
    result = set_autostart(False)
    assert result is True
    assert not is_autostart_enabled()
