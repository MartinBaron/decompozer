import sys
import sqlite3

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

def add_ingredient_in_db(ingredient_name):
    c.execute("SELECT count(*) FROM ingredients WHERE name = '" + ingredient_name + "';")
    values = c.fetchall()
    if values[0][0] == 0:
	    ingredient_nutri_list = []
	    for n in nutri :
			nutri_input_value = raw_input("Please give the amount of " + str(n) + " for 100g of your ingredient "+ ingredient_name +":\n")
			ingredient_nutri_list.append(nutri_input_value)
	    ingredient_nutri_list_string = ""
	    for i in ingredient_nutri_list:
	        ingredient_nutri_list_string = ingredient_nutri_list_string + str(i) + ","
	    ingredient_nutri_list_string = ingredient_nutri_list_string[:-1]
	    c.execute("INSERT INTO ingredients (name," + nutri_list_string +" ) values ('"+ ingredient_name+ "', "+ ingredient_nutri_list_string +"); ") 
	    conn.commit()
	    c.execute("SELECT id FROM ingredients WHERE name = '" + ingredient_name + "';")
	    values = c.fetchall()
	    print values[0][0]
	    return values[0][0]
    else :
        print "this ingredient already exists in db, cool !\n"
        c.execute("SELECT id FROM ingredients WHERE name = '" + ingredient_name + "';")
        values = c.fetchall()
        return values[0][0]

def add_product_to_db(product_name, ingredient_id_order_matrix):
    product_nutri_list = []
    for n in nutri :
	    nutri_input_value = raw_input("Please give the amount of " + str(n) + " for 100g of your product "+ product_name +":\n")
	    product_nutri_list.append(nutri_input_value)
    product_nutri_list_string = ""
    for i in product_nutri_list :
		product_nutri_list_string = product_nutri_list_string + str(i) + ","
    product_nutri_list_string = product_nutri_list_string[:-1]
    c.execute("INSERT INTO products (name, " + nutri_list_string + ") values ('" + product_name + "', " + product_nutri_list_string + ");")
    conn.commit()
    c.execute ("SELECT id FROM products WHERE name = '" + product_name +"';")
    values = c.fetchall()
    id_product = values[0][0]
    for i in range(0, len(ingredient_id_order_matrix)):
    	order_ingredient = ingredient_id_order_matrix[i][0]
    	id_ingredient = ingredient_id_order_matrix[i][1]
    	c.execute("INSERT INTO ingredients_list (fk_id_products, fk_id_ingredients, list_order) values (" + str(id_product) + ", " + str(id_ingredient) + ", "+ str(order_ingredient) + ");")
    conn.commit()

if __name__ == '__main__':
    product_name = raw_input("Give the product name in capital letters \n")
    sqlite_file = '/Users/robinarmant/workspace/food/nutrition.db'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    nutri = get_nutritional_elements()
    nutri_list_string = ""
    for n in nutri :
    	nutri_list_string = nutri_list_string + str(n) + ","
    nutri_list_string = nutri_list_string[:-1]
    print nutri_list_string

    c.execute("SELECT * FROM products WHERE name = '" + product_name + "';")
    values = c.fetchall()
    if len(values) > 0:
    	print "This product already exists in the db with the following attributes :\n"
    	print values[0][1:]
    	sys.exit()
    else :
        print "New product !"
        ingredients_list = []
        input_value = raw_input("Please give the first ingredient of the product:\n")
        ingredients_list.append([1,add_ingredient_in_db(input_value)])
        counter = 1
        while input_value != "END":
            counter = counter + 1
            input_value = raw_input("Please give the next ingredient of the product (type END if you gave them all):\n")
            if input_value == 'END':
            	pass
            else :
                ingredients_list.append([counter,add_ingredient_in_db(input_value)])
        print ingredients_list
        add_product_to_db(product_name, ingredients_list)
        