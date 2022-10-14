import math


class Expression:

    def parse_expr(self, expr: str) -> int:
        op = 0
        op1 = 0
        op = self.parse_factor(expr)
        if len(expr) != 0:
            if expr[0] == '+':
                expr = expr[1:1 + len(expr) - 1]
                op1 = self.parse_expr(expr)
                op += op1
            elif expr[0] == '-':
                expr = expr[1:1 + len(expr) - 1]
                op1 = self.parse_expr(expr)
                op -= op1
        return op

    def parse_factor(self, expr: str) -> int:
        op = 0
        op1 = 0
        op = self.parse_term(expr)
        if len(expr) != 0:
            if expr[0] == '*':
                expr = expr.value[1:1 + len(expr) - 1]
                op1 = self.parse_factor(expr)
                op *= op1
            elif expr[0] == '/':
                expr.value = expr[1:1 + len(expr) - 1]
                op1 = self.parse_factor(expr)
                op = math.floor(op / op1)
        return op

    def parse_term(self, expr: str) -> int:
        return_value = 0
        if len(expr) != 0:
            if str.isdigit(expr[0]):
                return_value = self.parse_number(expr)
                return return_value
            elif expr.value[0] == '(':
                expr.value = expr.value[1:1 + len(expr.value) - 1]
                return_value = self.parse_expr(expr)
                return return_value
            elif expr.value[0] == ')':
                expr.value = expr.value[1:1 + len(expr.value) - 1]
        return return_value

    def parse_number(self, expr: str) -> int:
        number_temp = ""
        i = 0
        while (i < len(expr)) and str.isdigit(expr[i]):
            if str.isdigit(expr[0]):
                number_temp += (expr[0])
                expr = expr[1:1 + len(expr) - 1]
            i += 1
        return int(number_temp)

expr='2+2'
number_temp = ""
i = 0
while (i < len(expr)) and str.isdigit(expr[i]):
    if str.isdigit(expr[0]):
        number_temp += (expr[0])
        expr = expr[1:1 + len(expr) - 1]
    i += 1
