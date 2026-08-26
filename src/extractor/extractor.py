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