import subprocess
import os

def test_count_bytes(tmp_path):
    test_file = tmp_path / "test_file.txt"
    test_file.write_bytes(b"Hello, World!")
    
    result = subprocess.run(['python3', 'ccwc.py', '-c', str(test_file)], capture_output=True, text=True)
    assert result.returncode == 0
    assert result.stdout.strip() == f"13 {test_file}"

def test_count_lines(tmp_path):
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Hello\nWorld\n")
    
    result = subprocess.run(['python3', 'ccwc.py', '-l', str(test_file)], capture_output=True, text=True)
    assert result.returncode == 0
    assert result.stdout.strip() == f"2 {test_file}"

def test_count_words(tmp_path):
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Hello, World!")
    
    result = subprocess.run(['python3', 'ccwc.py', '-w', str(test_file)], capture_output=True, text=True)
    assert result.returncode == 0
    assert result.stdout.strip() == f"2 {test_file}"

def test_count_unicode_characters(tmp_path):
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Hello, World! 😊")
    
    result = subprocess.run(['python3', 'ccwc.py', '-m', str(test_file)], capture_output=True, text=True)
    assert result.returncode == 0
    assert result.stdout.strip() == f"15 {test_file}"