import frappe

@frappe.whitelist(allow_guest=True)
def get_property_type():
    proprty_loactions=frappe.get_all("Property Located Type",
    filters={"is_active":1},
    fields=["images",
    "location_type"])

    return proprty_loactions 