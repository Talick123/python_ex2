
import os

def convertSQLtoCSV(file_name):
    file = open(file_name, 'r')

    if not file:
        print("File cannot be opened")

    for line in file:
        line = line.split()
        if line and line[0] == "CREATE" and line[1] == "TABLE":
            # print(line[2][1:-1] + "\n")
            create_new_csv_table(line[2][1:-1], file)


def create_new_csv_table(file_name, sql_file):
     
    csv_file = open("./csv_output/" + file_name + ".csv", "w")
    output_list = []

    for line in sql_file:        
        line = line.split()
        if line and line[0][0] == "`":
            output_list.append(line[0][1:-1])
        else:
            csv_file.write(','.join(output_list) + '\n') 
            break

    csv_file.close()
     # insert columns

     # check insert into
     # close file

f = os.getcwd().split("\\")
the_path = "/".join(f)
convertSQLtoCSV(the_path + "/../demo-sql/demo.sql")

# convertSQLtoCSV(r"C:\Users\Tali\Documents\Hadassah\Second Year\Second Semester\OS2\Python Exercises\demo-sql\demo.sql")