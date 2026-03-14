# Task 1: Floating-point arithmetic
# In Python, floating-point arithmetic can lead to unexpected results due to the way numbers are represented in memory. This is a common issue in many programming languages. Let's see an example:

print(0.1 + 0.2 - 0.3)

x = 0.1 + 0.2 - 0.3
print(x)

# The output of the above code will not be 0, but a very small number close to zero (like 5.551115123125783e-17). This is because 0.1, 0.2, and 0.3 cannot be represented exactly in binary floating-point format, leading to precision errors.