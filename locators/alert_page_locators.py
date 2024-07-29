from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:

    NEW_TAB_BUTTON = (By.CSS_SELECTOR, "button[id='tabButton']")

    TITLE_NEW = (By.CSS_SELECTOR, "h1[id='sampleHeading']")

    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, "button[id='id='windowButton']")

class AlertsPageLocators:

    SEE_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='alertButton']")
    APPER_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='timerAlertButton']")
    CONFIRM_BUTTON = (By.CSS_SELECTOR, "button[id='confirmButton']")
    PROMPT_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='promtButton']")
    PROMPT_IMPUT = (By.CSS_SELECTOR, "span[id='promptResult']")
