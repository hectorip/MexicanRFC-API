import hug
"""
Generates the  RFC and CURP strings from the personal data provided.
"""


@hug.get()
def rfc(name):
    return {"RFC": name[1].upper()}


@hug.post()
def curp(body):
    """
    Returns the CURP almost complete
    """
    return body