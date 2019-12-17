package com.example.hcr_app;


import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

public class Threshold {
    @Expose
    @SerializedName("threshold")
    private Integer threshold;

    public void setThreshold(Integer x) {
        threshold = x;
        return;
    }

    // bunch of boring getters and setters
}
