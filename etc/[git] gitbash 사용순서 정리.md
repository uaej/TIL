# [git] git bash에서 push할때 단계
> git bash를 사용하고 있으면서도 각 단계가 정확히 뭘 의미하는지, 어떻게 사용해야 하는건지 잘 모르고 사용해서 혼란스러웠던 부분을 정리하려 한다.


## 1. git push 단계
- `git add [filename]`
- `git commit -m "commit message"`
- `git push origin master`

## 1. git add [filename]
  - add 명령어 : git local 저장소에 해당 파일을 저장한다
  - \*를 사용하면 해당 폴더에서 수정된 모든 사항을 저장한다.
  - -i 옵션으로 파일 1개를 저장할 때마다 대화식으로 저장할 수 있다.

## 2. git commit -m "commit message"
 - 변경사항을 확정한다. 여기서부터는 되돌릴 수 없다.
 - "commit message"에서는 이번에 수정된 사항에 대해 간단한 설명을 추가할 수 있다.

## 3. git push origin master
 - push는 로컬 repository에 저장된 것을 원격 repository에 복사하는 것을 말한다.
 - **origin** 은 원격 저장소에서 로컬 저장소로 clone해서 데이터를 받아온 경우 로컬에서 원격 저장소의 이름이 자동으로 origin으로 등록되어 있다, 즉 origin은 원격 저장소를 이용해 관리할때 사용하는 단어이다.
 - **master** 는 원격 repository의 여러 branch중에 master branch에 해당 변경사항을 push 하겠다는 의미를 말한다.
 만일 다른 branch에 push하고 싶을 경우 master위치에 해당 branch의 이름을 쓰면 된다.

## 참고
- https://blog.outsider.ne.kr/866
- https://rogerdudler.github.io/git-guide/index.ko.html
