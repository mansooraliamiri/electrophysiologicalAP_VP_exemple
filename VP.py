import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Hypothetical dataset for the variation potential over time
variation_data = {
    "Time (ms)": [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300],
    "Membrane Potential (mV)": [-70, -65, -60, -50, -40, -45, -50, -60, -65, -68, -70]
}

# Convert to DataFrame
variation_df = pd.DataFrame(variation_data)

# Convert time to seconds and membrane potential to Volts for calculation
time_s = np.array(variation_df["Time (ms)"]) / 1000  # convert ms to s
membrane_potential_V = np.array(variation_df["Membrane Potential (mV)"]) / 1000  # convert mV to V

# Assume a membrane capacitance (Cm) value - this is a hypothetical value
Cm = 1e-6  # Farads (F)

# Calculate dV/dt
dV_dt = np.diff(membrane_potential_V) / np.diff(time_s)

# Plotting the graph for variation potential
plt.figure(figsize=(12, 10))

# Plot for Membrane Potential
plt.subplot(2, 1, 1)  # 2 rows, 1 column, 1st subplot
plt.plot(variation_df["Time (ms)"], variation_df["Membrane Potential (mV)"], marker='o', color='purple')
plt.title('Variation in Membrane Potential Over Time in Response to Stress')
plt.xlabel('Time (ms)')
plt.ylabel('Membrane Potential (mV)')
plt.axhline(y=-70, color='g', linestyle='--', label='Resting Potential (-70 mV)')
plt.legend()
plt.grid(True)

# Plot for dV/dt
plt.subplot(2, 1, 2)  # 2 rows, 1 column, 2nd subplot
plt.plot(variation_df["Time (ms)"][:-1], dV_dt, marker='o', color='orange')  # Exclude the last time point
plt.title('Rate of Change of Membrane Potential Over Time')
plt.xlabel('Time (ms)')
plt.ylabel('dV/dt (V/s)')
plt.grid(True)

plt.tight_layout()
plt.show()
