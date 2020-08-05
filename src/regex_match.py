import regex

def match_function(in_str):
    """
    (String) -> (iterable of re.Match objects)
    Checks whether or not an input string matches the regular expression
    The string must contain a
            -function name composed of characters and digits
            -a set of variables composed of characters separated by ,
            -a set of output functions with matching parentheses
    It CANNOT contain a '\' """

    pattern = "(([a-zA-Z]|[0-9])+\s*\({1}([a-zA-Z](,)*)+(\){1})\s*={1})\s*(\((([^\(\)\\\\]*)|(?6))*\))"

    res = regex.finditer(pattern, in_str)
    return res

def match_closed_parentheses(in_str):
    """ (String) -> (re.Match)"""
    pattern = "\((([^\(\)]*)|(?R))*\)"
    return regex.match(pattern, in_str)


def match_commands(in_str):
    """ (String) -> (Re.match)"""
    pattern = "(\\\\)[a-zA-Z]*\{[^\\\\\{\}]*\}"
    return regex.finditer(pattern, in_str)


n = 0
while(n< 3):
    s = input()
    for f in match_commands(s):
        print(f)
