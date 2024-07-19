# Helper function to validate char length
def char_len_check(min_char: int, max_char: int, word: str) -> bool:
    if min_char <= len(word) <= max_char:
        return True
    else:
        return False

# Helper function to remove last line of multiline string
def remove_last_line_from_str(string: str) -> str:
    return string[:string.rfind('\n')]
