import frappe

@frappe.whitelist(allow_guest=True)
def get_property_detils_for_cards():
    cards=frappe.get_all("Property Detials",
                         
         filters={"is_active":1},
                         fields=["url",
                                 "project_name",
                                 "location",
                                 "price",
                                 "bedrooms",
                                 "bathrooms",
                                 "area",
                                 "image"],
        # fields=["*"],
                                #  order_by="creation asc"
                         )
    

    return cards





@frappe.whitelist(allow_guest=True)
def get_property_details(url):
    property = frappe.get_doc("Property Detials", {"url": url})

    return property.as_dict()    



#simillar project api
@frappe.whitelist(allow_guest=True)
def get_similar_projects(location_type, current_project):

    return frappe.get_all(
        "Property Detials",
        filters={
            "property_location_type": location_type,
            "project_name": ["!=", current_project]
        },
        fields=["*"],
        # limit_page_length=4
    )



#This projectlist page filter api

import frappe
import json

@frappe.whitelist()
def list_get_property_detils_for_cards(property_location_type=None, bathrooms=None, bedroom=None):

    filters = {}

    if property_location_type:
        location_list = json.loads(property_location_type)
        if location_list:
            filters["property_location_type"] = ["in", location_list]

    if bathrooms:
        bathroom_list = json.loads(bathrooms)
        if bathroom_list:
            filters["bathrooms"] = ["in", bathroom_list]

    if bedroom:
        bedroom_list = json.loads(bedroom)
        if bedroom_list:
            filters["bedrooms"] = ["in", bedroom_list]

    print("Filters =", filters)

    data = frappe.get_all(
        "Property Detials",
        filters=filters,
        fields=[
            "project_name",
            "location",
            "price",
            "bedrooms",
            "bathrooms",
            "area",
            "image",
            "url"
        ]
    )

    return data

@frappe.whitelist(allow_guest=True)
def dupliacte_get_property_detils_for_cards():
    cards=frappe.get_all("Property Detials",
                         
         filters={"is_active":1}, 
         fields=["*"])

    return  cards         
