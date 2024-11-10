import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

# Data for Gantt chart
tasks = ['Research', 'Prototype Development', 'User Testing', 'Product Finalization', 'Market Launch']
start_dates = [dt.date(2024, 1, 1), dt.date(2024, 3, 1), dt.date(2024, 5, 1), dt.date(2024, 7, 1), dt.date(2024, 9, 1)]
end_dates = [dt.date(2024, 2, 28), dt.date(2024, 4, 30), dt.date(2024, 6, 30), dt.date(2024, 8, 31), dt.date(2024, 10, 31)]

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
for i, task in enumerate(tasks):
    ax.barh(task, (end_dates[i] - start_dates[i]).days, left=start_dates[i], color='#2ecc71')

ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.xlabel('Timeline')
plt.title('Project Timeline for SamsungEcoVision')
plt.show()
