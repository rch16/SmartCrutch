package com.example.hcr_app.ui.gallery;

import android.app.Activity;
import android.app.DatePickerDialog;
import android.content.Context;
import android.view.View;
import android.widget.DatePicker;
import android.widget.EditText;
import android.widget.TextView;


import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.Locale;
import java.util.TimeZone;

public class MyEditTextDatePicker  implements View.OnClickListener, DatePickerDialog.OnDateSetListener {
    TextView _editText;
    final Calendar myCalendar = Calendar.getInstance();

    private Context _context;

    public MyEditTextDatePicker(Context context, EditText editText)
    {
        Activity act = (Activity)context;
        this._editText = editText;
        this._editText.setOnClickListener(this);
        this._context = context;
        updateDisplay();
    }

    public void prev_day() {
        myCalendar.add(Calendar.DATE, -1);
        updateDisplay();
    }

    public void next_day() {
        myCalendar.add(Calendar.DATE, 1);
        updateDisplay();
    }

    @Override
    public void onDateSet(DatePicker view, int year, int monthOfYear, int dayOfMonth) {
        myCalendar.set(Calendar.YEAR, year);
        myCalendar.set(Calendar.MONTH, monthOfYear);
        myCalendar.set(Calendar.DAY_OF_MONTH, dayOfMonth);
        updateDisplay();
    }

    @Override
    public void onClick(View v) {
        Calendar calendar = Calendar.getInstance(TimeZone.getDefault());

        DatePickerDialog dialog = new DatePickerDialog(_context, this,
                calendar.get(Calendar.YEAR),
                calendar.get(Calendar.MONTH),
                calendar.get(Calendar.DAY_OF_MONTH));
        dialog.show();

    }

    public Calendar returnDate() {
        return myCalendar;
    }

    // updates the date in the birth date EditText
    private void updateDisplay() {
        String myFormat = "dd/MM/yy"; //In which you need put here
        SimpleDateFormat sdf = new SimpleDateFormat(myFormat, Locale.UK);

        _editText.setText(sdf.format(myCalendar.getTime()));
    }
}