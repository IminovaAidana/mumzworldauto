from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Step 1: Open the mumzworld webstore
driver.get("https://www.mumzworld.com")

# Step 2: Search for a product
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("baby stroller")
search_box.send_keys(Keys.RETURN)
time.sleep(3)

# Step 3: Add the product to the bag
product = driver.find_element(By.XPATH, "//div[@class='product-item']")
product.click()
time.sleep(2)
add_to_bag_button = driver.find_element(By.ID, "add-to-bag")
add_to_bag_button.click()
time.sleep(2)

# Step 4: Go to the view bag page
view_bag_button = driver.find_element(By.XPATH, "//a[contains(text(),'View Bag')]")
view_bag_button.click()
time.sleep(2)

# Step 5: Increase the quantity to 5 items
quantity_input = driver.find_element(By.NAME, "quantity")
quantity_input.clear()
quantity_input.send_keys("5")
time.sleep(2)

# Step 6: Click "Proceed to checkout"
checkout_button = driver.find_element(By.XPATH, "//button[contains(text(),'Proceed to Checkout')]")
checkout_button.click()
time.sleep(2)

# Step 7: Register a new user
register_button = driver.find_element(By.XPATH, "//a[contains(text(),'Register')]")
register_button.click()
time.sleep(2)

# Fill in registration form
first_name = driver.find_element(By.NAME, "first_name")
first_name.send_keys("John")
last_name = driver.find_element(By.NAME, "last_name")
last_name.send_keys("Doe")
email = driver.find_element(By.NAME, "email")
email.send_keys("johndoe@example.com")
password = driver.find_element(By.NAME, "password")
password.send_keys("Password123")
confirm_password = driver.find_element(By.NAME, "confirm_password")
confirm_password.send_keys("Password123")
time.sleep(2)

# Submit the registration form
submit_button = driver.find_element(By.XPATH, "//button[contains(text(),'Create Account')]")
submit_button.click()
time.sleep(5)

# Close the browser
driver.quit()