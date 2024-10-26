# Iris Plant Data Explorer

## Overview
The **Iris Plant Data Explorer** is an interactive web application built using Streamlit. It allows users to explore the well-known Iris dataset, which consists of measurements from three species of iris plants. The app provides various visualizations and user inputs to analyze and filter the data.

## Features
- Display the preview of the Iris dataset.
- Show data overview, including shape, columns, and data types.
- Basic statistics of the dataset.
- Visualizations:
  - Pairplot using Seaborn.
  - Interactive scatter plot (Sepal Length vs. Sepal Width) using Plotly.
  - Boxplot by species using Plotly.
  - Distribution plots for petal length using Plotly.
- User input filters for selecting species and measurements.
- Map display of randomly generated geolocation data.
- Interactive widgets for user engagement.
- Progress bar to demonstrate asynchronous operations.
- User feedback mechanism.

## Installation
To run this app, ensure you have Python and Streamlit installed. You can install the required libraries using pip:

```bash
pip install streamlit pandas numpy matplotlib seaborn plotly
```

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Vigneshwar-B/Iris_Plant_Data_Explorer.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Iris_Plant_Data_Explorer
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Developer
**Vigneshwar B**

## Acknowledgements
- This application utilizes the Iris dataset available through the Seaborn library.
- Special thanks to Streamlit, Seaborn, Plotly, and all contributors of the libraries used.

## License
This project is open-source and available under the [MIT License](LICENSE).

```

Feel free to modify any sections as needed!
