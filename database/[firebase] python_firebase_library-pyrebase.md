# pyrebase
> pyrebase README를 필요한 부분만 골라서 해석해 놓음.

## pyrebase란?
firebase API의 간단한 파이썬 wrapper

## python 버전
python3에 맞춰서 쓰여짐. python2에서는 잘 작동하지 않을 수 있음.

## pyrebase를 application에 추가
유저 기반의 허가만을 사용하려면 아래의 설정을 따라 만들 수 있다.
    import pyrebase

    config = {
    "apiKey": "apiKey",
    "authDomain": "projectId.firebaseapp.com",
    "databaseURL": "https://databaseName.firebaseio.com",
    "storageBucket": "projectId.appspot.com"
    }

    firebase = pyrebase.initialize_app(config)

## 서비스 사용
Pyrebase app에는 여러 개의 Firebase 서비스를 사용할 수 있다.
`firebase.auth()` : Authentication
`firebase.database()` : Database
`firebase.stroage()` : Storage

## Database 사용
<li> child()메소드를 사용해 경로를 만들 수 있다.
    db = firebase.database()
    db.child("users").child("Mority")

<li> 데이터 저장
- push
 : push() 메소드를 사용하면 유니크한 데이터,
- set
- update
- remove
- multi-location updates

<li> 데이터 읽기
- val
- key
- each
- get
- shallow
- streaming
- close the stream
## 출처
https://github.com/thisbejim/Pyrebase
