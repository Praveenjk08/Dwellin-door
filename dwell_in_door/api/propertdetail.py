import frappe
import json


@frappe.whitelist(allow_guest=True)
def get_property_detils_for_cards():
    cards = frappe.get_all(
        "Property Detials",
        filters={"is_active": 1},
        fields=[
            "url",
            "project_name",
            "location",
            "price",
            "bedrooms",
            "bathrooms",
            "area",
            "image"
        ],
    )

    return cards


@frappe.whitelist(allow_guest=True)
def get_property_details(url):
    property = frappe.get_doc(
        "Property Detials",
        {"url": url}
    )

    return property.as_dict()


# ============================================================
# SIMILAR PROJECTS API
# ============================================================
# Similar properties are selected manually in the
# custom_similar_properties child table.
# ============================================================

@frappe.whitelist(allow_guest=True)
def get_similar_projects(current_project):

    property_doc = frappe.get_doc(
        "Property Detials",
        {"project_name": current_project}
    )

    similar_projects = []

    # Get manually selected properties
    for row in property_doc.custom_similar_properties:

        if not row.property:
            continue

        try:
            similar_property = frappe.get_doc(
                "Property Detials",
                row.property
            )

            # Only active properties should be displayed
            if not similar_property.is_active:
                continue

            similar_projects.append({
                "url": similar_property.url,
                "project_name": similar_property.project_name,
                "location": similar_property.location,
                "price": similar_property.price,
                "bedrooms": similar_property.bedrooms,
                "bathrooms": similar_property.bathrooms,
                "area": similar_property.area,
                "image": similar_property.image,
                "property_location_type": similar_property.property_location_type
            })

        except frappe.DoesNotExistError:
            continue

    return similar_projects


# ============================================================
# PROJECT LIST PAGE FILTER API
# ============================================================

@frappe.whitelist(allow_guest=True)
def list_get_property_detils_for_cards(
    property_location_type=None,
    bathrooms=None,
    bedroom=None
):

    filters = {}

    if property_location_type:
        location_list = json.loads(property_location_type)

        if location_list:
            filters["property_location_type"] = [
                "in",
                location_list
            ]

    if bathrooms:
        bathroom_list = json.loads(bathrooms)

        if bathroom_list:
            filters["bathrooms"] = [
                "in",
                bathroom_list
            ]

    if bedroom:
        bedroom_list = json.loads(bedroom)

        if bedroom_list:
            filters["bedrooms"] = [
                "in",
                bedroom_list
            ]

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

    cards = frappe.get_all(
        "Property Detials",
        filters={"is_active": 1},
        fields=["*"]
    )

    return cards