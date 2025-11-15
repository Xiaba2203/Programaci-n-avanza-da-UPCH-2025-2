# P1.py - Buscaminas mejorado y coloreado
from tkinter import *
import tkinter as tk
import random
import time

# Eliminé la primera ventana extra para evitar crear dos Tk()

class Minesweeper:
    COLORS = {
        1: "#0b57d0",  # azul
        2: "#0b9b2b",  # verde
        3: "#d02b2b",  # rojo
        4: "#6a2bd0",  # morado
        5: "#8b0000",  # marrón oscuro
        6: "#2b6a6a",
        7: "#111111",
        8: "#666666"
    }

    def __init__(self, size=5, mines=None):
        self.size = size
        # menor dificultad por defecto: aproximadamente size*size/8 minas si no se especifica
        self.total_mines = mines if mines is not None else max(1, (size * size) // 8)
        self.flags = set()
        self.revealed = set()
        self.mines = set()
        self.started = False
        self.start_time = None
        self.timer_job = None
        self.hints_left = 3  # número de pistas disponibles

        # ventana
        self.root = tk.Tk()
        self.root.title(f"Buscaminas {size}x{size}")
        self.root.resizable(False, False)
        self.root.configure(bg="#dfe6e9")

        # panel superior: bandera, tiempo, smiley y hint
        top = tk.Frame(self.root, padx=8, pady=8, bg="#dfe6e9")
        top.pack(fill="x")

        self.flags_label = tk.Label(top, text=f"Banderas: 0 / {self.total_mines}", width=20, bg="#dfe6e9")
        self.flags_label.pack(side="left")

        self.timer_label = tk.Label(top, text="Tiempo: 0s", width=12, bg="#dfe6e9")
        self.timer_label.pack(side="left", padx=(8,0))

        # Botón smiley (reinicio)
        self.smiley = tk.Button(top, text="🙂", width=3, command=self.reset, bg="#ffffff")
        self.smiley.pack(side="right", padx=(4,0))

        # Botón de pista
        self.hint_btn = tk.Button(top, text=f"Pista ({self.hints_left})", command=self.use_hint, bg="#ffd166")
        self.hint_btn.pack(side="right", padx=(4,0))

        # tablero
        self.board_frame = tk.Frame(self.root, padx=8, pady=8, bg="#dfe6e9")
        self.board_frame.pack()

        self.buttons = {}
        for r in range(size):
            for c in range(size):
                b = tk.Button(self.board_frame, width=3, height=1, font=("TkDefaultFont", 12), relief="raised", bg="#b2bec3")
                b.grid(row=r, column=c, padx=2, pady=2)
                b.config(command=lambda rr=r, cc=c: self.on_left_click(rr, cc))
                b.bind("<Button-3>", lambda ev, rr=r, cc=c: self.on_right_click(ev, rr, cc))
                # chord: click izquierdo sobre número revelado
                b.bind("<Button-1>", lambda ev, rr=r, cc=c: self.on_left_click(rr, cc))
                b.bind("<Enter>", lambda ev, btn=b: btn.config(bg="#dfe6e9"))
                b.bind("<Leave>", lambda ev, btn=b: btn.config(bg="#b2bec3"))
                self.buttons[(r,c)] = b

        self.place_mines()
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.mainloop()

    def place_mines(self):
        positions = [(r,c) for r in range(self.size) for c in range(self.size)]
        self.mines = set(random.sample(positions, self.total_mines))

    def neighbors(self, r, c):
        for dr in (-1,0,1):
            for dc in (-1,0,1):
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r+dr, c+dc
                if 0 <= nr < self.size and 0 <= nc < self.size:
                    yield (nr,nc)

    def count_adjacent(self, r, c):
        return sum((nr,nc) in self.mines for nr,nc in self.neighbors(r,c))

    def on_left_click(self, r, c):
        # iniciar reloj en primer movimiento
        if not self.started:
            self.started = True
            self.start_time = time.time()
            self.update_timer()
        # si ya revelado, intentar chord: si número == banderas adyacentes -> revelar vecinos
        if (r,c) in self.revealed:
            num = self.count_adjacent(r,c)
            adj_flags = sum(1 for nb in self.neighbors(r,c) if nb in self.flags)
            if num > 0 and adj_flags == num:
                for nb in self.neighbors(r,c):
                    if nb not in self.revealed and nb not in self.flags:
                        self.reveal_cell(*nb)
                if self.check_win():
                    self.game_over(True)
            return
        # si hay bandera, no hacer nada
        if (r,c) in self.flags:
            return
        # si es mina -> perder
        if (r,c) in self.mines:
            self.reveal_mine(r,c)
            self.game_over(False)
            return
        # descubrir casilla; si 0 adyacentes, revelar en onda
        self.flood_reveal(r,c)
        # checar victoria
        if self.check_win():
            self.game_over(True)

    def on_right_click(self, event, r, c):
        # toggle bandera, no afectar si ya revelado
        if (r,c) in self.revealed:
            return "break"
        b = self.buttons[(r,c)]
        if (r,c) in self.flags:
            self.flags.remove((r,c))
            b.config(text="", fg="black", bg="#b2bec3")
        else:
            if len(self.flags) < self.total_mines:
                self.flags.add((r,c))
                b.config(text="⚑", fg="white", bg="#ff6b6b")
        self.update_flags_label()
        return "break"

    def reveal_cell(self, r, c):
        if (r,c) in self.revealed:
            return
        if (r,c) in self.flags:
            return
        self.revealed.add((r,c))
        b = self.buttons[(r,c)]
        adj = self.count_adjacent(r,c)
        b.config(relief="sunken", state="disabled", bg="#f1f2f6")
        if adj == 0:
            b.config(text="")
        else:
            b.config(text=str(adj), fg=self.COLORS.get(adj, "#000000"), font=("TkDefaultFont", 12, "bold"))
        # cambiar color de fondo sutil según adyacente
        if adj == 0:
            b.config(bg="#e0f7fa")
        elif adj >= 3:
            b.config(bg="#fff0f0")

    def flood_reveal(self, r, c):
        stack = [(r,c)]
        while stack:
            rr, cc = stack.pop()
            if (rr,cc) in self.revealed or (rr,cc) in self.flags:
                continue
            self.revealed.add((rr,cc))
            b = self.buttons[(rr,cc)]
            adj = self.count_adjacent(rr,cc)
            b.config(relief="sunken", state="disabled")
            if adj == 0:
                b.config(text="", bg="#e0f7fa")
                for nb in self.neighbors(rr,cc):
                    if nb not in self.revealed:
                        stack.append(nb)
            else:
                b.config(text=str(adj), fg=self.COLORS.get(adj, "#000000"), font=("TkDefaultFont", 12, "bold"), bg="#f7fff7")
        self.update_flags_label()

    def reveal_mine(self, r, c):
        # mostrar la mina que explotó y todas las demás
        for (mr,mc) in self.mines:
            b = self.buttons[(mr,mc)]
            if (mr,mc) == (r,c):
                b.config(text="✹", bg="#ff4d4d", state="disabled", fg="black")
            else:
                b.config(text="✹", bg="#ffd6d6", state="disabled")
        # deshabilitar botones restantes
        for pos, btn in self.buttons.items():
            btn.config(state="disabled")

    def check_win(self):
        return len(self.revealed) == self.size*self.size - self.total_mines

    def game_over(self, won):
        if self.timer_job:
            self.root.after_cancel(self.timer_job)
            self.timer_job = None
        elapsed = int(time.time() - self.start_time) if self.start_time else 0
        msg = "¡Ganaste!" if won else "Perdiste"
        self.root.title(f"{msg} - Tiempo: {elapsed}s")
        # si ganó, marcar minas con bandera automática y colorear tablero
        if won:
            for m in self.mines:
                if m not in self.flags:
                    b = self.buttons[m]
                    b.config(text="⚑", fg="white", bg="#7bed9f")
            self.smiley.config(text="😎", bg="#9bffb3")
        else:
            self.smiley.config(text="😵", bg="#ff8a80")
        for b in self.buttons.values():
            b.config(state="disabled")

    def update_flags_label(self):
        used = len(self.flags)
        self.flags_label.config(text=f"Banderas: {used} / {self.total_mines}")

    def update_timer(self):
        if not self.started or self.start_time is None:
            return
        elapsed = int(time.time() - self.start_time)
        self.timer_label.config(text=f"Tiempo: {elapsed}s")
        self.timer_job = self.root.after(1000, self.update_timer)

    def reset(self):
        try:
            if self.timer_job:
                self.root.after_cancel(self.timer_job)
        except Exception:
            pass
        self.root.destroy()
        # reiniciar con misma configuración (misma dificultad)
        Minesweeper(size=self.size, mines=self.total_mines)

    def on_close(self):
        if self.timer_job:
            self.root.after_cancel(self.timer_job)
        self.root.destroy()

    def use_hint(self):
        if self.hints_left <= 0:
            return
        # encontrar una casilla segura no revelada ni marcada
        candidates = [(r,c) for r in range(self.size) for c in range(self.size)
                      if (r,c) not in self.revealed and (r,c) not in self.flags and (r,c) not in self.mines]
        if not candidates:
            return
        pos = random.choice(candidates)
        # revelar esa casilla (como ayuda)
        self.hints_left -= 1
        self.hint_btn.config(text=f"Pista ({self.hints_left})", state="normal" if self.hints_left>0 else "disabled")
        self.reveal_cell(*pos)
        # si al revelar hay 0 ady, expandir onda
        if self.count_adjacent(*pos) == 0:
            self.flood_reveal(*pos)
        if not self.started:
            self.started = True
            self.start_time = time.time()
            self.update_timer()
        if self.check_win():
            self.game_over(True)

# lanzar el juego (menos minas por defecto)
if __name__ == "__main__":
    Minesweeper(size=5)  # cambia size y/o mines para ajustar dificultad