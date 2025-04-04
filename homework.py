import matplotlib.pyplot as plt
Employee_name=["Pankaj", "Meghna", "david", "Lisa"]
Role=["ceo","worker","worker"]
salary=[100, 200]
marks_perc = []
for x in Employee_name:
    res = (x/50)*100
    marks_perc.append(res)
print(marks_perc)
def line_chart_of_Employee_and_name():
    plt.plot(Employee_name,Role)
    plt.title("Employee names Graph")
    plt.xlabel("Employee names")
    plt.ylabel("role")
    plt.show()
line_chart_of_Employee_and_name()
def percentage_bar_chart():
    plt.plot(Employee_name,Role)
    plt.title("Employee name Percentage Graph")
    plt.xlabel("Employee names")
    plt.ylabel("Role")
    plt.show()
percentage_bar_chart()