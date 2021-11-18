
class Budget:
  
    def __init__(self, food : float, clothing: float, entertainment: float) -> None:
        self.table = {}
        self.table["food"] = food
        self.table["clothing"] = clothing
        self.table["entertainment"] = entertainment
    
    def deposit(self, amount: float, category: str) -> None:
        if category in self.table: 
            self.table[category] += amount
        else:
           print("there must be an error")
    
    def withdraw(self, amount: float, category: str) -> None:
        if category in self.table:
            if self.table[category] >= amount:
                self.table[category] -= amount
            else:
                print("not enough in your balance")
        else:
            print("there must be an error")

    def transfer(self, amount: float, source: str, target: str):
        self.table[source] -= amount
        self.table[target] += amount

    def get_balance(self, category: str) -> float:
        return self.table[category]
