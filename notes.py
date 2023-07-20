
#V.3.0

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
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows(notes)


def create_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, 'w+', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['id', 'date', 'title', 'text'])
    else:
        return


def add_note():
    now = datetime.now()
    time = now.strftime("%m/%d/%Y, %H:%M:%S ")

    title = input('Enter the title of the note: ')
    text = input('Enter the text of the note: ')

    df = pd.read_csv(FILENAME)

    new_id = len(df) + 1  # Calculate the new ID as the current length of DataFrame + 1

    new_note = pd.DataFrame({
        'id': [new_id],
        'date': [time],
        'title': [title],
        'text': [text]
    })

    df = pd.concat([df, new_note], ignore_index=True)

    df.to_csv(FILENAME, index=False)


def all_notes():
    df = pd.read_csv(FILENAME)
    df['date'] = pd.to_datetime(df.date)
    df.sort_values(by='date', ascending=True, inplace=True)
    print(df)


def find_note(note_id):
    df = pd.read_csv(FILENAME)
    note = df[df['id'] == note_id]
    if not note.empty:
        print(note)
    else:
        print('Note not found')


def edit_notes():
    now = datetime.now()
    new_time = now.strftime("%m/%d/%Y, %H:%M:%S ")
    note_id = int(input('Enter the ID of the note: '))
    df = pd.read_csv(FILENAME)

    note = df[df['id'] == note_id]
    if not note.empty:
        index = note.index[0]  # Get the index of the matching note
        print('Old Title:', note['title'].values[0])
        print('Old Text:', note['text'].values[0])

        choice = input('Do you want to edit the title and text? (yes/no): ').lower()
        if choice == 'yes':
            new_title = input('Enter new title: ')
            new_text = input('Enter new text: ')
        else:
            new_title = note['title'].values[0]
            new_text = note['text'].values[0]

        df.at[index, 'date'] = new_time
        df.at[index, 'title'] = new_title
        df.at[index, 'text'] = new_text

        df.to_csv(FILENAME, index=False)
    else:
        print('Note not found')


def delete_note():
    note_id = int(input('Enter the ID of the note you want to delete: '))
    df = pd.read_csv(FILENAME)

    note = df[df['id'] == note_id]
    if not note.empty:
        index = note.index[0]  # Get the index of the matching note
        df.drop(index, inplace=True)
        df.to_csv(FILENAME, index=False)
        print('Note deleted successfully.')
    else:
        print('Note not found')


while True:
    create_file()

    command = input('Enter the command add_note, all_notes, find_note, edit_note, delete_note ->>> ')
    if command == 'add_note':
        add_note()
    elif command == 'all_notes':
        all_notes()
    elif command == 'find_note':
        note_id = int(input('Enter the ID of the note: '))
        find_note(note_id)
    elif command == 'edit_note':
        edit_notes()
    elif command == 'delete_note':
        delete_note()
    else:
        print('Command not found ')
