from django.contrib import admin
from django.urls import path

from Gym_diet_plan_App import views

urlpatterns = [
    path('', views.login, name="login"),
    path('login_action', views.login_action, name="login_action"),
    path('admin_home', views.admin_home, name="admin_home"),
    path('trainer_home', views.trainer_home, name="trainer_home"),
    path('approve_diet_expert_view', views.approve_diet_expert_view, name="approve_diet_expert_view"),
    path('approve_diet_expert_view_search', views.approve_diet_expert_view_search, name="approve_diet_expert_view_search"),
    path('accept_trainer/<int:trainer_id>', views.accept_trainer, name="accept_trainer"),
    path('reject_trainer/<int:trainer_id>', views.reject_trainer, name="reject_trainer"),
    path('manage_food', views.manage_food, name="manage_food"),
    path('add_new_food', views.add_new_food, name="add_new_food"),
    path('add_new_food_action', views.add_new_food_action, name="add_new_food_action"),
    path('update_food/<int:food_id>', views.update_food, name="update_food"),
    path('update_food_action', views.update_food_action, name="update_food_action"),
    path('delete_food/<int:food_id>', views.delete_food, name="delete_food"),
    path('manage_exercise', views.manage_exercise, name="manage_exercise"),
    path('manage_exercise_search', views.manage_exercise_search, name="manage_exercise_search"),
    path('add_new_exercise', views.add_new_exercise, name="add_new_exercise"),
    path('add_new_exercise_action', views.add_new_exercise_action, name="add_new_exercise_action"),
    path('update_exercise/<int:exercise_id>', views.update_exercise, name="update_exercise"),
    path('update_exercise_action', views.update_exercise_action, name="update_exercise_action"),
    path('delete_exercise/<int:exercise_id>', views.delete_exercise, name="delete_exercise"),
    path('view_feedback', views.view_feedback, name="view_feedback"),
    path('view_feedback_search', views.view_feedback_search, name="view_feedback_search"),
    path('assign_expert_to_user', views.assign_expert_to_user, name="assign_expert_to_user"),
    path('assign_expert_to_user_search', views.assign_expert_to_user_search, name="assign_expert_to_user_search"),
    path('assign_trainer/<int:user_id>', views.assign_trainer, name="assign_trainer"),
    path('assign_trainer_action/<int:trainer_id>', views.assign_trainer_action, name="assign_trainer_action"),
    path('view_complaint_send_reply', views.view_complaint_send_reply, name="view_complaint_send_reply"),
    path('view_complaint_send_reply_search', views.view_complaint_send_reply_search, name="view_complaint_send_reply_search"),
    path('complaint_reply/<int:complaint_id>', views.complaint_reply, name="complaint_reply"),
    path('complaint_reply_action', views.complaint_reply_action, name="complaint_reply_action"),
    path('manage_attendance_trainer', views.manage_attendance_trainer, name="manage_attendance_trainer"),
    path('manage_attendance_trainer_search', views.manage_attendance_trainer_search, name="manage_attendance_trainer_search"),
    path('mark_attendance', views.mark_attendance, name="mark_attendance"),
    path('manage_food_search', views.manage_food_search, name="manage_food_search"),
    path('assign_trainer_search', views.assign_trainer_search, name="assign_trainer_search"),
    path('logout', views.logout, name="logout"),

    # ////////////////////////////////// Trainer ///////////////////////////////////////////

    path('trainer_register', views.trainer_register, name="trainer_register"),
    path('registration_action', views.registration_action, name="registration_action"),
    path('view_assigned_users', views.view_assigned_users, name="view_assigned_users"),
    path('view_assigned_users_search', views.view_assigned_users_search, name="view_assigned_users_search"),
    path('add_and_manage_video', views.add_and_manage_video, name="add_and_manage_video"),
    path('add_and_manage_video_search', views.add_and_manage_video_search, name="add_and_manage_video_search"),
    path('add_new_video', views.add_new_video, name="add_new_video"),
    path('add_new_video_action', views.add_new_video_action, name="add_new_video_action"),
    path('update_video/<int:video_id>', views.update_video, name="update_video"),
    path('update_video_action', views.update_video_action, name="update_video_action"),
    path('delete_video/<int:video_id>', views.delete_video, name="delete_video"),
    path('add_manage_tips', views.add_manage_tips, name="add_manage_tips"),
    path('add_manage_tips_search', views.add_manage_tips_search, name="add_manage_tips_search"),
    path('add_new_tips', views.add_new_tips, name="add_new_tips"),
    path('add_new_tips_action', views.add_new_tips_action, name="add_new_tips_action"),
    path('update_tip/<int:tip_id>', views.update_tip, name="update_tip"),
    path('update_tips_action', views.update_tips_action, name="update_tips_action"),
    path('delete_tip/<int:tip_id>', views.delete_tip, name="delete_tip"),
    path('search_user_progress', views.search_user_progress, name="search_user_progress"),
    path('view_user_progress_level', views.view_user_progress_level, name="view_user_progress_level"),
    path('view_diet_chart', views.view_diet_chart, name="view_diet_chart"),
    path('view_diet_chart_search', views.view_diet_chart_search, name="view_diet_chart_search"),
    path('add_manage_attendance', views.add_manage_attendance, name="add_manage_attendance"),
    path('add_attendance_action', views.add_attendance_action, name="add_attendance_action"),
    path('search_user_attendance', views.search_user_attendance, name="search_user_attendance"),
    path('view_attendance_user', views.view_attendance_user, name="view_attendance_user"),
    path('view_feedback_expert', views.view_feedback_expert, name="view_feedback_expert"),
    path('view_feedback_expert_search', views.view_feedback_expert_search, name="view_feedback_expert_search"),

    #  /////////////////////////////  web service  ///////////////////////////////////

    path('login_code', views.login_code, name="login_code"),
    path('user_registration', views.user_registration, name="user_registration"),
    path('view_progress', views.view_progress, name="view_progress"),
    path('send_feedback', views.send_feedback, name="send_feedback"),
    path('send_complaint', views.send_complaint, name="send_complaint"),
    path('view_complaint_reply', views.view_complaint_reply, name="view_complaint_reply"),
    path('view_tips', views.view_tips, name="view_tips"),
    path('view_attendance', views.view_attendance, name="view_attendance"),
    path('view_video', views.view_video, name="view_video"),
    path('view_exercise_video', views.view_exercise_video, name="view_exercise_video"),


]

