# [node.js] date-utils에서 timezone설정 변경하는 방법

## 1. 원래 사용할 때

    var date = new Date();
    var d = date.toISOString();
    console.log(d);

결과는 현재 시각보다 9시간 적게 출력된다.
이유는 timezone이 항상 UTC-0로 설정되어 있기 때문이다.

##2. timezone 반영하기

    var timezoneOffset = new Date().getTimezoneOffset() * 60000;
    var timezoneDate = new Date(Date.now() - timezoneOffset);
    var d = timezoneDate.toISOString();


## 출처
<li>http://bloodguy.tistory.com/entry/JavaScript-DatetoISOString-timezone-offset-%EB%B0%98%EC%98%81
