## [python] 파일입출력

## 1. 순서
<li> open
<li> read/write
<li> close

## 2. open
`파일 객체 = open(파일 이름, 파일 열기 모드)`

<li>파일 열기 모드
- r : 읽기모드
- w : 쓰기모드  
  , 파일을 w모드로 열면 동일 이름 파일이 있을 경우에는 덮어쓰고 없으면 새로 생성한다.
-a : 추가모드

## 3. 읽기
<li> readline() :

`파일객체.readline()`

파일의 첫번째 줄을 리턴, 호출할때마다 다음 줄 리턴

<li> readlines() :

`파일객체.readlines()`

파일의 전체에서 한줄씩 리스트에 넣어서 반환

<li> read() :

`파일객체.read()`

파일 내용의 전체를 문자열로 리턴

## 4. 쓰기

`파일객체.write(DATA)`

DATA는 문자열

## 5. close

`파일객체.close()`
