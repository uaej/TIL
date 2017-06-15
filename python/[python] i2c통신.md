# [python] i2c통신
> 파이썬을 이용해서 i2c 통신하는 방법을 요약정리

## 1. smbus
<li> i2c통신을 위한 파이썬의 라이브러리이다.
<li> 설치하려면


    sudo apt-get update

    sudo apt-get install python3-smbus

## 2. ic2포트 초기화

    import smbus
    dev = smbus.SMBus(1)
괄호 안의 숫자는 ic2 포트 2개(0, 1) 중 1번을 선택한다는 의미다.

## 3. 함수들

    read_i2c_block_Data(addr, cmd [, length])
    write_i2c_block_data(addr, cmd, lst)


## 4. 출처
http://studymake.tistory.com/494
