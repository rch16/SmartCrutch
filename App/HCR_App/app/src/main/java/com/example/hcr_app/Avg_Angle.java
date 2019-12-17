package com.example.hcr_app;

import android.os.AsyncTask;
import android.util.Log;

import com.google.api.services.sheets.v4.model.ValueRange;

import java.io.IOException;
import java.util.List;

import static androidx.constraintlayout.widget.Constraints.TAG;

//TODO: change return type to something meaningful
public class Avg_Angle extends AsyncTask<Void,Void,List<List<Object>>> {
    @Override

    protected List<List<Object>> doInBackground(Void... voids) {
        final String range = "Avg_Angle_When_Hitting_Floor!1:4";
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
        List<List<Object>> Data = result.getValues(); // returns list of list. Outer List indexes row
        if (Data == null || Data.isEmpty()) {
            System.out.println("No data found.");
        } else {
            System.out.println("Test for first row in avg_angles" + Data.get(0));
            for (List row : Data) {
                // Print columns A and E, which correspond to indices 0 and 4.
                Log.d(TAG, row.get(0) + "," + row.get(1) + "," + row.get(2)+"," + row.get(3));
            }
        }
        return Data;
    }

}

