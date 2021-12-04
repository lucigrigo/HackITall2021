import os
import sys
from scraper_factory import ScraperFactory
from settings import SITES

def init_scrapers():
    return {platform:ScraperFactory.generate(site_url=url, platform=platform) for platform, url in SITES.items()}

if __name__ == "__main__":
    # scrapers = init_scrapers()
    # for platform, scraper in scrapers.items():
    #     print(f'---   ---\nScraping platform {platform}')
    #     jobs = scraper.scrape_jobs('software engineer', ['Java'], 'Bucuresti')
    #     candidates = scraper.scrape_candidates('software engineer', ['Java'], 'Bucuresti')
    #     print(f'Jobs = {jobs}\nCandidates = {candidates}\n---   ---\n')

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
