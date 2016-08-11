from tkinter import *
import webbrowser

windowSizeX = "300"
windowSizeY = "300"

# prints out the registered browsers I can use
# print(webbrowser._tryorder)

# registers firefox (i think this is done correctly)
firefoxPath = "C:/Program Files (x86)/Mozilla Firefox/firefox.exe %s &"
firefoxBrowser = webbrowser.get(firefoxPath)

# web links to be opened in tabs
urlYoutube = "https://www.youtube.com/"
urlReddit = "https://us.reddit.com/"


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)

        # exit button
        quitButton = Button(self, text="Exit", command=self.client_exit)
        quitButton.place(x=270, y=270)

        # start firefox/chrome browser button
        internetButton = Button(self, text="Open Browser", command=self.open_browser)
        internetButton.place(x=150, y=150)

    # browser button command
    def open_browser(self):
        print("Open browser button pressed")
        firefoxBrowser.open(urlYoutube)
        firefoxBrowser.open(urlReddit)

    def client_exit(self):
        print("Exit button pressed")
        exit()

# base window variable
root = Tk()
app = Window(root)

# Sets size for window
root.geometry(windowSizeX + "x" + windowSizeY)
root.mainloop()

# Manual exit confirmation written by me
print("Program has reached this point.")
