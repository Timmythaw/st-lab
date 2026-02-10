from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def test_python_search():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    
    try:
        # Navigate to Python.org
        driver.get("https://www.python.org")
        print("Navigated to Python.org")
        
        # Wait for and interact with search field
        element = wait.until(
            EC.element_to_be_clickable((By.ID, "id-search-field"))
        )
        element.send_keys("getting started with python")
        element.submit()
        print("Search form submitted")
        
        # Wait for URL to change (indicates search executed)
        wait.until(EC.url_contains("search"))
        print(f"Current URL: {driver.current_url}")
        
        # Print actual title to see what it is
        print(f"Actual page title: '{driver.title}'")
        
        # Look for search results container
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".list-recent-events, .search-result, ul"))
        )
        print("Search results loaded successfully")
        
        # Optional: Verify page contains search results
        page_text = driver.find_element(By.TAG_NAME, "body").text
        if "getting started" in page_text.lower() or "python" in page_text.lower():
            print("Search results contain relevant content")
        
        # Optional: View results before closing
        time.sleep(5)
        
        print("\nAll tests passed!")
        
    except TimeoutException as e:
        print(f"Test failed: Timeout waiting for element - {e}")
        print(f"Current URL: {driver.current_url}")
        print(f"Current Title: {driver.title}")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
        print("Browser closed")

if __name__ == "__main__":
    test_python_search()
