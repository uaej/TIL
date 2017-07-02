# multi tread 사용법

## 0. 스레드란?
프로그램의 실행 단위가 프로세스라면, 프로세스의 실행 단위를 스레드라고 부른다.

스레드는 하나의 프로세스 내에서 동작하면서 자원을 공유한다.

## 1. 스레드 문법
    #include <ptread.h>

    ptread_create(&tid, NULL, threadRun, NULL);
    ptread_join(tid, NULL);

## 2. 스레드의 문제점
공유된 메모리를 사용하기 때문에 다른 스레드가 언제 끼어들어 어떤 값을 수정할 지 모르기 때문에 원하는 동작이 되지 않는다.

-> 크리티컬 섹션 동기화 방식
: 어떤 값에 대한 사용이 끝나기 전까지는 그 값을 사용하려는 다른 스레드가 멈춰있게 함으로써 그 값의 신빙성을 유지한다.
-> 이벤트, 세마포어, 뮤텍스 등을 이용한 동기화 방식들이 있다.

## 출처
<li>http://elky.tistory.com/197
<li>http://www.geeksforgeeks.org/multithreading-c-2/
