import requests

def check_aml(name):
    aml_database = ["Sumit Rathod", "Dikshant Karande"] 
    if name in aml_database:
        return {"flagged": True, "reason": "Blacklisted in AML database"}
    return {"flagged": False}
