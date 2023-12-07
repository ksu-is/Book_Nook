import sys
import csv

def add(i):
    with open('data.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(i)

def view():
    data = []
    with open('data.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    print(data)
    return data

#view()

def remove(i):

    def save(j):
        with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(j)
            
    new_list = []
    title = i.title()

    with open('data.csv', 'r')as file:
        reader =csv.reader(file)
        for row in reader:
            new_list.append(row)

            for element in row:
                if element == title:
                    new_list.remove(row)
    save(new_list)

def update(i):

    def update_newlist(j):
        with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(j)

    new_list = []
    title = i[0].title()
    #['Demo','Demo','j.r.r','genre','read','5']
    #Do not change title name!

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)
            
            for element in row:
                if element == title:
                    title = i[1]
                    author = i[2]
                    genre = i[3]
                    status = i[4]
                    rate = i[5]

                    data = [title, author, genre, status, rate]
                    index = new_list.index(row)
                    new_list[index] = data

    update_newlist(new_list)

def search(i):
    data = []
    title = i.title()

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for element in row:
                if element == title:
                    data.append(row)
    
    print(data)
    return data
