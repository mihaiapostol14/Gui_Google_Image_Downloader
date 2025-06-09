import os

import customtkinter
from icrawler.builtin import GoogleImageCrawler

from helper import Helper


class Frame(customtkinter.CTkFrame,Helper):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


        # add widgets onto the frame, for example:
        # add widgets to app
        self.search = None
        self.max_num = None
        self.label = customtkinter.CTkLabel(self, text='Gui Google Image Downloader', font=('Arial',20))
        self.label.pack(padx=10, pady=10)

        self.search_entry = customtkinter.CTkEntry(self, width=350, height=40,placeholder_text='Typing Search Image')
        self.search_entry.pack(padx=10, pady=10)


        self.max_count = customtkinter.CTkEntry(self, width=350, height=40,placeholder_text='Typing Count Image')
        self.max_count.pack(padx=10, pady=10)

        self.count_image_label = customtkinter.CTkLabel(self, text='', font=('Arial', 20))
        self.count_image_label.pack(padx=10, pady=5)

        self.download_button = customtkinter.CTkButton(self, text='Download',command=self.download_image)
        self.download_button.pack(padx=20, pady=10)

        self.open_dir_button = customtkinter.CTkButton(self, text='Open', command=self.open_output_directory)
        self.open_dir_button.pack(padx=20, pady=10)

    def download_image(self):
        # TODO: This statement will be to create folder if she was not created
        self.search = self.search_entry.get()
        self.max_num = int(self.max_count.get())

        if not os.path.exists(f'{self.search}'):
            os.mkdir(self.search)

        google_crawler = GoogleImageCrawler(storage={'root_dir': f'{self.search}'})
        google_crawler.crawl(keyword=self.search, max_num=self.max_num)
        return self.count_image()

    def count_image(self):
        if self.directory_exists(directory_name=self.search):
            self.count_image_label.configure(text=f'Count image {self.search} is {len(os.listdir(self.search))}')
            self.open_dir_button.configure(text=f'Open {self.search}')



    def open_output_directory(self):
        if self.directory_exists(directory_name=self.search):
            os.startfile(self.search)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Gui Google Image Downloader')
        self.geometry("350x400")
        self.resizable(False,False)
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.frame = Frame(master=self)
        self.frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")



app = App()
app.mainloop()

