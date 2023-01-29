# Try to parse an integer out of a string
# Returns integer or None
def try_parse_int(value_to_convert):
    try:
        return int(value_to_convert)
    except ValueError:
        return None
