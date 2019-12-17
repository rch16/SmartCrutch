package com.example.hcr_app.ui.home;

import android.os.Build;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.EditText;
import android.widget.TextView;

import androidx.annotation.Nullable;
import androidx.annotation.NonNull;
import androidx.annotation.RequiresApi;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.Observer;
import androidx.lifecycle.ViewModelProviders;

import com.example.hcr_app.Avg_Weight;
import com.example.hcr_app.R;

import java.util.concurrent.ExecutionException;


public class  HomeFragment extends Fragment {

    private HomeViewModel homeViewModel;

    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {
        homeViewModel =
                ViewModelProviders.of(this).get(HomeViewModel.class);
        View root = inflater.inflate(R.layout.fragment_home, container, false);

        final TextView box2_1 = root.findViewById(R.id.box2_1);
        final TextView box2_2 = root.findViewById(R.id.box2_2);
        final TextView box3_1 = root.findViewById(R.id.box3_1);
        final TextView box3_2 = root.findViewById(R.id.box3_2);

        final TextView title2_1 = root.findViewById(R.id.title2_1);
        final TextView title2_2 = root.findViewById(R.id.title2_2);
        final TextView title3_1 = root.findViewById(R.id.title3_1);
        final TextView title3_2 = root.findViewById(R.id.title3_2);
        final TextView progressBarTitle= root.findViewById(R.id.progressbartitle);


        homeViewModel.getText().observe(this, new Observer<String>() {
            @RequiresApi(api = Build.VERSION_CODES.P)
            @Override
            public void onChanged(@Nullable String s) {
                try {
                    box2_1.setText( new Avg_Weight().execute().get() + " kG"); //Print average weight on crutch
                } catch (ExecutionException e) {
                    e.printStackTrace();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                box2_1.setTextSize(25);
                box2_2.setText("25.7 kG");
                box2_2.setTextSize(25);
                box3_1.setText("Have you done your exercises for today?");
                box3_1.isElegantTextHeight();
                box3_1.setTextSize(28);
                box3_2.setText("Stay Motivated");
                box3_2.setTextSize(30);
                title2_1.setText("Average Weight on Crutch Yesterday");
                title2_1.setTextSize((float) 20);
                title2_2.setText("Today aim for");
                title3_1.setText("");
                title3_2.setText("");
                progressBarTitle.setText("Progress");

            }
        });
        return root;
        }
}