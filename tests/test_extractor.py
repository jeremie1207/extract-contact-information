import pytest

from src.extractor.extractor import emails_extractor, phone_numbers_extractor


@pytest.fixture
def sample_text() -> str:
    return """
        Contact Us
        Reach Us by Email - email is the best way to reach us
        General inquiries and order questions: info@nostarch.com
        Discount codes and promotions: We offer promo codes periodically 
        via our newsletter. Sign up here to get notified. We are unable to 
        issue individual coupon codes by request.
        Wholesale, bookstore, and bulk orders (20+ copies): sales@nostarch.com
        Academic requests: academic@nostarch.com (Further information)
        Conference and event inquiries: conferences@nostarch.com
        Errata - please send any errata reports to: errata@nostarch.com
        Media requests: media@nostarch.com
        Proposals or editorial inquiries: editors@nostarch.com
        Rights inquiries: rights@nostarch.com (Further information)
        Interested in working with us? 
        View our current job openings
        Physical Address
        No Starch Press Inc
        245 8th Street
        San Francisco, CA 94103
        USA

        Mailing Address
        No Starch Press Inc
        329 Primrose Road,  #42
        Burlingame, CA 94010-4093
        USA

        Phone: 613-555-1234
            613.555.1234
            613 555 1234
            (613) 555-1234
            +1 613 555 1234
            +1-613-555-1234

        Reach Us on Social Media
        Twitter Facebook Instagram Linkedin Pinterest
    """



def test_emails_extractor(sample_text: str) -> None:
    expected_result: list[str] = ['info@nostarch.com', 'sales@nostarch.com', 
                                'academic@nostarch.com', 
                                'conferences@nostarch.com', 
                                'errata@nostarch.com', 'media@nostarch.com', 
                                'editors@nostarch.com', 'rights@nostarch.com']
    
    actual_result: list[str] = emails_extractor(sample_text)
    
    
    assert sorted(actual_result) == sorted(expected_result)

    
def test_emails_extractor_error() -> None:
    with pytest.raises(TypeError, match=r"text should be a string"):
        emails_extractor(1) # type: ignore[arg-type]
    
def test_phone_number_extractor(sample_text: str) -> None:
    expected_result = [
        "613-555-1234",
        "613.555.1234",
        "613 555 1234",
        "(613) 555-1234",
        "+1 613 555 1234",
        "+1-613-555-1234"
    ]
    
    actual_result = phone_numbers_extractor(sample_text)
    
    assert sorted(actual_result) == sorted(expected_result)
    
def test_phone_number_extractor_error() -> None:
    with pytest.raises(TypeError, match=r"text should be a string"):
        phone_numbers_extractor(1) # type: ignore[arg-type]