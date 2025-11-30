import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")
st.title("Forecast Results Dashboard")

uploaded_file = st.file_uploader("Choose an Excel file with forecast data", type=["xlsx", "xls"])

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file, engine='openpyxl')
        st.success("File uploaded successfully!")

        st.write("### Raw Data Preview:")
        st.dataframe(df.head())

        st.write("### Full Data:")
        st.dataframe(df)

        # Attempt to find suitable columns for plotting
        numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
        if numeric_cols:
            st.write("### Forecast Visualization:")
            selected_column = st.selectbox("Select a numerical column to visualize", numeric_cols)

            if selected_column:
                fig, ax = plt.subplots(figsize=(10, 5))
                sns.lineplot(data=df, y=selected_column, ax=ax)
                ax.set_title(f"Trend of {selected_column}")
                ax.set_xlabel("Index")
                ax.set_ylabel(selected_column)
                st.pyplot(fig)
        else:
            st.info("No numerical columns found in the uploaded file for plotting.")

    except Exception as e:
        st.error(f"Error reading file or processing data: {e}")
else:
    st.info("Please upload an Excel file to get started.")
