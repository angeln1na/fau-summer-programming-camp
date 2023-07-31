# WARNING: tkinter library may have some issues 
# import the library
from tkinter import filedialog
def open_file():
  filetypes = (
    ("Image files", "*.png *.jpg *.jpeg *.gif"),
    ("All files", "*.*")
  )
  filepath = filedialog.askopenfilename(filetypes=filetypes)
  if filepath:
    ##### Display the selected image #####
    # 2. create a variable img and set it equal to PhotoImage where it is passing file=filepath
    
    # 3. write img_label.config and pass image=img

    # 4. write img_label.image and set it qual to img
def exit_program():

  # 5. write root.destroy open & close parentheses

# 6. create the variable root and set it eqwual to Tk like in the example program
##### Create a label for displaying the image #####
# 7. write image_label is equal to Label passing root

# 8. Create a button to open a file dialog for image selection
open_button = Button(root, text="Open Image", command=open_file)

##### Create a button to exit the program ###
# 9. similar to the open_button copy but make your own variable and remember the commands are calling the def

#### Pack the widgets onto the window ####
# 10. 1st for image
img_label.pack()

# 11. 2nd for opening

# 12. 3rd for exiting

#####How does the program start?#####
# 13. Similar to the example program
