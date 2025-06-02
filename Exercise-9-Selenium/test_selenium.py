import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def driver():
  options = webdriver.ChromeOptions()
  driver = webdriver.Chrome(options=options)
  driver.get('https://duckduckgo.com')

  search_bar = driver.find_element(By.ID, 'searchbox_input')
  search_bar.send_keys('calculator')
  search_button = driver.find_element(By.CSS_SELECTOR, '.searchbox_searchButton__LxebD')
  search_button.click()

  yield driver
  driver.quit()

def click_number(driver, number):
  for digit in str(number):
    driver.find_element(By.XPATH, f"//button[text() = '{digit}']").click()

def calc_sum(driver, num1, num2):
  click_number(driver, num1)
  driver.find_element(By.XPATH, "//button[text() = '+']").click()
  click_number(driver, num2)
  driver.find_element(By.XPATH, "//button[text() = '=']").click()
  return int(driver.find_element(By.ID, 'display').text)

def calc_multiplication(driver, num1, num2):
  click_number(driver, num1)
  driver.find_element(By.XPATH, "//button[text() = '×']").click()
  click_number(driver, num2)
  driver.find_element(By.XPATH, "//button[text() = '=']").click()
  return int(driver.find_element(By.ID, 'display').text)

def calc_division(driver, num1, num2):
  click_number(driver, num1)
  driver.find_element(By.XPATH, "//button[text() = '÷']").click()
  click_number(driver, num2)
  driver.find_element(By.XPATH, "//button[text() = '=']").click()
  return int(driver.find_element(By.ID, 'display').text)

def get_calculation_history(driver):
  results = driver.find_elements(By.CSS_SELECTOR, '.tile__past-result')
  history = [int(result.text) for result in results]
  history.reverse()
  return history

def test_sum_two_numbers(driver):
  assert calc_sum(driver, 15, 25) == 40

def test_sum_and_divide_result_by_10(driver):
  result = calc_sum(driver, 18, 22)
  division_result = calc_division(driver, result, 5)

  assert result == 40
  assert division_result == 8

def test_two_operations_check_last_result(driver):
  mult = calc_multiplication(driver, 7, 4)
  sum = calc_sum(driver, 9, 6)
  history = get_calculation_history(driver)

  assert mult == 28
  assert sum == 15
  assert history[-1] == 15

def test_three_operations_check_history(driver):
  operations = [
    calc_sum(driver, 45, 55),
    calc_division(driver, 60, 12),
    calc_multiplication(driver, 8, 9),
  ]
  
  assert get_calculation_history(driver) == operations