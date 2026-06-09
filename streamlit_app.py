import streamlit as st

st.set_page_config(page_title="Streamlit CI/CD Demo", layout="wide")

conn = st.connection("snowflake")

# Derive environment from the database name
db_info = conn.query("SELECT CURRENT_DATABASE() AS db")
db_name = db_info["DB"].iloc[0]

if "DEV" in db_name:
    env = "DEV"
elif "PROD" in db_name:
    env = "PROD"
else:
    env = db_name

st.title("Streamlit CI/CD Demo")
st.subheader(f"Environment: {env}")

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
