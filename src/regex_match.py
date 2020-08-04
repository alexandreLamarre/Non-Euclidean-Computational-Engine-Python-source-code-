import regex

def match_function(in_str):
    """ Checks whether or not an input string matches the regular expression
    for a function, in terms of what makes a function usually valid in mathematics

    Returns an iterable of re.Match objects"""
    pattern = "(([a-zA-Z]|[0-9])+\s*\({1}([a-zA-Z](,)*)+(\){1})\s*={1})\s*(\((([^\(\)]*)|(?6))*\))"

    res = regex.finditer(pattern, in_str)
    return res

def match_closed_parentheses(in_str):
    pattern = "\((([^\(\)]*)|(?R))*\)"
    return regex.match(pattern, in_str)


