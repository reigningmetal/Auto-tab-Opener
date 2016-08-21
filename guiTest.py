from tkinter import *
import webbrowser

# window size and position variables
windowSizeX = "300"
windowSizeY = "300"

quitButtonX = 265
quitButtonY = 270

entertainTabsButtonX = 100
entertainTabsButtonY = 100

workingTabsButtonX = 50
workingTabsButtonY = 50


# prints out the registered browsers I can use
# print(webbrowser._tryorder)

# registers firefox (i think this is done correctly)
firefoxPath = "C:/Program Files (x86)/Mozilla Firefox/firefox.exe %s &"
firefoxBrowser = webbrowser.get(firefoxPath)

# web links to be opened in tabs
urlYoutube = "https://www.youtube.com/"
urlReddit = "https://us.reddit.com/"
urlWorkReddit = "https://us.reddit.com/"
urlStackOverflow = "http://stackoverflow.com/"


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Auto-Tab-Opener")
        self.pack(fill=BOTH, expand=1)

        # exit button
        quitButton = Button(self, text="Exit", command=self.client_exit)
        quitButton.place(x=quitButtonX, y=quitButtonY)

        # start firefox / chrome entertainment tabs button
        entertainTabsButton = Button(self, text="Entertainment Mode", command=self.entertain_Button)
        entertainTabsButton.place(x=entertainTabsButtonX, y=entertainTabsButtonY)

        # start firefox / chrome working tabs button
        workingTabsButton = Button(self, text="Working Mode", command=self.working_Button)
        workingTabsButton.place(x=workingTabsButtonX, y=workingTabsButtonY)

    # browser button command
    def entertain_Button(self):
        print("entertainment button pressed")
        firefoxBrowser.open(urlYoutube)
        firefoxBrowser.open(urlReddit)

    # browser button command 2
    def working_Button(self):
        print("working button pressed")
        firefoxBrowser.open(urlWorkReddit)
        firefoxBrowser.open(urlStackOverflow)

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
