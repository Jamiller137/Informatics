# Both round the same way
print(round(1.235, 2))     # → 1.23 (rounds down to even)
print(f"{1.235:.2f}")      # → "1.23" (same)

print(round(1.245, 2))     # → 1.25 (rounds up to even) 
print(f"{1.245:.2f}")      # → "1.25" (same)

print(round(1.236, 2))     # → 1.24 (clear round up)
print(f"{1.236:.2f}")      # → "1.24" (same)
