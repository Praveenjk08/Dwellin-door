import frappe

@frappe.whitelist(allow_guest=True)
def lead_add_api():
    name = frappe.form_dict.get("name")
    phone = frappe.form_dict.get("phone")
    email = frappe.form_dict.get("email")
    service = frappe.form_dict.get("service")
    

    add_lead = frappe.get_doc({
        "doctype": "CRM Lead",
        "first_name": name,
        "mobile_no": phone,
        "email": email,
        "service": service,
        "source": "Website",
    })

    add_lead.insert(ignore_permissions=True)
    frappe.db.commit()

    return {"message": "Lead added successfully"}