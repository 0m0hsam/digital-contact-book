import tkinter as tk
from tkinter import Frame, Label, Button
import csv, os, datetime
from tkinter import messagebox


def main():
    root = tk.Tk()
    root.option_add("*Font",  "Helvatica 14")
    frm_main = Frame(root)
    frm_main.master.title("Digital Contact Book")
    frm_main.pack(padx=4, pady=4, fill=tk.BOTH, expand=True)
    setup_main(frm_main)
    
    frm_main.mainloop()

def setup_main(frm):
    lbl_head =Label(frm,text="Create New Contact", font=("Helvetica", 20, "bold"), fg="blue")
    lbl_head.grid(row=0,ipadx=0,column=0,padx=3,pady=3,)
    lbl_firstname =Label(frm,text="Firstname", font=("Helvetica", 10, "bold", "italic"))
    lbl_firstname.grid(row=1,ipadx=0,column=0,padx=3,pady=3, sticky=tk.W)
    ent_firstname =tk.Entry(frm, width=30, justify=tk.LEFT)
    ent_firstname.grid(row=2,column=0,padx=3,pady=3)
    lbl_Surname =Label(frm,text="Surname", font=("Helvetica", 10, "bold", "italic"))
    lbl_Surname.grid(row=3,column=0,padx=3,pady=3, sticky=tk.W)
    ent_surname =tk.Entry(frm, width=30, justify=tk.LEFT)
    ent_surname.grid(row=4,column=0,padx=3,pady=3)
    lbl_number=Label(frm,text="Contact Number", font=("Helvetica", 10, "bold", "italic"))
    lbl_number.grid(row=5,column=0,padx=3,pady=3, sticky=tk.W)
    ent_phone_number =tk.Entry(frm, width=30, justify=tk.LEFT)
    ent_phone_number.insert(0, "+44 1234 567890")  # Example default value
    ent_phone_number.grid(row=6,column=0,padx=3,pady=3)
    lbl_email =Label(frm,text="Email", font=("Helvetica", 10, "bold", "italic"))
    lbl_email.grid(row=7,column=0,padx=3,pady=3, sticky=tk.W)
    ent_email =tk.Entry(frm, width=30, justify=tk.LEFT)
    ent_email.grid(row=8,column=0,padx=3,pady=3)
    lbl_address =Label(frm,text="Address", font=("Helvetica", 10, "bold", "italic"))
    lbl_address.grid(row=9,column=0,padx=3,pady=3, sticky=tk.W)
    ent_address =tk.Entry(frm, width=30, justify=tk.LEFT)
    ent_address.grid(row=10,column=0,padx=3,pady=3)
    lbl_user_email =Label(frm,text="User Email Address", font=("Helvetica", 10, "bold", "italic"))
    lbl_user_email.grid(row=11,column=0,padx=3,pady=3, sticky=tk.W)
    user_email_entry =tk.Entry(frm, width=30, justify=tk.LEFT)
    user_email_entry.grid(row=12,column=0,padx=3,pady=3)
    btn_save = Button(frm, text="Save Contact", width=20, font=("Helvetica", 10, "bold"), bg="lightgreen", fg="black")
    btn_save.grid(row=13, column=0, padx=3, pady=3) 
    lbl_display = Label(frm, text="", font=("Helvetica", 10, "bold"), bg="black", relief=tk.SUNKEN)
    lbl_display.grid(row=4, column=2, padx=3, pady=6, sticky=tk.W+tk.E+tk.N+tk.S, rowspan=11, columnspan=4)
    
    #create a striaght vertical line to separate the left and right side of the contact book
    line = tk.Frame(frm, width=2, bg="blue")
    line.grid(row=0, column=1, rowspan=14, padx=40, pady=5, sticky=tk.N+tk.S)
    
    #search contacts
    lbl_search = Label(frm, text="Search Contacts number or email", font=("Helvetica", 10, "bold", "italic"))
    lbl_search.grid(row=1, column=2, padx=3, pady=3, sticky=tk.W)
    ent_search = tk.Entry(frm, width=25, justify=tk.LEFT)
    ent_search.grid(row=2, column=2,padx=3, pady=3)
    lbl_search_email = Label(frm, text="Enter your contact book email address", font=("Helvetica", 10, "bold", "italic"))
    lbl_search_email.grid(row=1, column=3, padx=3, pady=3, sticky=tk.W)
    ent_search_email = tk.Entry(frm, width=25, justify=tk.LEFT)
    ent_search_email.grid(row=2, column=3,padx=3, pady=3)
    btn_search = Button(frm, text="Search Contact", width=30, font=("Helvetica", 10, "bold"), bg="lightgreen", fg="black") 
    btn_search.grid(columnspan=6, row=3, column=2, padx=3, pady=3)
   
        
    def save_contact():
        firstname = ent_firstname.get()
        surname = ent_surname.get()
        phone_number = ent_phone_number.get()
        email = ent_email.get()
        email = email.replace(" ", "").lower()  # Normalize email
        phone_number = phone_number.replace(" ", "")  # Normalize phone number
        address = ent_address.get()
        user_email = user_email_entry.get()
        date_and_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if not user_email.endswith(".com") and not user_email.endswith(".com"):
            lbl_display.config(text="Please enter a valid email address.", fg="red")
            return
        
        if not (firstname and surname and phone_number and email and address and user_email):
            lbl_display.config(text="All fields must be filled out!", fg="red")
            return
        
        folder_path = "Contact_Folder"  # Replace with your desired folder name
        file_name = user_email + ".csv"  # Name of the CSV file
        file_path = os.path.join(folder_path,  file_name)
        if not os.path.exists(folder_path):
         os.makedirs(folder_path)
        # Check if the file already exists
        if not os.path.exists(file_path):
            create_csv_file(file_path, firstname, surname, phone_number, email, address, date_and_time, user_email)
        else:
            add_contact(file_path, firstname, surname, phone_number, email, address, date_and_time, user_email)
        
    # Here you would typically save the contact to a database or file
    btn_save.config(command=save_contact)
    
    # Search contacts function
    def search_contacts():
        search_term = ent_search.get()
        search_email = ent_search_email.get()
        search_term = search_term.replace(" ", "").lower()  # Normalize search term
        search_email = search_email.replace(" ", "").lower()
        
        folder_path = "Contact_Folder"  # Replace with your desired folder name
        file_name = search_email + ".csv"  # Name of the CSV file
        file_path = os.path.join(folder_path,  file_name)
        
        
        if not search_term and search_email:
            lbl_display.config(text="Please enter a search term.", fg="red")
            return
        if not search_email.endswith(".com"):
            lbl_display.config(text="Enter a vaild email or contact number", fg="red")
            return
       
        try:
            with open(file_path, mode='r') as contacts_file:
                reader = csv.reader(contacts_file, delimiter=',')
                contacts = list(reader)

                CONTACT_FIRSTNAME_INDEX = 0
                CONTACT_SURNAME_INDEX = 1
                CONTACT_PHONE_INDEX = 2
                CONTACT_EMAIL_INDEX = 3
                CONTACT_ADDRESS_INDEX = 4
                CONTACT_DATE_INDEX = 5
                for contact in contacts:
                    if contact[CONTACT_EMAIL_INDEX] == search_term or contact[CONTACT_PHONE_INDEX] == search_term:
                        lbl_display.config(text=f"Firstname: {contact[CONTACT_FIRSTNAME_INDEX]}\n"
                                                f"Surname: {contact[CONTACT_SURNAME_INDEX]}\n"
                                                f"Phone Number: {contact[CONTACT_PHONE_INDEX]}\n"
                                                f"Email: {contact[CONTACT_EMAIL_INDEX]}\n"
                                                f"Address: {contact[CONTACT_ADDRESS_INDEX]}\n"
                                                f"Date and Time: {contact[CONTACT_DATE_INDEX]}", 
                                                fg="white", justify=tk.LEFT, padx=5, pady=5)
                        return
                    else:
                        lbl_display.config(text="Contacts email or phone number not found!", fg="red")
                    
        except FileNotFoundError:
            lbl_display.config(text="Your user contact ebook not found!.", fg="red")
        
        
    #Search button action
    # btn_search.config(command=lambda: search_contacts(ent_search.get()))
    btn_search.config(command=search_contacts)
    
    #create a new csv file if it does not exist, otherwise add a new contact to the existing csv file with the user email address  
    def create_csv_file(file_name, firstname, surname, phone_number, email, address, date_and_time, user_email):
        with open(file_name, mode='w', newline='') as contacts_file:
            writer = csv.writer(contacts_file)
            writer.writerow(["Firstname", "Surname", "Phone Number", "Email", "Address", "Date and Time"])
            writer.writerow([firstname, surname, phone_number, email, address, date_and_time])
        lbl_display.config(text=f"Contact saved: {firstname} {surname} \nTo a new Contact Book with email: {user_email}", fg="green")
    
    def add_contact(file_name, firstname, surname, phone_number, email, address, date_and_time, user_email):
        with open(file_name, 'a', newline='') as contacts_file:
            writer = csv.writer(contacts_file)
            writer.writerow([firstname, surname, phone_number, email, address, date_and_time])
        lbl_display.config(text=f"Contact added: {firstname} {surname} \nTo an existing Contact Book with email: {user_email}", fg="blue")

    # def read_contacts():
    #     try:
    #         with open('contacts.csv', mode='r') as contacts_file:
    #             reader = csv.reader(contacts_file)
    #             contacts = list(reader)
    #             if len(contacts) > 1:
    #                 lbl_display.config(text="\n".join([f"{row[0]} {row[1]}" for row in contacts[1:]]), fg="black")
    #             else:
    #                 lbl_display.config(text="No contacts found.", fg="red")
    #     except FileNotFoundError:
    #         lbl_display.config(text="No contacts file found.", fg="red")
if __name__ == "__main__":
    main()