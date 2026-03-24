from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list(self):
        # You heard about a cool new website to track todos
        # You visit the site
        self.browser.get('http://localhost:8000')

        # You notice the page title mentions To-Do
        self.assertIn('To-Do', self.browser.title)

        # You notice an input box inviting you to enter a to-do
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # You type a new to-do item
        inputbox.send_keys('Buy a new MacBook')

        # When you hit enter the page refreshes and shows your item
        inputbox.send_keys(Keys.ENTER)

        # There is a table showing your to-do items
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertTrue(
            any('Buy a new MacBook' in row.text for row in rows)
        )


if __name__ == '__main__':
    unittest.main()