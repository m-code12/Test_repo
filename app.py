import sys
import website_analysis

if __name__ == '__main__':
    site_domain = "http://fastcoder.netlify.com"
    spider = website_analysis.Spider(site_domain)
    spider.crawl()
