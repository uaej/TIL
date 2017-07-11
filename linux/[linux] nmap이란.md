# nmap이란?

## 0. nmap이란?
network mapper의 약자로, 컴퓨터와 서비스를 찾을 때 쓰인다.

## 1. nmap의 기능
<li> 호스트 탐지 : 네트워크 상의 컴퓨터들을 확인한다. 예를 들어 ping 응답이나 특정 포트가 열린 컴퓨터들을 나열한다.
<li> 포트 스캔 : 하나 혹은 그 이상의 대상 컴퓨터들에 열린 포트들을 나열한다.
<li> 버전 탐지 : 응용 프로그램의 이름과 버전 번호를 확인하기 위해 원격 컴퓨터의 네트워크 서비스에 주의를 기울인다.
<li> 운영 체제 탐지 : 원격으로 운영 체제와 네트워크 장치의 하드웨어 특성을 확인한다.

## 2. 옵션
<li>sT	일반적인 TCP 포트스캐닝.
<li>-sS	이른바 'half-open' 스캔으로 추적이 어렵다.
<li>-sP	ping 을 이용한 일반적인 스캔.
<li>-sU	UDP 포트 스캐닝.
<li>-PO	대상 호스트에 대한 ping 응답을 요청하지 않음 .
<li>log 기록과 filtering 을 피할 수 있다.
<li>-PT	일반적이 ICMP ping이 아닌 ACK 패킷으로 ping 을 보내고
RST 패킷으로 응답을 받는다.
<li>-PI	일반적인 ICMP ping 으로 방화벽이나 필터링에 의해 걸러진다.
<li>-PB	ping 을 할 때 ICMP ping 과 TCP ping을 동시에 이용한다.
<li>-PS	ping 을 할 때 ACK 패킷대신 SYN 패킷을 보내 스캔.
<li>-O	대상 호스트의 OS 판별.
<li>-p	대상 호스트의 특정 포트를 스캔하거나, 스캔할 포트의 범위를 지정.
ex) -p 1-1024
<li>-D	Decoy 기능으로 대상 호스트에게 스캔을 실행한 호스트의 주소를 속인다.
<li>-F	/etc/services 파일 내에 기술된 포트만 스캔.
<li>-I	TCP 프로세서의 identd 정보를 가져온다.
<li>-n	IP 주소를 DNS 호스트명으로 바꾸지 않는다. 속도가 빠르다.
<li>-R	IP 주소를 DNS 호스트명으로 바꿔서 스캔. 속도가 느리다.
<li>-o	스캔 결과를 택스트 파일로 저장.
<li>-i	스캔 대상 호스트의 정보를 지정한 파일에서 읽어서 스캔.
<li>-h	도움말 보기

## 3.
크래커의 해킹에 사용되거나, 컴퓨터 시스템에 허가받지 않은 접근 시도를 할 수 있다.
주로 열린 포트를 찾아 공격할 때 사용된다.

## 출처
<li>https://ko.wikipedia.org/wiki/Nmap
<li>http://coffeenix.net/doc/security/nmap.html
