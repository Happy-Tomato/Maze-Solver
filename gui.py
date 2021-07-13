from tkinter import *
import Maze


def gui():
    root = Tk()
    root.title('Maze Solver')
    root.geometry('800x780')
    count = 0
    button_list = []
    size = 20

    frame_up = LabelFrame(root, text='Functions')
    frame_down = LabelFrame(root, text='Maze')
    frame_up.pack()
    frame_down.pack()
    global supply_mode
    supply_mode = 0
    global src
    src = 0
    global obstacles
    obstacles = []
    global dest
    dest = 1000

    def button_mode(mode):
        global supply_mode
        supply_mode = mode
        print(supply_mode)

    def button_click(button_no):
        global supply_mode
        if supply_mode == 1:                                # starting point    when supply mode = 1
            button_list[button_no].config(bg='#00FF00')
            global src
            src = button_no
            start_button['state'] = DISABLED
            supply_mode = 0
        if supply_mode == 2:                                # for obstacles      when supply_mode = 2
            button_list[button_no].config(bg='#b4b4b4')
            global obstacles
            obstacles.append(button_no)
        if supply_mode == 3:                                # for destination    when supply_mode = 3
            button_list[button_no].config(bg='#FF0000')
            global dest
            dest = button_no
            destination_button['state'] = DISABLED
            supply_mode = 0

    start_button = Button(frame_up, text='Select Starting Point', command=lambda: button_mode(1))
    obstacle_button = Button(frame_up, text='Select Obstacles', command=lambda: button_mode(2))
    destination_button = Button(frame_up, text='Select Destination', command=lambda: button_mode(3))

    start_button.grid(row=0, column=1, sticky="ew", padx=10, pady=5)
    obstacle_button.grid(row=0, column=2, sticky="ew", padx=10, pady=5)
    destination_button.grid(row=0, column=3, sticky="ew", padx=10, pady=5)

    for i in range(size):
        for j in range(size):
            button_list.append(Button(frame_down, text=f'{count}', padx=5, pady=5, command=lambda x=count: button_click(x)))
            button_list[count].grid(row=i, column=j, sticky="ew")
            count += 1

    def solution():                                         # Maze script is called
        pathing = Maze.func(src, obstacles, dest, size)
        for value in pathing:
            button_list[value].config(bg='#00c5ff')         # path color is turned blue
        button_list[src].config(bg='#00FF00')               # source color changed back to green

    go_button = Button(frame_up, text='Find Path', command=solution)
    go_button.grid(row=0, column=4, padx=10, pady=5)

    def restart():
        root.destroy()
        gui()
        
    restart_button = Button(frame_up, text='Clear', command=restart)
    restart_button.grid(row=0, column=5, padx=10, pady=5)

    def sample():
        sample_obstacles = {"Sample 1": [40, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 41, 61, 81, 101, 121, 141, 161, 181, 182, 201, 221, 241, 261, 281, 301, 321, 341, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 378, 379, 339, 338, 318, 298, 278, 258, 238, 239, 219, 199, 179, 159, 139, 119, 99, 79, 59, 39, 43, 63, 83, 103, 45, 65, 85, 123, 105, 143, 144, 145, 146, 186, 185, 184, 183, 122, 106, 108, 88, 68, 48, 26, 90, 110, 49, 50, 51, 52, 53, 91, 92, 93, 95, 115, 135, 155, 175, 195, 215, 235, 255, 172, 212, 152, 151, 150, 149, 148, 187, 189, 188, 169, 230, 231, 232, 229, 228, 227, 54, 55, 56, 77, 57, 117, 97, 118, 156, 176, 196, 216, 236, 178, 173, 174, 225, 224, 223, 243, 263, 283, 323, 324, 325, 326, 327, 328, 329, 309, 289, 269, 249, 265, 285, 286, 287, 267, 297, 296, 295, 294, 293, 292, 252, 253, 291, 330, 331, 332, 333, 334, 335, 336, 337, 264, 288],
                            "Sample 2": [0, 1, 2, 3, 4, 5, 6, 26, 46, 8, 9, 11, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 391, 393, 392, 394, 395, 396, 397, 398, 399, 379, 359, 339, 319, 299, 279, 259, 239, 219, 199, 179, 159, 139, 119, 99, 79, 59, 39, 101, 102, 62, 63, 64, 84, 104, 105, 105, 106, 107, 108, 109, 110, 89, 69, 70, 71, 111, 112, 113, 93, 73, 75, 76, 77, 97, 117, 137, 136, 135, 155, 175, 195, 215, 235, 255, 177, 197, 217, 218, 275, 256, 257, 277, 297, 317, 337, 357, 356, 131, 151, 171, 191, 172, 173, 174, 125, 145, 165, 185, 164, 163, 205, 204, 206, 207, 227, 247, 267, 266, 265, 264, 263, 262, 242, 222, 301, 302, 303, 286, 306, 128, 148, 168, 169, 189, 209, 229, 230, 231, 232, 249, 269, 308, 309, 289, 328, 348, 368, 364, 344, 372, 352, 351, 331, 311, 312, 292, 293],
                            "Sample 3": [180, 161, 142, 123, 104, 85, 66, 47, 28, 9, 30, 51, 72, 93, 114, 135, 156, 177, 198, 201, 222, 243, 263, 264, 285, 306, 327, 348, 369, 390, 371, 352, 333, 314, 295, 276, 257, 238, 219, 124, 125, 126, 127, 145, 165, 29, 49, 69, 89, 90, 129, 130, 131, 132, 152, 172, 192, 212, 211, 210, 168, 169, 230, 250, 250, 270, 175, 194, 174, 224, 205, 225, 183, 227, 247, 248, 308, 328, 313, 312, 311, 275, 255, 252, 253, 273, 273, 350, 370]
                           }
        global obstacles
        obstacles = sample_obstacles[clicked.get()]
        for item in obstacles:
            button_list[item].config(bg='#b4b4b4')

    clicked = StringVar()
    clicked.set("Sample 1")
    sample_label = Label(frame_up, text="Mazes->")
    sample_label.grid(row=0, column=6, padx=10, pady=5)
    dropdown = OptionMenu(frame_up, clicked, "Sample 1", "Sample 2", "Sample 3")
    dropdown.grid(row=0, column=7, padx=10, pady=5)
    level_button = Button(frame_up, text='Select', command= sample)
    level_button.grid(row=0, column=8, padx=10, pady=5)

    mainloop()
if __name__=="__main__":
    gui()

