from django.shortcuts import render, redirect

from .models import Monster, Character

def select_participants(request):
    selected_participants = []
    monsters = Monster.objects.all()
    characters = Character.objects.all()

    if request.method == 'POST':
        participant_type = request.POST.get('participant_type')
        
        if participant_type == 'monstro':
            selected_participants = monsters
        elif participant_type == 'personagem':
            selected_participants = characters
    
    return render(request, 'tracker/select_participants.html', {
        'participants_list': selected_participants,
    })