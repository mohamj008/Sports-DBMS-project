import sqlite3
import random

# Define the handle_error decorator
def handle_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as ve:
            print("ValueError:", ve)
            # Custom error handling logic for ValueError
            # You can log, print, or raise a custom exception here
        except sqlite3.IntegrityError as ie:
            print("IntegrityError:", ie)
            # Custom error handling logic for IntegrityError
            # You can log, print, or raise a custom exception here
        except Exception as e:
            print("An unexpected error occurred:", e)
            # Custom error handling logic for other exceptions
            # You can log, print, or raise a custom exception here
    return wrapper

##create connection to a database
conn = sqlite3.connect('maringosports.db')

##create a cursor to modify the db
cur = conn.cursor()


@handle_error
def create_tables():
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
        Age_Group TEXT
        )
        """)

    # Create the EnrollmentFees table to store enrollment fee details
    cur.execute("""CREATE TABLE IF NOT EXISTS EnrollmentFees (
        enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        member_id INTEGER,
        member_name TEXT,
        enroll_type TEXT DEFAULT 'Individual',
        group_name TEXT DEFAULT 'None',
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

    # Create the Members_Games table to store the association between members and games
    cur.execute("""CREATE TABLE IF NOT EXISTS Members_Games (
        member_id INTEGER,
        game_id INTEGER,
        PRIMARY KEY (member_id, game_id),
        FOREIGN KEY (member_id) REFERENCES Members (member_id),
        FOREIGN KEY (game_id) REFERENCES Available_Games (Game_id)
        )
    """)

    ##create a table for games patrons
    cur.execute("""CREATE TABLE IF NOT EXISTS Games_Patrons
            (patron_id INTEGER PRIMARY KEY,
            full_name TEXT,
            patron_for_game INTEGER,
            FOREIGN KEY(patron_for_game) REFERENCES Available_Games(Game_id) ON DELETE CASCADE
            )
            """)

    # Create the LossesAndDamages table
    cur.execute("""CREATE TABLE IF NOT EXISTS LossesAndDamages (
        loss_id INTEGER PRIMARY KEY AUTOINCREMENT,
        item TEXT,
        market_value INT,
        surcharged_price INT,
        game_id INTEGER,
        game_captain INTEGER,
        FOREIGN KEY (game_id) REFERENCES Available_Games(Game_id),
        FOREIGN KEY (game_captain) REFERENCES Members(member_id)
        )
    """)

    ##create table for store_items
    conn.execute("""CREATE TABLE IF NOT EXISTS store_items
            (Item TEXT PRIMARY KEY,
            Price INT,
            Stock_level INT
            )
            """)

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

    ##create a discounts table
    cur.execute("""CREATE TABLE IF NOT EXISTS discounts (
        discount_id INTEGER PRIMARY KEY AUTOINCREMENT,
        member_name TEXT,
        discount_amount REAL
    )""")

    # Create the FacilitationFees table to store facilitation fee details
    cur.execute("""CREATE TABLE IF NOT EXISTS FacilitationFees (
        facilitation_id INTEGER PRIMARY KEY AUTOINCREMENT,
        member_id INTEGER,
        member_name TEXT,
        game_id INTEGER,
        patron_id INTEGER,
        facilitation_fee INT,
        patron_commission INT,
        FOREIGN KEY (member_id) REFERENCES Members (member_id),
        FOREIGN KEY (game_id) REFERENCES Available_Games (Game_id),
        FOREIGN KEY (patron_id) REFERENCES Games_Patrons (patron_id)
        )
    """)

    conn.commit()

##@handle_error
##insert members into the table
def add_member(full_name, gender, next_of_kin, date_of_birth,
               contact_details, sub_county, school_or_college,
               age, various_games_ids, weight_kg,
                height_m, special_needs, enroll_type, group_name, age_group):
    ##handle any exception
    try:
        cur.execute("""INSERT INTO Members
        (Full_Name, Gender, Next_of_kin, Date_of_birth,
        Contact_Details, Sub_County, School_or_College, Age,
        Various_Games_of_Interest_in_order, Weight_kg, Height_m, Special_Needs,
        Enrollment_type, Group_Name, Age_Group)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (full_name, gender.strip(), next_of_kin, date_of_birth,
         contact_details, sub_county, school_or_college,
         age.strip(),  ",".join(various_games_ids), weight_kg, height_m,
         special_needs, enroll_type.strip(), group_name, age_group))
        conn.commit()

            # Get the member ID of the newly inserted member
        cur.execute("SELECT member_id FROM Members WHERE Full_Name = ?", (full_name,))
        member_id = cur.fetchone()[0]

    # Insert the member's interests into the Members_Games table
        for game_id in various_games_ids:
            cur.execute("INSERT INTO Members_Games (member_id, game_id) VALUES (?, ?)", (member_id, int(game_id.strip())))

        conn.commit()
        print(f'Member {full_name} added successfully!')


    except ValueError:
        print("Invalid input. Please enter a valid input.")        
    except sqlite3.IntegrityError as e:
        print("Error:", e)
        print("Failed to add member. Please check your input and try again.")
    except Exception as e:
        print("An unexpected error occurred:", e)
        print("Failed to add member. Please try again later.")

        
# Call the add_member() function to add new members



@handle_error
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

@handle_error
##function to add available games
def add_avail_games():
    ##list of available games
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

@handle_error
##function to create patron    
def create_patron(pat_id, name, gameid):
    
    ##insert patrons names into the table
    cur.execute("""INSERT INTO Games_Patrons
            VALUES (?,?,?)
    """, (pat_id, name, gameid))
    conn.commit()


@handle_error
##function to update available games list
def update_avail_games(gameid, patid, captid):
    cur.execute("UPDATE Available_Games SET Game_Patron = ? WHERE Game_id = ?", (patid, gameid))
    cur.execute("UPDATE Available_Games SET Game_Captain = ? WHERE Game_id = ?", (captid, gameid))
    conn.commit()
    print('Games Updated Successfully!')
    
@handle_error
##function to add facilitation fees
def add_facilitation_fee(memb_id, memb_name, game_id, patr_id, facilitation_fee, patron_commission):
    cur.execute("SELECT Full_Name FROM Members WHERE member_id = ?", (memb_id,))
    memb_name = cur.fetchone()[0]
    
    patron_commission = facilitation_fee * 0.2  # Calculate the patron's commission (20% of facilitation fee)
    
    cur.execute("""INSERT INTO FacilitationFees
        (member_id, member_name, game_id, patron_id, facilitation_fee, patron_commission)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (memb_id, memb_name, game_id, patr_id, facilitation_fee, patron_commission))
    conn.commit()
    print(f'Facilitation Fees for member {memb_name} added successfully!')


@handle_error
# Function to add enrollment details
def add_enrollment(member_id, member_name, enroll_type, group_name, enrollment_fee):
    try:
        # Retrieve the member's name based on the provided member_id
        cur.execute("SELECT Full_Name FROM Members WHERE member_id = ?", (member_id,))
        member_name = cur.fetchone()[0]

        # Retrieve the enroll_type based on the provided member_id
        cur.execute("SELECT Enrollment_Type FROM Members WHERE member_id = ?", (member_id,))
        enroll_type = cur.fetchone()[0]

        # Calculate the enrollment_fee based on the enroll_type
        if enroll_type.lower() == "individual":
            enrollment_fee = 1000
        else:
            enrollment_fee = 500

        # If group_name is not provided, use the value from the database
        if not group_name:
            cur.execute("SELECT Group_Name FROM Members WHERE member_id = ?", (member_id,))
            group_name = cur.fetchone()[0]

        # Insert the enrollment details into the EnrollmentFees table
        cur.execute("""INSERT INTO EnrollmentFees
                (member_id, member_name, enroll_type, group_name, enrollment_fee)
                VALUES (?, ?, ?, ?, ?)
                """, (member_id, member_name, enroll_type, group_name, enrollment_fee))

        # Commit the changes to the database
        conn.commit()

        print(f'Enrollment for member {member_name} added successfully!')

    except Exception as e:
        # Handle exceptions and roll back changes if an error occurs
        conn.rollback()
        raise e


        
@handle_error
##function to add loss and damage

def record_loss_or_damage(item, market_value, surcharged_price, game_id, game_captain):
    print("Record Losses and Damages")
    
    cur.execute("SELECT Game_Captain FROM Available_Games WHERE Game_ID = ?", (game_id,))
    game_captain = cur.fetchone()[0]

     
    # Insert the loss or damage record into the LossesAndDamages table
    cur.execute("""INSERT INTO LossesAndDamages
        (item, market_value, surcharged_price, game_id, game_captain)
        VALUES (?, ?, ?, ?, ?)""",
                (item, market_value, surcharged_price, game_id, game_captain))
    conn.commit()
    print("Loss or damage recorded successfully!")

    
##show all members
def show_all_members():
    try:
        cur.execute("SELECT * FROM Members")
        members = cur.fetchall()
        return members
    except Exception as e:
        print("An error occurred while fetching members:", e)
        return []
    

# Function to show all games
def show_all_games():
    try:
        cur.execute("SELECT * FROM Available_Games")
        games = cur.fetchall()
        return games
    except Exception as e:
        print("An error occurred while fetching games:", e)
        return []
    

# Function to show all enrollment fees
def show_enrollment_fees():
    cur.execute("SELECT member_id, member_name, enroll_type, group_name, enrollment_fee FROM EnrollmentFees")
    enrollment_fees = cur.fetchall()
    return enrollment_fees



##function to show total enroll fee
def show_total_enroll():
    cur.execute("""SELECT SUM(enrollment_fee)
        FROM EnrollmentFees""")
    totals = cur.fetchone()
    return totals

# Function to show all facilitation fees
def show_facilitation_fees():
    cur.execute("SELECT * FROM FacilitationFees")
    fees = cur.fetchall()
    return fees


def show_total_facs():
    cur.execute("SELECT SUM(facilitation_fee) FROM FacilitationFees")
    total_facs = cur.fetchone()
    return total_facs


def show_patron_comm():
    cur.execute("SELECT patron_id, patron_commission FROM FacilitationFees")
    pat_comm = cur.fetchall()
    return pat_comm

# Function to show all losses and damages
def show_losses_and_damages():
    cur.execute("SELECT * FROM LossesAndDamages")
    losses = cur.fetchall()
    return losses


       

