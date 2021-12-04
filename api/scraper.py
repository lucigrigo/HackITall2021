from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from settings import *

class LinkedInScraper:
    '''
        TODO: implement login logic and then run search for profiles; implement search_jobs logic
    '''
    def __init__(self, site_url : str):
        self.site_url = site_url
    
    def scrape_candidates(self, job_title : str, skills : list, location : str):
        options = Options()
        options.headless = True

        search_url = self.site_url + '/?keywords='
        if job_title:
            words = job_title.split(' ')
            for idx, w in enumerate(words):
                search_url += str(w)
                if idx != len(words) - 1:
                    search_url += '%20'
            if skills:
                search_url += '%20'
        for idx, skill in enumerate(skills):
            search_url += str(skill)
            if idx != len(skills) - 1:
                search_url += '%20'
        search_url += '&origin=GLOBAL_SEARCH_HEADER&sid=S%3Bj'

        #print(f'scraping url \'{search_url}\'')
        driver = webdriver.Chrome(options=options, executable_path=CHROME_DRIVER_PATH)
        driver.get(search_url)
        results = driver.find_elements_by_xpath('//*[@id="main"]/div/div/div[2]/ul/li[1]/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a')
        candidates = [r.get_attribute('href') for r in results]
        driver.quit()
        return candidates # TODO: turn this into a dict

    def scrape_jobs(self, job_title : str, skills : list, location : str):
        return {}

class HipoScraper:
    def __init__(self, site_url : str):
        self.site_url = site_url
    
    def scrape_jobs(self, job_title : str, skills : list, location : str):
        options = Options()
        options.headless = True

        search_url = self.site_url
        if location:
            search_url += '/' + location + '/'
        else:
            search_url += '/Toate-Orasele/'
        if job_title:
            words = job_title.split(' ')
            for idx, w in enumerate(words):
                search_url += w
                if idx != len(words) - 1:
                    search_url += '-'
            if skills:
                search_url += '-'
        for idx, skill in enumerate(skills):
            search_url += str(skill)
            if idx != len(skills) - 1:
                search_url += '-'

        # /html/body/div[1]/div[1]/div[2]/div/table/tbody/tr[1]/td[1]/a
        # /html/body/div[1]/div[1]/div[2]/div/table/tbody/tr[2]/td[1]/a
        # /html/body/div[1]/div[1]/div[2]/div/table/tbody/tr[9]/td[1]/a

        driver = webdriver.Chrome(options=options, executable_path=CHROME_DRIVER_PATH)
        driver.get(search_url)
        results = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[2]/div/table/tbody/tr")
        jobs = {}
        for r in results:
            elem = r.find_element(By.XPATH, "//td[1]/a")
            title = elem.get_attribute('title')
            link = elem.get_attribute('href')
            jobs[title] = link
        driver.quit()
        return jobs

    def scrape_candidates(self, job_title : str, skills : list, location : str):
        return {}

KNOWN_PLATFORMS = {
    LINKEDIN_NAME:LinkedInScraper,
    HIPO_NAME:HipoScraper
}

class ScraperFactory:
    def generate(site_url : str, platform : str):
        return KNOWN_PLATFORMS.get(platform, lambda: 'Unknown platform')(site_url)