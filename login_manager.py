from playwright.sync_api import sync_playwright
import time, os, json

SESSION_FILE = "playwright/session.json"

def save_session(context):
    with open(SESSION_FILE, "w") as f:
        json.dump(context.storage_state(), f)

def load_session(playwright):
    browser = playwright.chromium.launch(headless=True)
    if os.path.exists(SESSION_FILE):
        context = browser.new_context(storage_state=SESSION_FILE)
    else:
        context = browser.new_context()
    return browser, context

def login_to_instagram():
    with sync_playwright() as p:
        browser, context = load_session(p)
        page = context.new_page()

        if not os.path.exists(SESSION_FILE):
            page.goto("https://www.instagram.com/accounts/login/")
            page.wait_for_selector("input[name='username']", timeout=15000)
            print("🔐 Please log in manually (username + password + 2FA)")
            while "/accounts" in page.url:
                time.sleep(2)
            print("✅ Login successful. Saving session.")
            save_session(context)
        else:
            print("🔁 Session loaded.")

        return browser, context, page
