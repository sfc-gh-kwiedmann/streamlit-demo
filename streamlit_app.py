import streamlit as st
import os

st.set_page_config(page_title="Streamlit CI/CD Demo", layout="wide")

env = os.getenv("STREAMLIT_ENV", "unknown")

st.title("Streamlit CI/CD Demo")
st.subheader(f"Environment: {env}")

conn = st.connection("snowflake")

df = conn.query("""
    SELECT
        CURRENT_USER() AS user_name,
        CURRENT_ROLE() AS role_name,
        CURRENT_DATABASE() AS database_name,
        CURRENT_SCHEMA() AS schema_name,
        CURRENT_WAREHOUSE() AS warehouse_name
""")

st.dataframe(df, use_container_width=True)
st.success(f"App deployed successfully to {env}!")
