# [python] string을 바이너리 파일로 변환하는 법
> 스택 오버플로우의 질문 및 답변을 해석 및 요약한 것

## 1. 질문
`my_string = b'the string'`

위의 문법에서

1. 문자열 앞에 있는 문자'b'의 의미는 무엇인가요?
2. 이 것(b)를 사용함으로써 얻는 이익은 무엇인가요?
3. 이것을 사용할 적절한 상황은 무엇인가요?

## 2. 답변
파이썬 3.3의 documentation에 따르면
>Bytes literals are always prefixed with 'b' or 'B'; they produce an instance of the bytes type instead of the str type. They may only contain ASCII characters; bytes with a numeric value of 128 or greater must be expressed with escapes.  ----------------------------------
바이트 상수는 언제나 앞에 'b'또는 'B'가 붙어야 합니다. 그것들은 str타입 대신 인스턴스를 바이트들을 생성합니다.
그것들은 오직 ASCII문자만 포함할 수 있으며, 128 이상의 숫자 값은 ESCAPE로 표현되어야만 한다.
## 출처


https://stackoverflow.com/questions/6269765/what-does-the-b-character-do-in-front-of-a-string-literal
여기 해석/정리하기
