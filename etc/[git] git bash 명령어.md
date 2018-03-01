# [git] git bash 명령어

## 1. 새로운 저장소 만들기(init)
    git init

## 2. 저장소 복제하기(clone)
    # local repository copy
    git clone /local/repository/path
    # remote repository copy
    git clone 사용자명@호스트:/원격/저장소/경로

## 3. 파일 추가(add)
    git add *
    git add <파일이름>

## 4. 확정(commit)
    git commit -m "commit message"


## 5. 변경내용 발행(push)

    git push origin master(혹은 branch이름)s

    git remote add origin <원격 서버 주소>
    =>기존의 원격 서버를 복사한 것이 아닐때
--------------------
## 6. commit 목록 확인
git log --branches --not --remotes
git status

## 출처
<li> https://rogerdudler.github.io/git-guide/index.ko.html
<li> https://blog.outsider.ne.kr/820
