from django.shortcuts import render, get_object_or_404, redirect
from .forms import PlayerForm
import openpyxl
from openpyxl.styles import Font
from django.http import HttpResponse
from .models import Player


def player_list(request):
    players = Player.objects.all()
    return render(request, 'core/player_list.html', {'players': players})

def player_detail(request, pk):
    player = get_object_or_404(Player, pk=pk)
    return render(request, 'core/player_detail.html', {'player': player})

def player_create(request):
    if request.method == "POST":
        print(request.FILES)
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            player = form.save()
            return redirect('player_detail', pk=player.pk)
        else:
            print(form.errors)
    else:
        form = PlayerForm()
    return render(request, 'core/player_form.html', {'form': form})


def player_update(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == "POST":
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            player = form.save()
            return redirect('player_detail', pk=player.pk)
    else:
        form = PlayerForm(instance=player)
    return render(request, 'core/player_form.html', {'form': form})

def player_delete(request, pk):
    player = get_object_or_404(Player, pk=pk)
    player.delete()
    return redirect('player_list')




def export_players_to_excel(request):
    players = Player.objects.all()

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'Players'

    headers = ['ID', 'Name', 'Profile Image', 'Email', 'Aadhar Number', 'Primary Contact Number',
               'Secondary Contact Number', 'Date of Birth', 'Gender', 'State', 'Role',
               'Batting Style', 'Bowling Style', 'Handedness', 'Sports Role', 'ID Card Number',
               'Medical Certificates', 'Guardian Name', 'Relation', 'Guardian Mobile Number']
    sheet.append(headers)

    for col in sheet.iter_cols(min_col=1, max_col=len(headers), min_row=1, max_row=1):
        for cell in col:
            cell.font = Font(bold=True)

    for player in players:
        sheet.append([
            player.id, player.name, player.image.url if player.image else '', player.email, player.aadhar_number,
            player.primary_contact_number, player.secondary_contact_number, player.date_of_birth, player.gender,
            player.state, player.role, player.batting_style, player.bowling_style, player.handedness, player.sports_role,
            player.id_card_number, player.medical_certificates.url if player.medical_certificates else '',
            player.guardian_name, player.relation, player.guardian_mobile_number
        ])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=players.xlsx'
    workbook.save(response)

    return response

