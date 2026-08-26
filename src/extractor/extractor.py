import re


def emails_extractor(text: str) -> list[str]:
    """Extract emails from a given text

    Args:
        text (str): a text that can contains emails

    Returns:
        list[str]: list of extracted emails
    """
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    
    return re.findall(pattern, text)

def phone_numbers_extractor(text: str) -> list[str]:
    """Extract phone number from a given text

    Args:
        text (str): a text that can contains phone number

    Returns:
        list[str]: list of extracted phone number
    """
    
    pattern = (
        r"(?:\+1[ -]?)?"
        r"(?:\(\d{3}\)[ -]\d{3}-\d{4}"
        r"|\d{3}[-. ]\d{3}[-. ]\d{4})"
    )
    
    return re.findall(pattern, text)