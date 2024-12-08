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
    test_file.write_text("Hello, World! \u00A9")
    
    result = subprocess.run(['python3', 'ccwc.py', '-m', str(test_file)], capture_output=True, text=True)
    assert result.returncode == 0
    assert result.stdout.strip() == f"15 {test_file}"

def test_no_options(tmp_path):
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Hello, World!\n")
    
    result = subprocess.run(['python3', 'ccwc.py', str(test_file)], capture_output=True, text=True)
    assert result.returncode == 0
    assert result.stdout.strip() == f"1 2 14 {test_file}"

def test_no_file_stdin():
    result = subprocess.run(['python3', 'ccwc.py'], input="Hello, World!", capture_output=True, text=True)
    assert result.returncode == 0
    assert result.stdout.strip() == "1 2 13"