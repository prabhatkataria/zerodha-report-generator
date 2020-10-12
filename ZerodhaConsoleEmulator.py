from selenium import webdriver
from time import sleep
from datetime import date
import calendar
from selenium.webdriver.common.keys import Keys
import os
from utils import SEGMENTS, getOutputPath, isDirectoryExists, createDirectory
from pdf_converter import createPdf


class ZerodhaConsoleEmulator(object):

    def __init__(self, clientId, password, pin, report):
        super()
        self.driver = webdriver.Firefox()
        self.driver.get('https://console.zerodha.com/')
        sleep(5)
        self.loggedIn = False
        self.clientId = clientId
        self.password = password
        self.pin = pin
        self.report = report

    def getSnapshot(self, name):
        return self.driver.save_screenshot(name)

    def closeDriver(self):
        self.driver.close()

    def login(self):
        self.driver.find_element_by_tag_name('button').click()
        sleep(2)
        self.driver.find_elements_by_id('userid')[0].send_keys(self.clientId)
        self.driver.find_elements_by_id('password')[0].send_keys(self.password)
        self.driver.find_element_by_tag_name('button').click()
        sleep(2)
        self.driver.find_elements_by_id('pin')[0].send_keys(self.pin)
        self.driver.find_element_by_tag_name('button').click()
        sleep(2)
        self.loggedIn = True

    def openTradebook(self):

        # open reports dropdown
        self.driver.find_elements_by_xpath(
            '//a[@class="dropdown-label reports-label"]')[0].click()

        # open tradebook page
        self.driver.find_elements_by_xpath(
            '//div[@class="dropdown-nav reports-dropdown"]//ul/li[1]/a')[0].click()

    def setTradebookDate(self, month, year):
        fromDt = date(year, month, 1)
        toDt = date(year, month, calendar.monthrange(year, month)[1])
        fromDt = date(year, month, 1)
        dateFormat = '%Y-%m-%d'
        dateStr = '{} ~ {}'.format(fromDt.strftime(
            dateFormat), toDt.strftime(dateFormat))
        self.driver.find_elements_by_xpath(
            '//div[@class="mx-datepicker mx-datepicker-range"]//input[@class="mx-input"]')[0].send_keys(Keys.CONTROL, 'a')
        self.driver.find_elements_by_xpath(
            '//div[@class="mx-datepicker mx-datepicker-range"]//input[@class="mx-input"]')[0].send_keys(dateStr)
        self.driver.find_elements_by_xpath(
            '//div[@class="su-input-group su-static-label"]//label')[0].click()

    def setTradebookSegment(self, segmentValue):
        path = '//option[@value="{}"]'.format(segmentValue)
        self.driver.find_elements_by_xpath(path)[0].click()
        self.driver.find_elements_by_xpath(
            "//button[@class='btn-blue']")[0].click()

    def logout(self):
        self.driver.find_elements_by_xpath(
            '//a[@class="dropdown-label user-id"]')[0].click()
        self.driver.find_elements_by_xpath(
            '//ul[@class="list-flat dropdown-nav-list"]/li[last()]')[0].click()

    def run(self):
        try:
            self.login()
            self.openTradebook()
            for period in self.report:
                month, year = (period.get("month"), period.get("year"))
                self.setTradebookDate(month, year)
                outputFolder = os.path.join(
                    os.getcwd(), 'output', '{}_{}'.format(year, month))
                if (not isDirectoryExists(outputFolder)):
                    createDirectory(outputFolder)
                for k, v in SEGMENTS.items():
                    self.setTradebookSegment(v)
                    sleep(5)

                    isSaved = self.getSnapshot(getOutputPath(
                        outputFolder, '{}.png'.format(k)))
                    print("took snapshot for {} and saved={}".format(k, isSaved))
                createPdf(outputFolder, "tradebook.pdf")

        finally:
            if(self.loggedIn):
                self.logout()
            self.closeDriver()
