"""
Given an infix expression in the form of string s. Convert this infix expression to postfix expression.

Infix expression: The expression of the form a op b. When an operator is in-between every pair of operands.
Postfix expression: The expression of the form a b op. When an operator is followed for every pair of operands.
Note: The order of precedence is: ^ greater than * equals to / greater than + equals to -. Ignore the right associativity of ^.

Examples :
Input: s = "a+b*(c^d-e)^(f+g*h)-i"
Output: abcd^e-fgh*+^*+i-
Explanation: After converting the infix expression into postfix expression, the resultant expression will be abcd^e-fgh*+^*+i-

Input: s = "A*(B+C)/D"
Output: ABC+*D/
Explanation: After converting the infix expression into postfix expression, the resultant expression will be ABC+*D/

Input: s = "(a+b)*(c+d)"
Output: ab+cd+*
"""


def InfixtoPostfix(string):
        postfix = ""
        stack = []
        prio = {'^': 1, '*': 2, '/': 2, '+': 3, '-': 3, '(': 4}
        
        for c in string:
            if c.isalnum():
                postfix += c
            elif c == '(':
                stack.append(c)
            elif c == ')':
                while stack[-1] != '(':
                    postfix += stack.pop()
                stack.pop()
            else:
                while stack and prio[stack[-1]] <= prio[c]:
                    postfix += stack.pop()
                stack.append(c)
        
        while stack:
            postfix += stack.pop()

        return postfix


arr = [
    '(A+B)*(C-D)',
    'A*(B+C)-D/E',
    '((A+B)*(C-D))/(E+F)',
    'A+B*C-D/E+F',
    '(A+B*(C-D))/E',
    '((A+B)*(C+D))/(E-F)+G',
    'A*(B+C)*(D-E)',
    '(A+B)*(C+(D-E))',
    'A+(B-C)*(D/E)',
    '((A+B)/C)+(D-E)'
]

for i in arr:
    print(InfixtoPostfix(i))
