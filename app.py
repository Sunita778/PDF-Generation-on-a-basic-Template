import streamlit as st
from pdf_generate import  fill_invoice_template

# Streamlit App
st.title("PDF GENERATION")

# Upload template PDF
template_pdf = st.file_uploader("Upload Invoice Template PDF", type="pdf")

# Input fields for invoice
st.header("Invoice Details")
invoice_nr = st.text_input("Invoice Number")
# date = st.text_input("Date (YYYY-MM-DD)")
date = st.date_input(label="Date")

st.header("Seller Information")
seller_name = st.text_input("Seller Name")

st.header("Billing Address")
to_name = st.text_input("Recipient Name")
to_company = st.text_input("Recipient Company")
to_address = st.text_area("Recipient Address")
postal_code = st.text_input("Postal Code")
to_phone = st.text_input("Phone Number")

st.header("Shipping Address")
ship_name = st.text_input("Shipping Recipient Name")
ship_company = st.text_input("Shipping Company")
ship_address = st.text_area("Shipping Address")
ship_postal_code = st.text_input("Shipping Postal Code")
ship_phone = st.text_input("Shipping Phone Number")

st.header("Comments")
comments = st.text_area("Comments or Special Instructions")

st.header("Item Details")
items = []
num_items = st.number_input("Number of Items", min_value=1, step=1)
for i in range(num_items):
    with st.expander(f"Item {i + 1}"):
        quantity = st.number_input(f"Quantity {i + 1}", min_value=1, step=1)
        description = st.text_input(f"Description {i + 1}")
        unit_price = st.number_input(f"Unit Price {i + 1}", min_value=0.0, step=0.01)
        total = quantity * unit_price
        items.append({"quantity": quantity, "description": description, "unit_price": unit_price, "total": total})

st.header("Summary")
subtotal = sum(item['total'] for item in items)
sales_tax = st.number_input("Sales Tax", min_value=0.0, step=0.01)
shipping_handling = st.number_input("Shipping & Handling", min_value=0.0, step=0.01)
total_due = subtotal + sales_tax + shipping_handling

if st.button("Generate Invoice"):
    if template_pdf:
        data = {
            "invoice_nr": invoice_nr,
            "date": date,
            "seller_name": seller_name,
            "to_name": to_name,
            "to_company": to_company,
            "to_address": to_address,
            "postal_code": postal_code,
            "to_phone": to_phone,
            "ship_name": ship_name,
            "ship_company": ship_company,
            "ship_address": ship_address,
            "ship_postal_code": ship_postal_code,
            "ship_phone": ship_phone,
            "comments": comments,
            "items": items,
            "subtotal": subtotal,
            "sales_tax": sales_tax,
            "shipping_handling": shipping_handling,
            "total_due": total_due,
        }

        # Save uploaded template temporarily
        template_path = "uploaded_template.pdf"
        with open(template_path, "wb") as f:
            f.write(template_pdf.read())

        # Output file path
        output_path = "filled_invoice.pdf"

        # Generate filled invoice
        fill_invoice_template(template_path, output_path, data)

        # Provide download link
        with open(output_path, "rb") as f:
            st.download_button("Download Invoice", f, file_name="filled_invoice.pdf")
    else:
        st.error("Please upload a template PDF.")
