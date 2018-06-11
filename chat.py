# -*- coding: utf-8 -*-
from __future__ import print_function
import pymysql
from kwchatbot import kwchatbot
import operator
import random
import time

#질문에 맞는 대답을 찾는 함수
# parameter 'st' = 사용자의 입력(질문)
def chat(question) :
    # 데이터베이스와 연결
    conn = pymysql.connect(host = 'localhost', user='root', passwd='', db='', charset='utf8')
    curs=conn.cursor()
    
    # 시작시간 측정
    startTime = time.time()
    
    # 데이터베이스로부터 모든 질문을 가져옴
    sql = "select text from question"
    curs.execute(sql)
    rows = curs.fetchall()
    
    # 사용자가 질문에 마침표나 물음표 등을 입력하지 않을 경우를 대비한 마침표 추가
    question += '.'
    
    # 데이터베이스로부터 읽어온 데이터(튜플)를 문자열로 변환
    for row in rows :
        stri = ''.join(row)
        question += ' ' + stri
    
    #kwchatbot.py 파일의 kwchatbot 객체 생성
    chatbot = kwchatbot()
    chatbot.summarize(question)   #chatbot class의 summarize함수 호출
    
    #dictionary 객체를 이용한 heap 생성
    heap = {0:0}
    
    #모든 sentence에 대해 반복
    for i in range(chatbot.num_sentences) :
        #만약 해당 sentence의 tf-idf 유사도 값이 0이면
        if(chatbot.matrix[i,0] == 0) :
            continue        #heap에 추가하지 않음
        heap[i] = chatbot.matrix[i,0]   #tf-idf값이 0이 아니면 heap에 추가 (key = sentence index, value = tf-dif 유사도)
    
    #만약 자기 자신을 제외하고 유사도가 모두 0인 경우
    if len(heap) < 2 :
        print("\t소요시간 : ", time.time() - startTime)
        return "무슨 말인지 모르겠어~" #모르겠다는 답변 반환

    #내림차순으로 sorting
    sorted_heap = sorted(heap.items(), key=operator.itemgetter(1), reverse=True) #sorted_heap : list 속에 tuple
    max_sim = sorted_heap[1]        #가장 높은 유사도 (sorted_heap[0] 은 자기자신(0번째 문장)에 대한 유사도값(1.0) -> 제외)
    question_index = max_sim[0]     #가장 유사도가 높은 문장의 question index값
        
    if(question_index == 0) :
        max_sim = sorted_heap[0]
        question_index = max_sim[0]
    if(max_sim[1] < 0.2) :
        print("\ttf-idf 값 : ", max_sim[1])
        print("\t소요시간 : ", time.time() - startTime)
        return "무슨 말인지 모르겠어~"
    
    print("\ttf-idf 값 : ", max_sim[1])
    
    print("\t질문 토큰 : ", chatbot.sentences[0].tokens)
    
    #가장 유사도가 높은 문장에 대한 answer index값을 얻어옴
    sql = "select a from qna where q = %d" %question_index
    curs.execute(sql)
    rows = curs.fetchall()
        
    #가장 유사도가 높은 질문에 해당하는 답변들 중에서 random으로 선택
    answer = random.choice(rows)
    
    #랜덤하게 얻은 answer index 에 해당하는 text를 database에서 가져옴
    sql = "select text from answer where seq=%d"%answer[0]
    curs.execute(sql)
    rows = curs.fetchall()
    #답변 추출
    answer = rows[0]
    #현재시간에서 시작시간을 빼서 소요시간 측정
    print("\t소요시간 : ", time.time() - startTime)
    
    #데이터베이스와 연결 종료
    conn.close()
    #답변 return아
    return answer[0]

if __name__ == '__main__' :
    user = input("질문 : ")
    print(chat(user))
    
