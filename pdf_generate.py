import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO

# Function to fill the invoice template with better alignment and fonts
def fill_invoice_template(template_path, output_path, data):
    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)

    # Set font style and size
    can.setFont("Helvetica-Bold", 9.5)

    # Invoice details
    can.drawRightString(170, 666, data['invoice_nr'])  
    can.drawRightString(170, 654, data['date'])       

    # Company information
    can.setFont("Helvetica", 11)
    can.drawString(190, 629, data['seller_name'])     

    # biliing address
    can.setFont("Helvetica", 9)
    can.drawString(170, 540, data['to_name'])          
    can.drawString(170, 529, data['to_company'])        
    can.drawString(170, 518, data['to_address'])       
    can.drawString(170, 507, data['postal_code'])        
    can.drawString(170, 496, data['to_phone'])         

    # shipping address
    can.drawString(420, 540, data['ship_name'])        
    can.drawString(420, 529,data['ship_company'])     
    can.drawString(420, 518, data['ship_address']) 
    can.drawString(420, 507, data['ship_postal_code'])        
    can.drawString(420, 496, data['ship_phone'])      

    # Comments or special instructions
    can.setFont("Helvetica-Oblique", 9)
    can.drawString(80, 450, data['comments'])

    # Table items
    y_position = 355  # Starting Y position for items
    can.setFont("Helvetica", 9.5)
    for item in data['items']:
        can.drawString(100, y_position, str(item['quantity']))     
        can.drawString(180, y_position, item['description'])      
        can.drawRightString(500, y_position, f"${item['unit_price']:.2f}") 
        can.drawRightString(550, y_position, f"${item['total']:.2f}")    
        y_position -= 20  # Move to the next line

    # Summary
    can.drawRightString(550, 210, f"${data['subtotal']:.2f}")             
    can.drawRightString(550, 190, f"${data['sales_tax']:.2f}")             
    can.drawRightString(550, 171, f"${data['shipping_handling']:.2f}")     
    can.drawRightString(550, 152, f"${data['total_due']:.2f}")              

    can.save()
    packet.seek(0)

    # Merge the overlay with the template
    template_reader = PdfReader(template_path)
    template_page = template_reader.pages[0]
    overlay_pdf = PdfReader(packet)
    overlay_page = overlay_pdf.pages[0]

    writer = PdfWriter()
    template_page.merge_page(overlay_page)
    writer.add_page(template_page)

    with open(output_path, "wb") as output_file:
        writer.write(output_file)