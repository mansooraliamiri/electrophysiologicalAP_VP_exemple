import pandas as pd
import matplotlib.pyplot as plt

# Creating a hypothetical dataset for membrane potential over time
data = {
    "Time (ms)": [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
    "Membrane Potential (mV)": [-70, -60, -55, 30, -55, -60, -65, -70, -70, -70, -70]
}

df = pd.DataFrame(data)

# Plotting the graph
plt.figure(figsize=(10, 6))
plt.plot(df["Time (ms)"], df["Membrane Potential (mV)"], marker='o')
plt.title('Membrane Potential Changes Over Time in Response to Stress')
plt.xlabel('Time (ms)')
plt.ylabel('Membrane Potential (mV)')
plt.axhline(y=-55, color='r', linestyle='--', label='Threshold Potential (-55 mV)')
plt.axhline(y=-70, color='g', linestyle='--', label='Resting Potential (-70 mV)')
plt.legend()
plt.grid(True)
plt.show()
