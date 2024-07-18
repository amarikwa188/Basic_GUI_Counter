from tkinter import Tk, Label, Button


class Counter:
    """
    Represents an instance of the counter application.
    """
    def __init__(self) -> None:
        self.root: Tk = Tk()
        self.root.geometry("200x100+500+200")
        self.root.resizable(0,0)
        self.root.title("Counter")

        self.FONT = "Helvetica"

        
        self.counter_text: Label = Label(self.root, text="0",
                                         font=(self.FONT, 25))
        self.counter_text.place(relx=0.5, rely=0.3, anchor="center")

        self.increment: Button = Button(self.root, text="+1", 
                                        command=self.add_count)
        self.increment.place(relx=0.35, rely=0.7, anchor="center")

        self.decrement: Button = Button(self.root, text=-1,
                                        command=self.subtract_count)
        self.decrement.place(relx=0.65, rely=0.7, anchor="center")

        self.root.mainloop()

    
    def add_count(self):
        """
        Increase the counter by one.
        """
        count: int = int(self.counter_text.cget("text"))
        count += 1
        self.counter_text.config(text=str(count))

    def subtract_count(self):
        """
        Decrease the counter by one.
        """
        count: int = int(self.counter_text.cget("text"))
        count -= 1
        self.counter_text.config(text=str(count))


if __name__ == "__main__":
    Counter()