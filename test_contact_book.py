from contact_book import setup_main, add_contact, search_contacts, create_csv_file
import csv
import datetime
import os
import pytest
from unittest.mock import MagicMock 
from tkinter import Tk, Label, Entry, Button


def test_setup_main_creates_widgets():
    root = Tk()
    frm = root
    setup_main(frm)

    # Check if widgets are created
    assert isinstance(frm.children['!label'], Label)
    assert isinstance(frm.children['!entry'], Entry)
    assert isinstance(frm.children['!button'], Button)

    # Check if labels have correct text
    assert frm.children['!label'].cget("text") == "Create New Contact"
    assert frm.children['!label2'].cget("text") == "Firstname"
    assert frm.children['!label3'].cget("text") == "Surname"
    assert frm.children['!label4'].cget("text") == "Contact Number"
    assert frm.children['!label5'].cget("text") == "Email"
    assert frm.children['!label6'].cget("text") == "Address"
    assert frm.children['!label7'].cget("text") == "User Email Address"

    root.destroy()

def test_create_csv_file():
    file_path = "test_contacts.csv"
    firstname = "John"
    surname = "Doe"
    phone_number = "+441234567890"
    email = "omohsam81@gmail.com"
    address = "123 Main St"
    date_and_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user_email = "omohsam81@gmail.com"
    lbl_display = MagicMock()
    create_csv_file(file_path, firstname, surname, phone_number, email, address, date_and_time, user_email, lbl_display)
    assert os.path.exists(file_path)    
    with open(file_path, newline='') as f:
        reader = list(csv.reader(f))
        assert reader[0] == ["Firstname", "Surname", "Phone Number", "Email", "Address", "Date and Time"]
        assert reader[1][0] == firstname
        assert reader[1][1] == surname
        assert reader[1][2] == phone_number
        assert reader[1][3] == email
        assert reader[1][4] == address
        
def test_add_contact():
    file_path = "test_contacts.csv"
    firstname = "John"
    surname = "Doe"
    phone_number = "+441234567890"
    email = "omohsam81@gmail.com"
    address = "123 Main St"
    date_and_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user_email = "omohsam81@gmail.com"
    lbl_display = MagicMock()
    # Create the file first
    create_csv_file(file_path, firstname, surname, phone_number, email, address, date_and_time, user_email, lbl_display)

def test_search_contacts():
    file_path = "test_contacts.csv"
    firstname = "John"
    surname = "Doe"
    phone_number = "+441234567890"
    email = "omohsam81@gmail.com"
    address = "123 Main St"
    date_and_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user_email = "omohsam81@gmail.com"
    lbl_display = MagicMock()
    # Create the file first
    create_csv_file(file_path, firstname, surname, phone_number, email, address, date_and_time, user_email, lbl_display)    
    
    pytest.main(["-v", "--tb=line", "-rN", __file__])