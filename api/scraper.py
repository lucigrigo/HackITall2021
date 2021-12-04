from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from settings import *
import re

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
        driver = webdriver.Chrome(options=options, executable_path=CHROME_DRIVER_PATH)

        search_url = self.site_url

        # Location
        if location:
            search_url += '/' + location + '/'
        else:
            search_url += '/Toate-Orasele/'

        # Job Title
        if job_title:
            words = job_title.split(' ')
            for idx, w in enumerate(words):
                search_url += w
                if idx != len(words) - 1:
                    search_url += '-'
            if skills:
                search_url += '-'

        # Skills
        for idx, skill in enumerate(skills):
            search_url += str(skill)
            if idx != len(skills) - 1:
                search_url += '-'

        # Get last page
        driver.get(search_url)
        r = driver.find_element_by_class_name("page-last")
        last_page_url = r.get_attribute("href")
        last_page = int(re.findall(r'\d+', last_page_url)[-1])

        count = 0
        jobs = {}
        for i in range(last_page):
            driver.get(search_url + f"/{i + 1}")
            ret_jobs = driver.find_elements_by_class_name("job-title")
            companies = driver.find_elements_by_class_name("cell-company")
            for i, job in enumerate(ret_jobs):
                company_name = companies[i].find_element_by_tag_name("span").text
                title = job.get_attribute('title')
                link = job.get_attribute('href')
                jobs[(title, company_name)] = link
                count += 1
                if count == MAX_JOBS:
                    driver.quit()
                    return jobs
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