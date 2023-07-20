
#V.1.2

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
# редактировать ее --> edit_note      и   удалять. --> TODO


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
            writer.writerow(['date', 'title', 'text'])
    else:
        return
        
      
        
        
       
      
#  
    
def add_note():
    now = datetime.now()
    time = now.strftime("%m/%d/%Y, %H:%M:%S ")
   
    title = input('Введите заголовок заметки: ')
    text = input('Введите текст заметки: ')
  
    df = pd.DataFrame ({
        'date':[time],
        'title': [title],
        'text': [text]
    })
    df = df.set_index('date') 
    df.to_csv(FILENAME, mode='a', index = True, header=False)
    
    



def all_notes():
    
    df = pd.read_csv(FILENAME)
    df['date'] = pd.to_datetime(df.date)
    df.sort_values(by = 'date', ascending= True, inplace= True)
    print(df)


def find_note(index):
    notes = read_notes()
    if index < 0 or index > len(notes):
        print('Note is NOT FOUND')
    else:
        print(notes[index])
   
# Проблема с индексацией, создает новый столбец с индексом   
    
def edit_notes():
    now = datetime.now()
    new_time = now.strftime("%m/%d/%Y, %H:%M:%S ")
    index = int(input('Enter the index of the note: '))
    df = pd.read_csv(FILENAME)
    
    df.loc[index, 'date'] = new_time
    new_title = input('Enter new title: ')
    df.loc[index, 'title'] = new_title
    
    new_text = input('Enter new text: ')
    df.loc[index, 'text'] = new_text
    
    df.to_csv(FILENAME, mode='w', header=True,)
 

# def delete_note():
    
    
while True:
    create_file()
    
    command = input('Enter the command add_note , all_notes , find_note, edit_note ->>> ')
    if command == 'add_note':
        add_note()
    elif command == 'all_notes':
        all_notes()
    elif command == 'find_note':
        index = int(input('Enter the number of the note: '))
        find_note(index)
    elif command == 'edit_note':  
        edit_notes()   
    # elif command == 'delete_note':  
    #     delete_note()  
    else:
        print('Command not found ')
        



