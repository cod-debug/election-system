from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.admin_votemaster.models import Election, Attendance, Nominee
from apps.admin_votemaster.forms import ElectionForm
from django.contrib.auth.models import User
from apps.admin_newstockholder.models import StockHolder
import datetime

# Create your views here.

def checkDate():
    datenow = datetime.date.today()
    Election.objects.filter(date_added=datenow).update(status='expired')

@login_required(login_url="")
def admin_votemaster(request):
    # checkDate()

    if request.method == 'POST':
        form = ElectionForm(request.POST)
        if form.is_valid(): #check if form is valid
            code = form['code'].value()
            desc = form['description'].value()
            target_date = form['target_date'].value()
            number_of_nominees = form['number_of_nominees'].value()
            number_of_winners = form['number_of_winners'].value()

            election_norepeat = Election.objects.filter(code=code) #Check if the election code is already used

            if election_norepeat:
                context = {'form': ElectionForm,
                   'election_list': Election.objects.all(),
                   'message': {'message': 'repeat'}
                   }

                return render(request, 'admin/content/admin_votemaster.html', context)
            else:
                election = Election.objects.create(
                    code=code,
                    description=desc,
                    target_date=target_date,
                    number_of_nominees=number_of_nominees,
                    number_of_winners=number_of_winners,
                    status="pending")

                context = {'form': ElectionForm,
                   'election_list': Election.objects.all(),
                   'message': {'message': 'success'}
                   }

                return redirect('admin_votemaster')
    else:
        form = ElectionForm()

    context = {'form': ElectionForm,
               'election_list': Election.objects.all().order_by('target_date'),
               'message': {'message': ''}
               }

    return render(request, 'admin/content/admin_votemaster.html', context)


@login_required(login_url="")
def admin_votemaster_attendance(request, id):
    stock_holder = StockHolder.objects.all()
    election = Election.objects.get(id=id)
    current_attendance = Attendance.objects.filter(election_code=election.code) #get current elections attendance record
    nominees = Nominee.objects.filter(election_code=election.code)


    if request.method == "POST":
        if request.POST.get("save_attendance"): # check if save button is clicked
            for item in stock_holder: # loop all the stakeholders
                if not request.POST.get('stock_holder' + str(item.id), None) == None:  #check if the checkbox in its corresponding stakehokder id is checked
                    if Attendance.objects.filter(sh_id=item.id, election_code=election.code):  #if this stakeholder has an attendance record for the current election, his/her status will just be updated as 'present'
                        Attendance.objects.filter(sh_id=item.id, election_code=election.code).update(at_status='present', sh_shares=item.sh_shares)
                    else:
<<<<<<< HEAD
                        attendance_record = Attendance(
                            sh_id=item.id,
                            election_code=election.code,
                            sh_fullname=item.sh_fname + " " + item.sh_lname,
                            at_status="present",
                            sh_email=item.sh_email,
                            sh_shares=item.sh_shares
                        )
=======
                        if item.sh_proxy_status == 'true':
                            attendance_record = Attendance(
                                sh_id=item.id,
                                election_code=election.code,
                                sh_fullname=item.sh_fname + " " + item.sh_lname,
                                at_status="present",
                                sh_email=item.sh_proxy_email,
                                sh_shares=item.sh_shares,
                                sh_classification = item.sh_classification,
                                sh_proxy_status = item.sh_proxy_status
                            )
                        else: 
                            attendance_record = Attendance(
                                sh_id=item.id,
                                election_code=election.code,
                                sh_fullname=item.sh_fname + " " + item.sh_lname,
                                at_status="present",
                                sh_email=item.sh_email,
                                sh_shares=item.sh_shares,
                                sh_classification = item.sh_classification,
                                sh_proxy_status = item.sh_proxy_status
                            )
>>>>>>> 66dd8f96c4f5249f531b2182bdd8f56c30c82d96

                        attendance_record.save() # save new attendance record to database with status "present"

                else: # codes in this section applies when the checkbox is unchecked
                    if Attendance.objects.filter(sh_id=item.id, election_code=election.code):  # if this stakeholder has an attendance record for the current election, his/her status will just be updated as 'absent'
                        Attendance.objects.filter(sh_id=item.id, election_code=election.code).update(at_status='absent', sh_shares=item.sh_shares)

                    else:  # will add new attendance record for this specific stakeholder with the status 'absent'
<<<<<<< HEAD
                        attendance_record = Attendance(
                            sh_id=item.id,
                            election_code=election.code,
                            sh_fullname=item.sh_fname + " " + item.sh_lname,
                            at_status="absent",
                            sh_email=item.sh_email,
                            sh_shares=item.sh_shares
                        )
=======
                        if item.sh_proxy_status == 'true':
                            attendance_record = Attendance(
                                sh_id=item.id,
                                election_code=election.code,
                                sh_fullname=item.sh_fname + " " + item.sh_lname,
                                at_status="absent",
                                sh_email=item.sh_proxy_email,
                                sh_shares=item.sh_shares,
                                sh_classification = item.sh_classification,
                                sh_proxy_status = item.sh_proxy_status
                            )
                        else: 
                            attendance_record = Attendance(
                                sh_id=item.id,
                                election_code=election.code,
                                sh_fullname=item.sh_fname + " " + item.sh_lname,
                                at_status="absent",
                                sh_email=item.sh_email,
                                sh_shares=item.sh_shares,
                                sh_classification = item.sh_classification,
                                sh_proxy_status = item.sh_proxy_status
                            )
>>>>>>> 66dd8f96c4f5249f531b2182bdd8f56c30c82d96
                        attendance_record.save() # save new attendance record to database with status "absent"
        else:
            print("invalid")

        election = Election.objects.get(id=id)
        current_attendance = Attendance.objects.filter(election_code=election.code) #get current elections attendance record
        nominees = Nominee.objects.filter(election_code=election.code)
        attendees = Attendance.objects.filter(election_code=election.code, at_status="present")

        total_shares = 0
        for at_present in attendees:
            total_shares = total_shares + int(at_present.sh_shares)

        context = {
            'form': ElectionForm,
            'stock_holder': stock_holder,
            'attendance': current_attendance,
            'election': election,
            'nominees': nominees,
            'count':  {
                'stock_holder_count': stock_holder.count(),
                'attendance_count': current_attendance.count(),
                'nominees_count': nominees.count(),
                'attendees_count': attendees.count(),
                'total_shares': total_shares
            }
        }# new database content

        return render(request, 'admin/content/admin_votemaster_attendance.html', context)

    attendees = Attendance.objects.filter(election_code=election.code, at_status="present")

    total_shares = 0
    for at_present in attendees:
        total_shares = total_shares + int(at_present.sh_shares)

    context = {
        'form': ElectionForm,
        'stock_holder': stock_holder,
        'attendance': current_attendance,
        'election': election,
        'nominees': nominees,
        'count':  {
            'stock_holder_count': stock_holder.count(),
            'attendance_count': current_attendance.count(),
            'nominees_count': nominees.count(),
            'attendees_count': attendees.count(),
            'total_shares': total_shares
        }
    }# new database content

    return render(request, 'admin/content/admin_votemaster_attendance.html', context)


@login_required(login_url="")
def admin_votemaster_nomination(request, id):
    stock_holder = StockHolder.objects.all()
    latest_election = Election.objects.get(id=id) #get latest election, meaning last created election or this day's election
    current_attendance = Attendance.objects.filter(election_code=latest_election.code) #get current elections attendance record
    nominees = Nominee.objects.filter(election_code=latest_election.code)

    attendees = Attendance.objects.filter(election_code=latest_election.code, at_status="present")

    total_shares = 0
    for at_present in attendees:
        total_shares = total_shares + int(at_present.sh_shares)

    context = {
        'form': ElectionForm,
        'stock_holder': stock_holder,
        'attendance': current_attendance,
        'nominees': nominees,
        'count':  {
            'stock_holder_count': stock_holder.count(),
            'attendance_count': current_attendance.count(),
            'nominees_count': nominees.count(),
            'attendees_count': attendees.count(),
            'total_shares': total_shares
        }
    }

    return render(request, 'admin/content/admin_votemaster_nomination.html', context)

@login_required(login_url="")
def admin_votemaster_add_nominee(request, sh_id, election_id):
    stock_holder = StockHolder.objects.all()
    latest_election = Election.objects.get(id=int(election_id)) #get latest election, meaning last created election or this day's election
    current_attendance = Attendance.objects.filter(election_code=latest_election.code) #get current elections attendance record
    selected_stockholder = StockHolder.objects.get(id=int(sh_id))
    nominees = Nominee.objects.filter(election_code=latest_election.code)
    message = {
        'message': ''
    }

    if not Nominee.objects.filter(sh_id=sh_id, election_code=latest_election.code):
        if not int(nominees.count()) >= int(latest_election.number_of_nominees):
            new_nominee = Nominee(
                sh_id=sh_id,
                election_code=latest_election.code,
                sh_fullname=selected_stockholder.sh_fname + " " + selected_stockholder.sh_lname,
            )
            new_nominee.save()
        else:
            message = {
                'message': 'limit'
            }

    nominees = Nominee.objects.filter(election_code=latest_election.code)
    latest_election = Election.objects.get(id=election_id) #get latest election, meaning last created election or this day's election
    current_attendance = Attendance.objects.filter(election_code=latest_election.code) #get current elections attendance record
    latest_election = Election.objects.get(id=election_id) #get latest election, meaning last created election or this day's election
    attendees = Attendance.objects.filter(election_code=latest_election.code, at_status="present")#get latest list of attendees in this election

    total_shares = 0
    for at_present in attendees:
        total_shares = total_shares + int(at_present.sh_shares)

    context = {
        'form': ElectionForm,
        'stock_holder': stock_holder,
        'attendance': current_attendance,
        'election': latest_election,
        'nominees': nominees,
        'message': message,
        'count':  {
            'stock_holder_count': stock_holder.count(),
            'attendance_count': current_attendance.count(),
            'nominees_count': nominees.count(),
            'attendees_count': attendees.count(),
            'total_shares': total_shares
        }
    }

    return render(request, 'admin/content/admin_votemaster_nomination.html', context)


# UPDATE ELECTION FUNCTION
def admin_votemaster_edit_election(request, id):
    message = {'update': ''}

    stock_holder = StockHolder.objects.all()
    election = Election.objects.get(id=id)
    current_attendance = Attendance.objects.filter(election_code=election.code) #get current elections attendance record
    nominees = Nominee.objects.filter(election_code=election.code)

    if request.method == 'POST':
        desc = request.POST.get('description')
        tdate = request.POST.get('target_date')
        code = request.POST.get('code')
        number_of_nominees = request.POST.get('number_of_nominees')
        number_of_winners = request.POST.get('number_of_winners')

        if desc and tdate and code:
            if not Election.objects.filter(code=code).exclude(id=id):
                if not int(nominees.count()) > int(number_of_nominees):
                    update_election = Election.objects.filter(id=id).update(
                        description=desc,
                        target_date=tdate,
                        code=code,
                        number_of_nominees=number_of_nominees,
                        number_of_winners=number_of_winners)

                    update_attendance = Attendance.objects.filter(election_code=election.code).update(election_code=code)
                    update_nominee = Nominee.objects.filter(election_code=election.code).update(election_code=code)
                    attendees = Attendance.objects.filter(election_code=election.code, at_status="present")

                    message = {'update': 'success'}
                else:
                    message = {'update': 'limit'}
            else:
                message = {'update': 'repeat'}

    election = Election.objects.get(id=id) #get updated election record
    current_attendance = Attendance.objects.filter(election_code=election.code) #get updated attendance record
    nominees = Nominee.objects.filter(election_code=election.code) #get updated nominee record
    attendees = Attendance.objects.filter(election_code=election.code, at_status="present")

    total_shares = 0
    for at_present in attendees:
        total_shares = total_shares + int(at_present.sh_shares)

    context = {
        'form': ElectionForm,
        'stock_holder': stock_holder,
        'attendance': current_attendance,
        'nominees': nominees,
        'election': election,
        'message': message,
        'count':  {
            'stock_holder_count': stock_holder.count(),
            'attendance_count': current_attendance.count(),
            'nominees_count': nominees.count(),
            'attendees_count': attendees.count(),
            'total_shares': total_shares
        }
    }


    return render(request, 'admin/content/admin_votemaster_edit_election.html', context)


# DELETE NOMINEE
@login_required(login_url="")
def admin_votemaster_remove_nominee(request, id, election_id):
    Nominee.objects.filter(id=id).delete()

    message = {'delete': ''}
    stock_holder = StockHolder.objects.all()
    election = Election.objects.get(id=election_id)
    current_attendance = Attendance.objects.filter(election_code=election.code) #get current elections attendance record
    nominees = Nominee.objects.filter(election_code=election.code)
    attendees = Attendance.objects.filter(election_code=election.code, at_status="present")

    total_shares = 0
    for at_present in attendees:
        total_shares = total_shares + int(at_present.sh_shares)


    context = {
        'form': ElectionForm,
        'stock_holder': stock_holder,
        'attendance': current_attendance,
        'nominees': nominees,
        'election': election,
        'message': message,
        'count':  {
            'stock_holder_count': stock_holder.count(),
            'attendance_count': current_attendance.count(),
            'nominees_count': nominees.count(),
            'attendees_count': attendees.count(),
            'total_shares': total_shares
        }
    }

    return render(request, 'admin/content/admin_votemaster_nomination.html', context)

@login_required(login_url="")
def admin_votemaster_delete_election(request, id):
    Election.objects.filter(id=id).delete()
    return redirect('admin_votemaster')