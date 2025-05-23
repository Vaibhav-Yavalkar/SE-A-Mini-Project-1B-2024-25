# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label, Frame
import mysql.connector
import HomePage

# from tkinter import *
# Explicit imports to satisfy Flake8


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\ASUS\Downloads\patient profile page\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class PatientDashboard(Tk):
    def __init__(self, email=None):
        super().__init__()
        self.email = email
        self.patient_data = None
        
        self.geometry("1280x720")
        self.configure(bg="#FFFFFF")
        self.title("Patient Dashboard")
        
        # If email is provided, fetch patient data from database
        if email:
            self.fetch_patient_data()
        
        # Setup the UI
        self.create_ui()
        self.resizable(False, False)
    
    def fetch_patient_data(self):
        """Fetch patient details from the database using email"""
        connection = None
        cursor = None
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Y@sh8105",
                database="Transplant"
            )
            cursor = connection.cursor(dictionary=True)
            
            # Query to get patient details
            cursor.execute("SELECT * FROM patients WHERE Email=%s", (self.email,))
            self.patient_data = cursor.fetchone()
            
            # Consume any remaining results to avoid "Unread result found" error
            while cursor.nextset():
                pass
                
        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
            self.patient_data = None
        finally:
            # Always properly close cursor and connection
            if cursor:
                cursor.close()
            if connection and connection.is_connected():
                connection.close()
    
    def create_ui(self):
        # Define output path and assets path
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\ASUS\Downloads\patient profile page\build\assets\frame0")
        
        def relative_to_assets(path):
            return ASSETS_PATH / Path(path)
        
        # Create Canvas
        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=720,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        
        # Background Image
        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            640.0, 360.0, image=self.image_image_1
        )
        
        # Separator Rectangle
        self.canvas.create_rectangle(
            -5.0, 92.0, 1280.0, 97.0, fill="#000000", outline=""
        )
        
        # Header Image
        self.image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            640.0, 51.0, image=self.image_image_2
        )
        
        # Profile Box Images
        self.image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            367.0, 415.0, image=self.image_image_3
        )
        
        self.image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            367.0, 415.0, image=self.image_image_4
        )
        
        self.image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
        self.image_5 = self.canvas.create_image(
            367.0, 312.0, image=self.image_image_5
        )
        
        # Text Labels for Personal Information
        self.canvas.create_text(
            161.0, 196.7, anchor="nw", text="Name :",
            fill="#000000", font=("Inter", 20 * -1)
        )
        
        self.canvas.create_text(
            161.0, 237.4, anchor="nw", text="Email :",
            fill="#000000", font=("Inter", 20 * -1)
        )
        
        self.canvas.create_text(
            161.0, 278.1, anchor="nw", text="Age :",
            fill="#000000", font=("Inter", 20 * -1)
        )
        
        self.canvas.create_text(
            161.0, 318.8, anchor="nw", text="Aadhaar no. :",
            fill="#000000", font=("Inter", 20 * -1)
        )
        
        self.canvas.create_text(
            161.0, 356.4, anchor="nw", text="Medical History :",
            fill="#000000", font=("Inter", 20 * -1)
        )
        
        self.canvas.create_text(
            161.0, 397.1, anchor="nw", text="Address :",
            fill="#000000", font=("Inter", 20 * -1)
        )
        
        # Additional Image
        self.image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
        self.image_6 = self.canvas.create_image(
            367.0, 534.0, image=self.image_image_6
        )
        
        # Text Labels for Additional Information
        self.canvas.create_text(
            161.0, 482.8, anchor="nw", text="Gender :",
            fill="#000000", font=("Inter", 20 * -1)
        )
        
        self.canvas.create_text(
            161.0, 520.4, anchor="nw", text="Blood Group :",
            fill="#000000", font=("Inter", 20 * -1)
        )
        
        self.canvas.create_text(
            159.0, 558.0, anchor="nw", text="Organ Needed :",
            fill="#000000", font=("Inter", 20 * -1)
        )
        
        # Status area Image
        self.image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
        self.image_7 = self.canvas.create_image(
            975.0, 436.0, image=self.image_image_7
        )
        
        # Create a white rectangle to cover the image background
        self.canvas.create_rectangle(
            675, 336, 1275, 536,  # Adjust coordinates to cover the status area
            fill="white", outline=""
        )
        
        # Personal Information Image
        self.image_image_8 = PhotoImage(file=relative_to_assets("image_8.png"))
        self.image_8 = self.canvas.create_image(
            362.0, 164.0, image=self.image_image_8
        )
        
        # Matching Status Image
        self.image_image_9 = PhotoImage(file=relative_to_assets("image_9.png"))
        self.image_9 = self.canvas.create_image(
            974.0, 354.0, image=self.image_image_9
        )
        
        # Add a back to home button
        self.back_button = Button(
            self,
            text="Back To Home",
            bg="#E9967A",
            fg="white",
            font=("Arial", 12, "bold"),
            borderwidth=0,
            highlightthickness=0,
            command=self.go_to_home_page,
            relief="flat"
        )
        self.back_button.place(x=1100, y=30, width=150, height=30)
        
        # Display patient data if available
        if self.patient_data:
            self.display_patient_data()
    
    def display_patient_data(self):
        """Display patient data on the dashboard next to labels"""
        if not self.patient_data:
            return
        
        # X position for data values
        data_x = 320
        
        # Name
        name_label = Label(
            self,
            text=self.patient_data.get('PatientName', 'N/A'),
            font=("Inter", 16),
            bg="white",
            anchor="w"
        )
        name_label.place(x=data_x, y=196)
        
        # Email
        email_label = Label(
            self,
            text=self.patient_data.get('Email', 'N/A'),
            font=("Inter", 16),
            bg="white",
            anchor="w"
        )
        email_label.place(x=data_x, y=237)
        
        # Age
        age_label = Label(
            self,
            text=str(self.patient_data.get('PatientAge', 'N/A')),
            font=("Inter", 16),
            bg="white",
            anchor="w"
        )
        age_label.place(x=data_x, y=278)
        
        # Aadhaar
        aadhaar_label = Label(
            self,
            text=self.patient_data.get('Aadhaar', 'N/A'),
            font=("Inter", 16),
            bg="white",
            anchor="w"
        )
        aadhaar_label.place(x=data_x, y=318)
        
        # Medical History
        medical_history_label = Label(
            self,
            text=self.patient_data.get('MedicalHistory', 'N/A'),
            font=("Inter", 16),
            bg="white",
            anchor="w",
            wraplength=400
        )
        medical_history_label.place(x=data_x, y=356)
        
        # Address
        address_label = Label(
            self,
            text=self.patient_data.get('PatientAddress', 'N/A'),
            font=("Inter", 16),
            bg="white",
            anchor="w",
            wraplength=400
        )
        address_label.place(x=data_x, y=397)
        
        # Gender
        gender_label = Label(
            self,
            text=self.patient_data.get('Gender', 'N/A'),
            font=("Inter", 16),
            bg="white",
            anchor="w"
        )
        gender_label.place(x=data_x, y=482)
        
        # Blood Group
        blood_group_label = Label(
            self,
            text=self.patient_data.get('PatientBloodGrp', 'N/A'),
            font=("Inter", 16),
            bg="white",
            anchor="w"
        )
        blood_group_label.place(x=data_x, y=520)
        
        # Organ Needed
        organ_label = Label(
            self,
            text=self.patient_data.get('NeededOrgan', 'N/A'),
            font=("Inter", 16),
            bg="white",
            anchor="w"
        )
        organ_label.place(x=data_x, y=558)
        
        # Check if there's a matched donor
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Y@sh8105",
                database="Transplant"
            )
            cursor = connection.cursor(dictionary=True)
            
            # Query to find matched donor
            cursor.execute("""
                SELECT donor_name FROM matches 
                WHERE recipient_name = %s
            """, (self.patient_data.get('PatientName', ''),))
            
            match_data = cursor.fetchone()
            
            # Consume any remaining results
            while cursor.nextset():
                pass
                
            if cursor:
                cursor.close()
            if connection and connection.is_connected():
                connection.close()
            
            # Display matched donor info if found
            if match_data and match_data.get('donor_name'):
                match_label = Label(
                    self,
                    text=f"You have been matched with: {match_data['donor_name']}",
                    font=("Inter", 18, "bold"),
                    bg="#F9F9FF",
                    fg="#333333"
                )
                match_label.place(x=975, y=435, anchor="center")
            else:
                # Display urgency level if no match
                urgency_label = Label(
                    self,
                    text=f"Urgency Level: {self.patient_data.get('Urgency', 'N/A')}",
                    font=("Inter", 18, "bold"),
                    bg="#F9F9FF",
                    fg="#333333"
                )
                urgency_label.place(x=975, y=435, anchor="center")
            
        except mysql.connector.Error as e:
            print(f"Error fetching match data: {e}")
            # Display urgency level if error
            urgency_label = Label(
                self,
                text=f"Urgency Level: {self.patient_data.get('Urgency', 'N/A')}",
                font=("Inter", 18, "bold"),
                bg="#F9F9FF",
                fg="#333333"
            )
            urgency_label.place(x=975, y=435, anchor="center")
    
    def go_to_home_page(self):
        """Navigate back to the home page"""
        self.destroy()
        HomePage.HomePage()

if __name__ == "__main__":
    app = PatientDashboard()
    app.mainloop()
