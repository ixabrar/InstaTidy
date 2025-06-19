from login_manager import login_to_instagram

def main():
    browser, context, page = login_to_instagram()
    print("📁 Going to saved posts...")
    page.goto("https://www.instagram.com/saved/")
    page.wait_for_timeout(5000)
    input("Press ENTER to close browser...")
    browser.close()

if __name__ == "__main__":
    main()
