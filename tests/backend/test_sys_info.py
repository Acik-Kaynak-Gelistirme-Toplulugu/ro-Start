"""
Tests for system information module
"""
import pytest
from backend.core.sys_info import get_size_str, get_cpu_info, get_gpu_info


def test_get_size_str():
    """Test byte size conversion to human readable format"""
    assert get_size_str(0) == "0.0 "
    assert get_size_str(1024) == "1.0 KB"
    assert get_size_str(1024 * 1024) == "1.0 MB"
    assert get_size_str(1024 * 1024 * 1024) == "1.0 GB"


def test_get_cpu_info():
    """Test CPU information retrieval"""
    cpu_info = get_cpu_info()
    assert cpu_info is not None
    assert isinstance(cpu_info, str)
    assert len(cpu_info) > 0


def test_get_gpu_info():
    """Test GPU information retrieval"""
    gpu_info = get_gpu_info()
    assert gpu_info is not None
    assert isinstance(gpu_info, str)
    # GPU info might be "N/A" on systems without dedicated GPU
    assert len(gpu_info) > 0
