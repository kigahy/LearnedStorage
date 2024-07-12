# SSAFY 부울경 1반 김가현 #
24/07/10~12 수업 내용 정리


### 목차 ###

1. Markdown 문법
2. CLI 문법
3. Git 개요
4. Git의 3가지 영역
5. Git 기초 문법
6. 파일을 GIT에 저장하기
7. vi편집기
8. Git에 Push하기
9. Git에 Pull & Clone 하기
10. Git 추적 예외 항목 만들기
11. 기타 Git 명령어
12. TIL로 성장하기


---
## markdown 문법 ##

vscode와 preview로 대조하여 확인할 것

- ### 제목 : #의 개수 많을수록 크기도 줄어듦 ###
 - `print` : 코드블럭
- 억음 뒤 프로그래밍 언어 입력하여 코드 작성하기
    ```python
    print("Hello World!")ㄴ
    ```
- [제목](링크) : 글자 클릭하면 링크로 연결
- ![제목](링크) : 이미지 추가, 크기 조정은 HTML 활용
- ![제목](./이미지명) : 로컬 폴더 안의 이미지 추가 가능
- 예시
    - [구글](https://google.com)
    - ![사진](https://fastly.picsum.photos/id/517/200/200.jpg?hmac=7n69zdD4qSZs14zMRZPUfLGKHFEIR9jTpoSEN1o990E)
- **굵은글씨**
- *기울임*
- ~~가운데 선~~
- shift + tab : 1수준 감소
- --- : 구분선
- <h3> HTML 제목 </h3> : 마크다운에서도 html 태그 활용 가능


---
## CLI 문법 ##

- `exit` : cmd창 닫기
- `pwd` : root 디렉토리~현재 디렉토리 경로 표시
- `.` : 현재 디렉토리
- `..` : 상위 디렉토리 (부모 폴더)
- desktop의 절대경로 : c:/Users/SSAFY/desktop으로 이동
- `touch` : 파일 생성 .txt .md 등
- `mkdir` : 디렉토리 생성
- `ls` : 디렉토리 내 파일 보기
    - `ls -a` : 숨겨진 파일도 보기
- `cd` : 디렉토리 이동하기


---
## Git 개요 ##

- 형상관리, 버전관리
- 분산 버전 관리 시스템
- 작업물을 로컬 저장소에 기록한 후, 중앙 서버와 동기화
- 개발자의 관리 순서
    1. 중앙 server는 최신 상태, 내 version 모름
    2. 중앙 server에서 최신 버전 내려받음
    3. 상대 작업자와 최신 버전으로 작업물 공유 가능


---
## Git의 4가지 영역 ##

- Working Directory(작업 공간) : 실제 작업 영역
- Staging Area(임시 저장 공간) : 작업 공간에서 변경된 파일 중, 다음 버전에 포함할 파일을 선택적으로 추가/제거하는 중간 준비 영역
- Repository(저장소) : 모든 버전, 변경 이력, 파일이 영구적으로 저장되는 영역
- **Working Directory**에서 `add`하면 **Staging Area**으로, **Staging Area**에서 `commit`하면 **Repository**로 이동하는 순서


---
## Git 문법 ##

- `git init` : 로컬 저장소 설정(초기화). 디렉토리를 git으로 버전관리 할 것을 선언
- `git add` : 변경사항 있는 파일을 SA 에 추가.
    - `git add a.txt` : 파일
    - `git add layer2_1` : 폴더
    - `git add a.txt, b.txt, layer2_1` : 여러개
    - `git add *.txt` : 확장자 설정
    - `git add .` : 모든 파일
- `git commit` : SA의 파일들을 저장소에 기록. 파라미터 -m 추가 가능
    - `git commit -m "로그인 기능 추가”` : 설명 추가
- `git status` : 디렉토리 내 파일의 상태 확인 가능
- `git rm —cached sample.txt` : **Staging Area**에서 **Working Directory**로 내림


---
## 파일을 Git에 저장하기 ##

준비물: Git Bash, VSCode

### Git Bash ###
1. 바탕화면 > 마우스 오른쪽 버튼 > git bash
2. `mkdir 디렉토리명` 디렉토리 생성
3. `touch 파일명` 파일 생성. 확장자는 `.txt` `.md` 가능
4. `code .` 다음 작업을 위해 vscode 실행

### VSCode ###
1. `git config --global user.email "in47821@gmail.com"` 이메일 설정값 저장
2. `git config --global user.name "kimgahyeonn"` 사용자 설정값 저장
    - `--global` 파라미터 : 시스템 전체에 설정값 저장
3. `git init` : git 저장소 초기화 및 디렉토리 내 .git 생성
4. 이때, vscode의 TERMINAL에서 디렉토리 옆이 (master) 로 변경되는 것을 반드시 확인
5. `git add 파일명` **Working Directory**을 **Staging Area**으로 불러옴
6. `git commit -m "커밋메시지"` **Staging Area**의 파일을 **Repository**로 이동함

### 중간 작업 ###
- `git log` : Repository에 쌓여 있는 commit history 보기
- `git log --online` : commit의 목록 한 줄 보기
- `git config --global -l` : 
- `rm -r .git` : (master)로 지정된 디렉토리의 git 제거 및 해제
- `git config --global -l` : 현재 저장된 파라미터 값 확인. 앞서 지정한 user.name 과 user.email 확인 가능 

### 추가 작업 ###
- `git log --oneline` : commit hash 값 확인하기, commit 내용 한줄로 간단히 보기
- `git commit --amdne` : 저장소에 올린 커밋 수정. 빠진 내용, 커밋 메시지 등


---
## vi 편집기 ##
- `i` : insert의 약자로, 내용 수정 추가 제거 등 작업 수행
- `:wq` : esc 후 변경사항 저장하고 종료
- `q!` : esc 후 변경사항 저장하지 않고 종료


---
## Git에 Push하기 ##

### 기본 문법 ###
- `push` : 로컬 pc에서 cloud의 저장소로 밀어냄
- `pull` : cloud에서 로컬 pc로 내려받음
- `clone` : 파일을 전부 내려받음
    - Remote Repository(원격 저장소)에서 Local pc로 가져옴
- fetch : 가져옴. 형상관리를 위하여 fetch, merge < `pull`로 둘 다 해결됨
- git revert & reset : 시스템 rollback

### 명령어 ###
- `git remote add origin <remote_repo_url>` : 로컬 저장소에 원격 저장소 추가
    - git은 `connect` 말고 `add` 사용
    - `origin`은 원격 저장소의 닉네임. 관행이지만 다른 이름 사용 가능
- `git remote -v` : 원격 저장소의 위치 알려줌
- `git push origin master` : 깃 레포지토리에 푸쉬함
    - `origin`은 닉네임, `master`은 local에서 하는 master branch의 내용
    - `origin`이라는 이름의 저장소에 `master`을 내보낸다는 뜻

### 순서 ###
- global > init > 파일 수정 > **add > commit > push**
1. `git add 파일명`
2. `git commit -m '커밋명'`
3. `git push origin master1`
- 2번 후 `git log --oneline`로 확인한 후, *head->master(로컬)* 의 브랜치, *origin/master(클라우드)* 브랜치의 저장 총 두 개
- 로컬 뿐만 아니라 원격 레포지토리 내에도 .git 디렉토리 존재


---
## Git에 Pull & Clone 하기 ##

- `git pull origin master` : 원격 저장소의 변경사항만 받아와서 저장. 로컬에 git 폴더가 이미 있을 때
- `git clone <remote_repo_url>` : 원격 저장소 전체를 복제(다운로드)
    - `clone` 통해 받은 프로젝트는 이미 `git init`이 되어 있음
    - `git init` 하기 전 디렉토리에 vscode에 (master) 있는지 확인
    - .git 안에 .git 존재하면 안 됨
    - url은 GitHub의 Repository에서 복사 가능


---
## Git 추적 예외 항목 만들기
- .gitignore (파일명 앞에 ‘.’ 입력, 확장자 없음
- `gitignore` : git에서 특정 파일이나 디렉토리를 추적하지 않도록 설정하는 데 사용하는 텍스트 파일
- `git init` 전에 만듦. 이후에 만들면 의미 없음
- `git status`
- 폴더 생성 후 vscode로 `.gitignore` 만들고 a.txt b.txt도 함께 만든 후, `.gitignore`에 a.txt 문구 추가한 후 `git init` 하면 a.txt는 추적하지 않음
- 만약 a.txt 추가하지 않고 `git.init`했다면 [Git ignore](https://www.toptal.com/developers/gitignore/) 에서 가져온 코드로 `.gitignore`에 추가


---
## 되돌리기 ##

### Git revert ###

- `git revert <commit id(해시값)>` : 재설정. 단일 commit을 실행 취소하는 것.  프로젝트 기록에서 commit을 없었던 일로 처리 후 그 결과를 새로운 commit으로 추가함
- 커밋 기록에서 삭제하거나 분리하는 대신, 지정된 변경 사항을 반전시키는 새 커밋을 생성
- git에서 기록이 손실되는 것을 방지하며 기록의 무결성과 협업의 신뢰성을 높임

### Git reset ###

- 되돌리기
- 특정 commit으로 되돌아갈 때, 되돌아간 commit 이후의 commit은 모두 삭제
- 옵션
    - --soft : 삭제된 커밋의 기록을 Staging Area에 남김
    - --mixed : 삭제된 커밋의 기록을 Working Directory에 남김 (기본 옵션 값)
    - --hard : 삭제된 commit의 기록을 남기지 않음
- `git reset --옵션 <해시값>`
- `git reflog` : hard option으로 지워진 커밋도 조회하여 복구 가능
- `git restore` : Modified 상태의 파일 되돌리기(파일 내용을 수정 전으로 되돌리기). Working directory 파일의 수정 사항을 취소하고, 원래 모습대로 되돌리는 작업

### Unstage ###
 - `git rm —cached` : Staging Area에서 Working Directory로 옮기기
- `git restore —straged` : Repository에 있는 것을 Working Directory로 돌리는 것


---
## 기타 Git 명령어 ##

- `mv -f first-repo git_advanced` : 디렉토리명 변경
- `git remote -v` : 현재 로컬 저장소에 등록된 원격 저장소 목록 보기
- `git remote rm 원격_저장소_이름` : 현재 로컬 저장소에 등록된 원격 저장소 삭제


---
## TIL로 성장하기 ##

- TIL(Today I Learned)을 통해 학습 기록
- Github로 포트폴리오 작성
- python 오픈소스 프로젝트에 기여함을 어필할 수 있음