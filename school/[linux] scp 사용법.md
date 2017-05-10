# 다른 서버로 복사 (보내기)
    scp 파일 계정@서버주소:목적경로
    scp test.txt testuser@135.79.246.80:/home/testuser/

→ test.txt를 135.79.246.80 서버의 /home/testuser/ 폴더에 업로드

# 다른 서버에서 복사 (가져오기)
## 기본 포트 사용
    scp 계정@서버주소:원본경로 목적파일명
## 다른 포트 사용
    scp -P 포트 계정@서버주소:원본경로 목적파일명
# 폴더 복사
    scp -r 계정@서버주소:원본경로 목적상위폴더
    scp -r testuser@135.79.246.81:/var/www/html/ /var/www/
