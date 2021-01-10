#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_selenium.base import Base


class TestWait(Base):

    def test_wait(self):
        # def wait(x):
        #     return len(self.driver.find_elements_by_link_text("热门")) >= 1
        # WebDriverWait(self.driver, 7).until(wait)
        self.driver.get("https://home.testing-studio.com")
        WebDriverWait(self.driver, 7).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@class="d-button-label"]')))
        self.driver.find_element_by_xpath('//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()
        self.driver.find_element_by_xpath('//*[@class="d-button-label"]').click()
        time.sleep(3)
