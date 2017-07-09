#RPi에서 firebase 접근하기


## 1. firebase 파이썬 라이브러리 링크
https://pypi.python.org/pypi/python-firebase

## 2. 설치 순서
<li>`sudo pip install requests`
<li>`sudo pip install python-firebase`

## 3. 테스트 예제
    from firebase import firebase
    firebase = firebase.FirebaseApplication("[firebase database address]", None)
    result = firebase.get('/led', None)

## 출처
<li> http://blog.naver.com/PostView.nhn?blogId=cosmosjs&logNo=220974639043&categoryNo=0&parentCategoryNo=56&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView

=> 위의 내용 요약본.
