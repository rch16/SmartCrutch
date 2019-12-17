package com.example.hcr_app;

import android.os.AsyncTask;
import android.util.Log;

import com.google.api.services.sheets.v4.model.ValueRange;

import java.io.IOException;
import java.util.List;

import static androidx.constraintlayout.widget.Constraints.TAG;

/**
 * Need to call the API read function on thread because Android
 * doesn't all network calls on main thread. Use AysncTask for this
 */
public class Avg_Weight extends AsyncTask <Void,Void,CharSequence> {

    @Override
    protected CharSequence doInBackground(Void... voids) {
        final String range = "Avg_Weight_On_Floor!B2";
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

        List<List<Object>> Avg_Weight_On_Floor = result.getValues();
        String Results_Char = null;
        if (Avg_Weight_On_Floor == null || Avg_Weight_On_Floor.isEmpty()) {
            System.out.println("No data found.");
        } else {
            System.out.println("Average Weight on Crutch in KG " + Avg_Weight_On_Floor.get(0));
            Results_Char =  Avg_Weight_On_Floor.get(0).toString();
            Results_Char = Results_Char.substring(1,Results_Char.length()-1); // make 4 significant figure
//                for (List row : Avg_Weight_On_Floor) {
//                    // Print columns A and E, which correspond to indices 0 and 4.
//                    Log.d(TAG, row.get(0) + "," + row.get(0));
//                }
        }
        return Results_Char;
    }

    @Override
    protected void onPostExecute(CharSequence result) {
       // printtoscreen("Average Weight on Crutch in KG " + result.get(0));
    }
}

