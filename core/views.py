from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from openpyxl import Workbook
from openpyxl.styles import Font
from .models import Player, Group
from .forms import PlayerForm, GroupForm

# View to list all players
def player_list(request):
    players = Player.objects.all()
    return render(request, 'core/player_list.html', {'players': players})

# View to display a single player's details
def player_detail(request, pk):
    player = get_object_or_404(Player, pk=pk)
    return render(request, 'core/player_detail.html', {'player': player})

# View to create a new player
def player_create(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Player created successfully!')
            return redirect('player_list')
        else:
            messages.error(request, 'Please correct the errors below.')
            print("Form errors:", form.errors)
    else:
        form = PlayerForm()
    return render(request, 'core/player_form.html', {'form': form, 'title': 'Create Player'})

# View to update an existing player
def player_update(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()
            messages.success(request, 'Player updated successfully!')
            return redirect('player_list')
        else:
            messages.error(request, 'Please correct the errors below.')
            print("Form errors:", form.errors)  # Optional: for debugging
    else:
        form = PlayerForm(instance=player)
    return render(request, 'core/player_form.html', {'form': form, 'title': 'Update Player'})

# View to delete a player
def player_delete(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == 'POST':
        player.delete()
        messages.success(request, 'Player deleted successfully!')
        return redirect('player_list')
    return render(request, 'core/player_confirm_delete.html', {'player': player})

# View to export players to Excel
def export_players_to_excel(request):
    players = Player.objects.all()

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = 'Players'

    headers = [
        'ID', 'Name', 'Profile Image', 'Email', 'Aadhar Number', 'Primary Contact Number',
        'Secondary Contact Number', 'Date of Birth', 'Gender', 'State', 'Role',
        'Batting Style', 'Bowling Style', 'Handedness', 'Sports Role', 'ID Card Number',
        'Medical Certificates', 'Guardian Name', 'Relation', 'Guardian Mobile Number'
    ]
    sheet.append(headers)

    # Make header row bold
    for cell in sheet[1]:
        cell.font = Font(bold=True)

    for player in players:
        sheet.append([
            player.id,
            player.name,
            player.image.url if player.image else 'N/A',
            player.email or 'N/A',
            player.aadhar_number or 'N/A',
            player.primary_contact_number or 'N/A',
            player.secondary_contact_number or 'N/A',
            player.date_of_birth or 'N/A',
            player.gender or 'N/A',
            player.state or 'N/A',
            player.role or 'N/A',
            player.batting_style or 'N/A',
            player.bowling_style or 'N/A',
            player.handedness or 'N/A',
            player.sports_role or 'N/A',
            player.id_card_number or 'N/A',
            player.medical_certificates.url if player.medical_certificates else 'N/A',
            player.guardian_name or 'N/A',
            player.relation or 'N/A',
            player.guardian_mobile_number or 'N/A'
        ])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=players.xlsx'
    workbook.save(response)

    return response



# --------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------



# View to manage player groups (create/update/delete groups)
def manage_groups(request):
    groups = Group.objects.all()
    players = Player.objects.all()

    if request.method == "POST":
        if 'create_group' in request.POST:
            group_form = GroupForm(request.POST)
            if group_form.is_valid():
                group_form.save()
                return redirect('manage_groups')
        elif 'update_group' in request.POST:
            group = get_object_or_404(Group, pk=request.POST.get('group_id'))
            group_form = GroupForm(request.POST, instance=group)
            if group_form.is_valid():
                group_form.save()
                return redirect('manage_groups')
        elif 'delete_group' in request.POST:
            group = get_object_or_404(Group, pk=request.POST.get('group_id'))
            group.delete()
            return redirect('manage_groups')
        elif 'add_player_to_group' in request.POST:
            group = get_object_or_404(Group, pk=request.POST.get('group_id'))
            player = get_object_or_404(Player, pk=request.POST.get('player_id'))
            player.groups.add(group)
            player.save()
            return redirect('manage_groups')
        elif 'remove_player_from_group' in request.POST:
            group = get_object_or_404(Group, pk=request.POST.get('group_id'))
            player = get_object_or_404(Player, pk=request.POST.get('player_id'))
            player.groups.remove(group)
            player.save()
            return redirect('manage_groups')
    else:
        group_form = GroupForm()

    context = {
        'groups': groups,
        'players': players,
        'group_form': group_form
    }
    return render(request, 'core/player_group_manage.html', context)
