# Creating a hypothetical dataset for the system potential over time
system_data = {
    "Time (ms)": [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300],
    "Potential Near Stress Site (mV)": [0, 5, 10, 20, 25, 20, 15, 10, 5, 2, 0],
    "Potential Far from Stress Site (mV)": [0, 1, 2, 5, 10, 8, 6, 4, 2, 1, 0]
}

system_df = pd.DataFrame(system_data)

# Plotting the graph for system potential
plt.figure(figsize=(10, 6))
plt.plot(system_df["Time (ms)"], system_df["Potential Near Stress Site (mV)"], marker='o', color='blue', label='Near Stress Site')
plt.plot(system_df["Time (ms)"], system_df["Potential Far from Stress Site (mV)"], marker='x', color='red', label='Far from Stress Site')
plt.title('System Potential Changes Over Time in Response to Stress')
plt.xlabel('Time (ms)')
plt.ylabel('Potential (mV)')
plt.legend()
plt.grid(True)
plt.show()
