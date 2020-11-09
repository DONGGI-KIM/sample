ybygbygbygbyg

$ git status
git init #시작
git remote add origin 주소 # github 저장소주소를 붙이면 연동됨
# 파일 local에서 만들기
# ctrl s 꼭하기
git add . # 살펴보기
git commit -m "바뀐내용" # 추가로 적을내용 적는다.
git push origin master #github 업로드
git branch # 현재 가지가 어디인지 확인한다.
git branch 명칭 # 새로운branch 만든다.
git checkout donggi # branch 이동한다.
git branch # 다시 확인하면 새로 만든 branch로 이동한걸 볼 수 있다.
# 파일을 다시 만든다. 그럼 branch 로 저장된다.
git add . # 바뀐걸 확인한다.
git commit -m "바뀐 내용을 적는다" # github가면 바뀐거 이름 적어준다.
#ctrl s 를해서 저장하는것을 잊지말자.
git push origin donggi # github로 연동할것이다.
