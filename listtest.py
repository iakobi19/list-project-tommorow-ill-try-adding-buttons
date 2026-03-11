import tkinter
#window setup stuff
window = tkinter.Tk()
window.title("simple window fr")
window.geometry("430x330")
window.configure(bg="black")

#list (why is this so hard)
my_list = tkinter.Listbox(window,bg="#333333",fg="white",font=("Arial", 12))

 #actual items on list
my_list.insert(1, "fruit")
my_list.insert(2, "vegetables")
my_list.insert(3, "i ran outta ideas")
my_list.insert(4, "love") 
my_list.insert(5, "beans")

#ACTUALLY putting the list on the screen claude helped!
my_list.pack(fill=tkinter.BOTH, expand=True, padx=40)


#trying to make ✓ def on_select(suffering):
def mark_done(event):
    selection = my_list.curselection()
    if selection:
        index = selection[0]
        text = my_list.get(index)
        if not text.startswith("✓ "):  
            my_list.delete(index)
            my_list.insert(index, "✓ " + text)
        else:
            my_list.delete(index)
            my_list.insert(index, text[2:]) 
my_list.bind('<<ListboxSelect>>', mark_done)
   
#non interactable text at the bottom
label = tkinter.Label(window, text="za list", bg="red", fg="white", font=("Arial", 12), relief=tkinter.SOLID, borderwidth=2, highlightbackground="red", highlightthickness=5)
label.pack(pady=10)


window.mainloop()