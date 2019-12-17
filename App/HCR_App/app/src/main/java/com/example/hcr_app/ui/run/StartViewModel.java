package com.example.hcr_app.ui.run;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

public class StartViewModel extends ViewModel {

    private MutableLiveData<String> mText;

    public StartViewModel() {
        mText = new MutableLiveData<>();
        mText.setValue("Press play to start your exercises");
    }

    public LiveData<String> getText() {
        return mText;
    }

}