CHROME_DRIVER_PATH = '/usr/bin/chromedriver'

INSTALLED_APPS = [
    'rest_framework',
    'django.core.management',
    'django.db',
    'selenium'
]

LINKEDIN_URL = 'https://www.linkedin.com/search/results/people'
LINKEDIN_NAME = 'LinkedIn'
HIPO_URL = 'https://www.hipo.ro/locuri-de-munca/cautajob/Toate-Domeniile'
HIPO_NAME = 'Hipo'

SITES = {
    LINKEDIN_NAME:LINKEDIN_URL,
    HIPO_NAME:HIPO_URL
}

MAX_JOBS = 100