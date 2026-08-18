def calculate(a, b, op):
    ops = {'+': a+b, '-': a-b, '*': a*b, '/': a/b if b else None}
    return ops.get(op)