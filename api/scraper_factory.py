from settings import *
from scrapers.ejobs_scraper import EJobsScraper
from scrapers.hipo_scraper import HipoScraper
from scrapers.linkedin_scraper import LinkedInScraper
    
KNOWN_PLATFORMS = {
    LINKEDIN_NAME:LinkedInScraper,
    HIPO_NAME:HipoScraper,
    EJOBS_NAME:EJobsScraper
}

class ScraperFactory:
    def generate(site_url : str, platform : str):
        return KNOWN_PLATFORMS.get(platform, lambda: 'Unknown platform')(site_url)