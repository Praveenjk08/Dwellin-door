import frappe

# @frappe.whitelist(allow_guest=True)
# def add_email(email):
#     email_1=frappe.get_doc({
#         "doctype":"NewsLetter",
#         "email":email})

#     email_1.insert(ignore_permissions=True)
#     frappe.db.commit()
#     return "Subscribed successfully"
@frappe.whitelist(allow_guest=True)
def add_email(email):

    if not email:
        return {
            "status": "error",
            "message": "Email is required."
        }

    # Check if already subscribed
    if frappe.db.exists("NewsLetter", {"email": email}):
        return {
            "status": "exists",
            "message": "This email is already subscribed."
        }

    doc = frappe.get_doc({
        "doctype": "NewsLetter",
        "email": email
    })

    doc.insert(ignore_permissions=True)
    frappe.db.commit()

    return {
        "status": "success",
        "message": "Thank you! You have successfully subscribed."
    }