package com.example.gym_diet_plan_android;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class send_feedback extends AppCompatActivity
{
    EditText e1_feedback;
    Button b1_send_feedback;
    String feedback_str, url;
    SharedPreferences sh;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_send_feedback);
        e1_feedback = findViewById(R.id.E1_EnterFeedback);
        b1_send_feedback = findViewById(R.id.B1_SendFeedback);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        b1_send_feedback.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View view)
            {
//                Toast.makeText(sent_complaint.this, "complaint toast ", Toast.LENGTH_SHORT).show();

                feedback_str = e1_feedback.getText().toString();

                if (feedback_str.equalsIgnoreCase("")) {
                    e1_feedback.setError("Enter Your Feedback");
                }
                else {
                    RequestQueue queue = Volley.newRequestQueue(send_feedback.this);
                    url = "http://" + sh.getString("ip", "") + ":5000/send_feedback";

                    // Request a string response from the provided URL.
                    StringRequest stringRequest = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
                        @Override
                        public void onResponse(String response) {
                            // Display the response string.
                            Log.d("+++++++++++++++++", response);
                            try {
                                JSONObject json = new JSONObject(response);
                                String res = json.getString("task");

                                if (res.equalsIgnoreCase("success")) {
                                    Toast.makeText(send_feedback.this, "Feedback sent successfully ", Toast.LENGTH_SHORT).show();
                                    Intent ik = new Intent(getApplicationContext(), home.class);
                                    startActivity(ik);
                                } else {
                                    Toast.makeText(send_feedback.this, "please try again", Toast.LENGTH_SHORT).show();
                                }
                            } catch (JSONException e) {
                                e.printStackTrace();
                            }
                        }

                    }, new Response.ErrorListener() {
                        @Override
                        public void onErrorResponse(VolleyError error) {
                            Toast.makeText(getApplicationContext(), "Error" + error, Toast.LENGTH_LONG).show();
                        }
                    }) {
                        @Override
                        protected Map<String, String> getParams() {


                            Map<String, String> params = new HashMap<String, String>();
                            params.put("Feedback", feedback_str);
                            params.put("lid", sh.getString("lid", ""));
                            return params;
                        }
                    };
                    queue.add(stringRequest);
                } }
        });
    }

    @Override
    public void onBackPressed() {
        Intent ik =new Intent(getApplicationContext(), home.class);
        startActivity(ik);
    }

}