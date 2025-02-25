import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Data
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

file_path = "processed_ssh_logs.csv"
df = load_data(file_path)

st.title("☠️ SSH Attack Analysis Dashboard")

# --- Top Attacking IPs ---
st.subheader("☠️ Top Attacking IPs")
top_ips = df["IP"].value_counts().head(10)
if not top_ips.empty:
    fig, ax = plt.subplots()
    top_ips.plot(kind="bar", ax=ax, color='red')
    ax.set_ylabel("Attack Count")
    ax.set_xlabel("IP Address")
    st.pyplot(fig)
else:
    st.write("No data available for attacking IPs.")

# --- Most Tested Usernames ---
st.subheader("Most Tested Usernames")
top_users = df["Username"].value_counts().head(10)
if not top_users.empty:
    fig, ax = plt.subplots()
    top_users.plot(kind="bar", ax=ax, color='blue')
    ax.set_ylabel("Attempt Count")
    ax.set_xlabel("Username")
    st.pyplot(fig)
else:
    st.write("No data available for tested usernames.")

st.success("Dashboard Loaded Successfully")

