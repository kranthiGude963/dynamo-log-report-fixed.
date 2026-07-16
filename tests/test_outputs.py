import json
import os

def load_report():
    path = "/app/report.json"
    if not os.path.exists(path):
        raise AssertionError("report.json not found at /app/report.json")
    with open(path) as f:
        return json.load(f)

def test_total_requests():
    """Report must contain a positive integer 'total_requests'."""
    report = load_report()
    assert "total_requests" in report, "Missing key: total_requests"
    assert isinstance(report["total_requests"], int), "total_requests must be int"
    assert report["total_requests"] > 0, "total_requests must be > 0"

def test_unique_ips():
    """Report must contain a positive integer 'unique_ips'."""
    report = load_report()
    assert "unique_ips" in report, "Missing key: unique_ips"
    assert isinstance(report["unique_ips"], int), "unique_ips must be int"
    assert report["unique_ips"] > 0, "unique_ips must be > 0"

def test_top_path():
    """Report must contain a non-empty string 'top_path'."""
    report = load_report()
    assert "top_path" in report, "Missing key: top_path"
    assert isinstance(report["top_path"], str), "top_path must be string"
    assert report["top_path"], "top_path must not be empty"
