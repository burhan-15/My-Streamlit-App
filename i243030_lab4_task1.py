import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="EDA Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Exploratory Data Analysis Interface")

# 2. Sidebar: Dataset Ingestion

#set header for sidebar
st.sidebar.header("Upload Your Dataset")
#create a file uploader in the sidebar for CSV files
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read dataset
    df = pd.read_csv(uploaded_file)
    # 3. Dataset Overview    

    #set subheader for dataset overview
    st.write("**First 5 Rows:**")
    #display the first 5 rows of the dataset
    st.write(df.head())
    #display the shape of the dataset
    st.write(df.shape)
    #display the data types of each column in the dataset
    st.write("**Column Data Types:**")
    st.write(df.dtypes)
    # Missing value summary
    st.write("**Missing Values per Column:**")
    st.write(df.isnull().sum())
   #display the count and percentage of missing values for each column in the dataset
    st.write("**Missing Values Percentage:**")
    st.write((df.isnull().sum() / len(df)) * 100)

    # Basic statistics for numerical columns
    st.write("**Basic Numerical Statistics:**")
    #display the basic statistics
    st.write(df.describe())
    
    # 4. Attribute Selection
    
    #set header for attribute selection in the sidebar
    st.sidebar.header("Attribute Selection")
    #create a selectbox in the sidebar to choose an attribute for visualization
    selected_column = st.sidebar.selectbox("Choose a column", df.columns)

    # Detect column type
    if df[selected_column].dtype in ['int64', 'float64']:
        column_type = "Numerical"
    else:
        column_type = "Categorical"

    
    # 5. Visualization Rendering
    
    st.subheader("Visualization")

    if column_type == "Numerical":

        # Remove missing values
        plot_data = df[selected_column].dropna()

        fig, ax = plt.subplots(figsize=(8, 5))

        sns.histplot(
            plot_data,
            bins=20,
            ax=ax
        )

        ax.set_xlabel(selected_column)
        ax.set_ylabel("Frequency")
        ax.set_title(f"Distribution of {selected_column}")

        st.pyplot(fig)

    else:

        fig, ax = plt.subplots(figsize=(8, 5))

        sns.countplot(
            x=selected_column,
            data=df,
            ax=ax
        )

        ax.set_xlabel(selected_column)
        ax.set_ylabel("Count")
        ax.set_title(f"Count of {selected_column}")

        plt.xticks(rotation=45)

        st.pyplot(fig)    

else:
    st.info("Please upload a CSV file to start EDA.")

