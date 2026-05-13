from playwright.sync_api import sync_playwright

url = "https://news.naver.com/section/105"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url, wait_until="networkidle")

    # 기사 제목 링크 요소들 선택
    articles = page.locator(".section_article.as_headline a.sa_text_title").all()

    for article in articles:
        link = article.get_attribute("href")
        title = article.locator("strong.sa_text_strong").inner_text()

        print(title)
        print(link)
        print("-" * 50)

    browser.close()