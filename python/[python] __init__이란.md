# `__init__`이란

## 1. 사용 예제
    class Service :
        a = "안녕하세요"
        def __init__(self, name) :
            self.name = name
        def sum(self, a, b) :
            result = a + b
            print("%님 %s + %s = %s입니다." % (self.name, a, b, result))

## 2. init의 의미란?
"객체를 만들 때 항상 실행된다"

객체를 생성한 후 메소드를 호출하지 않아도 알아서 호출되는 메소드.
어떤 상황에서든지 호출해야 하는 메소드일 경우 init에 넣어 사용자가 빼먹지 않고 사용할 수 있도록 한다.

그래서 위의 클래스의 객체를 생성할 때는 `a = Service("홍길동")` 처럼  
 `__init__`의 매개 변수도 함께 넣어서 클래스를 선언해야 한다.

## 출처
https://wikidocs.net/28
