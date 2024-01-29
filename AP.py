import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Hypothetical dataset for membrane potential over time (Action Potential)
ap_data = {
    "Time (ms)": [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
    "Membrane Potential (mV)": [-70, -60, -55, 30, -55, -60, -65, -70, -70, -70, -70]
}

# Convert to DataFrame
ap_df = pd.DataFrame(ap_data)

# Convert time to seconds and membrane potential to Volts for calculation
time_s_ap = np.array(ap_df["Time (ms)"]) / 1000  # convert ms to s
membrane_potential_V_ap = np.array(ap_df["Membrane Potential (mV)"]) / 1000  # convert mV to V

# Assume a membrane capacitance (Cm) value - this is a hypothetical value
Cm_ap = 1e-6  # Farads (F)

# Calculate dV/dt for Action Potential
dV_dt_ap = np.diff(membrane_potential_V_ap) / np.diff(time_s_ap)

# Plotting both Variation Potential and Action Potential in one graph
plt.figure(figsize=(12, 10))

# Plot for Action Potential
plt.subplot(2, 1, 1)  # 2 rows, 1 column, 1st subplot
plt.plot(ap_df["Time (ms)"], ap_df["Membrane Potential (mV)"], marker='o', color='blue')
plt.title('Action Potential Changes Over Time')
plt.xlabel('Time (ms)')
plt.ylabel('Membrane Potential (mV)')
plt.axhline(y=-55, color='r', linestyle='--', label='Threshold Potential (-55 mV)')
plt.axhline(y=-70, color='g', linestyle='--', label='Resting Potential (-70 mV)')
plt.legend()
plt.grid(True)

# Plot for Rate of Change of Membrane Potential in Action Potential
plt.subplot(2, 1, 2)  # 2 rows, 1 column, 2nd subplot
plt.plot(ap_df["Time (ms)"][:-1], dV_dt_ap, marker='o', color='red')  # Exclude the last time point
plt.title('Rate of Change of Membrane Potential in Action Potential Over Time')
plt.xlabel('Time (ms)')
plt.ylabel('dV/dt (V/s)')
plt.grid(True)

plt.tight_layout()
plt.show()

dV_dt_ap
