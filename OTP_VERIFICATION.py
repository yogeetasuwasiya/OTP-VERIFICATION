from tkinter import *
import random

class OTPVerificationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OTP Verification")
        self.root.geometry("300x200")
        
        self.generate_otp()
        
        self.label = Label(root, text="Enter OTP:")
        self.label.pack()
        
        self.otp_entry = Entry(root)
        self.otp_entry.pack()
        
        self.verify_button = Button(root, text="Verify", command=self.verify_otp)
        self.verify_button.pack()
        
    def generate_otp(self):
        self.otp = random.randint(1000, 9999)
        print("Generated OTP:", self.otp)
        
    def verify_otp(self):
        user_otp = int(self.otp_entry.get())
        if user_otp == self.otp:
            print("OTP Verified!")
        else:
            print("Incorrect OTP!")
        
root = Tk()
otp_app = OTPVerificationApp(root)
root.mainloop()
