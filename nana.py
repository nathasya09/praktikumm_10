import requests
import streamlit as st

# Your Spoonacular API key
spoonacular_api_key = "97df5efa7eaa49b9862a5d7b0326e1f9"

# Spoonacular API URLs
find_by_ingredients_url = "https://api.spoonacular.com/recipes/findByIngredients"
get_recipe_info_url = "https://api.spoonacular.com/recipes/{id}/information"

def fetch_recipes(ingredients):
    params = {
        "ingredients": ingredients,
        "number": 10,
        "apiKey": spoonacular_api_key
    }
    response = requests.get(find_by_ingredients_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error fetching recipes: {response.status_code}")
        return []

def get_recipe_info(recipe_id):
    url = get_recipe_info_url.format(id=recipe_id)
    params = {
        "apiKey": spoonacular_api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error fetching recipe details: {response.status_code}")
        return None

def main():
    st.title("Recipe Finder by Nathasya")
    st.write("Find recipes based on the ingredients you have at home!")

    ingredients = st.text_input("Enter the ingredients you have at home (separated by commas):")
    if ingredients:
        recipes = fetch_recipes(ingredients)
        if recipes:
            st.write("Here are some recipe suggestions:")
            for recipe in recipes:
                recipe_info = get_recipe_info(recipe['id'])
                if recipe_info:
                    
                    st.write(f"### {recipe_info['title']} ({recipe_info['readyInMinutes']} minutes)")
                    st.image(recipe_info['image'])
                    st.write("#### Ingredients:")
                    for ingredient in recipe_info['extendedIngredients']:
                        st.write(f"- {ingredient['original']}")
                    st.write("---")
        else:
            st.write("No recipes found.")

if __name__ == "__main__":
    main()

