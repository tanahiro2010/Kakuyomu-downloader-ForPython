import requests
from bs4 import BeautifulSoup
from sys import argv
from kakuyomu import Kakuyomu

def main():
    if len(argv) == 2:
        # Commands
        try:
            book_id = int(argv[1])
        except ValueError:
            print("Please enter a valid book id")
            return
        Kakuyomu_app = Kakuyomu(book_id=book_id)
        data = Kakuyomu_app.download()
        title = data['title']
        text = data['text']

        with open(file='{}.txt'.format(title), mode="w", encoding="utf-8") as file:
            file.write(text)
            file.close()
        print("[LOG] End save")
        return
    else:
        Kakuyomu_app = Kakuyomu()
        while True:
            command = input('Enter book id: ')
            try:
                book_id: int = int(command)
            except ValueError:
                if command == 'exit':
                    print("[LOG] Exiting program")
                    return
                print('Invalid book id')
                continue
            data = Kakuyomu_app.download(book_id=book_id)
            title = data['title']
            text = data['text']
            with open(file='{}.txt'.format(title), mode="w", encoding="utf-8") as file:
                file.write(text)



if __name__ == "__main__":
    main()