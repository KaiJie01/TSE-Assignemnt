import tkinter as tk
from tkinter import Tk, Entry, Text, Button, ttk
import customtkinter
import config
import os
from CTkTable import *
from PIL import Image
sql_conn = config.config_sql()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("1024x720")
root.title("Dental Appointment Booking System")
root.iconbitmap('toothdoctor_diente_10727.ico')

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "")
leftbtn_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "left.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "left.png")), size=(20, 20))
rightbtn_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "right.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "right.png")), size=(20, 20))

def clearFrame():
    # destroy all widgets from frame
    for widget in tabviewframe.winfo_children():
        widget.destroy()

    # this will clear frame and frame will be empty
    # if you want to hide the empty panel then
    tabviewframe.pack_forget()

def dentistrecord():
    clearFrame()
    select_all_dentists = "select * from dentists"
    dentistrecords = sql_conn._selectall(select_all_dentists)
    headers = ["DentistID", "FirstName", "LastName", "Specialty", "PhoneNumber", "Email", "OfficeAddress", "City",
               "State", "ZipCode"]
    table = ttk.Treeview(tabviewframe, columns=headers, show="headings", height=200)
    for column in headers:
        table.heading(column=column, text=column)
        table.column(column=column, width=200)
    for row_data in dentistrecords:
        table.insert(parent="", index="end", values=row_data)
    table.grid(padx=10, pady=5)
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview", background="gray", fieldbackground="gray", foreground="white")

def patientsrecord():
    clearFrame()
    select_all_patients = "select * from patients"
    patientrecords = sql_conn._selectall(select_all_patients)
    headers = ["PatientID", "FirstName", "LastName", "DateOfBirth", "Gender", "PhoneNumber", "Email", "Address",
                   "City", "State", "ZipCode"]
    table = ttk.Treeview(tabviewframe, columns=headers, show="headings", height=200)
    for column in headers:
        table.heading(column=column, text=column)
        table.column(column=column, width=200)
    for row_data in patientrecords:
        table.insert(parent="", index="end", values=row_data)
    table.grid(padx=10, pady=5)
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview", background="gray", fieldbackground="gray", foreground="white")

    #tableview = CTkTable(tabviewframe, row=1, column=10, values=dentistrecords, wraplength=100)
    #tableview.pack(expand=True, fill="both", padx=0, pady=0)

# set grid layout 1x2
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

navigationframe = customtkinter.CTkFrame(master=root, corner_radius=0)
navigationframe.grid(row=0, column=0, sticky="nsew")
navigationframe.grid_rowconfigure(8, weight=1)

navigation_frame_label = customtkinter.CTkLabel(navigationframe, text="Admin Page", font=("Roboto", 24), compound="left")
navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)
navigationframe.grid(row=0, column=0, padx=20, pady=20)

homebutton =  customtkinter.CTkButton(navigationframe, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    anchor="w")
homebutton.grid(row=1, column=0, sticky="ew")

appointmentbutton =  customtkinter.CTkButton(navigationframe, corner_radius=0, height=40, border_spacing=10, text="Patient Appointment",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    anchor="w")
appointmentbutton.grid(row=2, column=0, sticky="ew")

billingbutton =  customtkinter.CTkButton(navigationframe, corner_radius=0, height=40, border_spacing=10, text="Patient Billing",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    anchor="w")
billingbutton.grid(row=3, column=0, sticky="ew")

dentistbutton =  customtkinter.CTkButton(navigationframe, corner_radius=0, height=40, border_spacing=10, text="Dentist List",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    anchor="w", command=dentistrecord)
dentistbutton.grid(row=4, column=0, sticky="ew")

patientbutton =  customtkinter.CTkButton(navigationframe, corner_radius=0, height=40, border_spacing=10, text="Patient List",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    anchor="w", command=patientsrecord)
patientbutton.grid(row=5, column=0, sticky="ew")

treatmentbutton =  customtkinter.CTkButton(navigationframe, corner_radius=0, height=40, border_spacing=10, text="Treatment List",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    anchor="w")
treatmentbutton.grid(row=6, column=0, sticky="ew")

tabviewouterframe=customtkinter.CTkFrame(master=root)
tabviewouterframe.grid(row=0, column=1, padx=(0, 0), pady=(20, 0), sticky="nsew")
tabviewouterframe.grid_columnconfigure(0, weight=1)

tabviewframe = customtkinter.CTkScrollableFrame(master=tabviewouterframe, orientation="horizontal")
tabviewframe.grid(row=1, column=0, padx=(0, 0), pady=(20, 0), sticky="nsew", ipady=200)
tabviewframe.grid_columnconfigure(0, weight=1)

searchframe = customtkinter.CTkFrame(master=tabviewouterframe)
searchframe.grid(row=0, column=0, padx=(0, 0), pady=(20, 0), sticky="nsew")
searchframe.grid_columnconfigure(2, weight=1)

searchlabel = customtkinter.CTkLabel(searchframe, text="Search: ", font=("Arial", 12, "bold"))
searchlabel.grid(row=0, column=0, padx=(10, 5), pady=10, sticky=customtkinter.W)

searchbar = customtkinter.CTkEntry(searchframe, width=200)
searchbar.grid(row=0, column=1, padx=(0, 5), pady=10, sticky=customtkinter.NW)

leftbtn = customtkinter.CTkButton(master=searchframe, corner_radius=0, height=40, border_spacing=10, text="",
                                  fg_color="transparent", text_color=("gray10", "gray90"),
                                  hover_color=("gray70", "gray30"),
                                  image=leftbtn_image, anchor="w", width=10)
leftbtn.grid(row=0, column=3, padx=(0, 0), pady=(0, 0), sticky="ne")

rightbtn = customtkinter.CTkButton(master=searchframe, corner_radius=0, height=40, border_spacing=10, text="",
                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                   hover_color=("gray70", "gray30"),
                                   image=rightbtn_image, anchor="w", width=10)
rightbtn.grid(row=0, column=4, padx=(0, 0), pady=(0, 0), sticky="ne")

root.mainloop()