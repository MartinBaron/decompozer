import os
import sqlite3
import sys
import numpy as np
from scipy.optimize import nnls 


#STORING PRODUCT NUTRITIONNAL VALUES

#get the nutritionnal values from the made product
def get_product_nutri_values(product_name):
    nutri = get_nutritional_elements()
    product_values = dict()
    c.execute("SELECT * FROM products where name ='" + product_name + "';")
    values = c.fetchall()
    for i in range (0,len(nutri)):
        product_values[str(nutri[i])] = values[0][4+i]
    print product_values
    return product_values

#return the different ingredients from the product with their nutritionnal values
def get_ingredients_from_products(product_name):
	nutri = get_nutritional_elements()
	product_ingredients = []
	c.execute("SELECT list_order, ingredients.* FROM ingredients_list, ingredients, products where products.id = ingredients_list.fk_id_products and ingredients.id = ingredients_list.fk_id_ingredients and products.name ='" + product_name + "';")
	values = c.fetchall()

	for items in values:
		ingredients_values = dict()
		ingredients_values["order"] = items[0]
		ingredients_values["name"] = items[2]
		for i in range(0, len(nutri)):
			ingredients_values[str(nutri[i])] = items[4+i]
		print "ingredients_values " + str(ingredients_values)
		product_ingredients.append(ingredients_values)

	print product_ingredients
	return product_ingredients

#get the different nutritionnal values used in the db
def get_nutritional_elements():
    nutritional_elements = []
    c.execute("PRAGMA table_info(ingredients)")
    values = c.fetchall()
    nb_nutritional_elements = len(values)
    for i in range(3,nb_nutritional_elements):
    	nutritional_elements.append(values[i][1])
    print "We consider only the following nutritionnal values : " 
    print nutritional_elements
    return nutritional_elements

#compute the product's ingredients proportions
def get_ingredients_proportion(product_name):
	nutri = get_nutritional_elements()	
	product_ingredients = get_ingredients_from_products(product_name)
	product_values = get_product_nutri_values(product_name)

	product_ingredients_proportion = dict()

	nb_ingredients = len(product_ingredients)

	#building B matrix
	product_nutri = []
	for n in nutri:
		product_nutri.append(product_values[n])
	product_nutri.append(1)
	print product_nutri
	product_nutri_matrix  = np.array(product_nutri)

	#building A matrix
	ingredients_nutri = []
	for i in product_ingredients:
		ingredient_nutri = []
		for n in nutri:
			ingredient_nutri.append(i[n])
		ingredient_nutri.append(1)
		print "les valeurs nutri du premier ingredient sont :"
		print ingredient_nutri
		ingredients_nutri.append(ingredient_nutri)
	

	print "***"
	print ingredients_nutri
	ingredients_nutri_matrix = np.array(ingredients_nutri)
	print ingredients_nutri_matrix.T
	print product_nutri_matrix
	#resolution
	proportions_matrix = np.linalg.lstsq(ingredients_nutri_matrix.T, product_nutri_matrix)
	proportions_matrix2, rnorm = nnls(ingredients_nutri_matrix.T, product_nutri_matrix)
	print "les proportions des ingredients sont :"
	print proportions_matrix2





if __name__ == '__main__':
    product_name = raw_input("Give the product name in capital letters \n")
    print "***"
    print product_name
    sqlite_file = '/Users/robinarmant/workspace/food/nutrition.db'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    product_values = get_product_nutri_values(product_name)
    print "***"
    get_ingredients_from_products(product_name)
    print "***"
    get_nutritional_elements()
    print "***"
    get_ingredients_proportion(product_name)
