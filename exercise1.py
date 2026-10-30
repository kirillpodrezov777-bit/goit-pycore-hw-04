path = 'Data1.txt'
def totalsalary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total_salary = 0
            lines_count = 0
            for line in file.readlines():
                lines_count += 1
                name, salary = line.strip().split(',')
                total_salary += int(salary)
        average_salary = total_salary / lines_count
        return (total_salary, average_salary)
    except FileNotFoundError:
        return "File not found."
    except ValueError:
        return "Invalid data format in file."
    except ZeroDivisionError:
        return "Division by 0"
print(totalsalary(path))
