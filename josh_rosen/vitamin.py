"""
IMPORT STATEMENTS?
What do we need to import and how should we import it?
"""
import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib_inline
"""
Calculate the sum of all even numbers from 1 to 100 and store the result in a variable called even_sum.
"""
def q1():
    even_sum = sum(np.arange(1,101))
    return even_sum
"""
Given the following list of data points: [12, 15, 18, 21, 24], create a numpy array and calculate the mean, median, and standard deviation of these values. Store the results in separate variables.
"""
def q2():
    arr = [12, 15, 18, 21, 24]
    mean = np.mean(arr)
    std = np.std(arr)
    med = np.median(arr)
    return mean,std,med

"""
Perform matrix multiplication on two numpy arrays: A (2x3 matrix) and B (3x2 matrix). Store the result in a variable called result_matrix.
"""
def q3():
    A = np.array([[1, 2, 3],
              [4, 5, 6]])


    B = np.array([[7, 8],
              [9, 10],
              [11, 12]])
    result_matrix = A @ B
    return result_matrix


"""
Generate two random numpy arrays, data1 and data2, each with 100 samples.
Conduct a t-test to compare the means of data1 and data2.
Print the p-value from the t-test.
"""

def q4():
    data1 = np.random.normal(loc=0, scale=1, size=100)
    data2 = np.random.normal(loc=0.5, scale=1, size=100)    
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
    list_1 = ['josh', 18, 'Male', 95, 170]
    list_2 = ['brian', 20, 'Male', 86, 150]
    list_3 = ['anirud', 21, 'Male', 99, 164]
    list_4 = ['sinan', 17, 'Male', 89, 158]

    data_dict = {
    'Name': [list_1[0], list_2[0], list_3[0], list_4[0]],
    'Age': [list_1[1], list_2[1], list_3[1], list_4[1]],
    'Gender': [list_1[2], list_2[2], list_3[2], list_4[2]],
    'Score': [list_1[3], list_2[3], list_3[3], list_4[3]],
    'Height': [list_1[4], list_2[4], list_3[4], list_4[4]]
    }

    df = pd.DataFrame(data_dict)
    mean_age = df['Age'].mean()
    max_score = df['Score'].max()
    counts = df['Gender'].value_counts()
    plt.barh(counts.index, counts.values)
    plt.xlabel('Gender')
    plt.ylabel('Counts')
    return 


"""
Load a dataset (students.csv) into a pandas DataFrame.
Conduct a hypothesis test to compare a numerical variable between two or more groups in the dataset.
Use matplotlib to create appropriate visualizations (e.g., box plot, histogram) to represent the data.
Provide a summary of the hypothesis test results and your visualizations, explaining any insights gained from the analysis.
"""

def q6():
    df = pd.read_csv('students.csv')
    group_1 = df[df['Gender'] == 'Female']['Score']
    group_2 = df[df['Gender'] == 'Male']['Score']

    plt.figure(figsize=(10, 6))
    plt.subplot(1, 2, 1)
    plt.boxplot([group_1, group_2], labels=['Group1', 'Group2'])
    plt.title('Box Plot')

    plt.subplot(1, 2, 2)
    plt.hist(group_1, alpha=0.5, label='Group1', bins=15)
    plt.hist(group_2, alpha=0.5, label='Group2', bins=15)
    plt.xlabel('Score')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.legend()
    plt.show()
    return

def main():
    q1()
    q2()
    q3()
    q4()
    q5()
    q6()

if __name__ == "__main__":
    main()