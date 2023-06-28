import csv


PRODUCT_ID_INDEX = 0
PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2
PRODUCT_QUANTITY_INDEX = 1

def main():
    products_dict = read_dictionary("products.csv", PRODUCT_ID_INDEX)
    print("All Products")
    print(products_dict)
    print()

    with open("requests.csv", "rt") as file:
        requests = csv.reader(file)
        next(requests)
        print("Requested Items")
        for request in requests:
            product = products_dict[request[PRODUCT_ID_INDEX]]
            print(F"{product[PRODUCT_NAME_INDEX]}: {request[PRODUCT_QUANTITY_INDEX]} @ {product[PRODUCT_PRICE_INDEX]}")
            



def read_dictionary(filename, key_column_index):
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