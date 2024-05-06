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

public class view_progress extends AppCompatActivity
{
    ListView l1_view_progress;
    SharedPreferences sh;
    String url,user_id_str;
    ArrayList<String> date_arr, height_arr, weight_arr, user_id_arr;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_progress);


        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        l1_view_progress=findViewById(R.id.L1_ViewProgress);
        url = "http://" + sh.getString("ip", "") + ":5000/view_progress";
        RequestQueue queue = Volley.newRequestQueue(view_progress.this);

        StringRequest stringRequest = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                // Display the response string.
                Log.d("+++++++++++++++++", response);
                try {
                    Toast.makeText(view_progress.this, ""+response, Toast.LENGTH_SHORT).show();

                    JSONArray ar = new JSONArray(response);

                    date_arr = new ArrayList<>();
                    weight_arr = new ArrayList<>();
                    height_arr = new ArrayList<>();
                    user_id_arr = new ArrayList<>();

                    for (int i = 0; i < ar.length(); i++) {
                        JSONObject jo = ar.getJSONObject(i);
                        date_arr.add(jo.getString("Date"));
                        weight_arr.add(jo.getString("Weight"));
                        height_arr.add(jo.getString("Height"));
                        user_id_arr.add(jo.getString("user_id"));

                    }

//                     ArrayAdapter<String> ad=new ArrayAdapter<>(Home.this,android.R.layout.simple_list_item_1,name);
//                    lv.setAdapter(ad);

                    l1_view_progress.setAdapter(new custom_view_progress(view_progress.this,date_arr, weight_arr, height_arr, user_id_arr));
//                    view_product_list.setOnItemClickListener(view_product.this);

                } catch (Exception e) {
                    Toast.makeText(getApplicationContext(),"========="+e,Toast.LENGTH_LONG).show();
                    Log.d("=========", e.toString());
                }


            }

        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

                Toast.makeText(view_progress.this, "err" + error, Toast.LENGTH_SHORT).show();
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