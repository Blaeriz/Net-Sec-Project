import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("dark_background")

# Load Data
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

file_path = "processed_ssh_logs.csv"
df = load_data(file_path)

st.title("☠️ SSH Attack Analysis Dashboard")

top_ips = df["IP"].value_counts().head(10)

st.divider()

ip_container = st.container(border=True)

# --- Top Attacking IPs ---
ip_container.header("☠️ Top Attacking IPs")

# if not top_ips.empty:
#     # Create a larger figure for better visibility
#     fig, ax = plt.subplots(figsize=(10, 5))

#     # Plot data with better aesthetics
#     top_ips.plot(
#         kind="bar", 
#         ax=ax, 
#         color="#E84855",  # Soft red
#         edgecolor="black",  # Black edges for contrast
#         linewidth=1
#     )

#     # Improve labels and title
#     ax.set_title(f"Top {len(top_ips)} Attack Source IPs", fontsize=14, fontweight="bold")
#     ax.set_ylabel("Attack Count", fontsize=12)
#     ax.set_xlabel("IP Address", fontsize=12)

#     # Rotate x-axis labels for better readability
#     ax.tick_params(axis="x", rotation=45)

#     # Add grid lines for clarity
#     ax.grid(axis="y", linestyle="--", alpha=0.7)

#     # Optimize layout
#     plt.tight_layout()

#     # Display the figure in Streamlit
#     st.pyplot(fig)
# else:
#     # Display a message when no data is available
#     st.warning("No data available for attacking IPs.")

ip_container.bar_chart(top_ips, horizontal=True, x_label="Frequency", y_label="IPs", color="#E84855", height=500)

st.divider()

user_container = st.container(border=True)
# --- Most Tested Usernames ---
user_container.header("Most Tested Usernames")
top_users = df["Username"].value_counts().head(10)
# if not top_users.empty:
#     fig, ax = plt.subplots(figsize=(10, 5))
#     top_users.plot(
#         kind="bar", 
#         ax=ax, 
#         color="#084887",  # Soft blue
#         edgecolor="black",  # Black edges for contrast
#         linewidth=1
#     )

#     # Improve labels and title
#     ax.set_title(f"Top {len(top_users)} Most Tested Usernames", fontsize=14, fontweight="bold")
#     ax.set_ylabel("Attempt Count", fontsize=12)
#     ax.set_xlabel("Username", fontsize=12)

#     # Rotate x-axis labels for better readability
#     ax.tick_params(axis="x", rotation=45)

#     # Add grid lines for clarity
#     ax.grid(axis="y", linestyle="--", alpha=0.7)

#     # Optimize layout
#     plt.tight_layout()

#     # Display the figure in Streamlit
#     st.pyplot(fig)
# else:
#     st.write("No data available for tested usernames.")
user_container.bar_chart(top_users, horizontal=True, x_label="Frequency", y_label="Usernames", color="#084887", height=500)

st.success("Dashboard Loaded Successfully")


