def reverse_string(string: str) -> str:
    """Reverses the input string."""
    return string[::-1]

def count_substring(string: str, substring: str) -> int:
    """Counts the occurrences of a substring in the input string."""
    return string.count(substring)

def to_uppercase(string: str) -> str:
    """Converts the input string to uppercase."""
    return string.upper()

def to_lowercase(string: str) -> str:
    """Converts the input string to lowercase."""
    return string.lower()