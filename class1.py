class window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('hello with Buttons')

        self.label = tk.label(self,text="chose one")
        self.label.pack(fill=tk.BOTH,expad =1 padx=100,pady=60)

        Button1 = tk.Button(seld,text="button1",command=self.button11)
        button1.pack(side=tk.LEFT,padx(20,0),pady(0,20))

        Button2 = tk.Button(seld,text="button1",command=self.button22)
        button2.pack(side=tk.RIGHT,padx(0,20),pady(0,20))