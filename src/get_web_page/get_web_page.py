import logging

import requests

logger = logging.getLogger(__name__)

def get_web_page(url: str) -> str:
    """Retrieve the content of a web page for a given URL.

    Args:
        url: The URL of the web page to retrieve.

    Returns:
        The HTML content of the web page as a string.

    Raises:
        requests.exceptions.Timeout: If the request exceeds the timeout limit.
        requests.exceptions.ConnectionError: If a connection to the server
            cannot be established.
        requests.exceptions.HTTPError: If the server returns an unsuccessful
            HTTP status code.
        requests.exceptions.InvalidURL: If the provided URL is invalid.
        requests.exceptions.RequestException: If another request-related
            error occurs.
    """
    logger.info(f"Starting retrieval of page content from {url}")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

    except requests.exceptions.RequestException:
        logger.exception(f"Failed to retrieve page content from {url}")
        raise

    logger.info(f"Successfully retrieved page content from {url}")

    return response.text