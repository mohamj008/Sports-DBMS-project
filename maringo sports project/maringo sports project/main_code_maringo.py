import sqlite3
import random
import membersdb
import store_items
import tkinter as tk
from tkinter import ttk, messagebox

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


# Create tables
membersdb.create_tables()

# Create the main application window
app = tk.Tk()
app.title("Maringo Sports Club Management System")
app.geometry("800x600")

# Add input fields and labels to the GUI
full_name_label = tk.Label(app, text="Full Name:")
full_name_entry = tk.Entry(app)

gender_label = tk.Label(app, text="Gender:")
gender_entry = tk.Entry(app)

next_of_kin_label = tk.Label(app, text='Next of Kin: ')
next_of_kin_entry = tk.Entry(app)

date_of_birth_label = tk.Label(app, text='DOB (YYYY-MM-DD): ')
date_of_birth_entry = tk.Entry(app)

contact_details_label = tk.Label(app, text="Contact Details: ")
contact_details_entry = tk.Entry(app)

sub_county_label = tk.Label(app, text='Sub-County: ')
sub_county_entry = tk.Entry(app)

school_or_college_label = tk.Label(app, text='School or College: ')
school_or_college_entry = tk.Entry(app)

age_label = tk.Label(app, text='Age (integer): ')
age_entry = tk.Entry(app)

various_games_ids_label = tk.Label(app, text='Games of Interest (comma-seperated): ')
various_games_ids_entry = tk.Entry(app)

weight_kg_label = tk.Label(app, text='Weight (kg): ')
weight_kg_entry = tk.Entry(app)

height_m_label = tk.Label(app, text = 'Height (m): ')
height_m_entry = tk.Entry(app)

special_needs_label = tk.Label(app, text='Special Needs (if any): ')
special_needs_entry = tk.Entry(app)


enroll_type_label = tk.Label(app, text='Enrollment Type (Individual/group): ')
enroll_type_entry = tk.Entry(app)

group_name_label = tk.Label(app, text='Group Name (if any): ')
group_name_entry = tk.Entry(app)


# Function to handle member registration
@handle_error
def register_member():
    full_name = full_name_entry.get()
    gender = gender_entry.get()
    next_of_kin = next_of_kin_entry.get()
    date_of_birth = date_of_birth_entry.get()
    contact_details = contact_details_entry.get()
    sub_county = sub_county_entry.get()
    school_or_college = school_or_college_entry.get()
    age = age_entry.get()
    various_games_ids =  various_games_ids_entry.get()
    weight_kg = weight_kg_entry.get()
    height_m = height_m_entry.get()
    special_needs = special_needs_entry.get()
    enroll_type = enroll_type_entry.get()
    group_name = group_name_entry.get()
    age_group = None
     
 # Call the membersdb function to add the member to the database
    membersdb.add_member(full_name, gender, next_of_kin,
                         date_of_birth, contact_details, sub_county, school_or_college,
                         age, various_games_ids, weight_kg,
                         height_m, special_needs, enroll_type, group_name, age_group)

    membersdb.update_age_group()
    
       # Show a message box to inform the user that the registration was successful
    messagebox.showinfo("Success", "Member registered successfully!")
    pass

register_button = tk.Button(app, text="Register Member", command=register_member)


##function to show details entry
def show_member_details(): 
    full_name_label.pack()
    full_name_entry.pack()
    
    
    gender_label.pack()
    gender_entry.pack()

    
    next_of_kin_label.pack()
    next_of_kin_entry.pack()

    
    date_of_birth_label.pack()
    date_of_birth_entry.pack()

    
    contact_details_label.pack()
    contact_details_entry.pack()

    
    sub_county_label.pack()
    sub_county_entry.pack()

    
    school_or_college_label.pack()
    school_or_college_entry.pack()

    
    age_label.pack()
    age_entry.pack()

    
    various_games_ids_label.pack()
    various_games_ids_entry.pack()

    
    weight_kg_label.pack()
    weight_kg_entry.pack()

    
    height_m_label.pack()
    height_m_entry.pack()

    
    special_needs_label.pack()
    special_needs_entry.pack()

    
    enroll_type_label.pack()
    enroll_type_entry.pack()

    
    group_name_label.pack()
    group_name_entry.pack()

    register_button.pack()

    
##function to hide details
def hide_member_details():
    full_name_label.pack_forget()
    full_name_entry.pack_forget()

    gender_label.pack_forget()
    gender_entry.pack_forget()

    next_of_kin_label.pack_forget()
    next_of_kin_entry.pack_forget()

    date_of_birth_label.pack_forget()
    date_of_birth_entry.pack_forget()

    contact_details_label.pack_forget()
    contact_details_entry.pack_forget()

    sub_county_label.pack_forget()
    sub_county_entry.pack_forget()

    school_or_college_label.pack_forget()
    school_or_college_entry.pack_forget()

    age_label.pack_forget()
    age_entry.pack_forget()

    various_games_ids_label.pack_forget()
    various_games_ids_entry.pack_forget()

    weight_kg_label.pack_forget()
    weight_kg_entry.pack_forget()

    height_m_label.pack_forget()
    height_m_entry.pack_forget()

    special_needs_label.pack_forget()
    special_needs_entry.pack_forget()

    enroll_type_label.pack_forget()
    enroll_type_entry.pack_forget()

    group_name_label.pack_forget()
    group_name_entry.pack_forget()

    register_button.pack_forget()


##call function to add available games
def avail_game():
    membersdb.add_avail_games()
    messagebox.showinfo("Success", "Available games added successfully!")

    


# Add input fields and labels to the GUI
pat_id_label = tk.Label(app, text="Patron ID: ")
pat_id_entry = tk.Entry(app)

name_label = tk.Label(app, text='Patron Name: ')
name_entry = tk.Entry(app)

gameid_label = tk.Label(app, text='Game ID: ')
gameid_entry = tk.Entry(app)

##function to add patron
@handle_error
def add_patron():
    pat_id = pat_id_entry.get()
    name = name_entry.get()
    gameid = gameid_entry.get()
     ##call function to create patron
    membersdb.create_patron(pat_id, name, gameid)
    
    messagebox.showinfo("Success", "Patron registered successfully!")
    pass

##add button to register new game patron
add_pat_button = tk.Button(app, text='Add New Patron: ', command=add_patron)


##show patron detail entry in menu
def show_pat_details():
    pat_id_label.pack()
    pat_id_entry.pack()


    name_label.pack()
    name_entry.pack()



    gameid_label.pack()
    gameid_entry.pack()

    add_pat_button.pack()
    
##hide pat details in menu
def hide_pat_details():
    pat_id_label.pack_forget()
    pat_id_entry.pack_forget()


    name_label.pack_forget()
    name_entry.pack_forget()



    gameid_label.pack_forget()
    gameid_entry.pack_forget()

    add_pat_button.pack_forget()







# Add input fields and labels for updating available games
gameid_label = tk.Label(app, text='Game ID: ')
gameid_entry = tk.Entry(app)


patid_label = tk.Label(app, text='Patron ID: ')
patid_entry = tk.Entry(app)


captid_label = tk.Label(app, text="Captain ID: ")
captid_entry = tk.Entry(app)


def update_avail_games():

    
    # Get the values from the entry widgets
    gameid = gameid_entry.get()
    captid = captid_entry.get()
    patid = patid_entry.get()
    # Call the membersdb function to update available games in the database
    membersdb.update_avail_games(gameid, patid, captid)

    # Show a message box to inform the user that the update was successful
    messagebox.showinfo("Success", "Available games updated successfully!")

update_button = tk.Button(app, text="Update Game Details", command=update_avail_games)

##show games update details
def show_details():
    gameid_label.pack()
    gameid_entry.pack()

    patid_label.pack()
    patid_entry.pack()

    captid_label.pack()
    captid_entry.pack()
    update_button.pack()

##hide games update details
def hide_details():
    gameid_label.pack_forget()
    gameid_entry.pack_forget()

    patid_label.pack_forget()
    patid_entry.pack_forget()

    captid_label.pack_forget()
    captid_entry.pack_forget()

    update_button.pack_forget()


##function to show all members
def all_members():
    mem_data = membersdb.show_all_members()
    if mem_data:
       # Create a new window to display the table
        table_window = tk.Toplevel(app)
        table_window.title("All Members")

        # Create a Treeview widget
        tree = ttk.Treeview(table_window)
        tree["columns"] = ("ID", "Full Name", "Gender", "Next of Kin", "DOB", "Contact", "Sub-County", "School/College",
                           "Age", "Various Games", "Weight (kg)", "Height (m)", "Special Needs", "Enroll Type",
                           "Group Name", "Age Group")
        tree.heading("#0", text="", anchor="w")
        tree.heading("#1", text="ID", anchor="center")
        tree.heading("#2", text="Full Name", anchor="center")
        tree.heading("#3", text="Gender", anchor="center")
        tree.heading("#4", text="Next of Kin", anchor="center")
        tree.heading("#5", text="DOB", anchor="center")
        tree.heading("#6", text="Contact", anchor="center")
        tree.heading("#7", text="Sub-County", anchor="center")
        tree.heading("#8", text="School/College", anchor="center")
        tree.heading("#9", text="Age", anchor="center")
        tree.heading("#10", text="Various Games", anchor="center")
        tree.heading("#11", text="Weight (kg)", anchor="center")
        tree.heading("#12", text="Height (m)", anchor="center")
        tree.heading("#13", text="Special Needs", anchor="center")
        tree.heading("#14", text="Enroll Type", anchor="center")
        tree.heading("#15", text="Group Name", anchor="center")
        tree.heading("#16", text="Age Group", anchor="center")

        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("ID", width=50, anchor="center")
        tree.column("Full Name", width=200, anchor="center")
        tree.column("Gender", width=60, anchor="center")
        tree.column("Next of Kin", width=150, anchor="center")
        tree.column("DOB", width=100, anchor="center")
        tree.column("Contact", width=150, anchor="center")
        tree.column("Sub-County", width=100, anchor="center")
        tree.column("School/College", width=150, anchor="center")
        tree.column("Age", width=50, anchor="center")
        tree.column("Various Games", width=150, anchor="center")
        tree.column("Weight (kg)", width=100, anchor="center")
        tree.column("Height (m)", width=100, anchor="center")
        tree.column("Special Needs", width=100, anchor="center")
        tree.column("Enroll Type", width=60, anchor="center")
        tree.column("Group Name", width=100, anchor="center")
        tree.column("Age Group", width=100, anchor="center")


        # Insert data rows into the table
        for memb in mem_data:
            tree.insert("", "end", values=memb)

        # Add scrollbar to the table
        scrollbar = ttk.Scrollbar(table_window, orient="vertical", command=tree.yview)
        scrollbar = ttk.Scrollbar(table_window, orient="horizontal", command=tree.xview)
        tree.configure(yscroll=scrollbar.set)
        tree.configure(xscroll=scrollbar.set)

        # Pack the tree and scrollbar
        tree.pack(fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        table_window.geometry("1200x1200")

    else:
        messagebox.showinfo("No Members", "No members found in the database")


##facilitation fees
memb_id_label = tk.Label(app, text="Member ID: ")
memb_id_entry = tk.Entry(app)

game_id_label = tk.Label(app, text="Game ID")
game_id_entry = tk.Entry(app)

patr_id_label = tk.Label(app, text="Patron ID")
patr_id_entry = tk.Entry(app)

def add_facilitation():
    memb_id = memb_id_entry.get()
    memb_name = ""
    game_id = game_id_entry.get()
    patr_id = patr_id_entry.get()
    

    facilitation_fee = 500
    patron_commission = 0
    membersdb.add_facilitation_fee(memb_id, memb_name, game_id, patr_id, facilitation_fee, patron_commission)
    messagebox.showinfo("Success", "Facilitation Payment added successfully!")

fac_button = tk.Button(app, text="Add Facilitation", command=add_facilitation)

def show_memb_game_id():
    memb_id_label.pack()
    memb_id_entry.pack()
    game_id_label.pack()
    game_id_entry.pack()
    patr_id_label.pack()
    patr_id_entry.pack()
    fac_button.pack()
    
def hide_memb_game_id():
    memb_id_label.pack_forget()
    memb_id_entry.pack_forget()
    game_id_label.pack_forget()
    game_id_entry.pack_forget()
    patr_id_label.pack_forget()
    patr_id_entry.pack_forget()
    fac_button.pack_forget()
    
def add_facilitation():
    memb_id = memb_id_entry.get()
    memb_name = ""
    game_id = game_id_entry.get()
    patr_id = patr_id_entry.get()
    

    facilitation_fee = 500
    patron_commission = 0
    membersdb.add_facilitation_fee(memb_id, memb_name, game_id, patr_id, facilitation_fee, patron_commission)
    messagebox.showinfo("Success", "Facilitation Payment added successfully!")


##show facilitation payment
def show_facs():
    fac_fees = membersdb.show_facilitation_fees()
    if fac_fees:
       # Create a new window to display the table
        fac_window = tk.Toplevel(app)
        fac_window.title("Facilitation Payment")

        # Create a Treeview widget
        tree = ttk.Treeview(fac_window)
        tree["columns"] = ("Facil ID", "Memb ID", "Name", "Game ID", "Patron ID", "Facil Fees", "Commission")
        
        tree.heading("#0", text="", anchor="w")
        tree.heading("#1", text="Facil ID", anchor="center")
        tree.heading("#2", text="Member ID", anchor="center")
        tree.heading("#3", text="Name", anchor="center")
        tree.heading("#4", text="Game ID", anchor="center")
        tree.heading("#5", text="Patron ID", anchor="center")
        tree.heading("#6", text="Facil Fees", anchor="center")
        tree.heading("#7", text="Commission", anchor="center")

        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("Facil ID", width=50, anchor="center")
        tree.column("Memb ID", width=50, anchor="center")
        tree.column("Name", width=200, anchor="center")
        tree.column("Game ID", width=50, anchor="center")
        tree.column("Patron ID", width=50, anchor="center")
        tree.column("Facil Fees", width=100, anchor="center")
        tree.column("Commission", width=100, anchor="center")


        # Add the games data to the table
        for fees in fac_fees:
            tree.insert("", "end", values=fees)

        # Pack the Treeview widget and set its size
        tree.pack(fill="both", expand=True)

        # Set the window size based on the table's content
        fac_window.geometry("800x800")
    else:
        messagebox.showinfo("No Facilitation Fees", "No facilitation Data found in the database.")
         



def total_facs():
    facil_total = membersdb.show_total_facs()

    if facil_total:

        facil_window = tk.Toplevel(app)
        facil_window.title("Total Facilitation Paid")
        tree = ttk.Treeview(facil_window)
        
        tree["columns"] = ("Total facilitation Paid")
        
        tree.heading("#0", text="", anchor="w")
        
        tree.heading("#1", text="Total Facilitation", anchor="center")
        
        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("1", width=100, anchor="center")

        for totals in facil_total:
                    tree.insert("", "end", values=(totals,))

        tree.pack(fill="both", expand=True)


    else:
        
        messagebox.showinfo("No Facilitation Fees", "No facilitation Data found in the database.")


def patr_comm():
    pat_comm = membersdb.show_patron_comm()

    if pat_comm:

        patcomm_window = tk.Toplevel(app)
        patcomm_window.title("Patron Commission")
        tree = ttk.Treeview(patcomm_window)

        tree["columns"] = ("Patron ID", "Patron Commission")

        
        tree.heading("#0", text="", anchor="w")
        tree.heading("#1", text="Patron ID", anchor="center")
        tree.heading("#2", text="Patron Commission", anchor="center")


        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("#1", width=100, anchor="center")
        tree.column("#2", width=100, anchor="center")

        for comm in pat_comm:
            patron_id, patron_commission = comm  # Unpack the tuple
            tree.insert("", "end", values=(patron_id, patron_commission))

        tree.pack(fill="both", expand=True)
    else:
        
        messagebox.showinfo("No Patron Commission", "No commission Data found in the database.")

  
        

##enroll fees
member_id_label = tk.Label(app, text="Member ID: ")
member_id_entry = tk.Entry(app)

def add_enroll():
    member_id = member_id_entry.get()
    member_name = ""  # Initialize member_name to an empty string
    enroll_type = ""  # Initialize enroll_type to an empty string
    group_name = ""   # Initialize group_name to an empty string
    enrollment_fee = 0  # Initialize enrollment_fee to 0

    try:
        # Try to get the values of enroll_type and group_name from the user input
        enroll_type = enroll_type_entry.get()
        group_name = group_name_entry.get()

        # Call the membersdb function to add the enrollment
        membersdb.add_enrollment(member_id, member_name, enroll_type, group_name, enrollment_fee)

        # Show a message box to inform the user that the enrollment was successful
        messagebox.showinfo("Success", "Enrollment added successfully!")

    except ValueError as ve:
        # Handle the ValueError, e.g., show an error message box
        messagebox.showerror("Error", str(ve))

    except sqlite3.IntegrityError as ie:
        # Handle the IntegrityError, e.g., show an error message box
        messagebox.showerror("Error", str(ie))

    except Exception as e:
        # Handle other exceptions, e.g., show an error message box
        messagebox.showerror("Error", "An unexpected error occurred: " + str(e))


enroll_button = tk.Button(app, text="Add Enroll Fees", command=add_enroll)

def show_mem_id():
    member_id_label.pack()
    member_id_entry.pack()
    enroll_button.pack()
    
def hide_mem_id():
    member_id_label.pack_forget()
    member_id_entry.pack_forget()
    enroll_button.pack_forget()
    

def all_enroll():
    enrolls = membersdb.show_enrollment_fees()
    if enrolls:
       # Create a new window to display the table
        enrolls_window = tk.Toplevel(app)
        enrolls_window.title("All Enrollment Fees Payed")
        # Create a Treeview widget
        tree = ttk.Treeview(enrolls_window)
        tree["columns"] = ("Mem ID", "Name", "Enroll Type", "Group Name", "Enroll Fee")

        tree.heading("#0", text="", anchor="w")
        tree.heading("#1", text="Member ID", anchor="center")
        tree.heading("#2", text="Name", anchor="center")
        tree.heading("#3", text="Enroll Type", anchor="center")
        tree.heading("#4", text="Group Name", anchor="center")
        tree.heading("#5", text="Enroll Fee", anchor="center")

        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("Mem ID", width=50, anchor="center")
        tree.column("Name", width=200, anchor="center")
        tree.column("Enroll Type", width=100, anchor="center")
        tree.column("Group Name", width=150, anchor="center")
        tree.column("Enroll Fee", width=150, anchor="center")

        # Add the games data to the table
        for fee in enrolls:
            tree.insert("", "end", values=fee)

        # Pack the Treeview widget and set its size
        tree.pack(fill="both", expand=True)

        # Set the window size based on the table's content
        enrolls_window.geometry("800x800")
    else:
        messagebox.showinfo("No Enroll Fees", "No Enroll Data found in the database.")
         

def total_enroll():
    enrolls = membersdb.show_total_enroll()
    if enrolls:
        enrolls_window = tk.Toplevel(app)
        enrolls_window.title("Total Enrollment Fees")

        tree = ttk.Treeview(enrolls_window)

        tree["columns"] = ("Total Enroll Fee",)
        
        tree.heading("#0", text="", anchor="w")
        tree.heading("#1", text="Total Enroll Fee", anchor="center")
        
        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("Total Enroll Fee", width=150, anchor="center")

        for fee in enrolls:
            tree.insert("", "end", values=fee)
            
        tree.pack(fill="both", expand=True)
        

    else:
        messagebox.showinfo("No Enroll Fees", "No Fees found in the database.")
    
        

        
##function to show all games
def all_games():
    games_data = membersdb.show_all_games()
    if games_data:
         # Create a new window to display the games in a table
        games_window = tk.Toplevel(app)
        games_window.title("All Games")

        # Create a Treeview widget for the table
        tree = ttk.Treeview(games_window)

        # Define the columns for the table
        tree["columns"] = ("Game ID", "Game Name", "Patron ID", "Captain ID")

         # Configure column headings
        tree.heading("#0", text="", anchor="w")
        tree.heading("Game ID", text="Game ID", anchor="center")
        tree.heading("Game Name", text="Game Name", anchor="center")
        tree.heading("Patron ID", text="Patron ID", anchor="center")
        tree.heading("Captain ID", text="Captain ID", anchor="center")

        # Configure column widths
        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("Game ID", width=100, anchor="center")
        tree.column("Game Name", width=150, anchor="center")
        tree.column("Patron ID", width=100, anchor="center")
        tree.column("Captain ID", width=100, anchor="center")

        # Add the games data to the table
        for game in games_data:
            tree.insert("", "end", values=game)

        # Pack the Treeview widget and set its size
        tree.pack(fill="both", expand=True)

        # Set the window size based on the table's content
        games_window.geometry("500x300")


    else:
        messagebox.showinfo("No Games", "No games found in the database.")


##losses and damages
item_label = tk.Label(app, text="Item")
item_entry = tk.Entry(app)

market_value_label = tk.Label(app, text="Market Value")
market_value_entry = tk.Entry(app)


game_id_label = tk.Label(app, text="Game ID")
game_id_entry = tk.Entry(app)

@handle_error
def add_loss_damage():
    item = item_entry.get()
    market_value = int(market_value_entry.get())
    game_id = int(game_id_entry.get())
    surcharged_price = (market_value * 0.1)
    
    game_captain = 0
    team_members = 0
    
    
    membersdb.record_loss_or_damage(item, market_value, surcharged_price, game_id, game_captain)
    

loss_button = tk.Button(app, text="Add Loss or Damage", command=add_loss_damage)

        
def show_loss_details():
    item_label.pack()
    item_entry.pack()

    market_value_label.pack()
    market_value_entry.pack()


    game_id_label.pack()
    game_id_entry.pack()

    loss_button.pack()
def hide_loss_details():
    item_label.pack_forget()
    item_entry.pack_forget()

    market_value_label.pack_forget()
    market_value_entry.pack_forget()


    game_id_label.pack_forget()
    game_id_entry.pack_forget()

    loss_button.pack_forget()
    
@handle_error
def all_loss_damage():
    losses = membersdb.show_losses_and_damages()
    if losses:

        losses_window = tk.Toplevel(app)
        losses_window.title("Losses And Damages")

        tree = ttk.Treeview(losses_window)

        tree["columns"] = ("loss id", "item", "market value", "surcharged price", "Game ID", "Game Capt")

        tree.heading("#0", text="", anchor="w")
        tree.heading("loss id", text="Loss ID", anchor="center")
        tree.heading("item", text="Item", anchor="center")
        tree.heading("market value", text="Market Value", anchor="center")
        tree.heading("surcharged price", text="Surcharged", anchor="center")
        tree.heading("Game ID", text="Game ID", anchor="center")
        tree.heading("Game Capt", text="Game Capt", anchor="center")

        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("loss id", width=100, anchor="center")
        tree.column("item", width=100, anchor="center")
        tree.column("market value", width=100, anchor="center")
        tree.column("surcharged price", width=100, anchor="center")
        tree.column("Game ID", width=100, anchor="center")
        tree.column("Game Capt", width=100, anchor="center")

        for loss in losses:
            tree.insert("", "end", values=loss)

        # Pack the Treeview widget and set its size
        tree.pack(fill="both", expand=True)

        # Set the window size based on the table's content
        losses_window.geometry("800x500")


    else:
        messagebox.showinfo("No Losses/Damages", "No Losses/Damages found in the database.")



##store items
def add_store():
    store_items.add_store_items()

def store_stuffs():
    stuff = store_items.show_store_items()

    if stuff:
        stuff_window = tk.Toplevel(app)
        stuff_window.title("Store Items")

        tree = ttk.Treeview(stuff_window)

        tree["columns"] = ("item", "price", "stock level")
        
        tree.heading("#0", text="", anchor="w")
        tree.heading("#1", text="Item", anchor="center")
        tree.heading("#2", text="Price", anchor="center")
        tree.heading("#3", text="Stock Level", anchor="center")

        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("item", width=200, anchor="center")
        tree.column("price", width=100, anchor="center")
        tree.column("stock level", width=50, anchor="center")

        for items in stuff:
            tree.insert("", "end", values=items)
        
        tree.pack(fill="both", expand=True)

        stuff_window.geometry("800x800")
        
    else:
        messagebox.showinfo("No items", "No items found in the database")


##sales 
item_label = tk.Label(app, text="Item")
item_entry = tk.Entry(app)

qty_label = tk.Label(app, text="Quant")
qty_entry = tk.Entry(app)

mem_id_label = tk.Label(app, text="Member ID")
mem_id_entry = tk.Entry(app)

@handle_error
def sales_insert():
    item = item_entry.get()
    qty = qty_entry.get()
    mem_id = mem_id_entry.get()
    store_items.insert_sales(item, qty, mem_id)
    store_items.discount_trigger()
    messagebox.showinfo("Sales Added Successfully!")
sales_button = tk.Button(app, text="Insert Sales", command=sales_insert)

@handle_error
def sales_details():
    item_label.pack()
    item_entry.pack()

    qty_label.pack()
    qty_entry.pack()

    mem_id_label.pack()
    mem_id_entry.pack()
    
    sales_button.pack()
    
def sales_hide():
    item_label.pack_forget()
    item_entry.pack_forget()

    qty_label.pack_forget()
    qty_entry.pack_forget()

    mem_id_label.pack_forget()
    mem_id_entry.pack_forget()

    sales_button.pack_forget()

##show all sales
@handle_error    
def all_sales():
    all_sales = store_items.show_sales()
    if all_sales:
        sales_window = tk.Toplevel(app)
        sales_window.title("Sales")

        tree = ttk.Treeview(sales_window)
        tree["columns"] = ("Sales ID", "Item", "Qty", "Price", "Name", "Total")

        tree.heading("#0", text="", anchor="w")
        tree.heading("#1", text="Sales ID", anchor="center")
        tree.heading("#2", text="Item", anchor="center")
        tree.heading("#3", text="Quant", anchor="center")
        tree.heading("#4", text="Price", anchor="center")
        tree.heading("#5", text="Name", anchor="center")
        tree.heading("#6", text="Total", anchor="center")

        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("Sales ID", width=100, anchor="center")
        tree.column("Item", width=200, anchor="center")
        tree.column("Qty", width=50, anchor="center")
        tree.column("Price", width=100, anchor="center")
        tree.column("Name", width=200, anchor="center")
        tree.column("Total", width=100, anchor="center")
        

        for sale in all_sales:
            tree.insert("", "end", values=sale)
        
        tree.pack(fill="both", expand=True)

        sales_window.geometry("1200x1200")
        
    else:
        messagebox.showinfo("No sales", "No sales found in the database")



items_label = tk.Label(app, text="Item")
items_entry = tk.Entry(app)

@handle_error
def sales_for():
    thing = items_entry.get()
    sales4 = store_items.show_sales4(thing)
    if sales4:
        sales4_window = tk.Toplevel(app)
        sales4_window.title("Sales")

        tree = ttk.Treeview(sales4_window)
        tree["columns"] = ("Sales ID", "Item", "Qty", "Price", "Name", "Total")

        tree.heading("#0", text="", anchor="w")
        tree.heading("#1", text="Sales ID", anchor="center")
        tree.heading("#2", text="Item", anchor="center")
        tree.heading("#3", text="Quant", anchor="center")
        tree.heading("#4", text="Price", anchor="center")
        tree.heading("#5", text="Name", anchor="center")
        tree.heading("#6", text="Total", anchor="center")

        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("Sales ID", width=100, anchor="center")
        tree.column("Item", width=200, anchor="center")
        tree.column("Qty", width=50, anchor="center")
        tree.column("Price", width=100, anchor="center")
        tree.column("Name", width=200, anchor="center")
        tree.column("Total", width=100, anchor="center")
        

        for sale in sales4:
            tree.insert("", "end", values=sale)
        
        tree.pack(fill="both", expand=True)

        sales_window.geometry("1200x1200")
        
    else:
        messagebox.showinfo("No sales", "No sales found in the database")

sales4_button = tk.Button(app, text="Show Item Sales", command=sales_for)

def show_sales_detail():
    items_label.pack()
    items_entry.pack()
    sales4_button.pack()

def hide_sales_detail():
    items_label.pack_forget()
    items_entry.pack_forget()
    
    sales4_button.pack_forget()
    

    
##purchases  
things_label = tk.Label(app, text="Item")
things_entry = tk.Entry(app)

qty_label = tk.Label(app, text="Quant")
qty_entry = tk.Entry(app)

price_label = tk.Label(app, text="Price")
price_entry = tk.Entry(app)


@handle_error
def add_purchase():
    item = things_entry.get()
    qty = qty_entry.get()
    price = price_entry.get()

    store_items.insert_purchase(item, qty, price)

add_prch_button = tk.Button(app, text="Insert Purchase", command=add_purchase)


def purch_show():
    things_label.pack()
    things_entry.pack()

    qty_label.pack()
    qty_entry.pack()

    price_label.pack()
    price_entry.pack()

    add_prch_button.pack()
    
@handle_error    
def purch_hide():
    things_label.pack_forget()
    things_entry.pack_forget()

    qty_label.pack_forget()
    qty_entry.pack_forget()

    price_label.pack_forget()
    price_entry.pack_forget()
    
    add_prch_button.pack_forget()
    
@handle_error
def show_purchase():
    purchd = store_items.show_purch()
    if purchd:
        purchase_window = tk.Toplevel(app)
        purchase_window.title("Purchases")

        tree = ttk.Treeview(purchase_window)
        tree ["columns"] = ("Purch ID", "Item", "Qty", "Price", "Total")

        tree.heading("#0", text="", anchor="w")
        tree.heading("#1", text="Purch ID", anchor="center")
        tree.heading("#2", text="Item", anchor="center")
        tree.heading("#3", text="Quant", anchor="center")
        tree.heading("#4", text="Price", anchor="center")
        tree.heading("#5", text="Total", anchor="center")

        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("Purch ID", width=100, anchor="center")
        tree.column("Item ID", width=100, anchor="center")
        tree.column("qty", width=50, anchor="center")
        tree.column("Price", width=100, anchor="center")
        tree.column("Total", width=100, anchor="center")

        for item in purchd:
            tree.insert("", "end", values=item)
        
        tree.pack(fill="both", expand=True)

        purchase_window.geometry("1200x1200")
        
    else:
        messagebox.showinfo("No Purchases", "No Purchases found in the database")



item_label = tk.Label(app, text="Item")
item_entry = tk.Entry(app)

@handle_error
def purchase_for():
    item = item_entry.get()
    purch4 = store_items.show_purch4(item)

    if purch4:
        purch4_window = tk.Toplevel(app)
        purch4e_window.title("Purchases")

        tree = ttk.Treeview(purch4_window)
        tree ["columns"] = ("Purch ID", "Item", "Qty", "Price", "Total")

        tree.heading("#0", text="", anchor="w")
        tree.heading("#1", text="Purch ID", anchor="center")
        tree.heading("#2", text="Item", anchor="center")
        tree.heading("#3", text="Quant", anchor="center")
        tree.heading("#4", text="Price", anchor="center")
        tree.heading("#5", text="Total", anchor="center")

        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("Purch ID", width=100, anchor="center")
        tree.column("Item ID", width=100, anchor="center")
        tree.column("qty", width=50, anchor="center")
        tree.column("Price", width=100, anchor="center")
        tree.column("Total", width=100, anchor="center")

        for things in purch4:
            tree.insert("", "end", values=things)
        
        tree.pack(fill="both", expand=True)

        purch4_window.geometry("1200x1200")
        
    else:
        messagebox.showinfo("No Purchases", "No Purchases found in the database")


        
##prch for button
purch4_button = tk.Button(app, text="Show Purch for Item", command=purchase_for)

def show_purch_details():
    item_label.pack()
    item_entry.pack()
    purch4_button.pack()
    
def hide_purch_details():
    item_label.pack_forget()
    item_entry.pack_forget()
    purch4_button.pack_forget()
    


##discounts

@handle_error    
def show_discounts():
    disco = store_items.show_disc()
    if disco:
        disc_window = tk.Toplevel(app)
        disc_window.title("Discounts")

        tree = ttk.Treeview(disc_window)
        tree ["columns"] = ("Disc ID", "Name", "Disc Amnt")

        tree.heading("#0", text="", anchor="w")
        tree.heading("#1", text="Disc ID", anchor="center")
        tree.heading("#2", text="Name", anchor="center")
        tree.heading("#3", text="Disc Amount", anchor="center")

        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("Disc ID", width=50, anchor="center")
        tree.column("Name", width=200, anchor="center")
        tree.column("Disc Amnt", width=100, anchor="center")

        for thing in disco:
            tree.insert("", "end", values=thing)
        
        tree.pack(fill="both", expand=True)

        disc_window.geometry("1200x1200")
        
    else:
        messagebox.showinfo("No Discounts", "No Discounts found in the database")

        
        


    
        

# Create menus
menu_bar = tk.Menu(app)
app.config(menu=menu_bar)


# Member Details Menu
member_details_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Member Details", menu=member_details_menu)
member_details_menu.add_command(label="Show Member Details", command=show_member_details)
member_details_menu.add_command(label="Hide Member Details", command=hide_member_details)
member_details_menu.add_separator()
member_details_menu.add_command(label="Show All Members", command=all_members)
member_details_menu.add_separator()
member_details_menu.add_command(label="Show Member Enroll details", command=show_mem_id)
member_details_menu.add_command(label="Hide Member Enroll details", command=hide_mem_id)
member_details_menu.add_separator()
member_details_menu.add_command(label="Show Enrollments", command=all_enroll)
member_details_menu.add_separator()
member_details_menu.add_command(label="Show Total Enroll Fees", command=total_enroll)
member_details_menu.add_separator()
member_details_menu.add_command(label="Show Facilitation Details", command=show_memb_game_id)
member_details_menu.add_command(label="Hide Facilitation Details", command=hide_memb_game_id)
member_details_menu.add_separator()
member_details_menu.add_command(label="Show Facilitation Fees", command=show_facs)
member_details_menu.add_separator()
member_details_menu.add_command(label="Show Total Facilitation Fees", command=total_facs)
member_details_menu.add_command(label="Show Patron Commission", command=patr_comm)

# Patrons Menu
patrons_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Patrons", menu=patrons_menu)
patrons_menu.add_command(label="Show patron Details", command=show_pat_details)
patrons_menu.add_command(label="Hide Patron Details", command=hide_pat_details)
patrons_menu.add_separator()




##games menu
games_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Games', menu=games_menu)
games_menu.add_command(label='Show Update Game Details', command=show_details)
games_menu.add_command(label='Hide Update Details', command=hide_details)
games_menu.add_separator()
games_menu.add_command(label="Add Games", command=avail_game)
games_menu.add_command(label='Show All games', command=all_games)
games_menu.add_separator()
games_menu.add_command(label='Show Loss Details', command=show_loss_details)
games_menu.add_command(label='Hide Loss Details', command=hide_loss_details)
games_menu.add_separator()
games_menu.add_command(label='Show All Losses', command=all_loss_damage)

##store menu
store_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Store Items", menu=store_menu)
store_menu.add_command(label="Add Store Items", command=add_store)
store_menu.add_command(label="Store Items", command=store_stuffs)
store_menu.add_separator()
store_menu.add_command(label="Sales Entries", command=sales_details)
store_menu.add_command(label="Hide Sales Entries", command=sales_hide)
store_menu.add_separator()
store_menu.add_command(label="All Sales", command=all_sales)
store_menu.add_separator()
store_menu.add_command(label="Show Sales 4 Item", command=show_sales_detail)
store_menu.add_command(label="Hide Sales 4 Item", command=hide_sales_detail)
store_menu.add_separator()
store_menu.add_command(label="Show Discounts", command=show_discounts)
store_menu.add_command(label="Show Purchases Details", command=purch_show)
store_menu.add_command(label="Hide Purchases Details", command=purch_hide)
store_menu.add_command(label="Show All Purchases", command=show_purchase)

##update age groups
membersdb.update_age_group()




# Function to handle closing the application
def close_app():
    # Close the connection and destroy the window
    conn.commit()
    cur.close()
    conn.close()
    app.destroy()  


# Close Menu
close_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Close", menu=close_menu)
close_menu.add_command(label="Close App", command=close_app)




# Start the main event loop
app.mainloop()
