print("hello python!")
#git add . = 내가 가진 파일을 git 으로 관리한다
print("This is Version 2")
print("This is Version 3")

# git init : 깃을 사용하기위한 명령어, 처음 한번만 실행하면됨
# git : 코드를 버전관리하는 도구, 세이브 파일과 비슷한 역할
# git add . : 변경된 파일을 세이브할 수 있도록 stage를 올려주는 명령어
# git commit -m "메세지" : 변경된 파일을 세이브하는 명령어, -m에는 저장 메세지를 적는다.
# git restore . : 파일을 잘못 작성했을 때 되돌린다.(주의 전부 다 되돌아간다.)
# git push origin mian : 로컬에 저장한 세이브 내용을 원격 저장소 (깃허브)로 전달
# git log :세이브 저장 내역을 확인하는 명령어