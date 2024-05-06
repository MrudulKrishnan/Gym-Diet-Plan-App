package com.example.gym_diet_plan_android;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class view_exercise_video extends AppCompatActivity
{
    ListView l1_view_video;
    SharedPreferences sh;
    String url,user_id_str;
    ArrayList<String>  video_arr, exercise_name_arr, description_arr, exercise_details_arr;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_exercise_video);


        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        l1_view_video=findViewById(R.id.L1_ViewVideo);
        url = "http://" + sh.getString("ip", "") + ":5000/view_exercise_video";
        RequestQueue queue = Volley.newRequestQueue(view_exercise_video.this);

        StringRequest stringRequest = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                // Display the response string.
                Log.d("+++++++++++++++++", response);
                try {
                    Toast.makeText(view_exercise_video.this, ""+response, Toast.LENGTH_SHORT).show();

                    JSONArray ar = new JSONArray(response);

                    video_arr = new ArrayList<>();
                    exercise_name_arr = new ArrayList<>();
                    description_arr = new ArrayList<>();
                    exercise_details_arr = new ArrayList<>();


                    for (int i = 0; i < ar.length(); i++) {
                        JSONObject jo = ar.getJSONObject(i);
                        video_arr.add(jo.getString("Video"));
                        exercise_name_arr.add(jo.getString("ExerciseName"));
                        description_arr.add(jo.getString("Description"));
                        exercise_details_arr.add(jo.getString("ExerciseDetails"));


                    }

//                     ArrayAdapter<String> ad=new ArrayAdapter<>(Home.this,android.R.layout.simple_list_item_1,name);
//                    lv.setAdapter(ad);

                    l1_view_video.setAdapter(new custom_view_exercise_video(view_exercise_video.this,exercise_name_arr, video_arr, description_arr, exercise_details_arr));
//                    view_product_list.setOnItemClickListener(view_product.this);

                } catch (Exception e) {
                    Toast.makeText(getApplicationContext(),"========="+e,Toast.LENGTH_LONG).show();
                    Log.d("=========", e.toString());
                }


            }

        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

                Toast.makeText(view_exercise_video.this, "err" + error, Toast.LENGTH_SHORT).show();
            }
        }) {
            @NonNull
            @Override
            protected Map<String, String> getParams() {
                Map<String, String> params = new HashMap<>();
                params.put("lid", sh.getString("lid", ""));
                return params;
            }
        };
        queue.add(stringRequest);
    }

    @Override
    public void onBackPressed() {
        Intent ik =new Intent(getApplicationContext(), home.class);
        startActivity(ik);
    }


}