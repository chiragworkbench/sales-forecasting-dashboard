import matplotlib.pyplot as plt

# Sample sales data
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [1500, 1800, 2400, 2100, 2800]

# Create a line chart
plt.plot(months, sales, marker="o", linestyle="-", color="b", label="Sales")

# Labels and title
plt.xlabel("Months")
plt.ylabel("Sales ($)")
plt.title("Monthly Sales Chart")
plt.legend()
plt.grid(True)

# Show the chart
plt.show()
