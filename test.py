from pdf_generate import fill_invoice_template

# Test data
data = {
    "invoice_nr": "INV-12345",
    "date": "2025-01-09",
    "seller_name": "ABC Corporation",
    "to_name": "John Doe",
    "to_company": "Doe Enterprises",
    "to_address": "123 Elm Street, Anytown, USA",
    "postal_code": "87650",
    "to_phone": "555-1234",
    "ship_name": "Jane Smith",
    "ship_company": "Smith Ventures",
    "ship_address": "456 Oak Avenue, Somecity, USA",
    "ship_postal_code": "8755432",
    "ship_phone": "555-5678",
    "comments": "Deliver by end of the week.",
    "items": [
        {"quantity": 2, "description": "Widget A", "unit_price": 5987650.00, "total": 100.00},
        {"quantity": 1, "description": "Gadget B", "unit_price": 75.00, "total": 75.00},
    ],
    "subtotal": 175.00,
    "sales_tax": 15.00,
    "shipping_handling": 10.00,
    "total_due": 200.00,
}

# Paths
template_path = r"C:\Users\sunit\Downloads\INVOICE.pdf"  # Path to your template PDF
output_path = "filled_invoice_test.pdf"  # Output file

# Fill the template
fill_invoice_template(template_path, output_path, data)

print(f"Invoice generated: {output_path}")