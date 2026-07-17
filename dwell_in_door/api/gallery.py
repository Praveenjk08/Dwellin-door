import frappe


@frappe.whitelist(allow_guest=True)
def get_all_tags():

    tags=frappe.get_all(
        "Tag",
        fields=["name"],
        )
    order_by="cretaed_asc"

    return tags    



# @frappe.whitelist(allow_guest=True)
# def get_gallery_by_tag(tag):

#     tagged_docs = get_tagged_docs("Gallery Page", tag)

#     gallery = []

#     for doc_name in tagged_docs:
#         doc = frappe.get_doc("Gallery Page", doc_name)

#         gallery.append({
#             "name": doc.name,
#             "gallery_image_name": doc.gallery_image_name,
#             "image": doc.iamge
#         })

#     return gallery



@frappe.whitelist(allow_guest=True)
def get_gallery_by_tag(tag=None):

    if not tag or tag == "All":
        return frappe.get_all(
            "Gallery Page",
            fields=["name",  "iamge"]
        )

    gallery = frappe.db.sql("""
        SELECT
            gp.name,
            gp.iamge
        FROM `tabGallery Page` gp
        INNER JOIN `tabTag Link` tl
            ON tl.document_name = gp.name
        WHERE tl.document_type = 'Gallery Page'
        AND tl.tag = %s
    """, (tag,), as_dict=True)

    return gallery
    