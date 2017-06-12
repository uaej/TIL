# ArrayList 클래스

## 0. 특징
<li> **객체**들을 삽입, 삭제, 검색 할 수 있는 **컨테이너 클래스**다.
<li> 배열의 길이 제한 단점을 보완. 배열은 처음 생성한 길이에서 더 추가되지 않지만, arrayList는 요소를 추가하고 싶을 때마다 더 추가할 수 있다.
<li> 삽입되는 객체의 수가 많아지면 **자동으로 크기가 조절**된다.
<li> 아이템을 ArrayList 맨 마지막이나 중간에 삽입할 수 있다.
<li> 아이템 삽입/삭제 시 자동으로 빈칸을 만들거나 채워준다.

## 1. 생성 방법

    private ArrayList<[객체형]> listViewItemList = new ArrayList<[객체형]>();

원하는 객체형을 가진 ArrayList를 생성한다.

## 2. 요소 삽입/검색
### <li> add(obj)
ArrayList에 요소를 삽입한다. list에 추가하고자 하는 요소를 인자값으로 준다.
다양한 객체를 삽입할 수 있다.(String, Integer, 이외의 객체)
### <li> get(i)
i는 ArrayList의 인덱스값. 0부터 요소들이 삽입된다.
ArrayList에서 요소를 검색하고 요소의 객체를 얻을 수 있다.

## 3. 주요 메소드
<li> `boolean add(E e)`

ArrayList의 맨 뒤에 요소 추가
<li>`void add(int index, E element)`

지정한 인덱스에 지정된 객체를 삽입
<li> `void clear()`

ArrayList의 모든 요소 삭제
<li>`E get(int index)`

지정한 인덱스의 요소 반환
<li>`int indexOf(Object o)`

지정한 객체와 같은 첫 번째 요소의 인덱스 반환. 없으면 -1 반환
<li> `int remove(int index)`

지정한 인덱스의 요소 삭제
<li> `int size()`

ArrayList가 포함하는 요소의 개수 반환
<li> `Object[] toArray()`

ArrayList의 모든 요소를 포함하는 배열을 반환
