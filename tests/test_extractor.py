import pytest

from src.extractor.extractor import emails_extractor


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

        Phone: 800.420.7240 or +1 415.863.9900
        Fax: +1 415.863.9950

        Reach Us on Social Media
        Twitter Facebook Instagram Linkedin Pinterest
    """



def test_emails_extractor(sample_text: str):
    expected_result: list[str] = ['info@nostarch.com', 'sales@nostarch.com', 
                                'academic@nostarch.com', 
                                'conferences@nostarch.com', 
                                'errata@nostarch.com', 'media@nostarch.com', 
                                'editors@nostarch.com', 'rights@nostarch.com']
    
    actual_result: list[str] = emails_extractor(sample_text)
    
    print(expected_result)
    print(actual_result)
    
    assert sorted(actual_result) == sorted(expected_result)

def test_emails_extractor_empty_text():
    empty_text: str = ""
    expected_result: list[str] = []
    
    
    actual_result: list[str] = emails_extractor(empty_text)
    
    assert actual_result == expected_result
    
def test_emails_extractor_no_email_in_given_text():
    text = "Hello, world!"
    expected_result: list[str] = []
    
    actual_result: list[str] = emails_extractor(text)
    
    assert actual_result == expected_result
    