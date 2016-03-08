from googlexml import GoogleXML as google
from splinter import Browser

search_query = 'How much wood could a woodchuck chuck?'

with Browser() as browser:
    browser.visit(google.search_url)
    browser.fill('q', search_query)
    button = browser.find_by_name('btnG') #TODO: Move btnG to GoogleXML
    button.click()