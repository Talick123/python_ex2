import os

def convertSQLtoCSV(file_name):
    file = open(file_name, 'r')

    if not file:
        print("File cannot be opened")

    for line in file:
        line_list = line.split()
        if line_list and line_list[0] == "CREATE" and line_list[1] == "TABLE":
            create_new_csv_table(line_list[2][1:-1], file)
        if line_list and line_list[0] == "INSERT" and line_list[1] == "INTO":
            insert_into(line_list[2][1:-1], line)

    file.close()


def create_new_csv_table(file_name, sql_file):
    csv_file = open("./csv_output/" + file_name + ".csv", "w")
    # csv_file = open("./csv_output/" + file_name + ".csv", "w")
    output_list = []

    for line in sql_file:
        line = line.split()
        if line and line[0][0] == "`":
            # print("34234 " + type(line))
            output_list.append(line[0][1:-1])
        else:
            csv_file.write(','.join(output_list) + '\n')
            break

    csv_file.close()
    return
     # check insert into


def insert_into(file_name, line):
    csv_file = open("./csv_output/" + file_name + ".csv", "a")

    i = line.index('(')

    values = line[i + 1 :-3]
    values = values.split( "),(" )
    csv_file.write('\n'.join(values))

    # csv_file.writelines(values)
    # print(values)
    # csv_file.write('\n')
    csv_file.close()
    return



f = os.getcwd().split("\\")
the_path = "/".join(f)
convertSQLtoCSV(the_path + "/../demo-sql/demo.sql")

# convertSQLtoCSV(r"C:\Users\Tali\Documents\Hadassah\Second Year\Second Semester\OS2\Python Exercises\demo-sql\demo.sql")
