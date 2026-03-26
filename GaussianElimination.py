import numpy as np

# Augmented matrix [A|b] voor het stelsel:
#   2x +  y - z =  8
#  -3x - y + 2z = -11
#  -2x + y + 2z = -3

augmented = np.array([
    [ 2,  1, -1,   8],
    [-3, -1,  2, -11],
    [-2,  1,  2,  -3],
], dtype=float)

n = len(augmented)

# Voorwaartse eliminatie
for col in range(n):
    # Gedeeltelijk pivoting: wissel rij met grootste pivot naar boven
    max_row = np.argmax(np.abs(augmented[col:, col])) + col
    augmented[[col, max_row]] = augmented[[max_row, col]]

    for row in range(col + 1, n):
        factor = augmented[row, col] / augmented[col, col]
        augmented[row] = augmented[row] - factor * augmented[col]

# Terug-substitutie
oplossing = np.zeros(n)
for i in range(n - 1, -1, -1):
    oplossing[i] = (augmented[i, -1] - np.dot(augmented[i, i+1:n], oplossing[i+1:])) / augmented[i, i]

variabelen = ["x", "y", "z"]

print("Oplossing:")
for var, waarde in zip(variabelen, oplossing):
    print(f"  {var} = {waarde:.4f}")

print(f"\nSnijpunt: ({oplossing[0]:.4f}, {oplossing[1]:.4f}, {oplossing[2]:.4f})")
