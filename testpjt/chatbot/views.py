from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse

from .forms import PostForm
from .models import Qna

import sys
sys.path.insert(0, r'..')
import original
from original import LexRank
import chat

# Create your views here.

def chatbot(request):
    return render(request, "chatbot/testChatbot.html", {})

def post(request):
    msg = ''
    if request.POST:
        msg = request.POST['question']
        answer = chat.chat(msg)

        return render(request, 'chatbot/response.html', {'question': msg , 'answer': answer})