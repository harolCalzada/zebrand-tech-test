from typing import List


def get_differences_between_product_instances(old, new) -> dict:
    """
    Compare two objects and return a dict of differences between them.
    """
    fields_to_compare = ['sku', 'name', 'price', 'brand']
    differences = {}
    for field in fields_to_compare:
        if field == 'price':
            old_value = str(old.price)
            new_value = str(new.price)
        else:
            old_value = getattr(old, field)
            new_value = getattr(new, field)
        if getattr(old, field) != getattr(new, field):
            differences[field] = {
                'old': old_value,
                'new': new_value
            }
    return differences
