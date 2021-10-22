from tkinter import *
from tkinter import messagebox

class player():
  # red rec
  def __init__(self, canvas, x, y):
    self.canvas = canvas
    self.id = canvas.create_rectangle(x * 30, y * 30, x * 30 + 30, y * 30 + 30,fill="red")
    self.x, self.y = x, y
    self.nx, self.ny = x, y
  
  # key setting
  def move(self, direction):
    if direction == 'w':
      self.nx, self.ny = self.x, self.y - 1
    elif direction == 'a':
      self.nx, self.ny = self.x - 1, self.y
    elif direction == 's':
      self.nx, self.ny = self.x, self.y + 1
    elif direction == 'd':
      self.nx, self.ny = self.x + 1, self.y
  
    # wall break setting
    if not self.is_collide():
      self.canvas.move(self.id, (self.nx - self.x) * 30, (self.ny - self.y) * 30)
      self.x, self.y = self.nx, self.ny
    
    # finish rec setting = 3
    if map[self.y][self.x] == 3:
      messagebox.showinfo(title="sucsses", message="미로를 통과했습니다.")

  # wall setting
  def is_collide(self):
    if map[self.ny][self.nx] == 1:
      return True
    else:
      return False

# key event
def keyevent(event):
  Player.move(repr(event.char).strip("'"))

# caption name
root = Tk()
root.title("미로 찾기")
root.resizable(False,False)

# screen size & setting
width, height = 540, 540
x, y = (root.winfo_screenmmwidth() - width) / 2, (root.winfo_screenmmheight() - height) / 2
root.geometry("%dx%d+%d+%d" % (width, height, x, y))

# canvas setting
canvas = Canvas(root,width=width, height=height, bg="white")
canvas.bind("<Key>",keyevent)
canvas.focus_set()
canvas.pack()

map = [
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 2, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 3, 1, 1, 1, 1],
  [1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1],
  [1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
  [1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
  [1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
  [1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1],
  [1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1],
  [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1],
  [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
  [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
  [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1],
  [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1],
  [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1],
  [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
  [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

for y in range(len(map[0])):
  for x in range(len(map[y])):
    if map[y][x] == 1:
      canvas.create_rectangle(x * 30, y * 30, x * 30 + 30, y * 30 + 30,fill="black")
    elif map[y][x] == 2:
      Player = player(canvas, x, y)
    elif map[y][x] == 3:
      canvas.create_rectangle(x * 30, y * 30, x * 30 + 30, y * 30 + 30,fill="blue")
  
root.mainloop()