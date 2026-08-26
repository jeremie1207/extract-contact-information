import logging
import re

logger = logging.getLogger(__name__)

def emails_extractor(text: str) -> list[str]:
    """Extract email addresses from the given text.

    Args:
        text: The text from which to extract email addresses.

    Returns:
        A list of email addresses found in the text.

    Raises:
        TypeError: If `text` is not a string.
    """
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    
    if not isinstance(text, str):
        raise TypeError("text should be a string")
    
    logger.info(f"Starting extraction of emails from :\n{text}")
    
    return re.findall(pattern, text)

def phone_numbers_extractor(text: str) -> list[str]:
    """Extract phone numbers from the given text.

    Args:
        text: The text from which to extract phone numbers.

    Returns:
        A list of phone numbers found in the text.

    Raises:
        TypeError: If `text` is not a string.
    """
    
    logger.info(f"Starting extraction of phone number from :\n{text}")
    
    if not isinstance(text, str):
        raise TypeError("text should be a string")
    
    pattern = (
        r"(?:\+1[ -]?)?"
        r"(?:\(\d{3}\)[ -]\d{3}-\d{4}"
        r"|\d{3}[-. ]\d{3}[-. ]\d{4})"
    )
    
    return re.findall(pattern, text)