app_name = "dwell_in_door"
app_title = "Dwell-In-Door"
app_publisher = "Praveen Jk"
app_description = "real estate app"
app_email = "praveenjk088@gmail.com"
app_license = "mit"

website_route_rules = [
    {"from_route": "/", "to_route": "/"},
    {"from_route": "/properties", "to_route": "/"},
    {"from_route": "/properties/<path:url>", "to_route": "/"},
    {"from_route": "/about-us", "to_route": "/"},
]
# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "dwell_in_door",
# 		"logo": "/assets/dwell_in_door/logo.png",
# 		"title": "Dwell-In-Door",
# 		"route": "/dwell_in_door",
# 		"has_permission": "dwell_in_door.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/dwell_in_door/css/dwell_in_door.css"
# app_include_js = "/assets/dwell_in_door/js/dwell_in_door.js"

# include js, css files in header of web template
# web_include_css = "/assets/dwell_in_door/css/dwell_in_door.css"
# web_include_js = "/assets/dwell_in_door/js/dwell_in_door.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "dwell_in_door/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "dwell_in_door/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "dwell_in_door.utils.jinja_methods",
# 	"filters": "dwell_in_door.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "dwell_in_door.install.before_install"
# after_install = "dwell_in_door.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "dwell_in_door.uninstall.before_uninstall"
# after_uninstall = "dwell_in_door.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "dwell_in_door.utils.before_app_install"
# after_app_install = "dwell_in_door.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "dwell_in_door.utils.before_app_uninstall"
# after_app_uninstall = "dwell_in_door.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "dwell_in_door.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "dwell_in_door.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"dwell_in_door.tasks.all"
# 	],
# 	"daily": [
# 		"dwell_in_door.tasks.daily"
# 	],
# 	"hourly": [
# 		"dwell_in_door.tasks.hourly"
# 	],
# 	"weekly": [
# 		"dwell_in_door.tasks.weekly"
# 	],
# 	"monthly": [
# 		"dwell_in_door.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "dwell_in_door.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "dwell_in_door.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "dwell_in_door.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "dwell_in_door.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["dwell_in_door.utils.before_request"]
# after_request = ["dwell_in_door.utils.after_request"]

# Job Events
# ----------
# before_job = ["dwell_in_door.utils.before_job"]
# after_job = ["dwell_in_door.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"dwell_in_door.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

