def arithmetic_arranger(problems, count_start=False):

    line_1 = ""
    line_2 = ""
    line_3 = ""
    line_4 = ""

    for i, problem in enumerate(problems):
        a, b, c = problem.split()
        d = max(len(a), len(c))

        if len(problems) > 5:
            return "Error: Too many problems."
        if len(a) > 4 or len(c) > 4:
            return "Error: Numbers cannot be more than four digits."
        if b == "+" or b == "-":
            try:
                a = int(a)
                c = int(c)
                if b == "+":
                    result = a + c
                else:
                    result = a - c
                line_1 = line_1 + f'{a:>{d+2}}'
                line_2 = line_2 + b + f'{c:>{d+1}}'
                line_3 = line_3 + ''.rjust(d + 2, '-')
                line_4 = line_4 + str(result).rjust(d + 2)
            except ValueError:
                return "Error: Numbers must only contain digits."
        else:
            return "Error: Operator must be '+' or '-'."

        if i < len(problems) - 1:
            line_1 += "    "
            line_2 += "    "
            line_3 += "    "
            line_4 += "    "

    if count_start:
        arranged_problems = line_1 + '\n' + line_2 + '\n' + line_3 + '\n' + line_4
    else:
        arranged_problems = line_1 + '\n' + line_2 + '\n' + line_3
    return arranged_problems
