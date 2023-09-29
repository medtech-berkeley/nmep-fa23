"""
IMPORT STATEMENTS?
What do we need to import and how should we import it?
"""
import numpy as np
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt

"""
Calculate the sum of all even numbers from 1 to 100 and store the result in a variable called even_sum.
"""
def q1():
    even_sum = 0

    for number in range(2, 101, 2):
        even_sum += number
    return even_sum

"""
Given the following list of data points: [12, 15, 18, 21, 24], create a numpy array and calculate the mean, median, and standard deviation of these values. Store the results in separate variables.
"""
def q2():
    data_array = np.array([12, 15, 18, 21, 24])

    mean_value = np.mean(data_array)
    median_value = np.median(data_array)
    std_deviation = np.std(data_array)
    return mean_value, median_value, std_deviation

"""
Perform matrix multiplication on two numpy arrays: A (2x3 matrix) and B (3x2 matrix). Store the result in a variable called result_matrix.
"""
def q3():
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = np.array([[7, 8], [9, 10], [11, 12]])
    result_matrix = np.dot(A, B)
    return result_matrix


"""
Generate two random numpy arrays, data1 and data2, each with 100 samples.
Conduct a t-test to compare the means of data1 and data2.
Print the p-value from the t-test.
"""

def q4():
    np.random.seed(42)
    data1 = np.random.randn(100)
    data2 = np.random.randn(100)
    t_statistic, p_value = stats.ttest_ind(data1, data2)
    print(p_value)
    return p_value


"""
1. Create 4 Lists with 5 elements in each:
Name 
Age 
Gender
Score

2. Create a dictionary from these fours lists
    Create a pandas DataFrame from a dictionary with columns: 'Name', 'Age', 'Gender', 'Score'.

3. Calculate the mean age and the maximum score in the DataFrame.
4. Plot a bar chart showing the count of each gender.
"""
def q5():
    Name = ['Amanda', 'Bob', 'Charlie', 'Dylan', 'Elizabeth']
    Age = [25, 30, 22, 35, 28]
    Gender = ["Female", "Male", "Male", "Male", "Female"]
    Score = [95, 89, 78, 92, 88]

    dict = {
        'Name': Name,
        'Age': Age,
        'Gender': Gender,
        'Score': Score,
    }

    df = pd.DataFrame(dict)

    mean_age = df['Age'].mean()
    max_score = df['Score'].max()

    gender_counts = df['Gender'].value_counts()

    plt.figure(figsize=(8, 6))
    gender_counts.plot(kind='bar', color='skyblue')
    plt.xlabel("Gender")
    plt.ylabel("Count")
    plt.show()


    return


"""
Load a dataset (students.csv) into a pandas DataFrame.
Conduct a hypothesis test to compare a numerical variable between two or more groups in the dataset.
Use matplotlib to create appropriate visualizations (e.g., box plot, histogram) to represent the data.
Provide a summary of the hypothesis test results and your visualizations, explaining any insights gained from the analysis.
"""

def q6():
    df = pd.read_csv('students.csv')
    num_variable = df["Score"]
    grp_variable = df["Gender"]


    f_statistic, p_value = stats.f_oneway(*[num_variable[df["Gender"] == group] for group in grp_variable.unique()])

    plt.figure(figsize=(10, 6))

    df.boxplot(column="Score", by="Gender", grid=False)
    plt.title("Box Plot of Scores by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Score")
    plt.show()

    if p_value < 0.05:
        print("Reject the null hypothesis")
    else:
        print("Fail to reject the null hypothesis")

    return p_value

def main():
    q1()
    q2()
    q3()
    q4()
    q5()
    q6()

if __name__ == "__main__":
    main()