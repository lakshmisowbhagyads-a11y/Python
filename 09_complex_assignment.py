# COMPLEX DATATYPE ASSIGNMENT
# ==========================

# SOLVED EXAMPLE
# --------------
# Question: Create a complex number and find its conjugate
print("SOLVED EXAMPLE:")
print("Create a complex number and find its conjugate")
z = 3 + 4j
conjugate = z.conjugate()
magnitude = abs(z)
print(f"Complex number: {z}")
print(f"Conjugate: {conjugate}")
print(f"Magnitude: {magnitude}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Create complex number 5 + 3j
z1 = 5 + 3j
print("Complex number:", z1)

# Question 2: Find the real part of complex number 7 - 2j
z2 = 7 - 2j
print("Real part:", z2.real)

# Question 3: Find the imaginary part of complex number 4 + 6j
z3 = 4 + 6j
print("Imaginary part:", z3.imag)

# Question 4: Add two complex numbers: (3 + 2j) and (1 + 4j)
z4a = 3 + 2j
z4b = 1 + 4j
print("Addition:", z4a + z4b)

# Question 5: Multiply two complex numbers: (2 + 3j) and (1 + 2j)
z5a = 2 + 3j
z5b = 1 + 2j
print("Multiplication:", z5a * z5b)

# Question 6: Find the magnitude of complex number 6 + 8j
z6 = 6 + 8j
print("Magnitude:", abs(z6))

# Question 7: Find the conjugate of complex number 5 - 7j
z7 = 5 - 7j
print("Conjugate:", z7.conjugate())

# Question 8: Subtract complex numbers: (10 + 5j) - (3 + 2j)
z8a = 10 + 5j
z8b = 3 + 2j
print("Subtraction:", z8a - z8b)

# Question 9: Divide complex numbers: (8 + 6j) / (2 + 1j)
z9a = 8 + 6j
z9b = 2 + 1j
print("Division:", z9a / z9b)
