from selenium import webdriver
import time 
import sys

driver = webdriver.Firefox()
driver.get("https://viewblock.io/arweave/block/0")
driver.get("https://viewblock.io/arweave/block/0?page="+sys.argv[1])

time.sleep(10)
print (driver.page_source)
driver.quit()
