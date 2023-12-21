class Recipe:
    def __init__(self, name_recipe:str, ingredients:str):
        """
        Inicijalizacija na objekt od klasata Recipe

        :param name_recipe:str, ime na receptot
        :param ingredients:str, sostojki
        """

        self.name_recipe=name_recipe
        self.ingredients=ingredients 

    @property
    def name_recipe(self):
        """
        getter
        """
        return self.__name_recipe
    
    @name_recipe.setter
    def name_recipe(self, name_recipe):
        """
        setter
        """
        self.__name_recipe=name_recipe

    @property
    def ingredients(self):
        """
        Getter za name_recipe
        """
        return self.__ingredients
    
    @ingredients.setter
    def ingredients(self, ingredients):
        """
        Setter za ingredients
        """
        self.__ingredients=ingredients

    def cook(self):
        """
        Apstrakcija
        """
        pass

    def __str__(self):
        return f"Recipe: {self.__name}, Ingredients: {self.__ingredients}"


class Dessert(Recipe):
      def __init__(self, name_recipe: str, ingredients: str, topping):
          super().__init__(name_recipe, ingredients)
          self._topping=topping

      @property
      def topping(self):
        """
        Getter za topping
        """
        return self._topping
      
      @topping.setter
      def topping(self, topping):
        """
        Setter za topping
        """
        self._topping=topping

      
      def cook(self):
        return f"Making {self._Recipe__name_recipe} with {self._topping} topping"

      def __str__(self):
        return f"Dessert: {self._Recipe__name_recipe}, Ingredients: {self._Recipe__ingredients}, Topping: {self._topping}"

dessert = Dessert("Cheesecake", ["cream cheese", "sugar", "sour cream", "flavor"], "raspberry sauce")
print(dessert)
print(f"Cooking: {dessert.cook()}")