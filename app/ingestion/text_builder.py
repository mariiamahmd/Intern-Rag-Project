def row_to_text(row):
  
    text = f"""
Company {row["company"]} created a purchase order with status {row["po_status"]} and closed status {row["closed_code"]}.

The order contains a {row["line_type"]} line for the item "{row["item_description"]}" (Item Number: {row["item_number"]}).

The item is an {row["inventory_type"]} item and belongs to the {row["main_category"]} main category, {row["group_category"]} group category, and {row["sub_group_category"]} sub-group category.

The purchase order was requested by buyer {row["buyer_name"]} and will be supplied by vendor {row["vendor_name"]}.

The ordered quantity is {row["quantity"]} {row["uom"]} at a unit price of {row["unit_price"]} {row["currency_code"]}, for a total amount of {row["amount"]} {row["currency_code"]}.

The payment term is {row["payment_term"]}.
"""

    return text.strip()


