package com.example.hcr_app;

import android.os.AsyncTask;
import android.util.Log;

import com.google.api.services.sheets.v4.model.ValueRange;

import java.io.IOException;
import java.util.List;

import static androidx.constraintlayout.widget.Constraints.TAG;


//TODO: decided where processing will be done and then change return type
public class AnglesOverTime extends AsyncTask<Void,Void,List<List<Object>>> {
    @Override

    protected List<List<Object>> doInBackground(Void... voids) {
        final String range = "Angles_Over_Time!1:5";
        ValueRange result = null;
        try {
            result = MainActivity.sheetsService.spreadsheets().values()
                    .get(MainActivity.spreadsheetId, range)
                    .setKey(GsheetsConfig.google_api_key)
                    .execute();

        } catch (IOException e) {
            e.printStackTrace();
            Log.d(TAG, "Threw null pointer error for result, result=" + result);
        }
        List<List<Object>> Data = result.getValues();
        if (Data == null || Data.isEmpty()) {
            System.out.println("No data found.");
        } else {
            System.out.println("Test for first row in anglesovertime " + Data.get(1).get(1) +" "+  Data.get(2).get(1));
            System.out.println("Test for first row in anglesovertime " + Data.get(1).get(2) +" "+  Data.get(2).get(2));
            for (List row : Data) {
                // Print columns A and E, which correspond to indices 0 and 4.
                Log.d(TAG, row.get(0) + "," + row.get(1) + "," + row.get(2)+"," + row.get(3)+"," + row.get(4));
            }
        }
        return Data;
    }
}
