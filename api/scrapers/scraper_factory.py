from scrapers.ejobs_scraper import EJobsScraper
from scrapers.hipo_scraper import HipoScraper
from scrapers.linkedin_scraper import LinkedInScraper
from scrapers.bestjobs_scraper import BestJobsScraper
from settings import *

KNOWN_PLATFORMS = {
    LINKEDIN_NAME:LinkedInScraper,
    HIPO_NAME:HipoScraper,
    EJOBS_NAME:EJobsScraper,
    BESTJOBS_NAME:BestJobsScraper
}

class ScraperFactory:
    def generate(site_url : str, platform : str):
        return KNOWN_PLATFORMS.get(platform, lambda: 'Unknown platform')(site_url)
