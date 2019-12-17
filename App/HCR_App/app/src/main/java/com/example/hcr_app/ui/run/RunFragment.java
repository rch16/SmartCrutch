package com.example.hcr_app.ui.run;

import java.util.Timer;
import java.util.concurrent.TimeUnit;

import android.app.Dialog;
import android.net.Uri;
import android.os.Bundle;
import android.os.Handler;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.view.Window;
import android.view.WindowManager;
import android.widget.ImageView;
import android.widget.ProgressBar;
import android.widget.TextView;
import android.widget.VideoView;

import androidx.annotation.Nullable;
import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.Observer;
import androidx.lifecycle.ViewModelProviders;
import androidx.navigation.Navigation;

import com.example.hcr_app.ApiService;
import com.example.hcr_app.R;
import com.example.hcr_app.SoundPoolPlayer;

import io.reactivex.Single;
import io.reactivex.SingleObserver;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.disposables.CompositeDisposable;
import io.reactivex.disposables.Disposable;
import io.reactivex.schedulers.Schedulers;
import okhttp3.OkHttpClient;
import retrofit2.Retrofit;
import retrofit2.adapter.rxjava2.RxJava2CallAdapterFactory;
import retrofit2.converter.gson.GsonConverterFactory;

public class RunFragment extends Fragment {

    private RunViewModel runViewModel;
    private Integer repetitions = 0;
    private Integer exercise = 1;
    private Boolean stop = Boolean.FALSE;

    private Handler updateHandler = new Handler();


    private void run_exercise(final View root,final SoundPoolPlayer sound){

        final ProgressBar progress_bar = root.findViewById(R.id.progressbar);
        final TextView progressText = root.findViewById(R.id.progresstext);
        final ImageView tick = root.findViewById(R.id.tick);

//        OkHttpClient okHttpClient = new OkHttpClient().newBuilder()
//                .connectTimeout(60, TimeUnit.SECONDS)
//                .readTimeout(60, TimeUnit.SECONDS)
//                .writeTimeout(60, TimeUnit.SECONDS)
//                .build();

        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("http://146.169.179.250:8000")
//                .client(okHttpClient)
                .addConverterFactory(GsonConverterFactory.create())
                .addCallAdapterFactory(RxJava2CallAdapterFactory.create())
                .build();


        ApiService apiService = retrofit.create(ApiService.class);// make a request by calling the corresponding method

        final TextView box_2 = root.findViewById(R.id.box2);
        Single<Exercise> person = apiService.getExerciseData( exercise );
        person.subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(new SingleObserver<Exercise>() {
                    @Override
                    public void onSubscribe(Disposable d) {
                        // we'll come back to this in a moment
                    }
                    @Override
                    public void onSuccess(Exercise person) {



                        Integer s = person.getExercise();
                        if (person.getExecution().equals("Correct")){
                            runViewModel.exercise_done();
                            box_2.setText(person.getExecution());

                            sound.playShortResource(R.raw.success_jingle);

                            progressText.setVisibility(View.INVISIBLE);
                            tick.setVisibility(View.VISIBLE);
                        }
                        else {
                            box_2.setText(person.getExecution());
                        }

                        // data is ready and we can update the UI

                        Handler handler = new Handler();
                        handler.postDelayed(new Runnable() {
                            @Override
                            public void run() {
                                progressText.setVisibility(View.VISIBLE);
                                tick.setVisibility(View.INVISIBLE);
                                if (stop == Boolean.FALSE){
                                    run_exercise(root, sound);
                                }
                            }
                        }, 750);

                    }
                    @Override
                    public void onError(Throwable e) {
                        box_2.setText(e.toString());

                        if (stop == Boolean.FALSE){
                            run_exercise(root, sound);
                        }
                    }
                });
    };

    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {

        final SoundPoolPlayer sound = new SoundPoolPlayer(getActivity());
        runViewModel =
                ViewModelProviders.of(this).get(RunViewModel.class);
        final View root = inflater.inflate(R.layout.fragment_run, container, false);
        final TextView progressText = root.findViewById(R.id.progresstext);
        final TextView box_1 = root.findViewById(R.id.box1);
        final TextView box_2 = root.findViewById(R.id.box2);
        final TextView help = root.findViewById(R.id.help);


        final String stringvalue = Math.round(repetitions) + "/5";
        final ProgressBar progress_bar = root.findViewById(R.id.progressbar);

        progressText.setText(stringvalue);
        progress_bar.setProgress(repetitions*20);

        final ImageView tick = root.findViewById(R.id.tick);
        tick.setVisibility(View.INVISIBLE);


        help.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                final Dialog dialog = new Dialog(getActivity());
                dialog.requestWindowFeature(Window.FEATURE_NO_TITLE);
                dialog.setContentView(R.layout.helpvideo);
                dialog.show();
                WindowManager.LayoutParams lp = new WindowManager.LayoutParams(ViewGroup.LayoutParams.WRAP_CONTENT, ViewGroup.LayoutParams.WRAP_CONTENT);
                lp.copyFrom(dialog.getWindow().getAttributes());
                dialog.getWindow().setAttributes(lp);
                final VideoView videoview = (VideoView) dialog.findViewById(R.id.help_video);
                Uri uri= Uri.parse("Test");
                if (exercise == 1){
                    uri= Uri.parse("android.resource://"+getActivity().getPackageName()+"/"+R.raw.exercise_arms);
                }
                else if (exercise == 2){
                    uri= Uri.parse("android.resource://"+getActivity().getPackageName()+"/"+R.raw.exercise_2);
                }
                else if (exercise == 3){
                    uri= Uri.parse("android.resource://"+getActivity().getPackageName()+"/"+R.raw.exercise_3);
                }
                else if (exercise == 4){
                    uri= Uri.parse("android.resource://"+getActivity().getPackageName()+"/"+R.raw.exercise_squat);
                }
                videoview.setVideoURI(uri);
                videoview.start();
            }
        });


        run_exercise(root, sound);

        runViewModel.getText().observe(this, new Observer<String>() {
            @Override
            public void onChanged(@Nullable String s) {
                progressText.setText(s);

            }
        });

        runViewModel.getProgressValue().observe(this, new Observer<Integer>() {
            @Override
            public void onChanged(@Nullable Integer s) {
                progress_bar.setProgress(s*20);
                if (s == 5){
                    if (exercise == 4){
                        Navigation.findNavController(root).navigate(R.id.go_to_start, null);
                        stop = Boolean.TRUE;
                    }

                    //Navigation.findNavController(root).navigate(R.id.go_to_self, null);
                }
            }
        });

        runViewModel.getExerciseName().observe(this, new Observer<String>() {
            @Override
            public void onChanged(@Nullable String s) {
                box_1.setText(s);
            }
        });

        runViewModel.getExerciseDescription().observe(this, new Observer<String>() {
            @Override
            public void onChanged(@Nullable String s) {
                box_2.setText(s);
            }
        });

        runViewModel.getExerciseNumber().observe(this, new Observer<Integer>() {
            @Override
            public void onChanged(@Nullable Integer s) {
                exercise = s;
            }
        });


        // create an instance of the ApiService

        Timer timer = new Timer();

        return root;
    }
}