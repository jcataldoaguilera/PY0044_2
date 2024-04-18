class Character():
    
    def __init__(self, name:str):
        self.name = name
        self.lvl = 1
        self.exp = 0
    
    def __str__(self):
        return f"Nombre: {self.name}, Nivel: {self.lvl}, Exp: {self.exp}"

    @property
    def status(self):
        pass
    
    @status.setter
    def status(self, exp: int):
        self.exp += exp
        a = int(exp/100)
        if exp >= 100:
            self.lvl += a
            self.exp = exp -a
    
    def __gt__(self, other):
        return self.lvl > other.lvl
    
    def __lt__(self, other):
        return self.lvl < other.lvl
    
    def __eq__(self, other):
        return self.lvl == other.lvl

if __name__ == '__main__':
    nuevo_personaje = Character("Evil666")
    print(nuevo_personaje)
