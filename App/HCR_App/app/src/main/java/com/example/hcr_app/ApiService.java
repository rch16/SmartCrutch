package com.example.hcr_app;

import com.example.hcr_app.ui.run.Exercise;

import io.reactivex.Single;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.adapter.rxjava2.Result;
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.PUT;
import retrofit2.http.Path;
import retrofit2.http.Query;

public interface ApiService {

    @GET("/api/start")
    Single<Exercise> getExerciseData(@Query("exercise_number") Integer exercise_number);

    @PUT("/api/set_threshold") //
    Call<Result> updateThreshold(@Query("threshold") Integer set);
}