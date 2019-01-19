CREATE TABLE INGREDIENTS(
   ID INTEGER PRIMARY KEY AUTOINCREMENT,
   NAME           TEXT    NOT NULL,
   ECO_SCORE        REAL,
   CARBO_HYDRATES REAL NOT NULL DEFAULT 0.00,
   SUGAR REAL NOT NULL DEFAULT 0.00,
   LIPIDS            REAL NOT NULL DEFAULT 0.00,
   PROTEINS            REAL NOT NULL DEFAULT 0.00
);

CREATE TABLE INGREDIENTS_LIST(
   ID INTEGER PRIMARY KEY     AUTOINCREMENT,
   FK_ID_PRODUCTS           INT    NOT NULL ,
   FK_ID_INGREDIENTS           INT    NOT NULL,
   LIST_ORDER        INT NOT NULL,
   QUANTITY REAL

);

CREATE TABLE PRODUCTS(
   ID INTEGER PRIMARY KEY     AUTOINCREMENT,
   NAME TEXT NOT NULL,
   FK_ID_INGREDIENTS_LIST           INT    ,
   PRICE            REAL,
      CARBO_HYDRATES REAL NOT NULL DEFAULT 0.00,
   SUGAR REAL NOT NULL DEFAULT 0.00,
   LIPIDS            REAL NOT NULL DEFAULT 0.00,
   PROTEINS            REAL NOT NULL DEFAULT 0.00
);


UPDATE products SET price = 3 WHERE name = 'CHOCOLAT BONNAT'
SELECT lipids, proteins FROM products 


WHERE name = 'CHOCOLAT BONNAT' 

name = 'CHOCOLAT BONNAT'


INSERT INTO products (name, carbo_hydrates, sugar, lipids, proteins) VALUES ('CHOCOLAT BONNAT', 42.6, 25.9, 46, 8.8);

insert into ingredients (name, carbo_hydrates, sugar, lipids, proteins) values ('FARINE BLE',76,0.3,1,10);
insert into ingredients (name, carbo_hydrates, sugar, lipids, proteins) values ('SUCRE',0,100,0,0);
insert into ingredients (name, carbo_hydrates, sugar, lipids, proteins) values ('BEURRE DE CACAO',0,0,100,0);
insert into ingredients (name, carbo_hydrates, sugar, lipids, proteins) values ('CACAO',58,1.8,14,20);
insert into ingredients (name, carbo_hydrates, sugar, lipids, proteins) values ('LAIT EN POUDRE',38,38,27,26);



