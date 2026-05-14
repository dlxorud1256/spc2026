from playwright.sync_api import sync_playwright
import csv

BASE_URL = "https://makemyproject.net/shop/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # 1. 쇼핑몰 접속
    page.goto(BASE_URL)

    # 2. 로그인
    page.fill("#uid", "user123")
    page.fill("#upw", "password1234")
    page.click("#loginBtn")

    # 로그인 완료 대기
    page.wait_for_function("""
        () => {
            const who = document.querySelector("#who");
            return who && !who.innerText.includes("비로그인");
        }
    """)

    print("로그인 완료:", page.locator("#who").inner_text())

    # 3. 상품 목록 로딩 대기
    page.wait_for_selector("#products .card a")

    # 4. 현재 페이지의 상품 제목 + 상세 링크 가져오기
    product_links = page.locator("#products .card a")

    products = []

    for i in range(product_links.count()):
        title = product_links.nth(i).inner_text()
        href = product_links.nth(i).get_attribute("href")

        # href가 products/26 같은 상대경로라서 절대주소로 변환
        detail_url = page.url.rstrip("/") + "/" + href

        products.append({
            "title": title,
            "url": detail_url
        })

    print(f"상품 {len(products)}개 수집 완료")
    print(products)


    input("브라우저를 닫으려면 Enter를 누르세요...")

    browser.close()