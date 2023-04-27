import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
    return data


if __name__ == '__main__':
    data = read_csv('/Users/macbookdejuan/Library/CloudStorage/OneDrive-Personal/Code/Platzi/Python_Back_End/PIP y entornos virtuales/py-project/data/data.csv')
    print(data[0])