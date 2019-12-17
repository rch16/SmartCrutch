package com.example.hcr_app.ui.run;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

public class Exercise {
    @Expose
    @SerializedName("exercise")
    private Integer exercise;
    @Expose
    @SerializedName("execution")
    private String execution;
    @Expose
    @SerializedName("feedback")
    private Float feedback;

    public Integer getExercise() {
        return exercise;
    }

    public String getExecution() {
        return execution;
    }

    public Float getFeedback() {
        return feedback;
    }
    // bunch of boring getters and setters
}
