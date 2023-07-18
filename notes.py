
#V.1.1

# Приложение должно запускаться без ошибок, 
# должно уметь сохранять данные
# в файл,  -> create_file, add_note
# уметь читать данные из файла, --> all_notes
# делать выборку по дате,  -->   all_notes показывает отфильтрованные по дате записки
# выводить на
# экран выбранную запись, --> find_note
# выводить на экран весь список записок, --> all_notes
# добавлять
# записку, --> add_note
# редактировать ее и удалять. --> TODO


from datetime import date, datetime
import csv
import os
import pandas as pd

now = datetime.now()

current_time = now.strftime("%H:%M:%S ")
current_date = date.today()  

FILENAME = 'notes.csv'




def read_notes():
    with open(FILENAME, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        return list(reader)
    
def write_notes(notes):
    with open(FILENAME, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerows(notes)
def create_file():
    if (os.path.exists(FILENAME) == False):
        with open(FILENAME, 'w+', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['date','title', 'text'])
    else:
        return
        
        # writer = csv.writer(csvfile, delimiter=';')
        
        
       
      
#  
    
def add_note():
   
    # date = date.today()
    now = datetime.now()
    time = now.strftime("%m/%d/%Y, %H:%M:%S ")
    # date = now.strftime("%m/%d/%Y")
    title = input('Введите заголовок заметки: ')
    text = input('Введите текст заметки: ')
    # notes = read_notes()
    # new_note = [title,";", text,";"]
    # new_date = [time]
    df = pd.DataFrame ({

        'date':[time],
        'title': [title],
        'text': [text]
        
    })
    df = df.set_index('date') 
    df.to_csv(FILENAME, mode='a', header=False)
    
    # print(df)
    # notes.append(new_date, new_note)
    # write_notes(notes)
    



def all_notes():
    

    # with open(FILENAME,'r') as file:
    #     csvreader = csv.reader(file)
    #     # for row in csvreader:
    #         # print(row)
    df = pd.read_csv(FILENAME)
    df['date'] = pd.to_datetime(df.date)
    df.sort_values(by = 'date', ascending= True, inplace= True)
    print(df)


def find_note(index):
    notes = read_notes()
    if index < 0 or index > len(notes):
        print('Note is NOT FOUND')
    else:
        print(notes[index+1])
   
    
    
    
# def show_notes():
#     notes = read_notes()
#     for i, (date, time, title, text) in enumerate(notes, start=1):
#         print(f'{i}.{date};{time}|{title}')
 
 
 
 
    
while True:
    create_file()
    command = input('Введите команду add_note , all_notes , find_note ->>> ')
    if command == 'add_note':
        add_note()
    elif command == 'all_notes':
        all_notes()
    elif command == 'find_note':
        index = int(input('Введите индекс записи: '))
        find_note(index)
    elif command == 'read_file':  
        read_notes()
        break
    else:
        print('Command not found ')
        
# def getcommands()

# notes_name = input("Введите заголовок вашей заметки: ")


