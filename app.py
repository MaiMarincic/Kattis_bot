import tkinter as tk
import tkinter.font as font
from parse_kattis import parse_kattis
import os

def read_tmp_file():
    path = "tmp.txt"
    with open(path) as file:
        data = file.read()
    data = data.split("\n")
    return "\n".join(data)


def read_file(n):
    path = str(n) + "del.txt"
    if os.path.getsize(path) > 0:
        with open(path) as file:
            data = file.read()
        data = data.split("\n")
        problem_ids = []
        titles = []
        difficultys = []
        for link in data:
            tmp = parse_kattis(link)
            problem_ids.append(tmp[0])
            titles.append(tmp[1])
            difficultys.append(str(tmp[2]))
        return [problem_ids, titles, difficultys]
    else:
        return ["-", "-", "-"]


def open_window_reserve():
    class Reserved(tk.Frame):
            def __init__(self, master=None):
                super().__init__(master)
                self.master = master
                self.master.title("Rezerviraj naloge")
                self.master.geometry("910x410")
                #self.master.configure(background="white")
                self.create_widgets()
            def create_widgets(self):
                self.header()
                #self.body()
                #self.footer()
            def header(self):

                my_font = font.Font(family='Helvetica')
                self.lb_rezervirajNaloge = tk.Label(self.master, text = "Rezerviraj naloge: ", font = my_font)
                self.lb_rezervirajNaloge.grid(row=0, column=0, padx=10, pady=10)

                self.lb_del = tk.Label(self.master, text = str(clicked.get()) + ' del', font = my_font)
                self.lb_del.grid(row=0, column=2, padx=10, pady=10)

                self.lb_dodajURL = tk.Label(self.master, text = "Kattis URL: ", font = my_font)
                self.lb_dodajURL.grid(row=1, column=0, padx=10, pady=10)

                self.inp_field = tk.Entry(self.master, width = 100)
                self.inp_field.grid(row=1, column=1, padx=10, pady=10)

                def add_problem():
                    string = self.inp_field.get()
                    with open('tmp.txt', 'a') as f:
                        f.write(string + '\n')
                    #TODO do shit here dumbaaaasssssss
                    new_text = ""
                    self.inp_field.delete(0, tk.END)
                    self.inp_field.insert(0, new_text)

                    self.lb_added = tk.Label(self.master, text = read_tmp_file(), font = my_font)
                    self.lb_added.grid(row=2, column=1, padx=10, pady=10)
                
                def read_tmp_file_2():
                    string = ""
                    return string
                
                def apply_button():
                    
                    self.lb_added = tk.Label(self.master, text = read_tmp_file_2(), font = my_font)
                    self.lb_added.grid(row=2, column=1, padx=10, pady=10)
                    open('tmp.txt', 'w').close()

                    


                self.bt_problem_button = tk.Button(self.master, text = "Dodaj nalogo", font = my_font, command = add_problem)
                self.bt_problem_button.grid(row=1, column = 2, padx=10, pady=10)

                self.bt_apply = tk.Button(self.master, text = " Apply ", font = my_font, bg="green", fg="white", command = apply_button)
                self.bt_apply.grid(row=2, column = 2, padx=10, pady=10)






    new_w = tk.Toplevel()
    Reserved(new_w)



class MainApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        #self.master.configure(background="white")
        self.master.title("Mai Marincic")
        self.master.geometry("500x410")
        self.create_widgets()

    def create_widgets(self):
        self.header()
        self.body()
        self.footer()

    def header(self):
        
        my_font = font.Font(family='Helvetica')
        self.lb_header1 = tk.Label(self.master, text = " ", font = my_font)
        self.lb_header1.grid(row=1, column=0)
        self.lb_header2 = tk.Label(self.master, text = " ", font = my_font)
        self.lb_header2.grid(row=1, column=1)
        self.lb_header2 = tk.Label(self.master, text = " ", font = my_font)
        self.lb_header2.grid(row=1, column=2)

        self.lb_del = tk.Label(self.master, text="Del:", font = my_font, width = 10, bg = "#ffd27f")
        self.lb_del.grid(row=0, column=0)

        self.lb_tvojeNaloge = tk.Label(self.master, text = "Tvoje Naloge: ", anchor="w", justify="left", font = my_font, width = 30, bg = "#ffd27f")
        self.lb_tvojeNaloge.grid(row=0, column=1)

        self.lb_stTock = tk.Label(self.master, text = "St. Tock: ", font = my_font, width = 10, bg = "#ffd27f")
        self.lb_stTock.grid(row=0, column=2, padx=10, pady=10)

    def body(self):

        my_font = font.Font(family='Helvetica')
        #1 del
        tab1 = read_file(1)
        self.lb_del1 = tk.Label(self.master, text = "1", width = 10, font = my_font, bg = "#ffe8bf")
        self.lb_del1.grid(row=2, column=0)

        self.lb_tvojeNaloge1 = tk.Label(self.master, text = "\n".join(tab1[1]), anchor="w", justify="left", width = 30, font = my_font)
        self.lb_tvojeNaloge1.grid(row=3, column=1)
        self.lb_stTock1 = tk.Label(self.master, text = "\n".join(tab1[2]), anchor="w", justify="left", font = my_font)
        self.lb_stTock1.grid(row=3, column=2)

        #2 del
        tab2 = read_file(2)
        self.lb_del2 = tk.Label(self.master, text = "2", width = 10, font = my_font, bg = "#ffe8bf")
        self.lb_del2.grid(row=4, column=0)

        self.lb_tvojeNaloge1 = tk.Label(self.master, text = "\n".join(tab2[1]), anchor="w", justify="left", width = 30, font = my_font)
        self.lb_tvojeNaloge1.grid(row=5, column=1)
        self.lb_stTock1 = tk.Label(self.master, text = "\n".join(tab2[2]), anchor="w", justify="left", font = my_font)
        self.lb_stTock1.grid(row=5, column=2)

        #3 del
        tab3 = read_file(3)
        self.lb_del2 = tk.Label(self.master, text = "3", width = 10, font = my_font, bg = "#ffe8bf")
        self.lb_del2.grid(row=6, column=0)

        self.lb_tvojeNaloge1 = tk.Label(self.master, text = "\n".join(tab3[1]), anchor="w", justify="left", width = 30, font = my_font)
        self.lb_tvojeNaloge1.grid(row=7, column=1)
        self.lb_stTock1 = tk.Label(self.master, text = "\n".join(tab3[2]), anchor="w", justify="left", font = my_font)
        self.lb_stTock1.grid(row=7, column=2)

        #4 del
        tab4 = read_file(4)
        self.lb_del2 = tk.Label(self.master, text = "4", width = 10, font = my_font, bg = "#ffe8bf")
        self.lb_del2.grid(row=8, column=0)

        self.lb_tvojeNaloge1 = tk.Label(self.master, text = "\n".join(tab4[1]), anchor="w", justify="left", width = 30, font = my_font)
        self.lb_tvojeNaloge1.grid(row=9, column=1)
        self.lb_stTock1 = tk.Label(self.master, text = "\n".join(tab4[2]), anchor="w", justify="left", font = my_font)
        self.lb_stTock1.grid(row=9, column=2)

    def footer(self):
        my_font = font.Font(family='Helvetica')
        self.lb_footer1 = tk.Label(self.master, text = " ", font = my_font, width = 10, bg = "#ffd27f")
        self.lb_footer1.grid(row=10, column=0)
        self.lb_footer2 = tk.Label(self.master, text = "Izberi seminarski del: ", font = my_font, width = 30, bg = "#ffd27f")
        self.lb_footer2.grid(row=10, column=1)
        self.lb_footer3 = tk.Label(self.master, text = " ", font = my_font, width = 10, bg = "#ffd27f")
        self.lb_footer3.grid(row=10, column=2)

        self.ddb_del = tk.OptionMenu(self.master, clicked, 1, 2, 3, 4)
        self.ddb_del.grid(row=11, column=1)

        self.bt_reserve = tk.Button(self.master, text = " Rezerviraj ", font = my_font, bg="green", fg="white", command = open_window_reserve)
        self.bt_reserve.grid(row=11, column=0, padx=10, pady=10)
        self.bt_return = tk.Button(self.master, text = " Vrni ", font = my_font, bg="green", fg="white")
        self.bt_return.grid(row=11, column=2, padx=10, pady=10)



        

root = tk.Tk()
clicked = tk.IntVar()   
clicked.set(1)
app = MainApp(master=root)
app.mainloop()




# def input_field(self):
#     self.inp_field = tk.Entry(self.master, width = 80)
#     self.inp_field.grid(row=1, column=1, padx=10, pady=10)

# def add_problem(self):
#     self.add_problem_button = tk.Button(self.master, text = "Dodaj nalogo")
#     self.add_problem_button.grid(row=1, column = 2, padx=10, pady=10)

# def add_labels(self):
