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


# @frappe.whitelist(allow_guest=True)
# def video_meeting_shedule(name, phone, email, visist_type, visiting_time, project_name):
#     add_lead = frappe.get_doc({
#         "doctype": "CRM Lead",
#         "first_name": name,
#         "mobile_no": phone,
#         "email": email,
#         "visist_type": visist_type,
#         "visiting_time": visiting_time,
#         "project_name": project_name
#     })

#     add_lead.insert(ignore_permissions=True)
#     frappe.db.commit()

#     return {"message": "Added Lead Successfully"}
@frappe.whitelist(allow_guest=True)
def video_meeting_shedule():
    data = frappe.form_dict

    add_lead = frappe.get_doc({
        "doctype": "CRM Lead",
        "first_name": data.get("name"),
        "mobile_no": data.get("phone"),
        "email": data.get("email"),
        "visist_type": data.get("visist_type"),
        "visiting_time": data.get("visiting_time"),
        "project_name": data.get("project_name"),
        "service":"Website Enquiry",
        "source": "Website",
    })

    add_lead.insert(ignore_permissions=True)
    frappe.db.commit()

    return {"message": "Thank you for your interest. Our team will contact you soon to confirm your virtual tour."}

@frappe.whitelist(allow_guest=True)
def detaip_page_coatct():
     data = frappe.form_dict
     add_lead=frappe.get_doc({
        "doctype": "CRM Lead",
        "first_name": data.get("name"),
        "mobile_no": data.get("phone"),
        "email": data.get("email"),
        "visiting_time": data.get("visiting_time"),
        "project_name": data.get("project_name"),
        "visist_type": "Website Enquiry",
        "service":"Website Enquiry" ,
        "source": "Website",
        
    })
     add_lead.insert(ignore_permissions=True)
     frappe.db.commit()
     return {"message": "Thank you for your interest."}
     

