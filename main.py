from tkinter import *
import datetime
import random

height = 600
width = 600

fps = 60

x_y_ratio = random.uniform(0.25, 0.75)

paused = False

velocity = 100   # px/s

if random.randint(0, 1) == 1:
    x_speed = velocity * x_y_ratio
    y_speed = velocity * (1 - x_y_ratio)
else:
    x_speed = - velocity * x_y_ratio
    y_speed = - velocity * (1 - x_y_ratio)


class CustomCanvas(Canvas):
    def __init__(self):
        Canvas.__init__(self, root, bg="#cccccc")
        self.parent = root

        self.now = datetime.datetime.now()

        self.focus_force()

        self.player1 = 0
        self.player2 = 0

        self.x_speed = x_speed
        self.y_speed = y_speed

        self.x = 300
        self.y = 300
        self.ball = self.create_oval(self.x, self.y, self.x + 10, self.y + 10, fill="#ffffff")

        self.player1_y = 275
        self.player2_y = 275

        self.player1_slider = self.create_rectangle(10, self.player1_y, 20, self.player1_y + 50, fill="#00ff00")
        #self.player1_slider = self.create_rectangle(10, self.player1_y, 20, self.player1_y + 50, fill="#00ff00")
        self.player2_slider = self.create_rectangle(width-10, self.player2_y, width-20, self.player2_y + 50, fill="#00ff00")

        self.bind("s", self.moveplayer1slideup)
        self.bind("w", self.moveplayer1slidedown)

        self.bind("<Down>", self.moveplayer2slideup)
        self.bind("<Up>", self.moveplayer2slidedown)

        #self.paused = False

        self.Update()

    def Update(self):
        global paused
        self.delete(self.ball)
        self.x = self.x + self.x_speed / fps
        self.y = self.y + self.y_speed / fps

        self.ball = self.create_oval(self.x, self.y, self.x+10, self.y+10, fill="#0000ff")

        print(self.x)

        if self.y <= 0 or self.y + 10 >= height:
            self.y_speed = - self.y_speed
        elif self.player1_y <= self.y <= self.player1_y + 50 and 10 <= self.x <= 20:
            self.x_speed = - self.x_speed
        elif self.player2_y <= self.y <= self.player2_y + 50 and width-10 >= self.x >= width-20:
            self.x_speed = - self.x_speed
        elif self.x <= 0:
            print(1)
            self.Win(self.player2)
        elif self.x+10 >= width:
            print(1)
            self.Win(self.player1)

        #if (self.now-datetime.datetime.now()).seconds >= 10:
        #    self.x_speed *= 1.05
        #    self.y_speed *= 1.05
        #    self.now = datetime.datetime.now()

        print(paused)

        if paused == False:
            self.after(round(1000 / fps), self.Update)

    def Win(self, player):
        global paused
        player += 1
        paused = True
        message = Tk()
        if self.player1 == 3:
            label = Label(message, text="Player 1 wins")
            label.pack()
            button = Button(message, text="Restart", command=lambda: self.restart(True, message))
        elif self.player2 == 3:
            message = Tk()
            label = Label(message, text="Player 2 wins")
            label.pack()
            button = Button(message, text="Restart", command=lambda: self.restart(True, message))
        else:
            button = Button(message, text="Restart", command=lambda: self.restart(False, message))
        button.pack()


    def restart(self, full_restart, window):
        global paused

        window.destroy()

        if full_restart:
            self.player1 = 0
            self.player2 = 0
            self.now = datetime.datetime.now()

        paused = False

        self.x = 300
        self.y = 300

        x_y_ratio = random.uniform(0.25, 0.75)
        print(x_y_ratio)

        velocity = 100  # px/s
        fps = 60

        if random.randint(0, 1) == 1:
            self.x_speed = velocity * x_y_ratio
            self.y_speed = velocity * (1 - x_y_ratio)
        else:
            self.x_speed = - velocity * x_y_ratio
            self.y_speed = - velocity * (1 - x_y_ratio)

        self.update()

    def moveplayer1slideup(self, none):
        #print(1)
        self.delete(self.player1_slider)

        if self.player1_y != 0:
            self.player1_y += 10

        self.player1_slider = self.create_rectangle(10, self.player1_y, 20, self.player1_y + 50, fill="#00ff00")

    def moveplayer1slidedown(self, none):
        #print(2)
        self.delete(self.player1_slider)

        if self.player1_y != height:
            self.player1_y -= 10

        self.player1_slider = self.create_rectangle(10, self.player1_y, 20, self.player1_y + 50, fill="#00ff00")

    def moveplayer2slideup(self, none):
        #print(3)
        self.delete(self.player2_slider)

        if self.player2_y != 0:
            self.player2_y += 10

        self.player2_slider = self.create_rectangle(width-10, self.player2_y, width-20, self.player2_y + 50, fill="#00ff00")

    def moveplayer2slidedown(self, none):
        #print(4)
        self.delete(self.player2_slider)

        if self.player2_y != height:
            self.player2_y -= 10

        self.player2_slider = self.create_rectangle(width-10, self.player2_y, width-20, self.player2_y + 50, fill="#00ff00")

root = Tk()
root.geometry("600x600")
root.title("Ping Pong")

canvas = CustomCanvas()
canvas.place(x=0, y=0, height=600, width=600)

root.mainloop()
