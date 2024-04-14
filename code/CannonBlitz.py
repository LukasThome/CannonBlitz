import tkinter as tk
from tkinter import messagebox
import random

class BattlefieldGame:
    def __init__(self, master):
        self.master = master
        self.rows = 3
        self.cols = 5
        self.current_player = 1
        self.saldo = [0, 0]  # Saldo de cada jogador
        self.create_boards()
        self.create_controls()
        self.add_fixed_bases(self.board1)  # Adiciona bases fixas para o jogador
        self.add_fixed_bases(self.board2)  # Adiciona bases fixas para o oponente


    def create_boards(self):
        frame1 = tk.Frame(self.master)
        frame1.grid(row=0, column=0, padx=10, pady=10)
        self.board1 = []
        for i in range(self.rows):
            row_buttons = []
            for j in range(self.cols):
                button = tk.Button(frame1, width=5, height=2, command=lambda row=i, col=j, player=1: self.button_click(row, col, player))
                button.grid(row=i, column=j, padx=1, pady=1)
                row_buttons.append(button)
            self.board1.append(row_buttons)

        tk.Label(self.master, text="").grid(row=1, column=0) #laber pra ter uma espaço em branco entre os dois grids

    
        frame2 = tk.Frame(self.master)
        frame2.grid(row=2, column=0, padx=3, pady=3)
        self.board2 = []
        for i in range(self.rows):
            row_buttons = []
            for j in range(self.cols):
                button = tk.Button(frame2, width=5, height=2, command=lambda row=i, col=j, player=2: self.button_click(row, col, player))
                button.grid(row=i, column=j, padx=1, pady=1)
                row_buttons.append(button)
            self.board2.append(row_buttons)

    def add_fixed_bases(self, board):
        fixed_base_positions = [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)]  # Posições fixas das bases
        for row, col in fixed_base_positions:
            self.set_base_position(board[row][col])

    def create_controls(self):
        control_frame = tk.Frame(self.master)
        control_frame.grid(row=0, column=1, rowspan=3, padx=10, pady=10)

        self.saldo_label = tk.Label(control_frame, text=f"Saldo: {self.saldo[0]}")
        self.saldo_label.grid(row=0, column=0, padx=3, pady=3)

        self.comprar_base_button = tk.Button(control_frame, text="Comprar Base $2", command=self.comprar_base, state=tk.ACTIVE)
        self.comprar_base_button.grid(row=1, column=0, padx=3, pady=3)

        self.tiro_preciso_button = tk.Button(control_frame, text="Tiro Preciso $1", command=self.tiro_preciso, state=tk.ACTIVE)
        self.tiro_preciso_button.grid(row=2, column=0, padx=3, pady=3)

        self.base_button = tk.Button(control_frame, text="Tiro Normal", command=self.tiro, state=tk.ACTIVE)
        self.base_button.grid(row=3, column=0, padx=3, pady=3)

        self.tiro_forte_button = tk.Button(control_frame, text="Tiro Forte $3", command=self.tiro_forte, state=tk.ACTIVE)
        self.tiro_forte_button.grid(row=4, column=0, padx=3, pady=3)


    def tiro_preciso(self):
        if self.saldo[self.current_player - 1] >= 1:
            # Deduz 1 do saldo do jogador atual
            self.saldo[self.current_player - 1] -= 1
            # Atualiza a exibição do saldo
            self.saldo_label.config(text=f"Saldo: {self.saldo[self.current_player - 1]}")
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)

            if self.board1[row][col]['bg'] == 'blue':  # Verifica se a posição do campo inimigo tem uma base
                self.saldo[0] += 1  # Adiciona 1 ao saldo do jogador 1
                self.saldo_label.config(text=f"Saldo: {self.saldo[0]}")  # Atualiza a exibição do saldo


            self.board1[row][col].configure(bg="red")
            self.master.after(2000, lambda: self.reset_board(row, col, self.board1))

           
            self.master.after(2000, self.computer_move)
        else:
            messagebox.showerror("Saldo Insuficiente", "Você não tem saldo suficiente para realizar um tiro preciso.")
        
    def tiro(self):
        row = random.randint(0, self.rows - 1)
        col = random.randint(0, self.cols - 1)


        if self.board1[row][col]['bg'] == 'blue':  # Verifica se a posição do campo inimigo tem uma base
                self.saldo[0] += 1  # Adiciona 1 ao saldo do jogador 1
                self.saldo_label.config(text=f"Saldo: {self.saldo[0]}")  # Atualiza a exibição do saldo

        self.board1[row][col].configure(bg="red")
        self.master.after(2000, lambda: self.reset_board([(row, col)], self.board1))
        self.master.after(2000, self.computer_move)


    def tiro_forte(self):
        if self.saldo[self.current_player - 1] >= 3:
            # Deduz 3 do saldo do jogador atual
            self.saldo[self.current_player - 1] -= 3
            # Atualiza a exibição do saldo
            self.saldo_label.config(text=f"Saldo: {self.saldo[self.current_player - 1]}")

            start_row, start_col = random.randint(0, self.rows - 3), random.randint(0, self.cols - 3)
            affected_positions = []  # Lista para armazenar as posições afetadas pelo tiro forte

            # Atira forte em todas as posições
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    self.board1[i][j].configure(bg="red")
                    affected_positions.append((i, j))  # Adiciona a posição à lista de posições afetadas

            # Após um certo tempo, limpa apenas as posições afetadas pelo tiro forte
            self.master.after(2000, lambda: self.reset_board(affected_positions))

            self.master.after(2000, self.computer_move)
        else:
            messagebox.showerror("Saldo Insuficiente", "Você não tem saldo suficiente para realizar um tiro forte.")


    def comprar_base(self):
        if self.saldo[self.current_player - 1] >= 2:
            # Deduz 1 do saldo do jogador atual
            self.saldo[self.current_player - 1] -= 2
            # Atualiza a exibição do saldo
            self.saldo_label.config(text=f"Saldo: {self.saldo[self.current_player - 1]}")    

            for button_row in self.board2:
                for button in button_row:
                    button.config(command=lambda b=button: self.set_base_position(b))
            

        else:
            messagebox.showerror("Saldo Insuficiente", "Você não tem saldo suficiente para comprar uma base.")
        
        self.master.after(2000, self.computer_move)
    
    def highlight_random_position(self, color):
        row = random.randint(0, self.rows - 1)
        col = random.randint(0, self.cols - 1)
        self.board1[row][col].configure(bg=color)

    def set_base_position(self, button):
        button.config(bg="blue")
        button.config(command=lambda: None)  # Desativa a função de clique no botão
        
    def reset_board(self, positions, board):
        for row, col in positions:
            board[row][col].configure(bg="white")
        

    def computer_move(self):
        row = random.randint(0, self.rows - 1)
        col = random.randint(0, self.cols - 1)
        self.board2[row][col].configure(bg="red")
        self.master.after(2000, lambda: self.reset_board([(row, col)], self.board2))

        


   
def main():
    root = tk.Tk()
    root.title("Cannon Blitz")
    game = BattlefieldGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
