from hostsparser import format_line, ParseError

import pytest

def test_ip_hostname():
    line = "192.168.1.2\tgoogle.com"
    result = ("192.168.1.2", ("google.com", ), None)
    assert format_line(*result) == line

def test_ip_hostname_comment():
    line = "192.168.1.2\tgoogle.com\t#I'm blocking google"
    result = ("192.168.1.2", ("google.com", ), "#I'm blocking google")
    assert format_line(*result) == line

def test_ip_two_hostnames():
    line = "192.168.1.2\tgoogle.com microsoft.com"
    result = ("192.168.1.2", ("google.com", "microsoft.com"), None)
    assert format_line(*result) == line

def test_ip_two_hostnames_comment():
    line = "192.168.1.2\tgoogle.com microsoft.com\t#I'm blocking microsoft too"
    result = ("192.168.1.2", ("google.com", "microsoft.com"), "#I'm blocking microsoft too")
    assert format_line(*result) == line

def test_nested_comment():
    line = "#Testing Nested Comments #This is nested"
    result = (None, None, "#Testing Nested Comments #This is nested")
    assert format_line(*result) == line

def test_comment():
    line = "#This is just a comment"
    result = (None, None, "#This is just a comment")
    assert format_line(*result) == line

def test_blank_line():
    line = ""
    result = (None, None, None)
    assert format_line(*result) == line
