import tkinter as tk
window = tk.Tk()
button = tk.Button(text='Lightswitch OFF', bg="white", fg="black")
button.pack(pady = 20, padx = 20)

# schijf hier tussen je code
# def Buttonclick():
    # process = True
    # if tk.Button(bg="white"):                                  #if window['background'] == 'white':
    #     tk.Button(text='lightswitch ON')
    #     print('Lightswitch ON')
    #     tk.Button(bg='black')
    # elif tk.Button(bg='black'):
    #     tk.Button(bg='black')
    #     tk.Button( tk.Button(text='lightswitch OFF'))
    #     print('Lightswitch OFF')
    #     tk.Button(bg='white')
def Buttonclick():
    if window['background'] == 'white':
        window['background'] = 'black'
    else:
        window['background'] = 'white'
    if window['background'] == 'white':
        button.config(text='Lightswitch ON')    #config == veranderen, command == iets gebeurd, doet of aanklikt.
        print('Lightswitch ON')
    elif window['background'] == 'black':
        button.config(text='Lightswitch OFF')
        print('Lightswitch OFF')

# schijf hier tussen je code
button.config(command=Buttonclick)
window.mainloop()
