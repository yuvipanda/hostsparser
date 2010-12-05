# Parser for hosts file

import re

class ParseError(Exception):
    pass

entry_regex = re.compile(r"""^
        \s*
        (?:
           ([0-9a-fA-F.:]+)\s+          # rough IP
           (                            # All HostNames
            (?:
               [a-zA-Z0-9:_.-]+
               \s?                      # For the case when hostname is followed by newline
            )+
           )
        )?
        \s*                             # When you have unlimited spaces!
        (\#.*)?                         # Comments always come last if there's any other content.
        $""", re.VERBOSE)

def parse_line(line):
    match = entry_regex.match(line)
    if not match:
        raise ParseError()
    return (match.groups()[0],
            tuple(match.groups()[1].split()) if match.groups()[1] else None,
            match.groups()[2])

def parse_file(f):
    '''Accepts a file-like object with data in hosts format, and yields (ip, (hosts,), comment) tuples'''
    for line in f:
        yield parse_line(line)

def format_line(ip, hosts, comment):
    formatted_line = ""
    if ip:
        formatted_line = ip + "\t" + " ".join(hosts)
    if comment:
        if ip:
            formatted_line += "\t"
        formatted_line += comment
    return formatted_line 
