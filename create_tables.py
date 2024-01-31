from connection import postgres_conn
cursor = postgres_conn.cursor()
def create_tables():

    cursor.execute("""CREATE TABLE country(
                country_id SERIAL PRIMARY KEY NOT NULL,
                country VARCHAR(50) NOT NULL,
                last_update TIMESTAMP without time zone DEFAULT NOW()
    )""")

    cursor.execute("""CREATE TABLE region(
                   region_id SERIAL PRIMARY KEY NOT NULL,
                   region VARCHAR(50) NOT NULL,
                   country_id INT REFERENCES country(country_id) NOT NULL,
                   last_update TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW() NOT NULL
    )""")
    
    cursor.execute("""CREATE TABLE address(
                   address_id SERIAL PRIMARY KEY NOT NULL,
                   address VARCHAR(50) NOT NULL,
                   address2 VARCHAR(50),
                   district VARCHAR(20) NOT NULL,
                   region_id INT REFERENCES region(region_id) NOT NULL,
                   phone VARCHAR(20) NOT NULL,
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")

    cursor.execute("""CREATE TABLE customer(
                   customer_id SERIAL PRIMARY KEY NOT NULL,
                   first_name VARCHAR(50) NOT NULL,
                   last_name VARCHAR(50) NOT NULL,
                   email VARCHAR(60) NOT NULL,
                   username VARCHAR(20) NOT NULL,
                   password VARCHAR(10) NOT NULL,
                   address_id INT NOT NULL REFERENCES address(address_id),
                   create_date DATE,
                   last_update TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW() NOT NULL,
                   UNIQUE(email,username)
    )""")

    cursor.execute("""CREATE TABLE basket(
                   basket_id SERIAL PRIMARY KEY NOT NULL,
                   customer_id INT NOT NULL REFERENCES customer(customer_id),
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")

    cursor.execute("""CREATE TABLE category(
                   category_id SERIAL PRIMARY KEY NOT NULL,
                   name VARCHAR(50) NOT NULL,
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")

    cursor.execute("""CREATE TABLE store(
                   store_id SERIAL PRIMARY KEY NOT NULL,
                   name VARCHAR(50) NOT NULL,
                   description VARCHAR(180),
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")

    cursor.execute("""CREATE TABLE product(
                   product_id SERIAL PRIMARY KEY NOT NULL,
                   name VARCHAR(180) NOT NULL,
                   description TEXT,
                   price FLOAT NOT NULL,
                   amount INT NOT NULL,
                   category_id INT NOT NULL REFERENCES category(category_id),
                   store_id INT NOT NULL REFERENCES store(store_id),
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")

    cursor.execute("""CREATE TABLE "order"(
                   order_id SERIAL NOT NULL PRIMARY KEY,
                   product_id INT NOT NULL REFERENCES product(product_id),
                   customer_id INT NOT NULL REFERENCES customer(customer_id),
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")


    cursor.execute("""CREATE TABLE "basket_product"(
                   basket_id INT NOT NULL REFERENCES basket(basket_id),
                   product_id INT NOT NULL REFERENCES product(product_id),
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")


    cursor.execute("""CREATE TABLE staff(
                   staff_id SERIAL NOT NULL PRIMARY KEY,
                   first_name VARCHAR(20) NOT NULL,
                   last_name VARCHAR(20) NOT NULL,
                   address_id INT NOT NULL REFERENCES address(address_id),
                   phone_number VARCHAR(20) NOT NULL,
                   email VARCHAR(60) NOT NULL,
                   username VARCHAR(20) NOT NULL,
                   password VARCHAR(20) NOT NULL,
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")



    cursor.execute("""CREATE TABLE payment(
                   payment_id SERIAL NOT NULL PRIMARY KEY,
                   order_id INT NOT NULL REFERENCES "order"(order_id),
                   payment_date DATE NOT NULL,
                   amount NUMERIC(8,2) NOT NULL,
                   staff_id INT NOT NULL REFERENCES staff(staff_id),
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")

    postgres_conn.commit()
    print("CREATE TABLE")
