# multi tread 사용법

## 0. 스레드란?
프로그램의 실행 단위가 프로세스라면, 프로세스의 실행 단위를 스레드라고 부른다.

스레드는 하나의 프로세스 내에서 동작하면서 자원을 공유한다.

## 1. 스레드 문법
    #include <ptread.h>

    int pthread_create(pthread_t *thread, const pthread_attr_t *attr, void *(*stat_routine)(void *), void *arg);
    // 새로운 스레드를 생성한다
    // thread : 스레드 식별자 번호
    // attr : 생성되는 스레드의 특성 지정, 기본은 NULL
    // stat_routine : 실제 스레드에서 실행될 스레드 함수
    // arg : 실행될 스레드 함수 stat_routine에 넘길 함수 인자

    pthread_t pthread_self(void);
    //해당 스레드의 스레드 번호를 리턴하는 함수

    int pthread_join(pthread_ th, void **thread_return);
    // 스레드의 종료를 기다려 스레드의 종료 값을 받아오고 스레드의 자원을 정리한다
    // th : join하고자 하는 스레드의 식별자
    // thread_return : 스레드의 리턴값

    int pthread_detach(pthread_t th);
    // main 스레드에서 pthread_create를 이용해 생성한 스레드를 분리
    //분리된 스레드는 종료할 때 pthread_join을 기다리지 않고 모든 자원이 즉시 해제된다

    void pthread_exit(void *retval);
    // 현재 실행중인 스레드를 종료한다

## 2. 스레드의 문제점
공유된 메모리를 사용하기 때문에 다른 스레드가 언제 끼어들어 어떤 값을 수정할 지 모르기 때문에 원하는 동작이 되지 않는다.

--------------------

<해결방법>

<li> 크리티컬 섹션 동기화 방식
: 어떤 값에 대한 사용이 끝나기 전까지는 그 값을 사용하려는 다른 스레드가 멈춰있게 함으로써 그 값의 신빙성을 유지한다.
<li> 그 외에도 이벤트, 세마포어, 뮤텍스 등을 이용한 동기화 방식들이 있다.

## 3. 스레드 컴파일 in C
    gcc -o thread_test thread_test.c -pthread

`-pthread`옵션이 꼭 있어야 함!!

## 4. 스레드 자원 공유 상태

<li> 스레드 간에 서로 공유하는 자원
- 작업디렉토리
- 파일지시자들
- 대부분의 전역변수와 데이타들
- UID 와 GID
- signal

<li>각각의 쓰레드가 고유하게 가지는 자원
- 에러번호(errno)
- 쓰레드 우선순위
- 스택
- 쓰레드 ID
- 레지스터 및 스택지시자

## 출처
<li>http://elky.tistory.com/197
<li>http://www.geeksforgeeks.org/multithreading-c-2/
<li>http://guswnsla1223.tistory.com/70
<li>https://www.joinc.co.kr/w/Site/Thread/Beginning/WhatThread
