# coding: utf8
"""
Обратная Польская нотация.
"""

from collections import namedtuple
import math

Func = namedtuple("Func", ["pr", "type", "call"])


operators = {
    "+": Func(1, "double", lambda a, b: a + b),
    "-": Func(1, "double", lambda a, b: a - b),
    "*": Func(2, "double", lambda a, b: a * b),
    "/": Func(2, "double", lambda a, b: a / b),
    "^": Func(3, "double", lambda a, b: a ** b),
    "!": Func(3, "single", lambda a: fact_tree(a)),
    "sin": Func(1, "single", lambda a: math.sin(a)),
    "pi": Func(3, "alias", lambda: math.pi),
}


def sub_tree(left, right):
    if left > right:
        return 1
    if left == right:
        return left
    if right - left == 1:
        return left * right

    middle = (left + right) // 2
    return sub_tree(left, middle) * sub_tree(middle + 1, right)


def fact_tree(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n == 1 or n == 2:
        return n
    return sub_tree(2, n)


def parser(string):
    tokens = []
    num = []
    opt = []
    s = string.replace(" ", "")
    for idx in range(len(s)):
        if operators.get(_make_token(opt)):
            if opt:
                tokens.append(_make_token(opt))
                opt = []
        if s[idx].isdigit():
            num.append(s[idx])

        elif s[idx] == "." and num:
            num.append(s[idx])

        elif s[idx] == "-" and (idx == 0 or s[idx - 1] == "("):
            num.append(s[idx])

        elif s[idx].isalpha() and s[idx].islower():
            if num:
                tokens.append(_make_token(num))
                num = []
            opt.append(s[idx])

        elif s[idx] in "+-*/%^!()":
            if num:
                tokens.append(_make_token(num))
                num = []
            tokens.append(s[idx])
    if num:
        tokens.append(_make_token(num))
    if opt:
        tokens.append(_make_token(opt))
    return tokens


def _is_float(token):
    if "." in token:
        return True


def _is_int(token):
    if token and token[-1].isdigit() and not _is_float(token):
        return True


def _make_token(sub):
    token = "".join([ch for ch in sub])
    if _is_int(token):
        return int(token)
    elif _is_float(token):
        return float(token)
    return token


def shunting_yard(tokens):
    stack = []
    out = []
    for token in tokens:
        if token in operators:
            while stack and stack[-1] != '(' \
                    and operators[token].pr <= operators[stack[-1]].pr:
                out.append(stack.pop())
            stack.append(token)
        elif token == ')':
            while stack:
                x = stack.pop()
                if x == '(':
                    break
                out.append(x)
        elif token == '(':
            stack.append(token)
        else:
            out.append(token)
    while stack:
        out.append(stack.pop())
    return out


def calculator(polish):
    stack = []
    for token in polish:
        if token in operators:
            if operators[token].type == "double":
                y, x = stack.pop(), stack.pop()
                stack.append(operators[token].call(x, y))
            elif operators[token].type == "single":
                x = stack.pop()
                stack.append(operators[token].call(x))
            elif operators[token].type == "alias":
                stack.append(operators[token].call())
        else:
            stack.append(token)
    return stack.pop()


formula = "-1+(1+2.76)*4.1 *pi +5!"

formula_tokens = parser(formula)
sort_tokens = shunting_yard(formula_tokens)
assert calculator(sort_tokens) == 167.43079234774024

formula = "sin(3- 2)"

formula_tokens = parser(formula)
sort_tokens = shunting_yard(formula_tokens)
assert calculator(sort_tokens) == 0.8414709848078965
