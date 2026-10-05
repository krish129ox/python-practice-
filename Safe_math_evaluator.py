import ast, operator as op

ops = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
       ast.Div: op.truediv, ast.Pow: op.pow, ast.USub: op.neg}

def ev(n):
    if isinstance(n, ast.Constant): return n.value
    if isinstance(n, ast.BinOp): return ops[type(n.op)](ev(n.left), ev(n.right))
    if isinstance(n, ast.UnaryOp): return ops[type(n.op)](ev(n.operand))
    raise ValueError("unsafe expression")

print(ev(ast.parse("2 + 3 * (4 - 1) ** 2", mode="eval").body))  # 29