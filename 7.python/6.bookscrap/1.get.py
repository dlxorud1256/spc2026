import requests
from bs4 import BeautifulSoup
import csv

# 1. books.toscrape.com 에 접속해서 페이지를 받아온다
url = "https://books.toscrape.com/"
response = requests.get(url)

# 인코딩 설정
response.encoding = "utf-8"

# 요청 성공 여부 확인
if response.status_code == 200:
    html = response.text

    # 2. DOM 을 bs4로 구성한다
    soup = BeautifulSoup(html, "html.parser")
    
    # 3. 첫 페이지의 도서명, 평점, 가격을 받아온다
    books = soup.select("article.product_pod")

    book_data = []

    for book in books:
        # 도서명
        title = book.select_one("h3 a")["title"]

        # 평점
        rating_class = book.select_one("p.star-rating")["class"]
        rating = rating_class[1]
        # 예: ['star-rating', 'Three'] 에서 Three 추출

        # 가격
        price = book.select_one("p.price_color").text

        book_data.append([title, rating, price])

    # 4. CSV파일로 저장한다
    with open("books.csv", "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)

        # CSV 헤더
        writer.writerow(["도서명", "평점", "가격"])

        # 데이터 저장
        writer.writerows(book_data)

    print("CSV 파일 저장 완료!")

else:
    print("페이지 요청 실패:", response.status_code)