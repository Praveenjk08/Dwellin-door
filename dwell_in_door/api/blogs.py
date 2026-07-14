import frappe

@frappe.whitelist(allow_guest=True)
def  get_all_blogs():
    blogs=frappe.get_all("Blogs",
                  filters={"is_active":1},
    
                  fields=["blog_name",
                          "blog_date",
                          "advice",
                          "image",
                          "url"],
                          order_by="creation asc")
    return blogs


@frappe.whitelist(allow_guest=True)
def get_blog_detail(route):

    blog = frappe.get_all(
        "Blogs",
        filters={"url": route},
        fields=["*"],
      
    )

    if not blog:
        return {}

    return blog