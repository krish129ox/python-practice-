from collections import defaultdict

handlers = defaultdict(list)

def on(event):
    def deco(fn):
        handlers[event].append(fn)
        return fn
    return deco

def emit(event, *a, **kw):
    for h in handlers[event]: h(*a, **kw)

@on("signup")
def welcome(user): print("Welcome", user)

@on("signup")
def log(user): print("Logged", user)

emit("signup", "Krish")