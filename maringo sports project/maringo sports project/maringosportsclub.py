import sqlite3
import random

##create connection to a database
conn = sqlite3.connect('maringosports.db')

##create a cursor to modify the db
cur = conn.cursor()


##create table for members
cur.execute("""CREATE TABLE IF NOT EXISTS Members
    (member_id INTEGER PRIMARY KEY AUTOINCREMENT,
    Full_Name TEXT NOT NULL,
    Gender TEXT CHECK (Gender COLLATE NOCASE IN ('M', 'F')),
    Next_of_kin TEXT,
    Date_of_birth DATE,
    Contact_Details TEXT,
    Sub_County TEXT,
    School_or_College TEXT,
    Age INTEGER CHECK (Age >= 12 AND Age <= 35),
    Various_Games_of_Interest_in_order TEXT,
    Weight_kg REAL,
    Height_m REAL,
    Special_Needs TEXT DEFAULT 'None',
    Enrollment_Type TEXT CHECK (Enrollment_Type COLLATE NOCASE IN ('Individual', 'Group')) NOT NULL,
    Group_Name TEXT DEFAULT NULL,
    Enroll_payed
    )
    """)

# Create the EnrollmentFees table to store enrollment fee details
cur.execute("""CREATE TABLE IF NOT EXISTS EnrollmentFees (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    member_id INTEGER,
    member_name TEXT,
    enroll_type TEXT,
    group_name TEXT,
    enrollment_fee INT,
    FOREIGN KEY (member_id) REFERENCES Members (member_id)
    )
    """)


##create table for available games
cur.execute("""CREATE TABLE IF NOT EXISTS Available_Games
    (Game_id INTEGER PRIMARY KEY AUTOINCREMENT,
    Game TEXT,
    Game_Patron INTEGER,
    Game_Captain INTEGER,
    FOREIGN KEY(Game_Captain) REFERENCES Members(member_id) ON DELETE SET NULL,
    FOREIGN KEY(Game_Patron) REFERENCES Games_Patrons(patron_id)
    )""")


available_games = [('Swimming', None, None),
                   ('Hockey',None, None),
                    ('Lawn Tennis', None, None),
                    ('Table Tennis', None, None),
                    ('Darts', None, None),
                   ('Badminton', None, None),
                   ('Volleyball', None, None),
                   ('Basketball',None, None),
                   ('Netball', None, None),
                   ('Football', None, None),
                   ('Baseball', None, None),
                   ('Rugby', None, None),
                   ('Pool', None, None),
                   ('Chess', None, None),
                   ('Draft', None, None)]



##insert games into the table
cur.executemany("""INSERT INTO Available_Games
        (Game, Game_Patron, Game_Captain)
        VALUES (?, ?, ?)
        """, available_games)



# Dictionary to store game IDs and count of members for each game
games_count = {}

# Function to display available games and let the user choose games of interest
def choose_games_of_interest():
    print("Available Games:")
    cur.execute("SELECT * FROM Available_Games")
    available_games = cur.fetchall()
    for game_id, game, _, _ in available_games:
        print(f"{game_id}. {game}")

    games_of_interest = input("Enter Game IDs of interest (comma-separated): ")
    return games_of_interest.split(",")

# Create the Members_Games table to store the association between members and games
cur.execute("""CREATE TABLE IF NOT EXISTS Members_Games (
    member_id INTEGER,
    game_id INTEGER,
    PRIMARY KEY (member_id, game_id),
    FOREIGN KEY (member_id) REFERENCES Members (member_id),
    FOREIGN KEY (game_id) REFERENCES Available_Games (Game_id)
    )
""")

##insert members into the table
def add_member():
    ##handle any exception
    try:
        full_name = input('Enter Full Name: ')
        gender = input('Enter Gender (M/F): ')
        next_of_kin = input('Enter Next of Kin: ')
        date_of_birth = input('Enter Date of Birth (YYYY-MM-DD): ')
        contact_details = input('Enter Contact Details: ')
        sub_county = input('Enter Sub-County: ')
        school_or_college = input('Enter School or College: ')
        age = int(input('Enter Age(12-35): '))
        various_games_ids = choose_games_of_interest()  # Collect game IDs
        weight_kg = float(input('Enter Weight (kg): '))
        height_m = float(input('Enter Height (m): '))
        special_needs = input('Enter Special Needs (if any): ')
        enroll_type = input ('Enrollment Type(Individual/group): ')
        group_name = input ('Group Name(if applicable): ')
        
    

        cur.execute("""INSERT INTO Members
        (Full_Name, Gender, Next_of_kin, Date_of_birth,
        Contact_Details, Sub_County, School_or_College, Age,
        Various_Games_of_Interest_in_order, Weight_kg, Height_m, Special_Needs,
        Enrollment_type, Group_Name)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (full_name, gender, next_of_kin, date_of_birth,
         contact_details, sub_county, school_or_college,
         age,  ",".join(various_games_ids), weight_kg, height_m,
         special_needs, enroll_type, group_name))

            # Get the member ID of the newly inserted member
        cur.execute("SELECT member_id FROM Members WHERE Full_Name = ?", (full_name,))
        member_id = cur.fetchone()[0]

    # Insert the member's interests into the Members_Games table
        for game_id in various_games_ids:
            cur.execute("INSERT INTO Members_Games (member_id, game_id) VALUES (?, ?)", (member_id, int(game_id.strip())))

        # Get the member ID of the newly inserted member
        cur.execute("SELECT member_id FROM Members WHERE Full_Name = ?", (full_name,))
        member_id = cur.fetchone()[0]

        conn.commit()
        print(f'Member {full_name} added successfully!')

           # Update the count of members for each game in the dictionary
        for game_id in various_games_ids:
            game_id = int(game_id.strip())
            if game_id not in games_count:
                games_count[game_id] = 1
            else:
                games_count[game_id] += 1


        conn.commit()
        print ('Member Added Successfully')
    except ValueError:
        print("Invalid input. Please enter a valid input.")        
    except sqlite3.IntegrityError as e:
        print("Error:", e)
        print("Failed to add member. Please check your input and try again.")
    except Exception as e:
        print("An unexpected error occurred:", e)
        print("Failed to add member. Please try again later.")

        
# Call the add_member() function to add new members

add_member()

##enrollment fees calculation

        # Insert enrollment fee details into the EnrollmentFees table
cur.execute("""INSERT INTO EnrollmentFees
            (member_id, member_name, enroll_type,  group_name, enrollment_fee)
            VALUES (?, ?, ?, ?, ?)""",
                    (member_id, full_name, enroll_type, group_name, enrollment_fee))

# Calculate the enrollment fee based on the enrollment type
if enroll_type.lower() == 'individual':
    enrollment_fee = 1000
elif enroll_type.lower() == 'group':
    num_members = int(input('Enter the number of people in the group: '))
    enrollment_fee = 500 * num_members
else:
    while True:
        print('Invalid enrollment type. Please enter "Individual" or "Group".')
        enroll_type = input('Enrollment Type (Individual/Group): ')
        if enroll_type.lower() == 'individual':
            enrollment_fee = 1000
            break
        elif enroll_type.lower() == 'group':
            num_members = int(input('Enter the number of people in the group: '))
            enrollment_fee = 500 * num_members
            break
            return


# Function to update age group for each member
def update_age_group():
    cur.execute("SELECT member_id, Age FROM Members")
    members = cur.fetchall()
    for member_id, age in members:
        age_group = ""
        if 12 <= age <= 17:
            age_group = "Minors"
        elif 18 <= age <= 25:
            age_group = "Middle Group"
        elif 26 <= age <= 35:
            age_group = "Seniors"

        cur.execute("UPDATE Members SET Age_Group = ? WHERE member_id = ?", (age_group, member_id))
    conn.commit()

update_age_group()

# Show the count of members for each game
def show_mem_game():
    print("Number of Members in Each Game:")
    for game_id, count in games_count.items():
        print(f"Game ID {game_id}: {count} members")


##show all members
def show_members():
    cur.execute('SELECT * FROM Members')
    members = cur.fetchall()
    for member in members:
        print(member)
    
    
show_members()
    
##create a table for games patrons
cur.execute("""CREATE TABLE IF NOT EXISTS Games_Patrons
        (patron_id INTEGER PRIMARY KEY,
        full_name TEXT,
        patron_for_game INTEGER,
        FOREIGN KEY(patron_for_game) REFERENCES Available_Games(Game_id) ON DELETE CASCADE
        )
        """)


def create_patron():
    pat_id = int(input('enter patron id: '))
    name = input('enter patron name: ')
    gameid = None  # Initialize to None for now, to be updated later
    rows = [(pat_id, name, gameid)]
    
    ##insert patrons names into the table
    cur.executemany("""INSERT INTO Games_Patrons
            VALUES (?,?,?)
    """, rows)
    conn.commit()

## call the create_patron() function for each game_id
for game_id in range(1, len(available_games) + 1):
    create_patron()



# Function to update Game_Captain in Available_Games
def update_game_captain(game_id):
    game_capt = int(input(f"Enter Game Captain (member id) for Game {game_id}: "))
    cur.execute("UPDATE Available_Games SET Game_Captain = ? WHERE Game_id = ?", (game_capt, game_id))
    conn.commit()

# Function to update Game_Patron in Available_Games
def update_game_patron(game_id):
    patron_id = int(input(f"Enter Patron ID for Game {game_id}: "))
    cur.execute("UPDATE Available_Games SET Game_Patron = ? WHERE Game_id = ?", (patron_id, game_id))
    conn.commit()

# Function to update both patron_for_game and Game_Captain in Available_Games
def update_game_info():
    for game_id in range(1, len(available_games) + 1):
        update_game_patron(game_id)
        update_game_captain(game_id)

# Call the update_game_info function to update both patron_for_game and Game_Captain for each game
update_game_info()

# Function to update patron_for_game in Games_Patrons
def update_pat4game(game_id):
    patron_id = int(input(f"Enter Patron ID for Game {game_id}: "))
    cur.execute("UPDATE Games_Patrons SET patron_for_game = ? WHERE patron_id = ?", (game_id, patron_id))
    conn.commit()
    
# Loop to update patron_for_game for each game_id
for game_id in range(1, len(available_games) + 1):
    update_pat4game(game_id)
    

## execute SELECT statement to fetch all rows from Games_Patrons
cur.execute("SELECT * FROM Games_Patrons")


##show all patrons
for patron in cur.fetchall():
    print(patron)
    
##select rows
cur.execute('SELECT * FROM Available_Games')

##print rows
for item in cur.fetchall():
    print(item)

# Create the LossesAndDamages table
cur.execute("""CREATE TABLE IF NOT EXISTS LossesAndDamages (
    loss_id INTEGER PRIMARY KEY AUTOINCREMENT,
    item TEXT,
    market_value INT,
    surcharged_price INT,
    game_id INTEGER,
    game_captain INTEGER,
    team_members TEXT,
    FOREIGN KEY (game_id) REFERENCES Available_Games(Game_id),
    FOREIGN KEY (game_captain) REFERENCES Members(member_id)
    )
""")

##record loss or dameges
def record_loss_or_damage():
    print("Record Losses and Damages")
    loss_id = random.randint(10000, 99999)
    item = input("Enter name of the item: ")
    market_value = int(input("Enter market value of the item: "))
    surcharged_price = int(market_value * 1.1)  # Surcharge at 110% of market value
    game_id = int(input("Enter game ID: "))
    game_captain = int(input("Enter the captain's member ID for the game: "))
    team_members = input("Enter member IDs of team members (comma-separated): ")

    # Insert the loss or damage record into the LossesAndDamages table
    cur.execute("""INSERT INTO LossesAndDamages
        (loss_id, item, market_value, surcharged_price, game_id, game_captain, team_members)
        VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (loss_id, item, market_value, surcharged_price, game_id, game_captain, team_members))
    conn.commit()
    print("Loss or damage recorded successfully!")

record_loss_or_damage()



##create table for store_items
conn.execute("""CREATE TABLE IF NOT EXISTS store_items
        (Item TEXT PRIMARY KEY,
        Price INT,
        Stock_level INT
        )
        """)


# Function to add store items or update their prices
def add_store_items(item, price, stock_level=0):
    try:
        cur.execute("INSERT INTO store_items (Item, Price, Stock_level) VALUES (?, ?, ?)", (item, price, stock_level))
    except sqlite3.IntegrityError:
        # Item already exists, update the price
        cur.execute("UPDATE store_items SET Price = ? WHERE Item = ?", (price, item))
    conn.commit()

# Adding store items
items_data = [
    ('Bloomer', 250),
    ('Games shorts', 750),
    ('Hockey stick', 2000),
    ('Socks', 350),
    ('Sports shoes', random.choice((1000, 1500, 2000, 3000, 3500, 4000))),
    ('Track suit', 1000),
    ('T-shirt', 800),
    ('Wrapper', 450)
]

for item, price in items_data:
    add_store_items(item, price)

print('Items were added successfully!')

##show items for customer
def items_4customer():
    cur.execute("SELECT Item, Price FROM store_items")
    items = cur.fetchall()
    for i in items:
        print(i)

items_4customer()

##item for admin
def item_adm():
    cur.execute("SELECT * FROM store_items")
    items = cur.fetchall()
    for i in items:
        print(i)

item_adm()        

##create a table for sales to mbrs
cur.execute("""CREATE TABLE IF NOT EXISTS Sales
    (sale_id INT PRIMARY KEY,
    item TEXT,
    Qty INT,
    Price INT,
    Member_name TEXT,
    Total INT,
    FOREIGN KEY (item) REFERENCES store_items(item)
    )
    """)

def id2name():
    mem_id = int(input('Enter member_id: '))
    cur.execute("""SELECT Full_Name FROM Members
                WHERE member_id = ? 
                """, (mem_id,))
    names = cur.fetchall()
    return names    

# Function to insert sales
def insert_sales():
    print('Sales')
    sales_id = random.randint(10000, 99999)
    item = input('Enter item name: ')
    qty = int(input('Quantity sold: '))

    # Fetch the price of the given item
    cur.execute("SELECT Price FROM store_items WHERE Item = ?", (item,))
    price = cur.fetchone()[0]

    # Calculate total
    total = qty * price

    mem_name = id2name()
    if mem_name:
        
        cur.execute("""INSERT INTO Sales (sale_id, item, Qty, Price, Member_name, Total)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (sales_id, item, qty, price, mem_name[0][0], total))
        conn.commit()
    else:
        print('Invalid Member ID. Sales cannot be added!!')
     # Update stock level in store_items after sales
    cur.execute("UPDATE store_items SET Stock_level = Stock_level - ? WHERE Item = ?", (qty, item))
    conn.commit()
          
insert_sales()    

##show all sales
def show_sales():
    print('Sales List')
    cur.execute("SELECT * FROM Sales")
    sale = cur.fetchall()
    print(sale)
    
show_sales()

##show sales for certain item
def show_sales4():
    print('Enter item to show sales: ')
    item_2show = input()
    cur.execute("SELECT * FROM Sales WHERE item = ?", (item_2show,))
    items = cur.fetchall()
    for item in items:
        print(item)

show_sales4()

##create purchases table
cur.execute("""CREATE TABLE IF NOT EXISTS Purchases
    (purchase_id INT PRIMARY KEY,
    item TEXT,
    Qty INT,
    Buying_price INT,
    Total INT,
    FOREIGN KEY (item) REFERENCES Store_items(item)
    )

    """)

##insert values into columns
def insert_purchase():
    print('Purchase List')
    p_id = random.randint(10000, 999999)
    item = input('Item Name: ')
    qty = int(input('Quantity Purchased: '))
    price = int(input('Buying Price: '))
    total = (qty * price)
    cur.execute(""" INSERT INTO Purchases
        VALUES (?, ?, ?, ?, ?)
        """, (p_id, item, qty, price, total))
    conn.commit()

      # Update stock level in store_items after purchase
    cur.execute("UPDATE store_items SET Stock_level = Stock_level + ? WHERE Item = ?", (qty, item))
    conn.commit()

insert_purchase()

##show all sales
def show_purch():
    print('Show Purchases')
    cur.execute("SELECT * FROM Purchases")
    prch = cur.fetchall()
    for item in prch:
        print(item)
    
show_purch()

##show sales for certain item
def show_purch4():
    print('Enter item to show purchases: ')
    item_2show = input()
    cur.execute("SELECT * FROM Purchases WHERE item = ?", item_2show)
    items = cur.fetchall()
    for item in items:
        print(item)

show_purch4()

##create a discounts table
cur.execute("""CREATE TABLE IF NOT EXISTS discounts (
    discount_id INTEGER PRIMARY KEY,
    member_name TEXT,
    discount_amount REAL
)""")


# Create a trigger to insert into discounts when sales > kshs. 100000
cur.execute("""CREATE TRIGGER IF NOT EXISTS disc_trigger
AFTER INSERT ON Purchases
FOR EACH ROW
WHEN (SELECT SUM(Total) FROM Sales WHERE Member_name = NEW.Member_name) > 10000
BEGIN
    -- Calculate the discount amount (5% of the total purchase value)
    INSERT INTO discounts (member_name, discount_amount)
    VALUES (NEW.Member_name, (SELECT SUM(Total) * 0.05 FROM Sales WHERE Member_name = NEW.Member_name));
END;
""")

##show discounts
def show_disc():
    cur.execute("SELECT * FROM discounts")
    disc = cur.fetchall()
    for disco in disc:
        print(disco) 

show_disc()

##commit the querry to the db
conn.commit()
          
##close cursor
cur.close()
##close the connection
conn.close()
