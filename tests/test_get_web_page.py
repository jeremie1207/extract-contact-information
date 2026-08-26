import pytest
import requests
from pytest_mock import MockerFixture

from src.get_web_page.get_web_page import get_web_page


def test_get_web_page(mocker : MockerFixture) -> None:
    mock_requests_get = mocker.patch(
        "src.get_web_page.get_web_page.requests.get"
    )
    
    mock_response = mocker.MagicMock(spec=requests.Response)
    mock_response.status_code = 200
    mock_response.reason = "OK"
    mock_response.ok = True
    mock_response.text = "Hello, world!"
    mock_requests_get.return_value = mock_response
    
    expect_text = "Hello, world!"
    
    url = "https://www.example.com"
    results = get_web_page(url)
    
    assert results == expect_text
    
def test_get_web_page_error(mocker : MockerFixture) -> None:
    mock_requests_get = mocker.patch(
        "src.get_web_page.get_web_page.requests.get"
    )
    
    mock_response = mocker.MagicMock(spec=requests.Response)
    mock_response.status_code = 404
    mock_response.reason = "Not Found"
    mock_response.ok = False
    mock_requests_get.return_value = mock_response
    
    mock_response.raise_for_status.side_effect = (
        requests.exceptions.HTTPError("404 Not Found")
    )
    
    url = "https://www.example.com/nonexistent"
    
    with pytest.raises(requests.exceptions.RequestException):
        get_web_page(url)