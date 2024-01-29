import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def sodium_current(V):
    """Hypothetical function for sodium ion current."""
    # These values are hypothetical and for demonstration purposes only
    G_Na = 120  # Maximum conductance for sodium (mS/cm^2)
    E_Na = 50   # Reversal potential for sodium (mV)
    return G_Na * (V - E_Na)

def potassium_current(V):
    """Hypothetical function for potassium ion current."""
    # These values are hypothetical and for demonstration purposes only
    G_K = 36    # Maximum conductance for potassium (mS/cm^2)
    E_K = -77   # Reversal potential for potassium (mV)
    return G_K * (V - E_K)

def leak_current(V):
    """Hypothetical function for leak current."""
    # These values are hypothetical and for demonstration purposes only
    G_L = 0.3   # Maximum conductance for leak (mS/cm^2)
    E_L = -54.4 # Reversal potential for leak (mV)
    return G_L * (V - E_L)

def external_current(t):
    """Hypothetical function for external current."""
    # This is a simple placeholder function. In reality, this could be any external influence.
    return 10 if 5 <= t <= 30 else 0  # Applying an external current between 5ms and 30ms

# Membrane capacitance (hypothetical value)
Cm = 1e-6  # Farads (F)

# Time and membrane potential for demonstration
time_ms = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
membrane_potential_mV = [-70, -60, -55, 30, -55, -60, -65, -70, -70, -70, -70]

# Convert membrane potential to Volts
membrane_potential_V = [V / 1000 for V in membrane_potential_mV]  # convert mV to V

# Calculating dV/dt based on the Hodgkin-Huxley formula
dV_dt = []
for i, V in enumerate(membrane_potential_V):
    if i < len(membrane_potential_V) - 1:
        # Calculate total ionic current
        I_ion = sodium_current(V) + potassium_current(V) + leak_current(V)
        # Calculate external current at this time point
        I_ext = external_current(time_ms[i])
        # Hodgkin-Huxley formula
        current_total = -I_ion + I_ext
        # Calculate dV/dt
        dV_dt.append(current_total / Cm)

# Output the calculated dV/dt values
print(dV_dt)

# Plotting both the membrane potential and the rate of change of membrane potential in a graph

plt.figure(figsize=(12, 10))

# Plot for Membrane Potential
plt.subplot(3, 1, 1)  # 2 rows, 1 column, 1st subplot
#plt.plot(time_ms, membrane_potential_mV, marker='o', color='blue')
#plt.axhline(y=-55, color='r', linestyle='--', label='Threshold Potential (-55 mV)')
#plt.axhline(y=-70, color='g', linestyle='--', label='Resting Potential (-70 mV)')
#plt.title('Membrane Potential Changes Over Time')
#plt.xlabel('Time (ms)')
#plt.ylabel('Membrane Potential (mV)')

plt.plot(time_ms, membrane_potential_mV, marker='o', color='blue')
plt.title('Membrane Potential Changes Over Time in Response to Stress')
plt.xlabel('Time (ms)')
plt.ylabel('Membrane Potential (mV)')
plt.axhline(y=-55, color='r', linestyle='--', label='Threshold Potential (-55 mV)')
plt.axhline(y=-70, color='g', linestyle='--', label='Resting Potential (-70 mV)')
plt.legend()
plt.grid(True)

# Plot for dV/dt
plt.subplot(3, 1, 2)  # 2 rows, 1 column, 2nd subplot
plt.plot(time_ms[:-1], dV_dt, marker='o', color='orange')  # Exclude the last time point
plt.title('Rate of Change of Membrane Potential Over Time (dV/dt)')
plt.xlabel('Time (ms)')
plt.ylabel('dV/dt (V/s)')
plt.grid(True)

plt.tight_layout()
#plt.show()


# Continuing from the previous code

# Calculate the absolute value of dV/dt to emphasize both depolarization and repolarization
absolute_dV_dt = np.abs(dV_dt)

# Plotting the graph for absolute dV/dt
#plt.figure(figsize=(12, 6))
plt.subplot(3, 1, 3)  # 3 rows, 1 column, 3nd subplot
# Plot for Absolute dV/dt
plt.plot(time_ms[:-1], absolute_dV_dt, marker='o', color='green')  # Exclude the last time point
plt.title('Absolute Rate of Change of Membrane Potential Over Time (|dV/dt|)')
plt.xlabel('Time (ms)')
plt.ylabel('|dV/dt| (V/s)')
plt.grid(True)

# Highlighting the region where action potential occurs
plt.axvspan(time_ms[2], time_ms[4], color='yellow', alpha=0.3, label='Action Potential Region')
plt.legend()

plt.show()


