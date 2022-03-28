#%%
# Student ID: 2019-1-60-228
# Student Name: Sherajum Monira Noha
# Lab Assignment - 1
import pandas as pd

df = pd.read_csv('dataset_lab04.csv')
df.info()


# %%
# 1. this cell must be executed before calling the function
def lab04_task1_2019_1_60_228():
    print('Number of rows: ', df.shape[0])
    print('Number of columns: ', df.shape[1])


# %%
# Task 1
lab04_task1_2019_1_60_228()


# %%
# 2. Describe (numerical summary) the time and amount column. Print this information.
def lab04_task2_2019_1_60_228():
    print(df.describe())


# %%
# Task 2
lab04_task2_2019_1_60_228()


# %%

# Task 3

# 3. There are 31 columns in the dataset. Compute some statistical measures like mean, median, standard
# deviation, variance using Pandas Function for at least two columns. Print this information.

def lab04_task3_2019_1_60_228():
    V1 = df[['V1']]
    print("The Mean is: ", V1.mean())
    print("The Median is: ", V1.median())
    print("The Standard Deviation is: ", V1.std())
    print("The Variance is: ", V1.var())

    V7 = df[['V7']]
    print("The Mean is: ", V7.mean())
    print("The Median is: ", V7.median())
    print("The Standard Deviation is: ", V7.std())
    print("The Variance is: ", V7.var())


# %%
# Task 3
lab04_task3_2019_1_60_228()


# %%

# Task 4

# 4. Show the Box Plot of Time and Amount column. Also print the value of Q1, Median, Q3, IQR. Are
# there any outliers? Explain your answer and print it.

def lab04_task4_2019_1_60_228():
    df.boxplot(column=['Time', 'Amount'])
    Time = df[['Time']]
    Amount = df[['Amount']]

    Q1_of_time = Time.quantile(0.25)
    Q3_of_time = Time.quantile(0.75)
    Q1_of_amount = Amount.quantile(0.25)
    Q3_of_amount = Amount.quantile(0.75)

    IQR_amount = Q3_of_amount - Q1_of_amount
    IQR_time = Q3_of_time - Q1_of_time

    UB_time = Q3_of_time + (IQR_time * 1.5)
    LB_time = Q1_of_time - (IQR_time * 1.5)
    UB_amount = Q3_of_amount + (IQR_amount * 1.5)
    LB_amount = Q1_of_amount - (IQR_amount * 1.5)

    max_time = Time.max()
    min_time = Time.min()
    max_amount = Amount.max()
    min_amount = Amount.min()

    if (max_time > UB_time).all() or (min_time < LB_time).all():

        print("There are outliers in time")
    else:
        print('There are no outliers in time')
    if (max_amount > UB_amount).all() or (min_amount < LB_amount).all():
        print("There are outliers in amount")
    else:
        print('There are no outliers in amount')


# %%
# Task 4
lab04_task4_2019_1_60_228()


# %%

# Task 5
# 5. Show the Histogram of Time and Amount column. Print the value of the Skewness and Kurtosis using
# appropriate Pandas functions. Comment on the type of the data distribution and print it.

def lab04_task5_2019_1_60_228():
    df.hist(column=['Time'], bins=5)
    df.hist(column=['Amount'], bins=5)

    Amount = df[['Amount']]
    Time = df[['Time']]
    print("Skewness of time: ", Time.skew())
    print("Kurtosis of time : ", Time.kurt())
    print("Skewness of amount: ", Amount.skew())
    print("Kurtosis of amount: ", Amount.kurt())
    if (Time.skew() > 0).all():
        print('The time histogram is positivly skewed')
    else:
        print('The time histogram is negetivly skewed')

    if (Amount.skew() > 0).all():
        print('The amount histogram is positivly Skewed')
    else:
        print('The amount Histogram is Negetivly Skewed')

    if (Time.kurt() > 3).all():
        print("The time data is leptokurtic cause the kurtosis value is greater than 3")
    elif (Time.kurt()).all == 3:
        print("The time data is mesokurtic cause the kurtosis value is equal to 3")
    else:
        print("The time data is platykurtic cause the kurtosis value is less than 3")

    if (Amount.kurt() > 3).all():
        print("The amount data is leptokurtic cause the kurtosis value is greater than 3")
    elif (Amount.kurt()).all == 3:
        print("The amount data is mesokurtic cause the kurtosis value is equal to 3")
    else:
        print("The amount data is platykurtic cause the kurtosis value is less than 3")


# %%
# Task 5
lab04_task5_2019_1_60_228()


# %%

# Task 6

# 6. Find the percentage of records with class value = 0 (Non-Fraudulent) and class value = 1 (Fraudulent).
# Print this information.

def lab04_task6_2019_1_60_228():
    Class = df[['Class']]

    x = (((df['Class'] == 0).sum()) / (Class.shape[0])) * 100
    print("Zero is ", (x), 'percent in the class')

    y = (((df['Class'] == 1).sum()) / (Class.shape[0])) * 100
    print("One is ", (y), 'percent in the class ')


# %%
# Task 6

lab04_task6_2019_1_60_228()


# %%
# Task 7
# 7. Show the result you have got in 6 using a Histogram.
def lab04_task7_2019_1_60_228():
    Class = df[['Class']]

    Class.hist(column=['Class'], bins=5)


# %%
# Task 7
lab04_task7_2019_1_60_228()


# %%

# Task 8
# 8. Show the result you have got in 6 using a Bar chart. Create the bar chart on the percentage value, not
# on the total number of occurrences.

def lab04_task8_2019_1_60_228():
    Class = df[['Class']]
    a = ((df['Class'] == 1).sum())
    zero = (a / (Class.shape[1]))

    b = ((df['Class'] == 0).sum())
    one = (b / (Class.shape[0]))
    pd.Series([zero, one]).plot(kind="bar")


# %%
# Task 8
lab04_task8_2019_1_60_228()


# %%
# Task 9

# Show the Histrogram (data distribution) of a few other columns (your choice) showing both positive
# and negative skew and also leptokurtic and platykurtic data distribution. So, you should display at least
# four Histograms.

def lab04_task9_2019_1_60_228():
    df.hist(column=['V7'], bins=5)
    df.hist(column=['V10'], bins=5)
    df.hist(column=['V15'], bins=5)
    df.hist(column=['V25'], bins=5)

    V7 = df[['V7']]
    V10 = df[['V10']]
    V15 = df[['V15']]
    V25 = df[['V25']]

    print("Skewness of V7: ", V7.skew())
    print("Kurtosis of V7: ", V7.kurt())
    print("Skewness of V10: ", V10.skew())
    print("Kurtosis of V10: ", V10.kurt())
    print("Skewness of V15: ", V15.skew())
    print("Kurtosis of V15: ", V15.kurt())
    print("Skewness of V25: ", V25.skew())
    print("Kurtosis of V25: ", V25.kurt())

    if (V7.skew() > 0).all():
        print('The V7 Histogram is positivly Skewed')
    else:
        print('The V7 Histogram is Negetivly Skewed')
    if (V7.kurt() > 3).all():
        print("The V7 data is leptokurtic cause the kurtosis value is greater than 3")
    elif (V7.kurt()).all == 3:
        print("The V7 data is mesokurtic cause the kurtosis value is equal to 3")
    else:
        print("The V7 data is platykurtic cause the kurtosis value is less than 3\n")

    if (V10.skew() > 0).all():
        print('The V10 Histogram is positivly Skewed')
    else:
        print('The V10 Histogram is Negetivly Skewed')
    if (V10.kurt() > 3).all():
        print("The V10 data is leptokurtic cause the kurtosis value is greater than 3")
    elif (V10.kurt()).all == 3:
        print("The V10 data is mesokurtic cause the kurtosis value is equal to 3")
    else:
        print("The V10 data is platykurtic cause the kurtosis value is less than 3\n")

    if (V15.skew() > 0).all():
        print('The V15 Histogram is positivly Skewed')
    else:
        print('The V15 Histogram is Negetivly Skewed')
    if (V15.kurt() > 3).all():
        print("The V15 data is leptokurtic cause the kurtosis value is greater than 3")
    elif (V15.kurt()).all == 3:
        print("The V15 data is mesokurtic cause the kurtosis value is equal to 3")
    else:
        print("The V15 data is platykurtic cause the kurtosis value is less than 3\n")

    if (V25.skew() > 0).all():
        print('The V25 Histogram is positivly Skewed')
    else:
        print('The V25 Histogram is Negetivly Skewed')
    if (V25.kurt() > 3).all():
        print("The V25 data is leptokurtic cause the kurtosis value is greater than 3")
    elif (V25.kurt()).all == 3:
        print("The V25 data is mesokurtic cause the kurtosis value is equal to 3")
    else:
        print("The V25 data is platykurtic cause the kurtosis value is less than 3\n")

    # %%


# Task 9
lab04_task9_2019_1_60_228()


# %%
# Task 10

# Find the highest positive correlation among all attributes. While finding the correlation, use appropriate
# code, not manually. Print this information accordingly.

def lab04_task10_2019_1_60_228():
    print("The highest positive correlation among all attributes are: ")
    print(df.corr().max())


# %%
# Task 10
lab04_task10_2019_1_60_228()


# %%

# Task 11

# Support your findings in Question 10 using a Scatter Plot.

def lab04_task11_2019_1_60_228():
    import matplotlib.pyplot as plt
    plt.scatter(x="Time", y="Amount", data=df)
    plt.show()


# %%
# Task 11
lab04_task11_2019_1_60_228()


# %%

# Task 12

# Find the highest negative correlation among all attributes. While finding the correlation, use
# appropriate code, not manually. Print this information accordingly.

def lab04_task12_2019_1_60_228():
    print("The highest negative correlation among all attributes are: ")
    print(df.corr().min())


# %%
# Task 12
lab04_task12_2019_1_60_228()


# %%

# Task 13

# Support your findings in Question 12 using a Scatter Plot.

def lab04_task13_2019_1_60_228():
    import matplotlib.pyplot as plt
    plt.scatter(x="Time", y="Amount", data=df)
    plt.show()


# %%
# Task 13
lab04_task13_2019_1_60_228()


# %%

# Task 14
# Create a Box Plot of the Amount Column.
def lab04_task14_2019_1_60_228():
    df.boxplot(column=['Amount'])


# %%
# Task 14
lab04_task14_2019_1_60_228()


# %%

# Task 15
#  Now create two other box plots side by side. The first one will show the Amount column value for
# which the class value = 0 (Non-Fraudulent) and the second one will show the Amount column value
# for which the class value = 1 (Fraudulent). Do you find any particular pattern by just considering
# Amount column. Explain your answer and print it accordingly.

def lab04_task15_2019_1_60_228_value0():
    x = (df['Class'] == 0)
    Amount_for_value0 = df[x]
    Amount_for_value0.boxplot(column=['Amount'])
    print(Amount_for_value0['Amount'])
    print("It's from exactly zero")
    # %%


# Task 15
lab04_task15_2019_1_60_228_value0()


# %%
def lab04_task15_2019_1_60_228_value1():
    y = (df['Class'] == 1)
    Amount_for_value1 = df[y]
    Amount_for_value1.boxplot(column=['Amount'])
    print(Amount_for_value1['Amount'])
    print("It's from above the zero")


# %%
lab04_task15_2019_1_60_228_value1()