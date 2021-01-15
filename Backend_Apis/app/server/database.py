import mysql.connector


def all_data(object):
    d = []
    for x in tuple(object):
        for y in tuple(x):
            d.append(y)
    return d


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")


if "firecompass" not in all_data(mycursor):
    mycursor.execute("CREATE DATABASE firecompass")
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="firecompass"
    )
else:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="firecompass"
    )
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
if 'persons' not in all_data(mycursor):
    mycursor.execute(
        "CREATE TABLE persons (person_id INT AUTO_INCREMENT PRIMARY KEY, person_name VARCHAR(255), amount DOUBLE)")
mycursor.execute("SHOW TABLES")
if 'lobbys' not in all_data(mycursor):
    mycursor.execute(
        "CREATE TABLE lobbys (lobby_id INT AUTO_INCREMENT PRIMARY KEY, lobby_name VARCHAR(255), lobby_fee INT)")
mycursor.execute("SHOW TABLES")
if 'winers' not in all_data(mycursor):
    mycursor.execute("CREATE TABLE winers (win_id INT AUTO_INCREMENT PRIMARY KEY, lobby_id INT,FOREIGN KEY (lobby_id) REFERENCES lobbys(lobby_id), person_id INT, FOREIGN KEY (person_id) REFERENCES persons(person_id), house DOUBLE)")


def person_info(persons) -> dict:
    d = []
    for x in persons:
        d.append({
            "id": x[0],
            "Name": x[1],
            "Amount": x[2],
        })
    return d


def lobbys_info(lobbys) -> dict:
    d = []
    for x in lobbys:
        d.append({
            "id": x[0],
            "Name": x[1],
            "Entry_Fee": x[2],
        })
    return d


def person(persons) -> dict:
    for x in persons:
        return{
            "id": x[0],
            "Name": x[1],
            "Amount": x[2],
        }


def lobby(lobby) -> dict:
    for x in lobby:
        return{
            "id": x[0],
            "Name": x[1],
            "Entry_Fee": x[2],
        }


def winners(winner) -> dict:
    d = []
    for x in winner:
        d.append({
            "id": x[0],
            "Lobby_Name": retrieve_lobby(x[2])["Name"],
            "Person_Name": retrieve_person(x[1])["Name"],
            "House": x[3],
        })
    return d

# Add a new person into to the database


def add_person(person_data: dict) -> dict:
    sql = "INSERT INTO persons (person_name, amount) VALUES (%s,%s)"
    val = (person_data["Name"], person_data["Amount"])
    print(val)
    mycursor.execute(sql, val)
    mydb.commit()
    return {"id": str(mycursor.lastrowid)}


def retrieve_persons():
    mycursor.execute("SELECT * FROM persons")
    myresult = mycursor.fetchall()
    return person_info(myresult)


# Retrieve a person with a matching ID
def retrieve_person(id: str) -> dict:
    sql = "SELECT * FROM persons WHERE person_id = %s"
    person_id = (int(id), )
    mycursor.execute(sql, person_id)
    myresult = mycursor.fetchall()
    return person(myresult)


def add_lobby(lobby_data: dict) -> dict:
    sql = "INSERT INTO lobbys (lobby_name, lobby_fee) VALUES (%s,%s)"
    val = (lobby_data["Name"], lobby_data["Entry_Fee"])
    print(val)
    mycursor.execute(sql, val)
    mydb.commit()
    return {"id": str(mycursor.lastrowid)}


def retrieve_lobbys():
    mycursor.execute("SELECT * FROM lobbys")
    myresult = mycursor.fetchall()
    return lobbys_info(myresult)


# Retrieve a lobby with a matching ID
def retrieve_lobby(id: str) -> dict:
    sql = "SELECT * FROM lobbys WHERE lobby_id = %s"
    lobby_id = (int(id), )
    mycursor.execute(sql, lobby_id)
    myresult = mycursor.fetchall()
    return lobby(myresult)


def add_winner(winner_data: dict) -> dict:
    fee = retrieve_lobby(winner_data["Lobby_id"])["Entry_Fee"]
    house = fee*winner_data["Person_limit"]*0.05
    win = fee*winner_data["Person_limit"] * 0.95
    sql = "UPDATE persons SET amount=%s WHERE person_id = %s"
    val = (win, winner_data["Winner_id"])
    mycursor.execute(sql, val)
    mydb.commit()
    sql = "INSERT INTO winers (lobby_id, person_id,house) VALUES (%s,%s,%s)"
    val = (winner_data["Lobby_id"], winner_data["Winner_id"], house)
    mycursor.execute(sql, val)
    mydb.commit()
    return {"id": str(mycursor.lastrowid)}


def retrieve_winners():
    mycursor.execute("SELECT * FROM winers")
    myresult = mycursor.fetchall()
    return winners(myresult)


def retrieve_deducted_amount(id: str, deduction: dict) -> dict:
    if retrieve_person(id)["Amount"] >= retrieve_lobby(deduction["Lobby_id"])["Entry_Fee"]:
        amount = retrieve_person(
            id)["Amount"] - retrieve_lobby(deduction["Lobby_id"])["Entry_Fee"]
        print(amount)
        sql = "UPDATE persons SET amount=%s WHERE person_id = %s"
        val = (amount, id)
        mycursor.execute(sql, val)
        mydb.commit()
        return retrieve_person(id)
    return []
