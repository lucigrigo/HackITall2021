from scrapers.scraper_factory import ScraperFactory
from settings import SITES
from flask import Flask, jsonify, request, Response
from json import dumps

app = Flask(__name__)

@app.route("/api/candidates", methods = ["GET"])
def get_candidates():
    job_title = request.args.get('job_title', '')
    skills = request.args.get('skills', [])
    location = request.args.get('location', '')
    scrape_results = []
    global scrapers
    for _, scraper in scrapers.items():
        r = scraper.scrape_candidates(job_title, skills, location)
        if r:
            scrape_results.append(r)
    return jsonify(scrape_results), 200

def obj_dict(obj):
    return obj.__dict__

@app.route("/api/jobs", methods = ["GET"])
def get_jobs():
    job_title = request.args.get('job_title', '')
    skills = request.args.get('skills', [])
    location = request.args.get('location', '')
    scrape_results = []
    global scrapers
    for _, scraper in scrapers.items():
        r = scraper.scrape_jobs(job_title, skills, location)
        if r:
            scrape_results.append(r)
    return jsonify(scrape_results), 200

def init_scrapers():
    return {platform : ScraperFactory.generate(url, platform) for platform, url in SITES.items()}

def main():
    global scrapers
    scrapers = init_scrapers()
    app.run()

if __name__ == '__main__':
    main()
