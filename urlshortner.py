import tkinter as tk
import tkinter.ttk as ttk
import requests

class URLShortner:
    def __init__(self, master=None):
        # build ui
        self.main_window = tk.Tk() if master is None else tk.Toplevel(master)
        self.frm_main = tk.Frame(self.main_window)
        self.lbl_app_name = tk.Label(self.frm_main)
        self.lbl_app_name.configure(background='#6200c4', font='{Arial} 24 {bold}', foreground='#ffffff', takefocus=False)
        self.lbl_app_name.configure(text='URL Shortner')
        self.lbl_app_name.pack(pady='30', side='top')
        self.ent_long_url = tk.Entry(self.frm_main)
        self.long_url = tk.StringVar(value='enter a long url here...')
        self.ent_long_url.configure(font='{Arial} 12 {}', justify='center', textvariable=self.long_url, width='80')
        _text_ = '''enter a long url here...'''
        self.ent_long_url.delete('0', 'end')
        self.ent_long_url.insert('0', _text_)
        self.ent_long_url.pack(side='top')
        self.btn_shorten = tk.Button(self.frm_main)
        self.btn_shorten.configure(background='#ffffff', font='{Arial} 16 {bold}', foreground='#8000ff', text='Click to Shorten')
        self.btn_shorten.pack(pady='50', side='top')
        self.btn_shorten.configure(command=self.make_short_link)
        self.short_url = tk.StringVar()
        self.ent_short_url = tk.Entry(self.frm_main)
        self.ent_short_url.configure(background='#6200c4', borderwidth='0', font='{Arial} 24 {}', foreground='#ffffff', textvariable=self.short_url)
        self.ent_short_url.configure(justify='center', readonlybackground='#6200c4', relief='flat', state='readonly')
        self.ent_short_url.configure(width='25')
        self.ent_short_url.pack(pady='50', side='top')
        self.frm_main.configure(background='#6200c4', height='480', width='800')
        self.frm_main.pack(side='top')
        self.main_window.configure(background='#6200c4', height='200', width='200')
        self.main_window.geometry('800x480')
        self.main_window.resizable(False, False)
        self.main_window.title('URL Shortner')

        # Main widget
        self.mainwindow = self.main_window

    def make_short_link(self):
        long_url = self.long_url.get()
        if long_url.startswith('http://') or long_url.startswith('https://') or long_url.startswith('ftp://'):

            headers = {
                'Authorization': 'Bearer 90344ea1864ca288d97775403390a23ae6f9e83b',
                'Content-Type': 'application/json',
            }

            data = '{ "long_url": "'+ self.long_url.get() +'", "domain": "bit.ly" }'

            response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)

            res = response.json()

            self.short_url.set(res['link'])


    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':
    app = URLShortner()
    app.run()

