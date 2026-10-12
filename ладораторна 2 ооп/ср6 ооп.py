import tkinter as tk

class SignalLight:
    def __init__(self, canvas, x, y, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = color
        self.active = False

        self.circle = canvas.create_oval(
            x - 40, y - 40,
            x + 40, y + 40,
            fill="gray",
            outline="white",
            width=3
        )

        canvas.tag_bind(
            self.circle,
            "<Button-1>",
            self.turn_on
        )

    def turn_on(self, event):
        for light in lights:
            light.turn_off()

        self.active = True
        self.canvas.itemconfig(
            self.circle,
            fill=self.color
        )

    def turn_off(self):
        self.active = False
        self.canvas.itemconfig(
            self.circle,
            fill="gray"
        )


def create_beacon():
    global lights

    canvas.delete("all")

    width = canvas.winfo_width()
    height = canvas.winfo_height()

    center_x = width // 2
    center_y = height // 2

    canvas.create_rectangle(
        center_x - 70,
        center_y - 190,
        center_x + 70,
        center_y + 190,
        fill="#444444",
        outline="white",
        width=3
    )

    canvas.create_text(
        center_x,
        center_y - 230,
        text="SHORELINE TOTTORI",
        fill="white",
        font=("Arial", 20, "bold")
    )

    lights = [
        SignalLight(canvas, center_x, center_y - 110, "red"),
        SignalLight(canvas, center_x, center_y, "yellow"),
        SignalLight(canvas, center_x, center_y + 110, "green")
    ]


def resize(event):
    create_beacon()


root = tk.Tk()
root.title("Shoreline Tottori — Сигнальний маяк")
root.geometry("600x600")
root.minsize(400, 400)

canvas = tk.Canvas(
    root,
    bg="#023EBA"
)

canvas.pack(
    fill="both",
    expand=True
)

lights = []

root.bind("<Configure>", resize)

root.mainloop()