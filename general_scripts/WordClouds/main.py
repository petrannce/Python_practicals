from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = """
Python is a programming language that lets you work quickly
and integrate systems more effectively. Python is powerful and fast;
it has easy-to-read syntax that runs clear and easy to debug.
"""

# Create a WordCloud object
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the WordCloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()