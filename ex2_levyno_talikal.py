'''
Written by: Noga Levy (ID: 315260927, login: levyno)
             and Tali Kalev (ID: 208629691, login: talikal)

Goal of the Program: the program recieves sql file and convert to csv files
                    for each table with its content.
                    ~ AND THATS IT ~
'''

from os.path import exists

def convertSQLtoCSV(file_name):
    '''open sql file to read and create csv files for each table with content'''
    # open sql file to read
    file = open(file_name, 'r')
    if not file:
        print("File cannot be opened")

    tables = {}
    for line in file:
        line_list = line.split()
        if line_list and line_list[0] == "CREATE" and line_list[1] == "TABLE":
            tables[line_list[2][1:-1]] = add_column_labels(file)
        if line_list and line_list[0] == "INSERT" and line_list[1] == "INTO":
            insert_into(line_list[2][1:-1], line, tables)

    file.close()

def add_column_labels(sql_file):
    '''recieve sql file and read the table's columns name -
    return string with the names'''
    columns = []

    for line in sql_file:
        line = line.split()
        if line and line[0][0] == "`":
            columns.append(line[0][1:-1])
        else:
            break;

    return ','.join(columns)


def insert_into(file_name, line, tables):
    ''' create csv file and fill it with the table content
        or adds to already existing file'''

    # check if the file already exist
    file_exists = exists("./" + file_name + ".csv")

    csv_file = open("./" + file_name + ".csv", "a")

    if not file_exists:
        csv_file.write(tables[file_name] + '\n')

    # find where the table values begin
    i = line.index('(')

    values = line[i + 1 :-3]
    values = values.split( "),(" )
    csv_file.write('\n'.join(values))

    csv_file.close()
    return

path = "C:/Users/Tali/Documents/Hadassah/Second Year/Second Semester/OS2/Python Exercises/demo-sql/demo.sql"
convertSQLtoCSV(path)
