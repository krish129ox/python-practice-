import re

spec = [("NUM", r"\d+\.?\d*"), ("ID", r"[A-Za-z_]\w*"),
        ("OP", r"[+\-*/=()]"), ("WS", r"\s+")]
rx = re.compile("|".join(f"(?P<{n}>{p})" for n, p in spec))

print([(m.lastgroup, m.group()) for m in rx.finditer("x = 3.5 * (y + 2)")
       if m.lastgroup != "WS"])