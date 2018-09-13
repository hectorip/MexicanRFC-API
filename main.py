import hug

@hug.get()
def rfc(name):
    return {"RFC": name[1].upper()}


@hug.get()
def curp(body):
    return body