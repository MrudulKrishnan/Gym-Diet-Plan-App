package com.example.gym_diet_plan_android;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class home extends AppCompatActivity {

    Button b1_diet_chart_prediction, b2_review_progress, b3_send_feedback, b4_view_video,
            b5_complaint_reply, b6_view_tips, b7_view_attendance, b8_chatbot, b9_logout,b10_view_exercise_video;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);

        b1_diet_chart_prediction = findViewById(R.id.B1_DietChartPrediction);
        b2_review_progress = findViewById(R.id.B2_ReviewProgress);
        b3_send_feedback = findViewById(R.id.B3_SendFeedback);
        b4_view_video = findViewById(R.id.B4_ViewVideo);
        b5_complaint_reply = findViewById(R.id.B5_ComplintReply);
        b6_view_tips = findViewById(R.id.B6_ViewTips);
        b7_view_attendance = findViewById(R.id.B7_ViewAttendance);
        b8_chatbot = findViewById(R.id.B8_ChatBot);
        b9_logout = findViewById(R.id.B9_Logout);
        b10_view_exercise_video = findViewById(R.id.B10_ViewExerciseVideo);


        b1_diet_chart_prediction.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

            }
        });

        b2_review_progress.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Intent i = new Intent(getApplicationContext(), view_progress.class);
                startActivity(i);


            }
        });

        b3_send_feedback.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Intent i = new Intent(getApplicationContext(), send_feedback.class);
                startActivity(i);

            }
        });

        b4_view_video.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Intent i = new Intent(getApplicationContext(), view_video.class);
                startActivity(i);

            }
        });

        b10_view_exercise_video.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Intent i = new Intent(getApplicationContext(), view_exercise_video.class);
                startActivity(i);

            }
        });

        b5_complaint_reply.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Intent i = new Intent(getApplicationContext(), send_complaints_view_reply.class);
                startActivity(i);

            }
        });

        b6_view_tips.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Intent i = new Intent(getApplicationContext(), view_tips.class);
                startActivity(i);

            }
        });

        b7_view_attendance.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Intent i = new Intent(getApplicationContext(), view_attendance.class);
                startActivity(i);

            }
        });

        b8_chatbot.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

            }
        });

        b9_logout.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Intent i = new Intent(getApplicationContext(), login.class);
                startActivity(i);

            }
        });
    }
}