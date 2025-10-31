# stack_evaluator.py
# Stack-based expression evaluator using only functions and lists

def push(stack, item):
    stack.append(item)

def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    return None

def peek(stack):
    if not is_empty(stack):
        return stack[-1]
    return None

def is_empty(stack):
    return len(stack) == 0

def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

def apply_op(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b

def evaluate_expression(expression):
    values = []
    ops = []
    i = 0

    while i < len(expression):
        ch = expression[i]

        if ch == ' ':
            i += 1
            continue

        if ch.isdigit():
            val = 0
            while i < len(expression) and expression[i].isdigit():
                val = val * 10 + int(expression[i])
                i += 1
            push(values, val)
            continue

        elif ch == '(':
            push(ops, ch)

        elif ch == ')':
            while not is_empty(ops) and peek(ops) != '(':
                b = pop(values)
                a = pop(values)
                op = pop(ops)
                push(values, apply_op(a, b, op))
            pop(ops)

        elif ch in "+-*/":
            while (not is_empty(ops)) and precedence(peek(ops)) >= precedence(ch):
                b = pop(values)
                a = pop(values)
                op = pop(ops)
                push(values, apply_op(a, b, op))
            push(ops, ch)

        i += 1

    while not is_empty(ops):
        b = pop(values)
        a = pop(values)
        op = pop(ops)
        push(values, apply_op(a, b, op))

    return pop(values)

def process_files(input_file='input.txt', output_file='output.txt'):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    results = []
    for line in lines:
        line = line.strip()
        if line == '-----':
            results.append('-----')
        elif line:
            result = evaluate_expression(line)
            results.append(str(int(result)))

    with open(output_file, 'w') as f:
        for item in results:
            f.write(item + '\n')

if __name__ == '__main__':
    process_files()
    print("✅ Evaluation complete. Results saved in output.txt")
