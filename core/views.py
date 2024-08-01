from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from openpyxl import Workbook
from openpyxl.styles import Font
from .models import Player, Group
from .forms import PlayerForm, GroupForm
from django.http import JsonResponse
import pandas as pd
from .forms import UploadFileForm


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
# def player_delete(request, pk):
#     player = get_object_or_404(Player, pk=pk)
#     if request.method == 'POST':
#         player.delete()
#         messages.success(request, 'Player deleted successfully!')
#         return redirect('player_list')
#     return render(request, 'core/player_confirm_delete.html', {'player': player})

def player_delete(request, pk):
    player = get_object_or_404(Player, pk=pk)
    player.delete()
    messages.success(request, 'Player deleted successfully!')
    return redirect('player_list')



# View to export players to Excel
def export_players_to_excel(request):
    players = Player.objects.all()

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = 'Players'

    headers = [
        'name', 'aadhar number', 'batting style', 'bowling style', 'date of birth', 'email', 'gender',
        'guardian mobile number', 'guardian name', 'handedness', 'id card number', 'profile image',
        'medical certificates', 'primary contact number', 'relation', 'role', 'secondary contact number',
        'sports role', 'state', 'address', 'district', 'pincode', 'aadhar card upload', 'marksheets upload',
        'pan card upload', 'additional information', 'age category', 'allergies', 'disease', 'height',
        'nationality', 'position', 'team', 'weight'
    ]
    sheet.append(headers)

    # Make header row bold
    for cell in sheet[1]:
        cell.font = Font(bold=True)

    for player in players:
        sheet.append([
            player.name,
            player.aadhar_number,
            player.batting_style,
            player.bowling_style,
            player.date_of_birth,
            player.email,
            player.gender,
            player.guardian_mobile_number,
            player.guardian_name,
            player.handedness,
            player.id_card_number,
            player.image.url if player.image else 'N/A',
            player.medical_certificates.url if player.medical_certificates else 'N/A',
            player.primary_contact_number,
            player.relation,
            player.role,
            player.secondary_contact_number,
            player.sports_role,
            player.state,
            player.address,
            player.district,
            player.pincode,
            player.aadhar_card_upload.url if player.aadhar_card_upload else 'N/A',
            player.marksheets_upload.url if player.marksheets_upload else 'N/A',
            player.pan_card_upload.url if player.pan_card_upload else 'N/A',
            player.additional_information,
            player.age_category,
            player.allergies,
            player.disease,
            player.height,
            player.nationality,
            player.position,
            player.team,
            player.weight
        ])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=players.xlsx'
    workbook.save(response)

    return response


def download_blank_excel(request):
    # Get the model fields
    fields = Player._meta.get_fields()

    # Extract field names, replace spaces with underscores, and ensure they are in lowercase
    headers = [
        field.name.replace(' ', '_').lower()
        for field in fields
        if field.name != 'id' and not field.many_to_one and not field.one_to_many
    ]

    # Create a new Workbook and select the active worksheet
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = 'Players'

    # Append the headers to the sheet
    sheet.append(headers)

    # Make header row bold
    for cell in sheet[1]:
        cell.font = Font(bold=True)

    # Create the HTTP response
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=blank_players.xlsx'
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
    group_form = GroupForm()

    if request.method == "POST":
        if 'create_group' in request.POST:
            group_form = GroupForm(request.POST)
            if group_form.is_valid():
                group = group_form.save()
                player_ids = request.POST.getlist('group_players')
                for player_id in player_ids:
                    player = Player.objects.get(pk=player_id)
                    player.groups.add(group)
                return redirect('manage_groups')
        elif 'update_group' in request.POST:
            group_id = request.POST.get('group_id')
            print(f"Updating group with id: {group_id}")  # Debug statement
            group = get_object_or_404(Group, pk=group_id)
            group_form = GroupForm(request.POST, instance=group)
            if group_form.is_valid():
                group_form.save()
                player_ids = request.POST.getlist('group_players')
                group.player_set.set(player_ids)  # Update the group with new players
                return redirect('manage_groups')
        elif 'delete_group' in request.POST:
            group_id = request.POST.get('group_id')
            print(f"Deleting group with id: {group_id}")  # Debug statement
            group = get_object_or_404(Group, pk=group_id)
            group.delete()
            return redirect('manage_groups')
        elif 'add_player_to_group' in request.POST:
            group_id = request.POST.get('group_id')
            player_id = request.POST.get('player_id')
            print(f"Adding player {player_id} to group {group_id}")  # Debug statement
            group = get_object_or_404(Group, pk=group_id)
            player = get_object_or_404(Player, pk=player_id)
            player.groups.add(group)
            player.save()
            return redirect('manage_groups')
        elif 'remove_player_from_group' in request.POST:
            group_id = request.POST.get('group_id')
            player_id = request.POST.get('player_id')
            print(f"Removing player {player_id} from group {group_id}")  # Debug statement
            group = get_object_or_404(Group, pk=group_id)
            player = get_object_or_404(Player, pk=player_id)
            player.groups.remove(group)
            player.save()
            return redirect('manage_groups')

    context = {
        'groups': groups,
        'players': players,
        'group_form': group_form
    }
    return render(request, 'core/player_group_manage.html', context)

def delete_group(request, group_id):
    print(f"Delete group function called for group id: {group_id}")  # Debug statement
    group = get_object_or_404(Group, pk=group_id)
    group.delete()
    return redirect('manage_groups')

def get_group_players(request):
    group_id = request.GET.get('group_id')
    group = get_object_or_404(Group, pk=group_id)
    players = group.player_set.all().values('pk', 'name', 'image')
    return JsonResponse({'players': list(players)})


import logging
logger = logging.getLogger(__name__)

def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES["file"]
            df = pd.read_excel(excel_file)

            # Debugging: Print column names and first few rows
            logger.info(f"DataFrame columns: {df.columns}")
            logger.info(f"DataFrame head: \n{df.head()}")

            for _, row in df.iterrows():
                try:
                    Player.objects.create(
                        name=row.get('name', ''),
                        email=row.get('email', ''),
                        primary_contact_number=row.get('primary_contact_number', ''),
                        secondary_contact_number=row.get('secondary_contact_number', ''),
                        date_of_birth=row.get('date_of_birth', None),
                        pincode=row.get('pincode', ''),
                        address=row.get('address', ''),
                        nationality=row.get('nationality', ''),
                        gender=row.get('gender', ''),
                        state=row.get('state', ''),
                        district=row.get('district', ''),
                        role=row.get('role', ''),
                        batting_style=row.get('batting_style', ''),
                        bowling_style=row.get('bowling_style', ''),
                        handedness=row.get('handedness', ''),
                        aadhar_number=row.get('aadhar_number', ''),
                        sports_role=row.get('sports_role', ''),
                        id_card_number=row.get('id_card_number', ''),
                        weight=float(row.get('weight', 0)) if pd.notna(row.get('weight', '')) else None,
                        height=float(row.get('height', 0)) if pd.notna(row.get('height', '')) else None,
                        age_category=row.get('age_category', ''),
                        team=row.get('team', ''),
                        position=row.get('position', ''),
                        guardian_name=row.get('guardian_name', ''),
                        relation=row.get('relation', ''),
                        guardian_mobile_number=row.get('guardian_mobile_number', ''),
                        disease=row.get('disease', ''),
                        allergies=row.get('allergies', ''),
                        additional_information=row.get('additional_information', ''),
                        image=row.get('image') if 'image' in row and pd.notna(row['image']) else None,
                        medical_certificates=row.get(
                            'medical_certificates') if 'medical_certificates' in row and pd.notna(
                            row['medical_certificates']) else None,
                        aadhar_card_upload=row.get('aadhar_card_upload') if 'aadhar_card_upload' in row and pd.notna(
                            row['aadhar_card_upload']) else None,
                        pan_card_upload=row.get('pan_card_upload') if 'pan_card_upload' in row and pd.notna(
                            row['pan_card_upload']) else None,
                        marksheets_upload=row.get('marksheets_upload') if 'marksheets_upload' in row and pd.notna(
                            row['marksheets_upload']) else None
                    )
                except ValueError as e:
                    logger.error(f"ValueError: {e} for row: {row}")
                except Exception as e:
                    logger.error(f"Exception: {e} for row: {row}")

            return redirect("player_list")
        else:
            logger.error("Form is invalid")
    else:
        form = UploadFileForm()
    return render(request, "player_list.html", {"form": form})
