from django.shortcuts import render, redirect

from .models import Monster, Character, Battle


def select_participants(request):
    logged_in_username = request.user.username

    monsters = Monster.objects.all()
    characters = Character.objects.all()

    battle = Battle.objects
    battle.create(created_by=logged_in_username)

    displayed_options = []

    filtered_battle = battle.filter(created_by=logged_in_username)
    ordered_battle = filtered_battle.order_by("created_at")
    this_battle = ordered_battle.first()

    if request.method == 'POST':

        participant_type_options = request.POST.get('participant_type')
        item_to_add = request.POST.get('added_option')

        if item_to_add:

            if item_to_add in monsters.values():
                this_battle.participant_monsters = item_to_add
            else:
                this_battle.participant_characters = item_to_add
     
        if participant_type_options == 'monstro':
            displayed_options = monsters
        elif participant_type_options == 'personagem':
            displayed_options = characters


    context = {
        'displayed_options': displayed_options,
        'participant_characters': this_battle.participant_characters,
        'participant_monsters': this_battle.participant_monsters,
    }

    return render(request, 'tracker/select_participants.html', context=context)