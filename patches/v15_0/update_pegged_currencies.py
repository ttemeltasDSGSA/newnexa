import frappe

from nexa.setup.install import update_pegged_currencies


def execute():
	update_pegged_currencies()
