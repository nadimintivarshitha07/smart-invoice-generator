from tkinter import *
from tkinter import messagebox
from reportlab.pdfgen import canvas
from datetime import datetime
import os

def generate_invoice():
    try:
        customer = customer_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()

        product = product_entry.get()
        quantity = int(quantity_entry.get())
        price = float(price_entry.get())

        total = quantity * price
        gst = total * 0.18
        grand_total = total + gst

        if not os.path.exists("invoices"):
            os.makedirs("invoices")

        invoice_id = datetime.now().strftime("%Y%m%d%H%M%S")
        pdf_path = f"invoices/Invoice_{invoice_id}.pdf"

        c = canvas.Canvas(pdf_path)

        # Logo
        c.drawImage("logo.png.jpeg", 30, 755, width=55, height=55)

        # Company Header
        c.setFont("Helvetica-Bold", 18)
        c.drawString(100, 790, "VN Invoices")

        c.setFont("Helvetica", 12)
        c.drawString(100, 770, "Smart Invoice Generator")

        # Invoice Title
        c.setFont("Helvetica-Bold", 22)
        c.drawString(230, 720, "INVOICE")

        # Invoice Information
        c.setFont("Helvetica", 12)
        c.drawString(50, 680, f"Invoice ID: {invoice_id}")
        c.drawString(400, 680, f"Date: {datetime.now().date()}")

        # Customer Details
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, 640, "Bill To")

        c.setFont("Helvetica", 12)
        c.drawString(50, 620, f"Name: {customer}")
        c.drawString(50, 600, f"Phone: {phone}")
        c.drawString(50, 580, f"Email: {email}")
        c.drawString(50, 560, f"Address: {address}")

        # Product Table
        c.line(50, 520, 550, 520)

        c.setFont("Helvetica-Bold", 12)
        c.drawString(60, 500, "Product")
        c.drawString(250, 500, "Qty")
        c.drawString(330, 500, "Price")
        c.drawString(450, 500, "Total")

        c.line(50, 490, 550, 490)

        c.setFont("Helvetica", 12)
        c.drawString(60, 470, product)
        c.drawString(250, 470, str(quantity))
        c.drawString(330, 470, f"Rs.{price}")
        c.drawString(450, 470, f"Rs.{total}")

        c.line(50, 450, 550, 450)

        # Totals
        c.drawString(350, 400, f"Subtotal: Rs.{total:.2f}")
        c.drawString(350, 380, f"GST (18%): Rs.{gst:.2f}")

        c.setFont("Helvetica-Bold", 14)
        c.drawString(350, 350, f"Grand Total: Rs.{grand_total:.2f}")

        # Footer
        c.setFont("Helvetica", 11)
        c.drawString(50, 250, "Thank you for your business!")

        c.line(380, 180, 520, 180)
        c.drawString(390, 160, "Authorized Signature")

        c.save()

        messagebox.showinfo(
            "Success",
            f"Invoice saved successfully!\n{pdf_path}"
        )

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter valid Quantity and Price."
        )


# GUI
root = Tk()
root.title("VN Invoices")
root.geometry("600x700")
root.configure(bg="#E6F3FF")

title = Label(
    root,
    text="VN Invoices",
    font=("Arial", 20, "bold"),
    bg="#E6F3FF"
)
title.pack(pady=10)

subtitle = Label(
    root,
    text="Smart Invoice Generator",
    font=("Arial", 12),
    bg="#E6F3FF"
)
subtitle.pack()

Label(root, text="Customer Name", bg="#E6F3FF").pack(pady=5)
customer_entry = Entry(root, width=40)
customer_entry.pack()

Label(root, text="Phone Number", bg="#E6F3FF").pack(pady=5)
phone_entry = Entry(root, width=40)
phone_entry.pack()

Label(root, text="Email", bg="#E6F3FF").pack(pady=5)
email_entry = Entry(root, width=40)
email_entry.pack()

Label(root, text="Address", bg="#E6F3FF").pack(pady=5)
address_entry = Entry(root, width=40)
address_entry.pack()

Label(root, text="Product Name", bg="#E6F3FF").pack(pady=5)
product_entry = Entry(root, width=40)
product_entry.pack()

Label(root, text="Quantity", bg="#E6F3FF").pack(pady=5)
quantity_entry = Entry(root, width=40)
quantity_entry.pack()

Label(root, text="Price", bg="#E6F3FF").pack(pady=5)
price_entry = Entry(root, width=40)
price_entry.pack()

Button(
    root,
    text="Generate Invoice",
    command=generate_invoice,
    font=("Arial", 12, "bold")
).pack(pady=20)

root.mainloop()