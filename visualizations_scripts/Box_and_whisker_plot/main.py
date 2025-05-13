import matplotlib.pyplot as plt

# Sample data
data = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70]

# Create a box and whisker plot
box_colour = 'lightblue'
median_colour = 'red'
whisker_colour = 'green'
flier_colour = 'orange'

plt.boxplot(data, 
            boxprops={'color': box_colour}, 
            medianprops={'color': median_colour}, 
            whiskerprops={'color': whisker_colour}, 
            flierprops={'color': flier_colour})

# Add labels and title
plt.xlabel('Sample Data')
plt.ylabel('Values')
plt.title('Box and Whisker Plot')

# Show the plot
plt.show()