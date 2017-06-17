# [python] class의 역할

## 1. class가 필요한 이유?
굳이 클래스 없이도 프로그램을 만들 수 있지만 클래스를 사용하면 중복되는 코드를 클래스를 이용해서 객체를 생성함으로써 쉽게 만들 수 있다.
함수와는 달리 각각의 객체끼리 변수를 공유하지 않는다.

## 2. 클래스 생성
    class Programmer :
        pass

## 3. 객체 생성
    kim = Programmer()
    park = Programmer()

1개의 클래스는 무수히 많은 객체를 만들어 낼 수 있다.

## 4. 객체 변수 참조
    객체이름.변수명
    ex) a = kim.name


## 5. 출처
https://wikidocs.net/28
