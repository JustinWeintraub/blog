from django.shortcuts import render, redirect
#from User.models import Profile
from .models import ChatMessage
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.http import HttpResponse
from .forms import ChatMessageCreationForm as Creation

@login_required
def chatboard(request):
    template_name='chat/board.html'
    ordering=['-date_posted'] #newest to odlest
    messages = ChatMessage.objects.all()

    while(messages.count()>15):
        messages.first().delete()
    #messages.filter(id=i)
    if(request.method=="POST"):
        #form = Creation(request.POST,instance=request.user)
        form = Creation(request.POST)
        if form.is_valid():
            #print(form.author.id)
            form=form.save(commit=False)
            form.author=request.user
            form.save()
            #print(ChatMessage.objects.all())
            return redirect('chat-board')
    else:
        form = Creation()
        #i need a form and the objects
    return render(request, 'chat/board.html', {'form':form,'chatmessages':messages})
def log(request):
    results = ChatMessage.objects.all()
    for i in results:
        if(i.author.profile.online()==False):
            i.delete()
    returner=""
    for i in results:
        returner+=("<p>"+str(i.author)+": "+str(i.content)+"</p>")
    return HttpResponse(returner)
# Create your views here.
