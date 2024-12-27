# Data Visualization with Python 📊

Welcome to the **Data Visualization with Python** repository! This repo aims to help you learn or remember essential data visualization principles using Python, with a focus on plotting variables $x$, $y_i$  , or $z$. Whether you're new to coding or an experienced user, you’ll find valuable insights on how to create clear and impactful data visualizations.

## Table of Contents
1. [Overview](#overview)
2. [Repository Structure](#repository-structure)
3. [Getting Started](#getting-started)
4. [Data](#data)
5. [Basic Visualization Examples](#basic-visualization-examples)
6. [Advanced Topics](#advanced-topics)
7. [Tips & Best Practices](#tips--best-practices)
8. [Contributing](#contributing)

---

## Overview
In this repository, we’ll illustrate how to:
- Load data using **Pandas** 🐼
- Create visualizations using **Seaborn** 🎨
- Understand essential visualization principles for effectively plotting **x** and **y** variables
- Communicate findings to both technical and non-technical audiences

The repository is designed for anyone interested in data visualization.

---

## Repository Structure

```
data-visualization-with-python/
├── data/
│   ├── graph_data.csv
│   ├── financial_data.csv
│   ├── biological_data.csv
│   ├── RNANGS_data.csv
│   └── tokenization_data.csv
├── notebooks/
│   ├── 01_Graph_Fundamentals.ipynb
│   ├── 02_Advanced_Graph.ipynb
│   ├── 03_Financial_Visualizations.ipynb
│   ├── 04_Biological_Visualizations.ipynb
│   ├── 05_RNANGS_Visualizations.ipynb
│   └── 06_Tokenization_Visualizations.ipynb
├── README.md
└── requirements.txt
```

1. **`data/`**: Contains sample datasets.
2. **`notebooks/`**: Jupyter notebooks showcasing visualizations.
3. **`README.md`**: Main documentation (this file).
4. **`requirements.txt`**: List of required Python packages.

---

## Getting Started
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/data-visualization-with-python.git
   ```
2. **Install Requirements**  
   ```bash
   cd data-visualization-with-python
   pip install -r requirements.txt
   ```
3. **Open Notebooks**  
   ```bash
   jupyter notebook
   ```
   Navigate to the `notebooks/` folder to explore the examples.

---

## Data
Inside the `data/` folder, you will find a simple dataset named `graph_data.csv` with columns:
- **x**: Independent variable  
- **y**: Dependent variable  

Feel free to replace `graph_data.csv` with your own dataset. The examples in this repository will adapt to any dataset containing **x** and **y** columns.

---

## Basic Visualization Examples
Open `01_basic_visualizations.ipynb` to explore:

1. **Line Plot** 🚀  
   Useful for understanding trends over a continuous range of **x**.  
   ```python
   import pandas as pd
   import matplotlib.pyplot as plt
   
   # Load data
   df = pd.read_csv('../data/graph_data.csv')
   
   # Basic line plot
   plt.plot(df['x'], df['y'], marker='o')
   plt.title('Line Plot: y vs. x')
   plt.xlabel('x')
   plt.ylabel('y')
   plt.show()
   ```

2. **Scatter Plot** 🌟  
   Ideal for visualizing the relationship between **x** and **y**.  
   ```python
   import seaborn as sns
   
   sns.scatterplot(data=df, x='x', y='y')
   plt.title('Scatter Plot: y vs. x')
   plt.show()
   ```

3. **Bar Plot** 🍫  
   Good for categorical **x** values or for summarizing data.  
   ```python
   # Simple bar plot
   sns.barplot(data=df, x='x', y='y')
   plt.title('Bar Plot: y by x')
   plt.show()
   ```

---

## Advanced Topics
Open `02_advanced_visualizations.ipynb` to learn about:
1. **Styling & Themes** ✨  
   - Applying Seaborn themes for professional-looking plots.
   - Customizing colors, markers, and line styles.

2. **Subplots** 🪄  
   - Displaying multiple visuals in a single figure.
   - Comparing different views of **x** and **y** side by side.

3. **Statistical Plots** 📈  
   - Regression plots to show trends and confidence intervals.
   - Box plots to visualize data distribution and outliers.

---

## Tips & Best Practices
1. **Label Everything**  
   - Clear titles, labels, and legends enhance readability.  
   - Remember to clarify the meaning of **x** and **y**.

2. **Keep It Simple**  
   - Use minimal chart junk; focus on clarity.
   - Choose appropriate plot types for your data (e.g., line, scatter, bar, box, histogram).

3. **Scalability**  
   - Ensure your plots remain clear when scaled for presentations or reports.

4. **Communicate Effectively**  
   - For non-technical audiences, explain the story behind the data in plain language.
   - For technical audiences, provide succinct details about methods, data sources, and limitations.

5. **Experiment and Iterate**  
   - Data visualization often requires trial and error.
   - Try multiple plot types before deciding on the best representation for **x** and **y**.

---

## Contributing
We welcome contributions to improve this repository. If you have ideas for new notebooks, different data visualization libraries, or additional topics, feel free to:
1. **Fork** this repository
2. **Create** a new branch
3. **Submit** a Pull Request

---

**Keep Visualizing!** 🌈 If you have any questions or suggestions, feel free to open an issue in this repository. Enjoy exploring the world of data visualization!
