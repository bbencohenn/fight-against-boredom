import time
from tkinter import Tk, Canvas
import os

def loading_animation(): #for option 2
    global current_slice

    canvas.delete("all")

    canvas.create_text(100, 50, text=f"{current_slice}%", font=("Arial", 18))

    slice_width = 30
    fill_level = (current_slice / 100) * canvas.winfo_width()  # Adjust width for canvas size

    canvas.create_rectangle(0, 80, fill_level, 100, fill="green")

    current_slice = (current_slice + 1) % 101

    root.after(20, loading_animation)

def loading_bar(current, total, bar_length=20):
  filled_length = int(round(bar_length * (current / total)))
  bar = '█' * filled_length + '-' * (bar_length - filled_length)
  print(f'Loading: [{bar}] {current}/{total} ({int(current / total * 100)}%)', end='\r')

def ANSI_bar(current, total, bar_length=20):
  filled_length = int(round(bar_length * (current / total)))
  color = RED if current < total else GREEN  # Change color based on completion
  bar = f"{color}{'█' * filled_length}{RESET}{'-' * (bar_length - filled_length)}"
  print(f'Loading: [{bar}] {current}/{total} ({int(current / total * 100)}%)', end='\r')


while True:
  print("""Loading animation options:
    1. Simple
    2. Simple loading bar (in external window)
    3. Simple loading bar (in console)
    4. Loading message with blinking cursor
    5. Coloured loading bar using ANSI Escape Sequences (limited compatibility)""")

  choice = int(input("Pick one (the corresponding number): "))

  if choice == 1:
      animation = ['|', '/', '-', '\\']
      a = 0
      for i in range(20):
          if a == 3:
              a=0
          print(animation[a])
          time.sleep(0.2)
          a += 1
          os.system('cls')

      print("Done!")
      time.sleep(2)
      os.system('cls')

  elif choice == 2:
      root = Tk()
      root.title("Loading Animation")
      canvas = Canvas(root, width=300, height=120)
      canvas.pack()
      current_slice = 0

      loading_animation()
      root.mainloop()

  elif choice == 3:
      os.system('cls')
      for i in range(101):
          loading_bar(i, 100)
          time.sleep(0.05)

      print("\nDone")
      time.sleep(2)
      os.system('cls')

  elif choice == 4:
      message = "Now Loading..."

      for _ in range(30):
        print(message + (" " if _ % 2 else "|"), end='\r')
        time.sleep(0.1)
      
      print("\nDone!")
      time.sleep(2)
      os.system('cls')



  elif choice == 5:
    RED = "\033[1;31m"  # Bright Red
    GREEN = "\033[0;32m"  # Green
    RESET = "\033[0m"  # Reset color


    os.system('cls')

    for i in range(101):
      ANSI_bar(i, 100)
      time.sleep(0.05)

    print("\nDone!")