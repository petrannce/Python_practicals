import matplotlib.pyplot as pyplot

BAR_WIDTH = 0.35

# Set up grouped bar charts data
teama_results = [60, 75, 56, 62, 58]
teamb_results = [55, 68, 65, 72, 68]

# Set up the index for each bar
index_teama = (1, 2, 3, 4, 5)
index_teamb = [x + BAR_WIDTH for x in index_teama]

# Determine the mid point for the ticks
ticks = [x + BAR_WIDTH / 2 for x in index_teama]
ticks_labels = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']

#Plot the bar chart
pyplot.bar(index_teama, teama_results, BAR_WIDTH, label='Team A', color='blue')
pyplot.bar(index_teamb, teamb_results, BAR_WIDTH, label='Team B', color='orange')

# Set up the graph
pyplot.xlabel('Quarter')
pyplot.ylabel('Results')

pyplot.title('Quarterly Results Comparison')
pyplot.xticks(ticks, ticks_labels)
pyplot.legend()

# Display the graph
pyplot.show()