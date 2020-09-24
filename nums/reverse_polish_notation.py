# coding: utf8
"""
Обратная Польская нотация.
"""

from collections import namedtuple
import math

Func = namedtuple("Func", ["pr", "type", "call"])


class OperatorTypes:
    DOUBLE = "DOUBLE"
    SINGLE = "SINGLE"
    ALIAS = "ALIAS"


OPERATORS = {
    "+": Func(1, OperatorTypes.DOUBLE, lambda a, b: a + b),
    "-": Func(1, OperatorTypes.DOUBLE, lambda a, b: a - b),
    "*": Func(2, OperatorTypes.DOUBLE, lambda a, b: a * b),
    "/": Func(2, OperatorTypes.DOUBLE, lambda a, b: a / b),
    "^": Func(3, OperatorTypes.DOUBLE, lambda a, b: a ** b),
    "!": Func(3, OperatorTypes.SINGLE, lambda a: _fact_tree(a)),
    "sin": Func(1, OperatorTypes.SINGLE, lambda a: math.sin(a)),
    "pi": Func(3, OperatorTypes.ALIAS, lambda: math.pi),
}


def _sub_tree(left, right):
    if left > right:
        return 1
    if left == right:
        return left
    if right - left == 1:
        return left * right

    middle = (left + right) // 2
    return _sub_tree(left, middle) * _sub_tree(middle + 1, right)


def _fact_tree(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n == 1 or n == 2:
        return n
    return _sub_tree(2, n)


def _parser(string):
    tokens = []
    num = []
    opt = []
    s = string.replace(" ", "")
    for idx in range(len(s)):
        if OPERATORS.get(_make_token(opt)):
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


def _shunting_yard(tokens):
    stack = []
    out = []
    for token in tokens:
        if token in OPERATORS:
            while stack:
                if stack[-1] == "(":
                    break
                if OPERATORS[token].pr > OPERATORS[stack[-1]].pr:
                    break
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


def _reverse_polish_notation(polish):
    stack = []
    for token in polish:
        if token in OPERATORS:
            if OPERATORS[token].type == OperatorTypes.DOUBLE:
                y, x = stack.pop(), stack.pop()
                stack.append(OPERATORS[token].call(x, y))
            elif OPERATORS[token].type == OperatorTypes.SINGLE:
                x = stack.pop()
                stack.append(OPERATORS[token].call(x))
            elif OPERATORS[token].type == OperatorTypes.ALIAS:
                stack.append(OPERATORS[token].call())
        else:
            stack.append(token)
    return stack.pop()


def reverse_polish_notation(formula):
    formula_tokens = _parser(formula)
    sort_tokens = _shunting_yard(formula_tokens)
    answer = _reverse_polish_notation(sort_tokens)
    return answer
