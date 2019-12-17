package com.example.hcr_app.ui.gallery;

import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.TextView;

import androidx.annotation.Nullable;
import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.Observer;
import androidx.lifecycle.ViewModelProviders;

import com.example.hcr_app.AnglesOverTime;
import com.example.hcr_app.R;
import com.jjoe64.graphview.GraphView;
import com.jjoe64.graphview.helper.DateAsXAxisLabelFormatter;
import com.jjoe64.graphview.series.DataPoint;
import com.jjoe64.graphview.series.LineGraphSeries;

import java.time.Month;
import java.util.Calendar;
import java.util.Date;
import java.util.List;
import java.util.Objects;
import java.util.concurrent.ExecutionException;

import static androidx.constraintlayout.widget.Constraints.TAG;


public class GalleryFragment extends Fragment {



    String[] Months = new String[]{"December","January","February","March","April","May","June","July","August","September","October","November","December"};
    int index = 0;
    private GalleryViewModel galleryViewModel;

    Calendar my_calendar = Calendar.getInstance();

    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {
        galleryViewModel =
                ViewModelProviders.of(this).get(GalleryViewModel.class);
        View root = inflater.inflate(R.layout.fragment_gallery, container, false);


        final EditText dateText = root.findViewById(R.id.date);

        final ImageButton leftbutton = root.findViewById(R.id.left_arrow);
        final ImageButton rightbutton = root.findViewById(R.id.right_arrow);

        final MyEditTextDatePicker date_picker = new MyEditTextDatePicker(getActivity(), dateText);
        final GraphView line_graph = root.findViewById(R.id.line_graph);

        List<List<Object>> Data = null;
        try {
            Data = new AnglesOverTime().execute().get();
        } catch (ExecutionException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        /**
        LineGraphSeries<DataPoint> Roll = new LineGraphSeries<>();
        LineGraphSeries<DataPoint> Pitch = new LineGraphSeries<>();
        LineGraphSeries<DataPoint> Yaw = new LineGraphSeries<>();
        for(int i = 1; i < Data.get(1).size(); i++){
            Roll.appendData(new DataPoint(Double.valueOf((String) Data.get(1).get(i)), Double.valueOf((String) Data.get(2).get(i))),false,5000);
            Pitch.appendData(new DataPoint(Double.valueOf((String) Data.get(1).get(i)), Double.valueOf((String) Data.get(3).get(i))),false,5000);
            Yaw.appendData(new DataPoint(Double.valueOf((String) Data.get(1).get(i)), Double.valueOf((String) Data.get(4).get(i))),false,5000);
        }


        Log.d(TAG, "Colour!!!!!!!!!!!!!!!!!!!!!!!!!!!!! "+Roll.getColor()); //blue
        Pitch.setColor(-1546548); // purple
        Yaw.setColor(-1413780); //reddish
        line_graph.addSeries(Roll);
        line_graph.addSeries(Pitch);
        line_graph.addSeries(Yaw);
         **/
        Calendar calendar = Calendar.getInstance();
        calendar.set(2019, 11, 1); // months start from 0
        Date d1 = calendar.getTime();
        calendar.add(Calendar.DATE,7);
        Date d2 = calendar.getTime();
        calendar.add(Calendar.DATE, 7);
        Date d3 = calendar.getTime();
        calendar.add(Calendar.DATE, 7);
        Date d4 = calendar.getTime();
        calendar.add(Calendar.DATE, 7);
        Date d5 = calendar.getTime();


        final LineGraphSeries<DataPoint> series = new LineGraphSeries<>(new DataPoint[] {
                new DataPoint(d1, 30),
                new DataPoint(d2, 29.6),
                new DataPoint(d3,29),
                new DataPoint(d4, 28),
                new DataPoint(d5,26)
        });
        line_graph.addSeries(series);

        line_graph.getGridLabelRenderer().setLabelFormatter(new DateAsXAxisLabelFormatter(getActivity()));
        line_graph.getGridLabelRenderer().setNumHorizontalLabels(3); // only 4 because of the space

        line_graph.getViewport().setMinX(d1.getTime());
        line_graph.getViewport().setMaxX(d2.getTime());
        line_graph.getViewport().setXAxisBoundsManual(true);

        line_graph.getViewport().setScalable(true);

// activate horizontal scrolling
        line_graph.getViewport().setScrollable(true);

// activate horizontal and vertical zooming and scrolling
        line_graph.getViewport().setScalableY(true);

// activate vertical scrolling
        line_graph.getViewport().setScrollableY(true);

        line_graph.getGridLabelRenderer().setHorizontalAxisTitle("Date");
        line_graph.getGridLabelRenderer().setVerticalAxisTitle("Weight on Crutch (kg)");

        final TextView textView = root.findViewById(R.id.graph_info);
        galleryViewModel.getText().observe(this, new Observer<String>() {
            @Override
            public void onChanged(@Nullable String s) {
                my_calendar = date_picker.returnDate();
                textView.setText(Months[index]);
            }
        });

        leftbutton.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                date_picker.prev_day();
                my_calendar = date_picker.returnDate();
                index--;
                index= (((index % 12) + 12) % 12);
                textView.setText(Months[index]);
                line_graph.removeSeries(series);
                if(Months[index]=="December"){
                    line_graph.addSeries(series);
                }

            }
        });

        rightbutton.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                date_picker.next_day();
                my_calendar = date_picker.returnDate();
                int day = my_calendar.get(Calendar.DATE);
                index++;
                index= (((index % 12) + 12) % 12);
                textView.setText(Months[index]);
                line_graph.removeSeries(series);
                if(Months[index]=="December"){
                    line_graph.addSeries(series);
                }
            }
        });

        return root;
    }
}