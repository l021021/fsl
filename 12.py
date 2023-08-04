import matplotlib.pyplot as plt
from selenium import webdriver

# Step 1: Convert HTML to an image using Selenium and Webdriver
html_file_path = 'map_terrain.html'  # Replace with the actual path to your HTML file
image_output_path = 'image.png'  # Replace with the path where you want to save the image

# Set up the web driver (you may need to download the appropriate driver for your browser)
driver = webdriver.Chrome()  # Or use webdriver.Firefox() for Firefox, etc.

# Open the HTML file and take a screenshot
driver.get(html_file_path)
driver.save_screenshot(image_output_path)

# Close the web driver
driver.quit()

# Step 2: Use Matplotlib to display the image as the background
img = plt.imread(image_output_path)

fig, ax = plt.subplots(figsize=(8, 6))

# Display the image as a background
ax.imshow(img, aspect='auto', alpha=0.5)

# Plot other elements on top of the background image (optional)
x = [1,2,34,4]
y = [2,4,5,6]
ax.scatter(x, y, color='red', marker='o', s=50)

# Hide the axis labels and ticks (optional)
ax.axis('off')

# Show the plot
plt.show()
