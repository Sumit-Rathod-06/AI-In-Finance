import re

def extract_fields(text):

    name_match = re.search(r"Name\s*:\s*([\w\s]+)", text)
    name = name_match.group(1).strip() if name_match else "Not found"

    address_match = re.search(r"Add:\s*(.+)", text)
    address = address_match.group(1).strip() if address_match else "Not found"

    dob_match = re.search(r"DOB:\s*(\w{2}-\w{2}-\w{2,4})", text)
    dob = dob_match.group(1).strip() if dob_match else "Not found"

    return {
        "name": name,
        "address": address,
        "dob": dob,
    }
