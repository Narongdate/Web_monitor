import csv
import shutil
import os
import sys
import subprocess
import datetime
from datetime import date, timedelta
import zipfile
import statistics

DataDict = {}


def cmd_response(cmd):
    response = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
    (out, err) = response.communicate()
    out1 = str(out)
    out2 = out1.replace('b\'', '')
    out3 = out2.replace('\\r\\n\'', '')
    out4 = out3.replace('\\\\', '\\')
    return out4


def make_dir(path):
    number_tester = 22
    saturn_path = path + '\SaturnHD'
    os.chdir(path)
    os.system('cd')
    os.system('mkdir SaturnHD')
    os.chdir(saturn_path)
    os.system('cd')
    for i in range(1, number_tester + 1):
        if i < 10:
            dir_name = 'RP0' + str(i)
        else:
            dir_name = 'RP' + str(i)
        os.chdir(saturn_path)
        os.system('mkdir ' + dir_name)


def clear_dir(path):
    SRC_RP01 = r'\\10.82.201.41\Archive\Saturn\RP01\SCC-COM\CsvLog\20180918'
    tester_path = []
    SaturnPath = path + '\SaturnHD'
    os.chdir(SaturnPath)
    os.system('cd')
    os.system('dir /b | findstr "RP" > DirName.txt')
    fo_DirName = open('DirName.txt', 'r')
    read_DirName = fo_DirName.read()
    line_DirName = read_DirName.split()
    for i in line_DirName:
        tester_path.append(SaturnPath + '\\' + i)
    for item in tester_path:
        os.chdir(item)
        os.system('cd')
        os.system('del / s *.zip')
        os.system('del / s *.csv')


def cur_date():
    yesterday = date.today() - timedelta(1)
    cur_date = str(yesterday).replace('-', '')
    return cur_date


def copy_file(path):
    SRC_RP01 = r'\\10.82.201.41\Archive\Saturn\RP01\SCC-COM\CsvLog\20180918'
    src_file = []
    SaturnPath = path + '\SaturnHD'
    dis_RP01 = SaturnPath + '\RP01'
    date = str(cur_date())
    os.chdir(SaturnPath)
    os.system('cd')
    os.system('dir /b | findstr "RP" > DirName.txt')
    fo_DirName = open('DirName.txt', 'r')
    read_DirName = fo_DirName.read()
    line_DirName = read_DirName.split()
    # line_DirName = ['RP01','RP02']
    for i in line_DirName:
        src_file.append(r'\\10.82.201.41\Archive\Saturn\{}\SCC-COM\CsvLog\{}'.format(i, date))
        src = r'\\10.82.201.41\Archive\Saturn\{}\SCC-COM\CsvLog\{}'.format(i, date)
        dis = SaturnPath + '\\' + i
        os.system('xcopy ' + src + '\*FUNCTION* ' + dis)
        os.system('xcopy ' + src + '\*FINAL* ' + dis)


def list_dir(path):
    os.chdir(path)
    os.system('dir /b | findstr "RP" > DirName.txt')
    fo_DirName = open('DirName.txt', 'r')
    read_DirName = fo_DirName.read()
    line_DirName = read_DirName.split()
    return line_DirName


def list_zip_file(path):
    os.chdir(path)
    os.system('dir /b | findstr ".zip" > DirName.txt')
    fo_DirName = open('DirName.txt', 'r')
    read_DirName = fo_DirName.read()
    list_file = read_DirName.split()
    return list_file


def list_text_file(path):
    os.chdir(path)
    os.system('dir /b | findstr ".txt" > txt_Name.txt')
    fo_DirName = open('txt_Name.txt', 'r')
    read_DirName = fo_DirName.read()
    list_file = read_DirName.split()
    return list_file

def date_diff(ref_date,cur_date):
    ref_split = ref_date.split('-')
    cur_split = cur_date.split('-')
    d1 = date(int(ref_split[0]), int(ref_split[1]), int(ref_split[2]))
    d2 = date(int(cur_split[0]), int(cur_split[1]), int(cur_split[2]))
    result = abs(d2 - d1).days
    return  result

def list_csv_file(path):
    os.chdir(path)
    os.system('dir /b | findstr ".csv" > DirName.txt')
    fo_DirName = open('DirName.txt', 'r')
    read_DirName = fo_DirName.read()
    list_file = read_DirName.split()
    return list_file

def copy_backup():
    path = r'C:\Users\1000256509\Desktop\data'
    path_backup = r'C:\Users\1000256509\Desktop\data\Backup'
    line_dir = list_dir(path)
    for i in line_dir:
        os.chdir(path + '\\' + i)
        os.system('del / s *.zip')
        os.system('xcopy ' + path_backup + ' ' + path + '\\' + i)


def extract_file(path):
    path_test = r'C:\Users\1000256509\Desktop\data'
    path_backup = r'C:\Users\1000256509\Desktop\data\Backup'
    SaturnPath = path + '\SaturnHD'
    line_dir = list_dir(SaturnPath)
    for i in line_dir:
        dis_path = SaturnPath + '\\' + i
        os.chdir(dis_path)
        os.system('del / s *POSTSIO*')
        list_file = list_zip_file(dis_path)
        for j in list_file:
            file_path = dis_path + '\\' + j
            print(file_path)
            zip_ref = zipfile.ZipFile(file_path, 'r')
            zip_ref.extractall(dis_path)
            zip_ref.close()
        os.chdir(dis_path)
        os.system('del / s *.zip')


def FindData(csv_filename):
    with open(csv_filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        line = csv.reader(csvfile)
        csv_row = []
        CellFolder_data = ''
        DriveSN1_data = ''
        YYYY_data = ''
        MM_data = ''
        DD_data = ''
        FTemp_data = 0
        CellFolder = 999
        DriveSN1 = 999
        FTemp = 999
        YYYY = 999
        MM = 999
        DD = 999
        for row in spamreader:
            csv_row.append(','.join(row))
            # print(', '.join(row))
        for i in range(0, len(csv_row)):
            if csv_row[i].find('YYYY') >= 0:
                split_data = csv_row[i].split(',')
                for j in range(0, len(split_data)):
                    if split_data[j] == 'CellFolder':
                        CellFolder = j
                        # print('CellFolder is ' + str(CellFolder))
                    if split_data[j] == 'DriveSN1':
                        DriveSN1 = j
                        # print('DriveSN1 is ' + str(DriveSN1))
                    if split_data[j] == 'FTemp':
                        FTemp = j
                        # print('DriveSN1 is ' + str(FTemp))
                    if split_data[j] == 'YYYY':
                        YYYY = j
                        # print('DriveSN1 is ' + str(FTemp))
                    if split_data[j] == 'MM':
                        MM = j
                        # print('DriveSN1 is ' + str(FTemp))
                    if split_data[j] == 'DD':
                        DD = j
                        # print('DriveSN1 is ' + str(FTemp))
            else:
                split_data = csv_row[i].split(',')
                for j in range(0, len(split_data)):
                    if j is YYYY: pre_YYYY = str(split_data[j])
                    if j is MM: pre_MM = str(split_data[j])
                    if j is DD: pre_DD = str(split_data[j])
                    if j is CellFolder and CellFolder_data is '':
                        CellFolder_data = split_data[j]
                        # print('CallFolder is : ' + str(CellFolder_data))
                    if j is DriveSN1 and DriveSN1_data is '':
                        DriveSN1_data = split_data[j]
                        # print('DriveSN1_data is : ' + str(DriveSN1_data))
                    if j is FTemp and int(split_data[j]) > (FTemp_data):
                        FTemp_data = int(split_data[j])
                        YYYY_data = pre_YYYY
                        MM_data = pre_MM
                        DD_data = pre_DD
                        # print('FTemp_data is : ' + str(FTemp_data))
        if FTemp_data > 0:
            output_text = str(CellFolder_data) + ',' + str(YYYY_data) + '-' + str(MM_data) + '-' + str(DD_data) + ',' \
                          + str(DriveSN1_data) + ',' + str(FTemp_data)
        else:
            output_text = 'NONE'
        # print ('Data file is : ' + output_text)
        return output_text


def process_data(path):
    path_test = r'C:\Users\1000256509\Desktop\data'
    SaturnPath = path + '\SaturnHD'
    data_list = []
    std_list = []
    line_dir = list_dir(SaturnPath)
    for i in line_dir:
        dis_path = SaturnPath + '\\' + i
        os.chdir(dis_path)
        list_file = list_csv_file(dis_path)
        for j in list_file:
            file_path = dis_path + '\\' + j
            # print(file_path)
            data_list.append(FindData(file_path))
            temp_data = FindData(file_path)
            split_data = temp_data.split(',')
            if len(split_data) > 1:
                std_list.append(int(split_data[len(split_data) - 1]))
        # f = open('Dialy_data.txt','w')
        # f.write('')
        # f.close()
        f = open('Dialy_data.txt', 'w+')
        for j in data_list:
            if j is not 'NONE': f.write(str(j) + '\r\n')
        f.close()
        os.chdir(dis_path)
        os.system('del / s *.csv')
        print(i)
        # print(data_list)
        data_list = []

    for i in line_dir:
        dis_path = SaturnPath + '\\' + i
        os.chdir(dis_path)
        f_file = open('Dialy_data.txt', 'r')
        read_file = f_file.read()
        readline = read_file.split()
        f_file.close()
        f = open('Dialy_data.txt', 'w+')
        std = statistics.stdev(std_list)
        mean = statistics.mean(std_list)
        for j in readline:
            split_data = j.split(',')
            if int(split_data[len(split_data) - 1]) <= mean:
                text = str(j) + ',Green '
                f.write(str(text) + '\r\n')
            elif int(split_data[len(split_data) - 1]) <= (mean + std):
                text = str(j) + ',Yellow '
                f.write(str(text) + '\r\n')
            else:
                text = str(j) + ',Red '
                f.write(str(text) + '\r\n')
        f.close()

    print(statistics.stdev(std_list))
    print(statistics.mean(std_list))
    std_list = []


def compare_data(path):
    path_test = r'C:\Users\1000256509\Desktop\data'
    SaturnPath = path + '\SaturnHD'
    line_dir = list_dir(SaturnPath)
    date_split = str(datetime.datetime.now()).split()
    cur_day = date_split[0]
    for i in line_dir:
        dis_path = SaturnPath + '\\' + i
        os.chdir(dis_path)
        list_file = list_text_file(dis_path)
        if 'Tester_data.txt' not in list_file:
            f = open('Tester_data.txt', 'w+')
            for k in range(1, 145):
                if k < 10:
                    column = '00' + str(k)
                elif k < 100:
                    column = '0' + str(k)
                else:
                    column = str(k)
                for j in range(1, 91):
                    if j < 10:
                        row = '00' + str(j)
                    elif j < 100:
                        row = '0' + str(j)
                    else:
                        row = str(j)
                    f.write('Cell' + str(column) + str(row) + ',' + str(cur_day) + ',NONE,NONE,NONE' + '\r\n')
            f.close()

        f_file = open('Tester_data.txt', 'r')
        read_file = f_file.read()
        testter_readline = read_file.split()
        f_file.close()
        f_file = open('Dialy_data.txt', 'r')
        read_file = f_file.read()
        daily_readline = read_file.split()
        f_file.close()
        testter_cell = {}
        daily_cell = {}
        tester_cell_list = []
        daily_cell_list = []
        for j in daily_readline:
            daily_split = j.split(',')
            daily_cell[daily_split[0]] = j
            daily_cell_list.append(daily_split[0])

        f = open('Tester_data.txt', 'w+')
        for j in testter_readline:
            tester_split = j.split(',')
            diff_day = date_diff(tester_split[1], cur_day)
            b = tester_split[0]
            if tester_split[0] in daily_cell_list:
                testter_cell[str(tester_split[0])] = daily_cell[str(tester_split[0])]
                tester_cell_list.append(tester_split[0])
                f.write(str(testter_cell[tester_split[0]]) + '\r\n')
            else:
                if int(diff_day) > 6:
                    testter_cell[tester_split[0]] = str(tester_split[0]) + ',' + str(cur_day) + ',NONE,NONE,NONE'
                    tester_cell_list.append(tester_split[0])
                    f.write(str(testter_cell[tester_split[0]]) + '\r\n')
                else:
                    testter_cell[tester_split[0]] = j
                    tester_cell_list.append(tester_split[0])
                    f.write(str(testter_cell[tester_split[0]]) + '\r\n')
        f.close()
        print(i)


def cal_ww():
    date_split = str(datetime.datetime.now()).split()
    date_split2 = date_split[0].split('-')
    c_year = date_split2[0]
    c_month = date_split2[1]
    C_day = date_split2[2]
    ref_month = '07'
    ref_day = '01'

    if int(c_month) <= 6:
        ref_year = str(int(c_year) - 1)
        text_year = c_year
    else:
        ref_year = c_year
        text_year = str(int(c_year) + 1)

    d1 = date(int(ref_year), int(ref_month), int(ref_day))
    d2 = date(int(c_year), int(c_month), int(C_day))
    result = abs(d2 - d1).days // 7 + 1
    if int(result) < 10:
        ww = str(text_year) + '0' + str(result)
    else:
        ww = str(text_year) + str(result)
    return ww


def copy_file_ww(path):
    SaturnPath = path + '\SaturnHD'
    line_dir = list_dir(SaturnPath)
    today = date.today().strftime("%A")
    print(today)
    if today in 'Friday':
        for i in line_dir:
            dis_path = SaturnPath + '\\' + i
            os.chdir(dis_path)
            file_name = 'WW' + cal_ww() + '.txt'
            os.system('copy Tester_data.txt ' + file_name)


# Main Program
cur_path = cmd_response('cd')
make_dir(cur_path)
clear_dir(cur_path)
copy_file(cur_path)
extract_file(cur_path)
process_data(cur_path)
compare_data(cur_path)
copy_file_ww(cur_path)

# copy_backup()
