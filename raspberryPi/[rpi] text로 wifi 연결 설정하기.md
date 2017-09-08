# text로 wifi 연결 설정하는 방법
> 휴대폰이나 컴퓨터, 혹은 rpi에 모니터를 연결했을 때는 gui환경에서 와이파이를 잡고 비밀번호를 사용할 수 있지만, ssh 접속을 했을 경우에는 텍스트로 설정을 해 주어야 한다

# 1. 설정할 위치
    cd /etc/wpa-supplicant/wpa-supplicant.conf

# 2. 설정하는 방법
    <li> wpa-psk 암호화 방식일때 - 일반적인 wifi 암호화 방식인 듯 하다
        network={
            ssid="networkName"
            key_mgmt=WPA-PSK
        }
key_mgmt는 해당 네트워크의 암호화 방식에 따라 달라질 수 있다.
라즈베리파이의 gui를 이용하여 네트워크에 연결할 시 자동으로 해당 사항을 이 파일에 써준다.
이 정보는 ssh를 이용할 때 wifi 접속에 편리하다
