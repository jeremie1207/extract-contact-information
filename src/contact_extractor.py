import logging

import click

from extractor.extractor import emails_extractor, phone_numbers_extractor
from get_web_page.get_web_page import get_web_page

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger(__name__)


@click.command()
@click.argument("url")
@click.option("--verbose", "-v", is_flag=True)
@click.option("--emails-only", "-e", is_flag=True)
@click.option("--phones-only", "-p", is_flag=True)
def extract_contact_information(url: str, verbose: bool, emails_only: bool, phones_only: bool):
    """Extract contact information from the provide web page"""
    
    logger.info("Starting extraction of contact information in the text")
    
    if verbose:
        logger.setLevel(logging.DEBUG)
        logger.debug("Starting debug mode")
    
    text = get_web_page(url)
    emails: list[str] = [] 
    phone_numbers: list[str] = []
    

    if emails_only:
        emails = emails_extractor(text)
    elif phones_only:
        phone_numbers = phone_numbers_extractor(text)
    else:
        emails = emails_extractor(text)
        phone_numbers = phone_numbers_extractor(text)
    
    if emails:
        click.echo("Emails")
        click.echo("------")
        
        for email in emails:
            click.secho(email, fg="green")
    
    if phone_numbers:
        click.echo("Phone Numbers")
        click.echo("------")
            
        for phone_number in phone_numbers:
            click.secho(phone_number, fg="green")
    
    
    click.echo("Extraction complete with success.")