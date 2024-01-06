from collections import defaultdict
from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ingredientToRecipe = defaultdict(set)
        recipeToIngredients = {}
        for i, recipe in enumerate(recipes):
            recipeToIngredients[recipe] = ingredients[i]
            for ingredient in ingredients[i]:
                ingredientToRecipe[ingredient].add(recipe)

        todo = set(recipes)
        supplySet = set(supplies)
        ans = set()
        while todo:
            nextTodo = set()
            for recipe in todo:
                allIngredientsInSupplies = True
                for ingredient in recipeToIngredients[recipe]:
                    if ingredient not in supplySet:
                        allIngredientsInSupplies = False
                # means we can generate this recipe and this recipe can also be supply
                if allIngredientsInSupplies:
                    ans.add(recipe)
                    supplySet.add(recipe)
                    if recipe in ingredientToRecipe:
                        nextTodo = nextTodo.union(ingredientToRecipe[recipe])
            todo = nextTodo

        return list(ans)


print(
    Solution().findAllRecipes(recipes=["bread"], ingredients=[["yeast", "flour"]], supplies=["yeast", "flour", "corn"]))
print(Solution().findAllRecipes(recipes=["bread", "sandwich"], ingredients=[["yeast", "flour"], ["bread", "meat"]],
                                supplies=["yeast", "flour", "meat"]))
print(Solution().findAllRecipes(recipes=["bread", "sandwich", "burger"],
                                ingredients=[["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]],
                                supplies=["yeast", "flour", "meat"]))
