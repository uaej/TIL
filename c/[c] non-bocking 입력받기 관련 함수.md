# non-blocking 관련 함수

## 1. tcgetattr(int fd, struct termios *termios_p)
> 헤더 : termios.h, unistd.h

<li> fd와 연관된 터미널 디바이스의 속성을 시험하는데 사용.(fd를 사용하기 위해 속성을 받기 위해 사용)
<li> termios_p에 속성이 반환
<li> 리턴값 : 성공 - 0, 실패 - -1
<li> errno :
 - EBADF : fd 인수가 유용한 파일 표
 - ENOTTY : fd 가 터미널과 연관이표주 없다.

<li> STDIN_FILENO : 표준 입력으로, 프로그램으로 들어가는 문자열 스트림이다. <unistd.h>에서 정의이고, 다른 헤더에서는 다르게 지정되어 있다.

## 2. tcsetattr(int fd, int optional_actions, const struct termios * termios_p)
> 헤더 : termios.h, unistd.h

<li> fd와 연관된 터미널 디바이스의 속성을 설정한다. 속성은 termios_p로부터 가져온다.
<li> optional_actions : 큐에 저장되어 있는 입력과 출력을 어떻게 취급할 것인지 지정
<li> optional_actions에 들어갈 수 있는 값 :
 - TSSANOW : 즉시 속성 변겅
 - TSARDRAIN : 큐에 출력이 쓰여질 때까지 기다린 후에 속성 변경
 - TCSAFLUSH : =TCSADRAIN, 큐의 입력 버림

## 3. fcntl(int fd, int cmd, long arg);
> 헤더 : unistd.h, fcntl.h

<li> 이미 열려있는 파일의 특성 제어를 위해 사용된다.
<li> cmd에 들어가는 명령어 :
 - F_DUPFD : 파일 지정자 복사
 - F_GETFD : fd에 대한 flag 값을 넘겨줌
 - F_GETFL : fd에 대한 플래그 값(open호출시 지정한 플래그) 를 돌려준다.
 - F_SETFL : fd의 플래그를 재 설정한다. 현재는 O_APPEND, O_NONBLOCK, O_ASYNC만을 설정할 수 있다.
 - 기타 다른 플래그

## 4. termios - struct
> 헤더 : termios.h


    struct termios {
      tcflag_t c_iflag;   //input modes
      tcflag_t c_oflag;   //output modes
      tcflag_t c_cflag;   //control modes
      tcflag_t c_lflag;   //local modes
      cc_t c_cc[NCCS];  //special characters
      speed_t c_ispeed;
      speed_t c_ospeed;
    };

## 5. getchar()
> 헤더 : stdio.h

<li> 표준 입력 함수
<li> 공백으로 입력처리
<li> 엔터가 입력될 때 까지 키보드 버퍼에 입력값 저장
