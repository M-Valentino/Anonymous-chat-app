from django.shortcuts import render, redirect
import random, string
import json

def index(request):
    return render(request, 'chat/index.html')

def lobby(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if len(name) > 16:
            return render(request, '403.html')
        
        lobby_code = request.POST.get('lobbycode')

        with open("chat/private/lobbies.json") as f:
            lobbies = json.load(f)

        lobby = next((l for l in lobbies if l['code'] == lobby_code), None)
        if lobby:
            if lobby['remaining_members'] > 0:
                lobby['remaining_members'] -= 1
                with open("chat/private/lobbies.json", "w") as file:
                    json.dump(lobbies, file)
                return render(request, 'chat/lobby.html', {'user_name': name, 'lobbycode': lobby_code, 'room_name': lobby['name'], 'max_num_members': lobby['max_num_members']})
            else:
                return render(request, 'chat/index.html', {'message': 'That lobby is full.'})
        else:
            return render(request, 'chat/index.html', {'message': 'Lobby does not exist. Please check your lobby code.'})

    # If user tries to visit /lobby/ without joinging a chat
    return redirect('/')


def create_lobby(request):
    if request.method == 'POST':
        lobby_name = request.POST.get('lobby_name')
        numMembers = int(request.POST.get('max_num_members'))

        if len(lobby_name) > 16:
            return render(request, '403.html')
        
        with open("chat/private/lobbies.json") as f:
            lobbies = json.load(f)

        while True:
            lobby_code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
            if not any(lobby['code'] == lobby_code for lobby in lobbies):
                break

        lobbies.append({'code': lobby_code, 'name': lobby_name, 'max_num_members': numMembers, 'remaining_members': numMembers})
        with open("chat/private/lobbies.json", "w") as file:
            json.dump(lobbies, file)
        
        return render(request, 'chat/create_lobby.html', {'lobby_code': lobby_code})
    
    return render(request, 'chat/create_lobby.html')
