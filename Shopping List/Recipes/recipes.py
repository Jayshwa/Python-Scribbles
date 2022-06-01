class Recipe():
    def __init__(self,name,cuisine,difficulty):
        self.name = name
        self.cuisine = cuisine
        self.difficulty = difficulty
        self.ingredients = None

    def burnt(self):
        print('I was burnt')

toast = Recipe('Toast','None','Easy')
print(toast.burnt())