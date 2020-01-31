import sqlite3

with sqlite3.connect('sqlite_dummyDB.db') as conn:  # Establishing connection
    print("Connection established with sqlite_dummyDB database")

    cursor_obj = conn.cursor()  # instantiating object or cursor using connection object
    print("Cursor Object Created")

    # CREATING A TABLE
    # SQL query for INSERT stored in a variable
    table = "CREATE TABLE IF NOT EXISTS employee2(_id integer, name text, age integer, salary float)"
    conn.execute(table)     # passing SQL query stored in a variable to the execute method
    conn.commit()     # this command saves all the changes to the database.
    print("table Employee created")

    print()

    create_result_query = "SELECT count(name) FROM sqlite_master WHERE type='table' AND name='employee2'"
    cursor_obj.execute(create_result_query)

    if cursor_obj.fetchone()[0] == 1:
        print("Table Exist")
    else:
        print("Table does not exits")

    print()

    # INSERTING DATA TO THE TABLE
    insert_emp = "INSERT INTO employee2 VALUES(4, 'shilp5', 33, 4.65)"  # SQL query for INSERT stored in a variable
    cursor_obj.execute(insert_emp)
    conn.commit()  # this command saves all the changes to the database.

    # checking if data was inserted. rowcount attribute of cursor class returns number of rows affected in database
    if cursor_obj.rowcount == 1:
        print("Employee inserted")
    else:
        print("Employee insertion failed")

    print()

    # # SELECTING DATA TO THE TABLE
    emp_select = "SELECT * FROM employee2"  # SQL query for SELECT stored in a variable
    cursor_obj.execute(emp_select)

    # OPTION 1:
    # When we use SELECT statement, the execute method updates cursor_obj with the list of tuple. The cursor_obj
    # fetches one row at time to save any memory usage. After 1st execution, it moves to 2nd row and so on and so
    # once all row are fetched, the cursor will have no more rows to fetch. There is now way we can fetch nth
    # row cursor have moved to (n+1)th row..
    for id, name, age, salary in cursor_obj:
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"Salary: {salary}")
        print("=" * 10)

    # OPTION 2
    # When we use SELECT statement, the execute method updates cursor_obj with the list of tuple. Now we can
    # use fetchall() method to fetch the entire data set of select statement.
    for id, name, age, salary in cursor_obj.fetchall():
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"Salary: {salary}")
        print("=" * 10)

    print()
