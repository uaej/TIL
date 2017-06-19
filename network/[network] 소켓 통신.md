# 소켓 통신

## 0. 소켓이란?
두 시스템 사이의 네트워크 연결을 나타내는 객체이다.
두 시스템 간의 정보에는 ip와 포트번호 등이 들어있다.

## 1. 서버
1. 서버 소켓 만들기(socket)
2. 소켓에 주소 할당(bind)
3. 연결 요청 대기(listen)
4. 연결 허용(accept)
5. 데이터 송수신(read & write)
6. 연결 종료(close)

## 2. 클라이언트
1. 소켓 생성(socket)
2. 연결(connect)
3. 데이터 송수신(read & write)
4. 연결 종료(close)

## 참고자료
<li>http://tobewiseys.tistory.com/75
<li>http://chan7ee.tistory.com/entry/%EC%86%8C%EC%BC%93socket-%ED%8F%AC%ED%8A%B8port-TCP-UDP-%EC%A0%95%EC%9D%98
<li>http://chan7ee.tistory.com/entry/소켓socket-포트port-TCP-UDP-정의
