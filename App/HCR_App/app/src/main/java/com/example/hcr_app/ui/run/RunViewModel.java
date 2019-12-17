package com.example.hcr_app.ui.run;

import android.os.Handler;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

public class RunViewModel extends ViewModel {

    private MutableLiveData<String> progress_text;
    private MutableLiveData<String> exercise_name;
    private MutableLiveData<String> exercise_description;
    private MutableLiveData<Integer> progress_value;
    private MutableLiveData<Integer> exercise_number;

    public RunViewModel() {
        exercise_number = new MutableLiveData<>();
        exercise_name = new MutableLiveData<>();
        exercise_description = new MutableLiveData<>();
        progress_value = new MutableLiveData<>();
        progress_text = new MutableLiveData<>();


        progress_value.setValue(0);
        exercise_number.setValue(1);

        exercise_name.setValue("Arm raise");
        exercise_description.setValue("Raise your arms above your head");

        final String stringvalue = Math.round(progress_value.getValue()) + "/5";

        progress_text.setValue(stringvalue);

    }

    public void exercise_done(){
        progress_value.setValue(progress_value.getValue() + 1);

        if (progress_value.getValue() == 5){
            Handler handler = new Handler();
            exercise_number.setValue(exercise_number.getValue() + 1);

            handler.postDelayed(new Runnable() {
                public void run() {

                    progress_value.setValue(0);
                    final String stringvalue = Math.round(progress_value.getValue()) + "/5";
                    progress_text.setValue(stringvalue);

                    if (exercise_number.getValue() == 1) {
                        exercise_name.setValue("Arm raise");
                        exercise_description.setValue("Raise your arms above your head");
                    }
                    else if (exercise_number.getValue() == 2) {
                        exercise_name.setValue("Lateral Leg Raise");
                        exercise_description.setValue("Raise your right leg to the side");
                    }
                    else if (exercise_number.getValue() == 3) {
                        exercise_name.setValue("Frontal Leg Raise");
                        exercise_description.setValue("Raise your arms above your head");
                    }
                    else if (exercise_number.getValue() == 4) {
                        exercise_name.setValue("Squat");
                        exercise_description.setValue("Bend your knees while keeping your back straight");
                    }
                }
            }, 2000);
        }

        final String stringvalue = Math.round(progress_value.getValue()) + "/5";
        progress_text.setValue(stringvalue);
        return;
    }

    public LiveData<String> getText() {
        return  progress_text;
    }

    public LiveData<String> getExerciseName() {
        return  exercise_name;
    }

    public LiveData<String> getExerciseDescription() {
        return  exercise_description;
    }

    public LiveData<Integer> getProgressValue() {
        return  progress_value;
    }

    public LiveData<Integer> getExerciseNumber() {
        return  exercise_number;
    }


}