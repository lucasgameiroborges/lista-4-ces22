import tkinter as tk



class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.historico = []
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Emitir extrato"
        self.hi_there["command"] = self.say_extrato
        self.hi_there.pack(side="left")

        self.saldo = tk.Button(self)
        self.saldo["text"] = "Consultar saldo"
        self.saldo["command"] = self.say_saldo
        self.saldo.pack(side="left")

        self.trans = tk.Button(self)
        self.trans["text"] = "Realizar transferência"
        self.trans["command"] = self.say_trans
        self.trans.pack(side="left")

        self.hist = tk.Button(self)
        self.hist["text"] = "Histórico de operações"
        self.hist["command"] = self.say_historico
        self.hist.pack(side="left")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_historico(self):
        print("\n Histórico de Operações (ordem de chamada): \n")
        print(self.historico)

    def say_trans(self):
        self.historico.append("Transferência")
        print("Você realizou uma transferência.")

    def say_extrato(self):
        self.historico.append("Emissão de extrato")
        print("Você emitiu seu extrato.")

    def say_saldo(self):
        self.historico.append("Consulta de Saldo")
        print("Você consultou seu saldo.")


root = tk.Tk()
app = Application(master=root)
app.master.minsize(600, 100)
app.master.title("CES22 - Bank App")
app.mainloop()