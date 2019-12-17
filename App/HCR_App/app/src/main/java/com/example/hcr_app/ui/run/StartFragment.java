package com.example.hcr_app.ui.run;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageButton;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.Observer;
import androidx.lifecycle.ViewModelProviders;
import androidx.navigation.Navigation;

import com.example.hcr_app.ApiService;
import com.example.hcr_app.MainActivity;
import com.example.hcr_app.R;

import io.reactivex.disposables.CompositeDisposable;
import retrofit2.Retrofit;
import retrofit2.adapter.rxjava2.RxJava2CallAdapterFactory;
import retrofit2.converter.gson.GsonConverterFactory;

public class StartFragment extends Fragment {

    private StartViewModel startViewModel;

    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {

        final MainActivity activity = (MainActivity) getActivity();
        activity.setStop(1);

        startViewModel =
                ViewModelProviders.of(this).get(StartViewModel.class);
        View root = inflater.inflate(R.layout.fragment_start, container, false);

        ImageButton start_button = root.findViewById(R.id.button);

        start_button.setOnClickListener(
                Navigation.createNavigateOnClickListener(R.id.go_to_run, null)
        );

        final TextView box_1 = root.findViewById(R.id.start_box1);

        startViewModel.getText().observe(this, new Observer<String>() {
            @Override
            public void onChanged(@Nullable String s) {
                box_1.setText(s);
            }
        });


        return root;
    }
}
