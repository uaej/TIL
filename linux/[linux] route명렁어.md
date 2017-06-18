# [linux] route
> 리눅스 man페이지 해석이나 다름없음 :-)

## 0. 라우팅 테이블이란?

route 명령이 수행되었을 때 보여주는 테이블으로, 컴퓨터 네트워크에서 목적지 주소를 목적지에 도달하기 위한 네트워크 노선으로 변환시키는 목적으로 사용된다.

라우팅 테이블 때문에 hop-by-hop라우팅 방식이 가능하다.


## 1. route 명령어
<li> 라우팅 테이블을 확인하거나 수정할 수 있다.
<li> 활성화되어 있는 네트워크 인터페이스를 통해 정적 라우트를 설정할 수 있다.

## 2. route옵션
<li> -F

 디폴트 값.

<li> -C

routing cache를 표시한다.

<li> -v

자세한 동작을 선택한다.

<li> -n

호스트의 이름을 표시하는 대신 숫자로 된 주소를 표시하는 옵션.네임 서버 경로가 사라진 이유를 확인하려는 경우 유용하다.

<li> -e

라우팅 테이블을 표시할 때 netstat표맷을 사용하여 표시한다.

<li> del

route를 삭제한다.

<li> add

새 route를 추가한다.

<li> target

목적지 네트워크나 host.
점으로 구분된 ip 주소나 host/network 이름을 줄 수 있다.

<li> -net

타겟이 네트워크라고 설정

<li> -host

타겟이 호스트라고 설정

<li> netmask NM

네트워크 route를 추가할 때, netmask가 필요하다.

<li> gw GW

route 패킷은 게이트웨이를 경유한다.

## 3. examples

<li> route add -net 127.0.0.1

테이블에 평범한 루프백 엔트리(자기 자신을 가리키는 것)를 추가한다.
넷마스크는 A클래스를 사용하므로 255.0.0.0을 사용

<li> route add -net 192.56.76.0 netmask 255.255.255.0 dev eth0

"eth0"를 통해 네트워크 192.56.76.x에 대한 경로를 추가한다.
하지만 192이므로 netmask가 필요하지는 않다.


## 4. 출처
<li>http://allinfo.tistory.com/375
<li> 리눅스 man 페이지
<li>https://ko.wikipedia.org/wiki/%EB%9D%BC%EC%9A%B0%ED%8C%85_%ED%85%8C%EC%9D%B4%EB%B8%94
