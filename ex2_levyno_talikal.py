def convertSQLtoCSV(file_name):
    file = open(file_name, 'r')

    if not file:
        print("File cannot be opened")

    for line in file:
        line = line.split()
        if line and line[0] == "CREATE" and line[1] == "TABLE":
            print(line[2] + "\n")
            # create_new_csv_table(line[2])




# create_new_csv_table(file_name):
#     csv_file = open(path+name+".csv", "a")
#     # check insert into
#     # close file

convertSQLtoCSV(r"C:\Users\Tali\Documents\Hadassah\Second Year\Second Semester\OS2\Python Exercises\demo-sql\demo.sql")
# convertSQLtoCSV("")
