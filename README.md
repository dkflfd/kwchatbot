# kwchatbot
## 광운대학교 산학연계SW프로젝트 

생생하조 한국어 챗봇 개발  


광운대학교 산학연계SW 팀 생생하조

2015722077 서나리

2015722078 김소희

## 시연 동영상
<https://www.youtube.com/watch?v=Omm55yvTkek&feature=youtu.be/>


## 설치
<pre><code>
pip install lexrankr
pip install pymysql
</code></pre>


## 사용법
1. chatbot.py 수정
<pre><code>
conn = pymysql.connect(host = 'localhost', user='root', passwd='', db='chatbot', charset='utf8')
</code></pre>
위의 passwd 부분에 **chatbot** database 의 비밀번호를 입력해 주어야 합니다.
2. testpjt 가 있는 폴더에서 cmd를 실행시키고 'python manage.py runserver'를 입력  
3. <http://127.0.0.1:8000/chatbot/> 에 접속  
4. 질문 입력창에 질문 입력  
5. 엔터 혹은 입력 버튼 클릭  
**github 에는 데이터베이스가 없으므로 동작이 되지 않습니다.**



## Web 화면
![html](https://user-images.githubusercontent.com/37467841/41412048-be117d80-7019-11e8-84d4-cc3bedfd8787.PNG)
