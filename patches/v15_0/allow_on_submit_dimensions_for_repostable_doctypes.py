import frappe

from nexa.accounts.doctype.accounting_dimension.accounting_dimension import (
	get_accounting_dimensions,
)
from nexa.accounts.doctype.repost_accounting_ledger.repost_accounting_ledger import (
	get_allowed_types_from_settings,
)


def execute():
	for dt in get_allowed_types_from_settings(child_doc=True):
		for dimension in get_accounting_dimensions():
			frappe.db.set_value("Custom Field", dt + "-" + dimension, "allow_on_submit", 1)
