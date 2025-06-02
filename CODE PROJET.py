import tkinter as tk
from tkinter import messagebox
import random

# Liste de mots possibles
MOTS = ["python", "robot", "intelligence", "machine", "ordinateur"]

# ASCII Art pour chaque étape du pendu
PENDU_ASCII = [
    "",
    "____\n",
    "____\n |   O\n",
    "____\n |   O\n |   |\n",
    "____\n |   O\n |  /|\n",
    "____\n |   O\n |  /|\n |  / \\\n",
    "____\n |   O\n |  /|\n |  / \\\n | MORT\n"
]

class JeuPendu:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu du Pendu")

        # Choisir un mot aléatoire
        self.mot_a_deviner = random.choice(MOTS)
        self.lettres_trouvees = ["_" for _ in self.mot_a_deviner]
        self.lettres_proposees = set()
        self.essais_restants = 6

        # Interface graphique
        self.label_mot = tk.Label(root, text=" ".join(self.lettres_trouvees), font=("Courier", 24))
        self.label_mot.pack(pady=10)

        self.label_ascii = tk.Label(root, text=PENDU_ASCII[0], font=("Courier", 12), justify="left")
        self.label_ascii.pack()

        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack()
        self.entry.focus()

        self.button = tk.Button(root, text="Proposer", command=self.proposer_lettre)
        self.button.pack(pady=5)

        self.label_info = tk.Label(root, text="Essais restants: 6")
        self.label_info.pack()

        self.label_erreur = tk.Label(root, text="", fg="red")
        self.label_erreur.pack()

    def proposer_lettre(self):
        lettre = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if not lettre.isalpha() or len(lettre) != 1:
            self.label_erreur.config(text="Entrez une seule lettre valide.")
            return

        if lettre in self.lettres_proposees:
            self.label_erreur.config(text=f"Vous avez déjà proposé la lettre '{lettre}'.")
            return

        self.lettres_proposees.add(lettre)
        self.label_erreur.config(text="")  # Réinitialiser le message d'erreur

        if lettre in self.mot_a_deviner:
            for i, c in enumerate(self.mot_a_deviner):
                if c == lettre:
                    self.lettres_trouvees[i] = lettre
        else:
            self.essais_restants -= 1

        self.label_mot.config(text=" ".join(self.lettres_trouvees))
        self.label_ascii.config(text=PENDU_ASCII[6 - self.essais_restants])
        self.label_info.config(text=f"Essais restants: {self.essais_restants}")

        if "_" not in self.lettres_trouvees:
            messagebox.showinfo("Félicitations", "Vous avez gagné !")
            self.root.destroy()
        elif self.essais_restants == 0:
            messagebox.showinfo("Perdu", f"Vous avez perdu. Le mot était: {self.mot_a_deviner}")
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = JeuPendu(root)
    root.mainloop()
