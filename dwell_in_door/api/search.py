import frappe


# @frappe.whitelist(allow_guest=True)
# def search_location(search=None):

#     if not search:
#         return []

#     return frappe.get_all(
#         "Property Detials",
#         filters={
#             "location": ["like", f"%{search}%"]
#         },
#         fields=["location"],
#         distinct=True,
#         limit_page_length=10
#     )

@frappe.whitelist(allow_guest=True)
def search_location(search=None):

    if not search:
        return []

    return frappe.get_all(
        "Property Detials",
        or_filters=[
            ["location", "like", f"%{search}%"],
            ["project_name", "like", f"%{search}%"],
            ["price", "like", f"%{search}%"]
        ],
        fields=[
            "project_name",
            "location",
            "price",
            "url"
        ],
        limit_page_length=10
    )

@frappe.whitelist(allow_guest=True)
def get_property_by_location_serach(location=None):

    if not location:
        return []

    return frappe.get_all(
        "Property Detials",
        filters={
            "location": ["like", f"%{location}%"]
        },
        fields=[
            "url",
            "project_name",
            "location",
            "property_location_type",
            "price",
            "image",
            "bedrooms",
            "bathrooms",
            "area"
        ],
        order_by="creation desc"
    )



#this intigarting the three fileds search and separte filds search   
@frappe.whitelist(allow_guest=True)
def search_property_three(location=None, property_type=None, price=None):

    filters = {}

    if location:
        filters["location"] = ["like", f"%{location}%"]

    if property_type:
        filters["bedrooms"] = property_type

    if price:
         filters["price"] = ["like", f"%{price}%"]

    return frappe.get_all(
        "Property Detials",
        filters=filters,
        fields=[
            "url",
            "project_name",
            "location",
            
            "property_location_type",
            "price",
            "image",
            "bedrooms",
            "bathrooms",
            "area"
        ]
    )