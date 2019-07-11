from django.shortcuts import render, redirect
#from User.models import Profile
from .models import ChatMessage
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .forms import ChatMessageCreationForm as Creation

@login_required
def chatboard(request):
    template_name='chat/board.html'
    ordering=['-date_posted'] #newest to odlest
    messages = ChatMessage.objects.all()
    if(request.method=="POST"):
        print("we are postin")
        #form = Creation(request.POST,instance=request.user)
        form = Creation(request.POST)
        if form.is_valid():
            #form.author=request.user
            #print(form.author.id)
            #print(form.author.id)
            #form.author.id = request.user.id
            form=form.save(commit=False)
            form.author=request.user
            form.save()
            print(ChatMessage.objects.all())
            return redirect('chat-board')
    else:
        form = Creation()
        #i need a form and the objects
    return render(request, 'chat/board.html', {'form':form,'chatmessages':messages})
# Create your views here.
