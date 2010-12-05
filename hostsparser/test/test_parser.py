from hostsparser import parse_line, ParseError

import pytest

def test_ip_hostname():
    line = "192.168.1.2 google.com"
    result = ("192.168.1.2", ("google.com", ), None)
    assert parse_line(line) == result

def test_ip_hostname_comment():
    line = "192.168.1.2 google.com #I'm blocking google"
    result = ("192.168.1.2", ("google.com", ), "#I'm blocking google")
    assert parse_line(line) == result

def test_ip_hostname_nospace_comment():
    line = "192.168.1.2 google.com#I'm blocking google"
    result = ("192.168.1.2", ("google.com", ), "#I'm blocking google")
    assert parse_line(line) == result

def test_ip_multiplespace_hostname():
    line = "192.168.1.2         google.com"
    result = ("192.168.1.2", ("google.com", ), None)
    assert parse_line(line) == result

def test_ip_tab_hostname():
    line = "192.168.1.2\tgoogle.com"
    result = ("192.168.1.2", ("google.com", ), None)
    assert parse_line(line) == result

def test_space_ip_hostname():
    line = " 192.168.1.2 google.com"
    result = ("192.168.1.2", ("google.com", ), None)
    assert parse_line(line) == result

def test_tab_ip_hostname():
    line = "\t192.168.1.2 google.com"
    result = ("192.168.1.2", ("google.com", ), None)
    assert parse_line(line) == result

def test_spaces_ip_hostname():
    line = "     192.168.1.2 google.com"
    result = ("192.168.1.2", ("google.com", ), None)
    assert parse_line(line) == result

def test_tabs_ip_hostname():
    line = "\t\t192.168.1.2 google.com"
    result = ("192.168.1.2", ("google.com", ), None)
    assert parse_line(line) == result

def test_ip_two_hostnames():
    line = "192.168.1.2 google.com microsoft.com"
    result = ("192.168.1.2", ("google.com", "microsoft.com"), None)
    assert parse_line(line) == result

def test_ip_two_hostnames_comment():
    line = "192.168.1.2 google.com microsoft.com #I'm blocking microsoft too"
    result = ("192.168.1.2", ("google.com", "microsoft.com"), "#I'm blocking microsoft too")
    assert parse_line(line) == result

def test_nested_comment():
    line = "#Testing Nested Comments #This is nested"
    result = (None, None, "#Testing Nested Comments #This is nested")
    assert parse_line(line) == result

def test_comment():
    line = "#This is just a comment"
    result = (None, None, "#This is just a comment")
    assert parse_line(line) == result

def test_all_spaces():
    line = "                "
    result = (None, None, None)
    assert parse_line(line) == result

def test_blank_line():
    line = ""
    result = (None, None, None)
    assert parse_line(line) == result

def test_invalid_only_ip():
    line = "192.168.1.2"
    with pytest.raises(ParseError):
        parse_line(line)

def test_invalid_random_chars():
    line = "adsfasdfghaser"
    with pytest.raises(ParseError):
        parse_line(line)

def test_invalid_space_random_chars():
    line = " dsafsaf "
    with pytest.raises(ParseError):
        parse_line(line)   

def test_invalid_ipv4_random():
    line = "linkigo.frikingo.blichero.blah google.com"
    with pytest.raises(ParseError):
        parse_line(line)

def test_invalid_ipv4_invalid_chars():
    line = "19:2.15-2.4.11 google.com"
    with pytest.raises(ParseError):
        parse_line(line)

def test_invalid_ipv4_overflow():
    line = "256.258.258.1 google.com"
    with pytest.raises(ParseError):
        parse_line(line)

def test_invalid_ipv6_random():
    line = "linkigo.:rikingo:::blichero:blah google.com"
    with pytest.raises(ParseError):
        parse_line(line)

def test_invalid_ipv6_invalid_chars():
    line = "ff:gge:fffee.cfe.ffe:ff2123:f google.com"
    with pytest.raises(ParseError):
        parse_line(line)
