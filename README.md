# Data Range Calculator (AI Foundations)

This project contains a Python implementation of a **Range Calculation** function. It was developed as part of my Artificial Intelligence studies to understand basic data dispersion and pre-processing.

## 📝 Description
The "Range" (Amplitude) is the difference between the maximum and minimum values in a dataset. In AI and Statistics, this is a fundamental step to understand data variability before feeding it into machine learning models.

The script manually iterates through data arrays to find the extremes without relying on built-in library shortcuts, demonstrating core algorithmic logic.

## 🚀 How it Works
The function `calculate_range` (originally `calcular_amplitude`) follows these steps:
1. Initialize `max` and `min` variables with the first element of the array.
2. Iterate through the list, updating the extremes.
3. Return the difference: $Range = Max - Min$.

## 💻 Code Example
```python
# Example of usage with financial data
food_expenses = [320.00, 450.00, 390.00, 510.00, 280.00]
print(f"Range: {calculate_range(food_expenses)}")
