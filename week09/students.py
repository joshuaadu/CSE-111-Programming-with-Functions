import csv


def main():
    i_number = input("Please enter an I-Number (xxxxxxxxx): ").replace("-", "")
    student_records = read_dictionary("students.csv", 0)
    # print(list(student_records.keys()))
    if i_number in student_records:
        student_record = student_records[i_number]
        print(student_record[1])
    else:
        print("No such student")

def read_dictionary(filename, key_column_index=0):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    with open(filename, "rt") as file:
        reader = csv.reader(file)
        next(reader)
        
        # for line in reader:
        #     print(line)

        return {row[key_column_index]: row for row in reader}
     



if __name__ == "__main__":
    main()