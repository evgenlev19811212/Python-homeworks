from sqlalchemy import create_engine, text

db_connection_string = "postgresql://myuser:mypassword@localhost:5432/QA"
db = create_engine(db_connection_string)


def test_insert():
    connection = db.connect()
    transaction = connection.begin()

    # таблица перед тестом
    result = connection.execute(text("SELECT * FROM customers"))
    rows = result.mappings().all()

    # создание новой сущности
    sql = text("INSERT INTO customers (customer_id, customer_nm) VALUES (7, 'customer 6')") # noqa
    connection.execute(sql)
    result1 = connection.execute(text("SELECT * FROM customers"))
    rows1 = result1.mappings().all()
    row = rows1[-1]
    assert len(rows1) - len(rows) == 1
    assert row['customer_id'] == 7
    assert row['customer_nm'] == "customer 6"

    # очистка тестовых данных
    sql = text("DELETE FROM customers WHERE customer_id = 7")
    connection.execute(sql)

    transaction.commit()
    connection.close()


def test_update():
    connection = db.connect()
    transaction = connection.begin()

    # таблица перед тестом
    result = connection.execute(text("SELECT * FROM customers"))
    rows = result.mappings().all()

    # создание новой сущности
    sql = text("INSERT INTO customers (customer_id, customer_nm) VALUES (7, 'customer 6')") # noqa
    connection.execute(sql)
    result1 = connection.execute(text("SELECT * FROM customers"))
    rows1 = result1.mappings().all()
    row = rows1[-1]
    assert len(rows1) - len(rows) == 1
    assert row['customer_id'] == 7
    assert row['customer_nm'] == "customer 6"

    # редактирование данных
    sql = text("UPDATE customers SET customer_nm = 'customer 7' WHERE customer_id = 7") # noqa
    connection.execute(sql)
    result2 = connection.execute(text("SELECT * FROM customers"))
    rows2 = result2.mappings().all()
    row = rows2[-1]
    assert len(rows2) - len(rows) == 1
    assert row['customer_id'] == 7
    assert row['customer_nm'] == "customer 7"

    # очистка тестовых данных
    sql = text("DELETE FROM customers WHERE customer_id = 7")
    connection.execute(sql)

    transaction.commit()
    connection.close()


def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    # таблица перед тестом
    result = connection.execute(text("SELECT * FROM customers"))
    rows = result.mappings().all()

    # создание новой сущности
    sql = text("INSERT INTO customers (customer_id, customer_nm) VALUES (7, 'customer 7')") # noqa
    connection.execute(sql)
    result1 = connection.execute(text("SELECT * FROM customers"))
    rows1 = result1.mappings().all()
    row = rows1[-1]
    assert len(rows1) - len(rows) == 1
    assert row['customer_id'] == 7
    assert row['customer_nm'] == "customer 7"

    # удаление тестовой сущности
    sql = text("DELETE FROM customers WHERE customer_id = 7")
    connection.execute(sql)
    result2 = connection.execute(text("SELECT * FROM customers"))
    rows2 = result2.mappings().all()
    row = rows2[-1]
    assert len(rows2) - len(rows) == 0
    assert row['customer_id'] == 6
    assert row['customer_nm'] == "customer 6"

    transaction.commit()
    connection.close()
