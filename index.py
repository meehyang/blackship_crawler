from urllib import parse

URL = "https://ameblo.jp/blackship-staff/page-%d.html"

def url_parse(url, page):
    url = parse.urlparse(url % page)
    return url

def main():
    # 크롤링할 url을 받아서 파싱
    # 파싱해서 필요한 정보만 뽑기
    # db 연결
    # db에 저장
    # 트위터 알림 (멘션 보내기 가능할지?)
    pass

if __name__ == "__main__":
    main();
    

