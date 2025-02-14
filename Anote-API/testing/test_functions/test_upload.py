import pytest
from upload import tokenize, decompose, parse_actual_labels_from_csv, get_text_from_url

# Dummy test data for the test cases
SAMPLE_TEXT = "This is a sample text\nwith multiple lines\nfor testing"
SAMPLE_HTML_URL = "https://example.com/sample.html"
SAMPLE_CSV = b"Label\nClass A\nClass B\nClass C"
SAMPLE_TEXT_URL = "https://example.com/sample.txt"

# Test Case 1: Test tokenize function
def test_tokenize():
    tokens = tokenize(SAMPLE_TEXT)
    assert len(tokens) == 3
    assert tokens[0] == "This is a sample text"

# Test Case 2: Test decompose function for local document
def test_decompose_local_document():
    result = decompose(SAMPLE_TEXT, local=True, document=True)
    assert "sample text" in result

# Test Case 3: Test parse_actual_labels_from_csv function
def test_parse_actual_labels_from_csv():
    labels = parse_actual_labels_from_csv(SAMPLE_CSV, hasHeader=True, labelColIndex=0)
    assert len(labels) == 3
    assert labels[0] == "Class A"

# Test Case 4: Test get_text_from_url function
def test_get_text_from_url():
    text = get_text_from_url(SAMPLE_TEXT_URL)
    assert "sample text content" in text

# Test Case 5: Test decompose function for remote HTML document
def test_decompose_remote_html():
    result = decompose(SAMPLE_HTML_URL, local=False, document=True, isHTML=True)
    assert "sample HTML content" in result