from datetime import datetime

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.db import connection
import json
from django.http import JsonResponse


# Create your views here.
from Gym_diet_plan_App.models import *


def login(request):
    return render(request, "login_index.html")


def logout(request):
    auth.logout(request)
    return render(request, "login_index.html")


def login_action(request):
    username = request.POST['Username']
    password = request.POST['Password']
    login_obj = Login.objects.get(Username=username, Password=password)
    if login_obj.Type == "admin":
        auth_obj = auth.authenticate(username="admin", password="admin")
        if auth_obj is not None:
            auth.login(request, auth_obj)
        return redirect("admin_home")
    elif login_obj.Type == "trainer":
        auth_obj = auth.authenticate(username="admin", password="admin")
        if auth_obj is not None:
            auth.login(request, auth_obj)
        request.session['trainer_id'] = login_obj.id
        return redirect("trainer_home")


@login_required(login_url='/')
def admin_home(request):
    return render(request, "admin/admin_index.html")


@login_required(login_url='/')
def trainer_home(request):
    return render(request, "expert/expert_index.html")


@login_required(login_url='/')
def approve_diet_expert_view(request):
    trainer_obj = Trainer.objects.all()
    return render(request, "admin/approve_diet_expert.html", {'trainer_obj': trainer_obj})


@login_required(login_url='/')
def approve_diet_expert_view_search(request):
    search = request.POST["search"]
    trainer_obj = Trainer.objects.filter(FirstName__istartswith=search)
    return render(request, "admin/approve_diet_expert.html", {'trainer_obj': trainer_obj, 'Search': search})


@login_required(login_url='/')
def accept_trainer(request, trainer_id):
    trainer_obj = Trainer.objects.get(id=trainer_id)
    login_obj = Login.objects.get(id=trainer_obj.LOGIN_ID.id)
    login_obj.Type = "trainer"
    login_obj.save()
    return HttpResponse('''<script>alert("Accepted successfully");
    window.location="/ "</script>''')


@login_required(login_url='/')
def reject_trainer(request, trainer_id):
    trainer_obj = Trainer.objects.get(id=trainer_id)
    login_obj = Login.objects.get(id=trainer_obj.LOGIN_ID.id)
    login_obj.Type = "rejected"
    login_obj.save()
    return HttpResponse('''<script>alert("Rejected successfully");
    window.location="/approve_diet_expert_view#about"</script>''')


@login_required(login_url='/')
def manage_food(request):
    food_obj = Food.objects.all()
    return render(request, "admin/manage_food.html", {'food_obj': food_obj})


@login_required(login_url='/')
def manage_food_search(request):
    food = request.POST['Search']
    food_obj = Food.objects.filter(FoodName__istartswith=food)
    return render(request, "admin/manage_food.html", {'food_obj': food_obj, 'food': food})


@login_required(login_url='/')
def add_new_food(request):
    return render(request, "admin/add_new_food.html")


@login_required(login_url='/')
def add_new_food_action(request):
    food_name = request.POST['Food_name']
    food_type = request.POST['Food_Type']
    time = request.POST['Time']
    quantity = request.POST['Quantity']
    food_obj = Food()
    food_obj.FoodName = food_name
    food_obj.FoodType = food_type
    food_obj.Time = time
    food_obj.Quantity = quantity
    food_obj.save()
    return HttpResponse('''<script>alert("add food successfully");
    window.location="/manage_food#about"</script>''')


@login_required(login_url='/')
def update_food(request, food_id):
    food_obj = Food.objects.get(id=food_id)
    request.session['food_id'] = food_id
    return render(request, "admin/update_food.html", {'food_obj': food_obj})


@login_required(login_url='/')
def update_food_action(request):
    food_obj = Food.objects.get(id=request.session['food_id'])
    food_name = request.POST['Food_name']
    food_type = request.POST['Food_Type']
    time = request.POST['Time']
    quantity = request.POST['Quantity']
    food_obj.FoodName = food_name
    food_obj.FoodType = food_type
    food_obj.Time = time
    food_obj.Quantity = quantity
    food_obj.save()
    return HttpResponse('''<script>alert("Update food successfully");
        window.location="/manage_food#about"</script>''')


@login_required(login_url='/')
def delete_food(request, food_id):
    food_obj = Food.objects.get(id=food_id)
    food_obj.delete()
    return HttpResponse('''<script>alert("Delete food successfully");
            window.location="/manage_food#about"</script>''')


@login_required(login_url='/')
def manage_exercise(request):
    exercise_obj = Exercise.objects.all()
    return render(request, "admin/manage_exercise.html", {'exercise_obj': exercise_obj})


@login_required(login_url='/')
def manage_exercise_search(request):
    search = request.POST['search_exercise']
    exercise_obj = Exercise.objects.filter(ExerciseName__istartswith=search)
    return render(request, "admin/manage_exercise.html", {'exercise_obj': exercise_obj, 'search': search})


@login_required(login_url='/')
def add_new_exercise(request):
    return render(request, "admin/add_new_exercise.html")


@login_required(login_url='/')
def add_new_exercise_action(request):
    exercise_name = request.POST['Exercise_name']
    exercise_type = request.POST['Exercise_type']
    details = request.POST['Details']
    video = request.FILES['Video']
    exercise_obj = Exercise()
    exercise_obj.ExerciseName = exercise_name
    exercise_obj.ExerciseType = exercise_type
    exercise_obj.ExerciseDetails = details
    exercise_obj.ExerciseVideo = video
    exercise_obj.save()
    return HttpResponse('''<script>alert("add exercise successfully");
        window.location="/manage_exercise#about"</script>''')


@login_required(login_url='/')
def update_exercise(request, exercise_id):
    request.session['exercise_id'] = exercise_id
    exercise_obj = Exercise.objects.get(id=exercise_id)
    return render(request, "admin/update_exercise.html", {'exercise_obj': exercise_obj})


@login_required(login_url='/')
def update_exercise_action(request):
    exercise_name = request.POST['Exercise_name']
    exercise_type = request.POST['Exercise_type']
    details = request.POST['Details']
    video = request.FILES['Video']
    exercise_obj = Exercise.objects.get(id=request.session['exercise_id'])
    exercise_obj.ExerciseName = exercise_name
    exercise_obj.ExerciseType = exercise_type
    exercise_obj.ExerciseDetails = details
    exercise_obj.ExerciseVideo = video
    exercise_obj.save()
    return HttpResponse('''<script>alert("updated exercise successfully");
            window.location="/manage_exercise#about"</script>''')


@login_required(login_url='/')
def delete_exercise(request, exercise_id):
    exercise_obj = Exercise.objects.get(id=exercise_id)
    exercise_obj.delete()
    return HttpResponse('''<script>alert("Delete exercise successfully");
                window.location="/manage_exercise#about"</script>''')


@login_required(login_url='/')
def view_feedback(request):
    obj = Feedback.objects.all()
    return render(request, "admin/view_feedback.html", {'f_obj': obj})


@login_required(login_url='/')
def view_feedback_search(request):
    username = request.POST['username']
    obj = Feedback.objects.filter(USER_ID__FirstName__istartswith=username)
    return render(request, "admin/view_feedback.html", {'f_obj': obj, 'username': username})


@login_required(login_url='/')
def view_feedback_expert(request):
    obj = Feedback.objects.all()
    return render(request, "expert/view_feedback_expert.html", {'f_obj': obj})


@login_required(login_url='/')
def view_feedback_expert_search(request):
    username = request.POST['username']
    obj = Feedback.objects.filter(USER_ID__FirstName__istartswith=username)
    return render(request, "expert/view_feedback_expert.html", {'f_obj': obj, 'username': username})


@login_required(login_url='/')
def assign_expert_to_user(request):
    assign_obj = Assign.objects.all()
    lis = []
    for i in assign_obj:
        lis.append(i.USER_ID.id)
    user_obj = User.objects.exclude(id__in=lis)
    return render(request, "admin/assign_expert_to_user.html", {'user_obj': user_obj})


@login_required(login_url='/')
def assign_expert_to_user_search(request):
    username = request.POST['user']
    user_obj = User.objects.filter(FirstName__istartswith=username)
    return render(request, "admin/assign_expert_to_user.html", {'user_obj': user_obj, 'username': username})


@login_required(login_url='/')
def assign_trainer(request, user_id):
    request.session['user_id'] = user_id
    trainer_obj = Trainer.objects.all()
    return render(request, "admin/assign_trainer.html", {'trainer_obj': trainer_obj})


@login_required(login_url='/')
def assign_trainer_search(request):
    search = request.POST['trainer_name']
    trainer_obj = Trainer.objects.filter(FirstName__istartswith=search)
    return render(request, "admin/assign_trainer.html", {'trainer_obj': trainer_obj, 'search': search})


@login_required(login_url='/')
def assign_trainer_action(request, trainer_id):
    assign_obj = Assign()
    assign_obj.Date = datetime.now().strftime("%d-%m-%y")
    assign_obj.Status = "pending"
    assign_obj.TRAINER_ID = Trainer.objects.get(id=trainer_id)
    assign_obj.USER_ID = User.objects.get(id=request.session['user_id'])
    assign_obj.save()
    return HttpResponse('''<script>alert("user assigned successfully");
                window.location="/assign_expert_to_user#about"</script>''')


@login_required(login_url='/')
def view_complaint_send_reply(request):
    complaint_obj = Complaints.objects.all()
    return render(request, "admin/view_complaint_send_reply.html", {'complaint_obj': complaint_obj})


@login_required(login_url='/')
def view_complaint_send_reply_search(request):
    username = request.POST['user']
    complaint_obj = Complaints.objects.filter(USER_ID__FirstName__istartswith=username)
    return render(request, "admin/view_complaint_send_reply.html",
                  {'complaint_obj': complaint_obj, 'username': username})


@login_required(login_url='/')
def complaint_reply(request, complaint_id):
    request.session['complaint_id'] = complaint_id
    return render(request, "admin/complaint_reply.html")


@login_required(login_url='/')
def complaint_reply_action(request):
    reply = request.POST['reply']
    complaint_obj = Complaints.objects.get(id=request.session['complaint_id'])
    complaint_obj.Reply = reply
    complaint_obj.save()
    return HttpResponse('''<script>alert("Replied successfully");
                window.location="/view_complaint_send_reply#about"</script>''')


@login_required(login_url='/')
def manage_attendance_trainer(request):
    trainer_obj = Trainer.objects.filter(LOGIN_ID__Type='trainer')
    return render(request, "admin/manage_attendance_trainer.html", {'trainer_obj': trainer_obj})


@login_required(login_url='/')
def mark_attendance(request):
    trainer_obj = Trainer.objects.filter(LOGIN_ID__Type='trainer')
    att = request.POST.getlist('checkbox')
    date = request.POST['textfield']
    for i in trainer_obj:
        if str(i.id) in att:
            ob = Attendance()
            ob.LOGIN_ID = Login.objects.get(id=i.LOGIN_ID.id)
            ob.Attendance = "1"
            ob.Date = date
            ob.save()
        else:
            ob = Attendance()
            ob.LOGIN_ID = Login.objects.get(id=i.LOGIN_ID.id)
            ob.Attendance = "0"
            ob.Date = date
            ob.save()
    return HttpResponse('''<script>alert("Replied successfully");
                window.location="/admin_home#hero"</script>''')


@login_required(login_url='/')
def manage_attendance_trainer_search(request):
    date = request.POST['Search']
    trainer_obj = Attendance.objects.filter(Date=date, LOGIN_ID__Type='trainer')
    return render(request, "admin/manage_attendance_trainer.html", {'trainer_obj': trainer_obj})


@login_required(login_url='/')
def view_assigned_users(request):
    assigned_obj = Assign.objects.filter(TRAINER_ID__LOGIN_ID__id=request.session['trainer_id'])
    return render(request, "expert/view_assigned_users.html", {'assigned_obj': assigned_obj})


@login_required(login_url='/')
def view_assigned_users_search(request):
    username = request.POST['user']
    assigned_obj = Assign.objects.filter(TRAINER_ID__LOGIN_ID__id=request.session['trainer_id'],
                                         USER_ID__FirstName__istartswith=username)
    return render(request, "expert/view_assigned_users.html", {'assigned_obj': assigned_obj})


@login_required(login_url='/')
def add_and_manage_video(request):
    video_obj = Videos.objects.filter(TRAINER_ID__LOGIN_ID=request.session['trainer_id'])
    return render(request, "expert/add_and_manage_video.html", {'video_obj': video_obj})


@login_required(login_url='/')
def add_and_manage_video_search(request):
    search_video = request.POST['video']
    video_obj = Videos.objects.filter(TRAINER_ID__LOGIN_ID=request.session['trainer_id'],
                                      Title__istartswith=search_video)
    return render(request, "expert/add_and_manage_video.html", {'video_obj': video_obj, 'search_video': search_video})


@login_required(login_url='/')
def add_new_video(request):
    return render(request, "expert/add_new_video.html")


@login_required(login_url='/')
def add_new_video_action(request):
    video_file = request.FILES['Video']
    title = request.POST['Title']
    description = request.POST['Description']
    video_obj = Videos()
    video_obj.Video = video_file
    video_obj.Title = title
    video_obj.Description = description
    video_obj.Date = datetime.now().strftime("%d-%m-%y")
    video_obj.TRAINER_ID = Trainer.objects.get(LOGIN_ID=request.session['trainer_id'])
    video_obj.save()
    return HttpResponse('''<script>alert("video added successfully");
                window.location="/add_and_manage_video#about"</script>''')


@login_required(login_url='/')
def update_video(request, video_id):
    request.session['video_id'] = video_id
    video_obj = Videos.objects.get(id=video_id)
    return render(request, "expert/update_video.html", {'video_obj': video_obj})


@login_required(login_url='/')
def update_video_action(request):
    video_file = request.FILES['Video']
    title = request.POST['Title']
    description = request.POST['Description']
    video_obj = Videos.objects.get(id=request.session['video_id'])
    video_obj.Video = video_file
    video_obj.Title = title
    video_obj.Description = description
    video_obj.Date = datetime.now().strftime("%d-%m-%y")
    video_obj.TRAINER_ID = Trainer.objects.get(LOGIN_ID=request.session['trainer_id'])
    video_obj.save()
    return HttpResponse('''<script>alert("video updated successfully");
                    window.location="/add_and_manage_video#about"</script>''')


@login_required(login_url='/')
def delete_video(request, video_id):
    video_obj = Videos.objects.get(id=video_id)
    video_obj.delete()
    return HttpResponse('''<script>alert("video deleted successfully");
                    window.location="/add_and_manage_video#about"</script>''')


@login_required(login_url='/')
def add_manage_tips(request):
    tips_obj = Tips.objects.filter(TRAINER_ID__LOGIN_ID=request.session['trainer_id'])
    return render(request, "expert/add_manage_tips.html", {'tips_obj': tips_obj})


@login_required(login_url='/')
def add_manage_tips_search(request):
    search_tip = request.POST['tips']
    tips_obj = Tips.objects.filter(TRAINER_ID__LOGIN_ID=request.session['trainer_id'], Tip__istartswith=search_tip)
    return render(request, "expert/add_manage_tips.html", {'tips_obj': tips_obj, 'search_tip': search_tip})


@login_required(login_url='/')
def add_new_tips(request):
    return render(request, "expert/add_new_tips.html")


@login_required(login_url='/')
def add_new_tips_action(request):
    tips = request.POST['Tips']
    tips_obj = Tips()
    tips_obj.Tip = tips
    tips_obj.Date = datetime.now().strftime("%d-%m-%y")
    tips_obj.TRAINER_ID = Trainer.objects.get(LOGIN_ID__id=request.session['trainer_id'])
    tips_obj.save()
    return HttpResponse('''<script>alert("Tips added successfully");
                    window.location="/add_manage_tips#about"</script>''')


@login_required(login_url='/')
def update_tip(request, tip_id):
    request.session['tip_id'] = tip_id
    tip_obj = Tips.objects.get(id=tip_id)
    return render(request, "expert/update_tips.html", {'tip_obj': tip_obj})


@login_required(login_url='/')
def update_tips_action(request):
    tips = request.POST['Tips']
    tips_obj = Tips.objects.get(id=request.session['tip_id'])
    tips_obj.Tip = tips
    tips_obj.Date = datetime.now().strftime("%d-%m-%y")
    tips_obj.TRAINER_ID = Trainer.objects.get(LOGIN_ID__id=request.session['trainer_id'])
    tips_obj.save()
    return HttpResponse('''<script>alert("Tips updated successfully");
                           window.location="/add_manage_tips#about"</script>''')


@login_required(login_url='/')
def delete_tip(request, tip_id):
    tip_obj = Tips.objects.get(id=tip_id)
    tip_obj.delete()
    return HttpResponse('''<script>alert("Tips deleted successfully");
                        window.location="/add_manage_tips#about"</script>''')


@login_required(login_url='/')
def trainer_register(request):
    return render(request, "registration_upload_index.html")


@login_required(login_url='/')
def registration_action(request):
    first_name = request.POST['First_name']
    last_name = request.POST['Last_name']
    experience = request.POST['Experience']
    age = request.POST['Age']
    gender = request.POST['Gender']
    place = request.POST['Place']
    post = request.POST['Post']
    pin = request.POST['Pin']
    phone = request.POST['Phone']
    email = request.POST['Email']
    photo = request.FILES['Photo']
    fss = FileSystemStorage()
    photo_file = fss.save(photo.name, photo)
    username = request.POST['Username']
    password = request.POST['Password']

    login_obj = Login()
    login_obj.Username = username
    login_obj.Password = password
    login_obj.Type = 'pending'
    login_obj.save()

    trainer_obj = Trainer()
    trainer_obj.FirstName = first_name
    trainer_obj.LastName = last_name
    trainer_obj.Experience = experience
    trainer_obj.Age = age
    trainer_obj.Gender = gender
    trainer_obj.Place = place
    trainer_obj.Post = post
    trainer_obj.Pin = pin
    trainer_obj.Phone = phone
    trainer_obj.Email = email
    trainer_obj.Photo = photo_file
    trainer_obj.LOGIN_ID = login_obj
    trainer_obj.save()

    return HttpResponse('''<script>alert("registration completed successfully");
                        window.location="/"</script>''')


@login_required(login_url='/')
def search_user_progress(request):
    user_obj = Assign.objects.filter(TRAINER_ID=request.session['trainer_id'])
    return render(request, "expert/search_user_progress.html", {'user_obj': user_obj})


@login_required(login_url='/')
def view_user_progress_level(request):
    user_name = request.POST['select']
    user_obj = Progress.objects.filter(USER_ID__FirstName__icontains=user_name)
    return render(request, "expert/view_user_progress_level.html", {'user_obj': user_obj})


@login_required(login_url='/')
def view_diet_chart(request):
    chart_obj = DietChart.objects.filter(TRAINER_ID__LOGIN_ID=request.session['trainer_id'])
    return render(request, "expert/view_diet_chart.html", {'chart_obj': chart_obj})


@login_required(login_url='/')
def view_diet_chart_search(request):
    username = request.POST['user']
    chart_obj = DietChart.objects.filter(TRAINER_ID__LOGIN_ID=request.session['trainer_id'],
                                         USER_ID__FirstName__istartswith=username)
    return render(request, "expert/view_diet_chart.html", {'chart_obj': chart_obj, 'username': username})


@login_required(login_url='/')
def add_manage_attendance(request):
    user_obj = Assign.objects.filter(TRAINER_ID__LOGIN_ID=request.session['trainer_id'])
    return render(request, "expert/add_manage_attendance.html", {'user_obj': user_obj})


def add_attendance_action(request):
    attendance = request.POST.getlist('checkbox')
    date = request.POST['textfield']

    user_obj = Assign.objects.filter(TRAINER_ID__LOGIN_ID=request.session['trainer_id'])
    for i in user_obj:
        if str(i.USER_ID.id) in attendance:
            attendance_obj = Attendance()
            attendance_obj.LOGIN_ID = Login.objects.get(id=i.USER_ID.id)
            attendance_obj.Attendance = '1'
            attendance_obj.Date = date
            attendance_obj.save()
        else:
            attendance_obj = Attendance()
            attendance_obj.LOGIN_ID = Login.objects.get(id=i.USER_ID.id)
            attendance_obj.Attendance = '0'
            attendance_obj.Date = date
            attendance_obj.save()
    return HttpResponse('''<script>alert("Replied successfully");
                    window.location="/trainer_home#hero"</script>''')


def search_user_attendance(request):
    user_obj = Assign.objects.filter(TRAINER_ID__LOGIN_ID=request.session['trainer_id'])
    return render(request, "expert/search_user_attendance.html", {'user_obj': user_obj})


def view_attendance_user(request):
    user_id = request.POST['select']
    user_obj = User.objects.get(id=user_id)
    attendance_obj = Attendance.objects.filter(LOGIN_ID__id=user_obj.id)

    return render(request, "expert/view_attendance.html", {'attendance_obj': attendance_obj})

# //////////////////////////////  webservice  /////////////////////////////////


def login_code(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        users = Login.objects.get(Username=username, Password=password)
        if users is None:
            data = {"task": "invalid"}
        else:
            request.session['user_id'] = users.id
            data = {"task": "valid", "id": users.id}
            r = json.dumps(data)
            return HttpResponse(r)
    except:
        data = {"task": "invalid"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)


def user_registration(request):
    first_name = request.POST['Firstname']
    last_name = request.POST['Lastname']
    age = request.POST['Age']
    gender = request.POST['Gender']
    height = request.POST['Height']
    weight = request.POST['Weight']
    place = request.POST['Place']
    post_office = request.POST['Post']
    pin_code = request.POST['Pin']
    phone = request.POST['Phone']
    email_id = request.POST['Email']
    photo = request.FILES['proof']
    fss = FileSystemStorage()
    photo_file = fss.save(photo.name, photo)
    username = request.POST['Username']
    password = request.POST['Password']

    lob = Login()
    lob.Username = username
    lob.Password = password
    lob.Type = 'user'
    lob.save()

    user_obj = User()
    user_obj.FirstName = first_name
    user_obj.LastName = last_name
    user_obj.Place = place
    user_obj.Post = post_office
    user_obj.Pin = pin_code
    user_obj.Phone = phone
    user_obj.Email = email_id
    user_obj.Photo = photo_file
    user_obj.Age = age
    user_obj.Gender = gender
    user_obj.Height = height
    user_obj.Weight = weight
    user_obj.LOGIN_ID = lob
    user_obj.save()
    data = {"task": "success"}
    r = json.dumps(data)
    return HttpResponse(r)


def view_progress(request):
    login_id = request.POST['lid']
    prog_obj = Progress.objects.filter(USER_ID__LOGIN_ID=login_id)
    prog_data = []
    for i in prog_obj:
        data = {'Date': i.Date, 'Weight': i.Weight, 'Height': i.Height, 'user_id': i.id}
        prog_data.append(data)
    r = json.dumps(prog_data)
    return HttpResponse(r)


def send_feedback(request):
    feedback = request.POST["Feedback"]
    u_id = request.POST["lid"]
    feedback_obj = Feedback()
    feedback_obj.FeedbackUser = feedback
    feedback_obj.Date = datetime.now().strftime("%d/%m/%y")
    feedback_obj.USER_ID = User.objects.get(LOGIN_ID=u_id)
    feedback_obj.save()
    data = {'task': 'success'}
    r = json.dumps(data)
    return HttpResponse(r)


def send_complaint(request):
    complaints = request.POST["complaint"]
    u_id = request.POST["lid"]

    reply1 = "waiting"
    complaint_obj = Complaints()
    complaint_obj.Complaint = complaints
    complaint_obj.Date = datetime.now().strftime("%d/%m/%y")
    complaint_obj.Reply = reply1
    complaint_obj.USER_ID = User.objects.get(LOGIN_ID=u_id)
    complaint_obj.save()
    data = {'task': 'success'}
    r = json.dumps(data)
    return HttpResponse(r)


def view_complaint_reply(request):
    user_id = request.POST['lid']
    complaint_obj = Complaints.objects.filter(USER_ID__LOGIN_ID=user_id)
    data = []
    for i in complaint_obj:
        row = {'Complaint': i.Complaint, 'Reply': i.Reply, 'Date': str(i.Date)}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)


def view_tips(request):
    prog_obj = Tips.objects.all()
    prog_data = []
    for i in prog_obj:
        data = {'Tips': i.Tip, 'Date': i.Date, 'Trainer': i.TRAINER_ID.FirstName + " " + i.TRAINER_ID.LastName}
        prog_data.append(data)
    r = json.dumps(prog_data)
    return HttpResponse(r)


def view_attendance(request):
    login_id = request.POST['lid']
    user_obj = User.objects.get(LOGIN_ID_id=login_id)
    prog_obj = Attendance.objects.filter(LOGIN_ID=user_obj.id)
    prog_data = []
    for i in prog_obj:
        if i.Attendance == "1":
            att = "present"
        elif i.Attendance == "0":
            att = "absent"

        data = {'Date': i.Date, 'Attendance': att}
        prog_data.append(data)
    r = json.dumps(prog_data)
    return HttpResponse(r)


def view_video(request):
    video_obj = Videos.objects.all()
    video_data = []
    for i in video_obj:
        data = {'Title': i.Title, 'Description': i.Description, 'Video': str(i.Video.url)}
        video_data.append(data)
    print(video_data)
    r = json.dumps(video_data)
    return HttpResponse(r)


def view_exercise_video(request):
    video_obj = Exercise.objects.all()
    video_data = []
    for i in video_obj:
        data = {'ExerciseName': i.ExerciseName, 'Description': i.ExerciseType, 'ExerciseDetails': i.ExerciseDetails,
                'Video': str(i.ExerciseVideo.url)}
        video_data.append(data)
    print(video_data)
    r = json.dumps(video_data)
    return HttpResponse(r)






