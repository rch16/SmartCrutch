import gspread
import gc
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import numpy as np
from openpyxl import load_workbook
from openpyxl.workbook import Workbook
import matplotlib.pyplot as plt
import math
from statistics import mean 
from sheetfu import SpreadsheetApp

def main():

    sa = SpreadsheetApp('/Users/loicalix-brown/Documents/UniWork/HCR/HCR.json')
    treated_spreadsheet = sa.open_by_url(url='https://docs.google.com/spreadsheets/d/1dbBRml3jIuftt9riloG60joDY4tMK1CEXvZ1XqmmmXc/edit#gid=193449416')
    angles = treated_spreadsheet.get_sheet_by_name('angles_Over_Time')
    angles_on_floor = treated_spreadsheet.get_sheet_by_name('Avg_Angle_When_Hitting_Floor')
    avg_weight_on_floor_sheet = treated_spreadsheet.get_sheet_by_name('Avg_Weight_On_Floor')

    raw_spreadsheet = sa.open_by_url(url='https://docs.google.com/spreadsheets/d/1s5Eu9foYRzJPQ9-k__CtCC0xfYES5D0h2s9j7a-iDuQ/edit?fbclid=IwAR3sGGrg41u9lMYpmeYZFFBBjc1Qr90PHP74ofCUEE_5VMgtDW74UC7u2Ls#gid=1211208218')
    raw_data = raw_spreadsheet.get_sheet_by_name('Sample_for_analysis')

    pp = pprint.PrettyPrinter()

    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name('/Users/loicalix-brown/Documents/UniWork/HCR/HCR.json', scope)

    client = gspread.authorize(creds)

    sheet = client.open('Smart_crutch_raw_data').sheet1

    angles_Over_Time = client.open('Smart_crutch_formatted_data').worksheet('Angles_Over_Time')
    avg_Weight_On_Floor = client.open('Smart_crutch_formatted_data').worksheet('Avg_Weight_On_Floor')
    avg_Angle_When_Hitting_Floor = client.open('Smart_crutch_formatted_data').worksheet('Avg_Angle_When_Hitting_Floor')

    df = sheet.get_all_records()

    accel_dict = {

    }

    timestamp = []
    accel_x = []
    accel_y = []
    accel_z = []
    gyro_x = []
    gyro_y = []
    gyro_z = []
    weight = []

    #Get the raw data from the sheet
    def getCurrentDate(raw_data):
        raw_data_range = raw_data.get_data_range()
        max_row = raw_data_range.get_max_row()
        current_date_row = max_row - 302 #modify to access row with the date and tme for each batch 
        print(current_date_row)
        current_date = sheet.row_values(current_date_row)
        return(current_date[0])
    current_date = getCurrentDate(raw_data)

    #Find the maximum row used in a spreadsheet 
    def getMaxRow(spreadsheet_name):
        raw_data_range = spreadsheet_name.get_data_range()
        max_row = raw_data_range.get_max_row()
        return(max_row) 
    
    #Find the maximum column used in the sheet
    def getMaxCol(spreadsheet_name):
        data_range = spreadsheet_name.get_data_range()
        nb_cols = data_range.get_max_column()
        return(nb_cols)

    #Get max rows of the raw data sheet
    max_row_raw_data = getMaxRow(raw_data) 

    #Extract the data from the sheet into arrays
    for i in range(max_row_raw_data-302,max_row_raw_data-300): #must be modified based on how long your batches are, only include the rwo with data
        # take each row of data one at a time
        dictionary = df[i]
        # get info from "data" key, split into array of strings, convert to array of ints
        data = [float(i) for i in dictionary["data"].split(',')]
        # add relevant data to relevant arrays
        # time_stamp = np.append(time_stamp, data[0])
        timestamp = np.append(timestamp, data[1])
        accel_x = np.append(accel_x, data[2])
        accel_y = np.append(accel_y, data[3])
        accel_z = np.append(accel_z, data[4])
        gyro_x = np.append(gyro_x, data[5])
        gyro_y = np.append(gyro_y, data[6])
        gyro_z = np.append(gyro_z, data[7])
        weight = np.append(weight,data[8])

    for i in range (0, len(weight)):
        weight[i] = int(weight[i])

    #Pi
    M_PI = 3.14159265358979323846

    # Calculating the picth roll and yaw angles at each timestamp
    pitch = []
    roll = []
    yaw = []

    def calcAngles(accel_x, accel_y, accel_z, timestamp, pitch, roll, yaw):
        for i in range(0,len(timestamp)):
            pitch = np.append(pitch, 180 * math.atan2(accel_x[i],math.sqrt(accel_y[i]*accel_y[i] + accel_z[i]*accel_z[i]))/M_PI)
            roll = np.append(roll, 180 * math.atan2(accel_y[i],math.sqrt(accel_x[i]*accel_x[i] + accel_z[i]*accel_z[i]))/M_PI)
            yaw = np.append(yaw,180 * math.atan2(accel_z[i],math.sqrt(accel_x[i]*accel_x[i] + accel_z[i]*accel_z[i]))/M_PI)
        return([pitch, roll, yaw])
    pitch_angle = calcAngles(accel_x, accel_y, accel_z, timestamp, pitch, roll, yaw)[0]
    roll_angle = calcAngles(accel_x, accel_y, accel_z, timestamp, pitch, roll, yaw)[1]
    yaw_angle = calcAngles(accel_x, accel_y, accel_z, timestamp, pitch, roll, yaw)[2]

    # Get the max column and row in the sheet with the orientation angles 
    max_col = getMaxCol(angles)

    # Set the column to be printed to to be one more than the current max column
    next_col_angles = max_col + 1

    # If the sheet has reach it's column limit add the amount of necessary columns to append the data to
    if max_col >= 24 or len(timestamp) >= 24:
        angles_Over_Time.add_cols(len(timestamp))

    # Give initial timestamp for this batch of readings
    for i in range (0,1):
        angles_Over_Time.update_cell(1,next_col_angles + i, current_date)

    # Sending values back to google sheet
    for i in range (0,len(timestamp)):
        angles_Over_Time.update_cell(2,next_col_angles + i, timestamp[i])
        angles_Over_Time.update_cell(3,next_col_angles + i, pitch_angle[i])
        angles_Over_Time.update_cell(4,next_col_angles + i, roll_angle[i])
        angles_Over_Time.update_cell(5,next_col_angles + i, yaw_angle[i])

    #Extracting values and timestamps during which the crutch is on the floor in a walking cycle 
    weight_threshold = 3

    weight_floor = []
    timestamp_floor = []

    for i in range(0,len(weight)):
        if weight[i] >= weight_threshold:
            weight_floor = np.append(weight_floor,weight[i]) 
            timestamp_floor = np.append(timestamp_floor,timestamp[i])
    print(weight_floor)

    # Calculating the average weight put on the crutch when on the floor
    avg_weight_floor = 0

    if np.amax(weight) >= weight_threshold:
        sum_weight_floor =  np.sum(weight_floor)
        avg_weight_floor = sum_weight_floor/len(weight_floor)
    print(avg_weight_floor)

    #Getting number of cols from the average weight on floor sheet 
    nb_col_avg_weight_on_floor = getMaxCol(avg_weight_on_floor_sheet)

    # Getting index of first empty column 
    max_col_avg_weight_on_floor = nb_col_avg_weight_on_floor + 1

    # Sending average weight on floor of one batch to the sheet
    avg_Weight_On_Floor.update_cell(1, max_col_avg_weight_on_floor, current_date)
    avg_Weight_On_Floor.update_cell(2, max_col_avg_weight_on_floor, avg_weight_floor)

    # Finding the index the where the crutch first hits the floor
    first_floor_index = []
    first_floor_index = np.append(first_floor_index, np.where(weight>=3))

    # Convert index from float to int
    first_floor_index = first_floor_index.astype(int)

    # Finding the timestamp at which the crutch hits the floor 
    first_floor_timestamp = np.empty

    if len(first_floor_index) > 0:
        first_floor_timestamp = np.append(first_floor_index, timestamp[first_floor_index[0]])

    # convert index from float to int
    #first_floor_timestamp = first_floor_timestamp.astype(int)

    # Calculate angles of the first time the crutch hits the floor
    floor_pitch = []
    floor_roll= []
    floor_yaw = []

    if len(first_floor_index) > 0: 
        floor_pitch  = np.append(floor_pitch, pitch_angle[first_floor_index[0]])
        floor_roll = np.append(floor_roll, roll_angle[first_floor_index[0]])
        floor_yaw = np.append(floor_yaw, yaw_angle[first_floor_index[0]])

    print(floor_roll)
    print(floor_pitch)
    print(floor_yaw)

    # Calculate average angles over a time period at which the crutch hits the floor 
    step_index = [1]

    # Finding the timestamp at which 
    for i in range(1,len(weight)-1):
        if weight[i] < weight_threshold and weight[i+1] >= weight_threshold:
            step_index = np.append(step_index, i+1)

    print(step_index)
    # Convert form float to int
    # step_index = step_index.astype(int)

    # Extract angles at steps
    step_roll = []
    step_pitch = []
    step_yaw = []

    for i in range(0,len(step_index)):
        step_roll = np.append(step_roll, roll_angle[step_index[i]])
        step_pitch = np.append(step_pitch, pitch_angle[step_index[i]])
        step_yaw = np.append(step_pitch, yaw_angle[step_index[i]])

    # Compute the mean of the angle of each axis across multipe steps at the point of hitting the floor 
    avg_step_pitch = []
    avg_step_roll = []
    avg_step_yaw = []

    avg_step_pitch =  mean(step_pitch)
    avg_step_roll = mean(step_roll)
    avg_step_yaw = mean(step_yaw)

    #Get the max col and row for the angles_on_floor sheet, change 2 to function later 
    nb_col_angles_on_floor = getMaxCol(angles_on_floor)

    # Set the column to be printed to to be one more than the current max column
    max_col_angles_on_floor = nb_col_angles_on_floor + 1

    # If the sheet has reach it's column limit add the amount of necessary columns to append the data to
    if max_col_angles_on_floor >= 26:
        angles_Over_Time.add_cols(1)

    #Send data to spreadsheet, must use update cell as api does not allow to append columns
    avg_Angle_When_Hitting_Floor.update_cell(1,max_col_angles_on_floor, current_date)
    avg_Angle_When_Hitting_Floor.update_cell(2,max_col_angles_on_floor,avg_step_pitch)
    avg_Angle_When_Hitting_Floor.update_cell(3,max_col_angles_on_floor,avg_step_roll)
    avg_Angle_When_Hitting_Floor.update_cell(4,max_col_angles_on_floor,avg_step_yaw)

main()