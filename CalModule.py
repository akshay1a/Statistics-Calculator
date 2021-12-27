import scipy.stats as st
import pandas as pd
import statistics


# def main():
#     def switch(op):
#         mydict = {
#             1: Central_Tendency(),
#             2: t_test_for_single_mean(),
#             3: T_Test_for_difference_of_two_means(),
#             4: F_test(),
#             5: Sample_Mean(),
#             6: Sample_Standard_deviation(),
#             7: Sample_Variance(),
#             8: Sample_Proportion(),
#             9: Sample_Populations_Means(),
#             10: Sample_Standard_Deviations(),
#             11: Sample_proportions(),
#             12: Confidence_limits_for_a_normal_mean(),
#             13: UnknownVariance(),
#             14: Confidence_limits_for_standard_deviation(),
#             15: Confidence_limits_for_Diff_of_populations_means()
#         }
#         return mydict.get(op, 'Thank You! Have a Good Day!')
#
#     print('''^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\n
#             Central tendency:
#             \t1.	Mean, median, mode, Standard deviation and Variance
#             Hypothesis testing:
#             \t2.	t-test for single mean
#             \t3.	t-test for difference of two means
#             \t4.	F-test for equality of population variances
#             \t5.	Sample Mean
#             \t6.	Sample Standard Deviation
#             \t7.	Sample Variance
#             \t8.	Sample Proportion
#             \t9.	Difference of two independent sample means
#             \t10.	Difference of two independent sample standard deviations
#             \t11.	Difference of two independent sample proportions
#             Interval Estimation
#             \t12.	Confidence interval for a normal mean
#             \t13.	Confidence interval for a normal mean when the variance is unknown
#             \t14.	Confidence limits for standard deviation
#             \t15.	Confidence limits for difference of population means
#             EXIT:
#             \tAny Other Key To Close The Program!
#         ''')
#     a = int(input('Choose a number to perform the calculations!  -->  '))
#     print('\n', switch(a))
def Central_Tendency():
    print('Central_Tendency')
    n = int(input("Enter the frequency number : "))
    Frequency = []
    print("enter the values:")
    for i in range(0, n):
        s = float(input())
        Frequency.append(s)

    dic = {'Frequency': Frequency}
    df = pd.DataFrame(dic)

    print("Mean = ", (statistics.mean(df['Frequency'])))

    print("Median = ", (statistics.median(df['Frequency'])))

    print("Mode = ", (statistics.mode(df['Frequency'])))

    print("Standard Deviation = ", (statistics.stdev(df['Frequency'])))

    print("Variance = ", (statistics.variance(df['Frequency'])))


def T_test_for_single_mean():
    print('T_test_for_single_mean\n')
    level_of_significance = int(input("Enter the level of significance "))
    level_of_significance = level_of_significance / 100

    critical_value = st.t.ppf(1 - (level_of_significance / 2), df=int(input("Enter the value of df ")))
    print("Critical Value = ", critical_value)
    μ = int(input("Enter the value of μ =  "))

    # taking the given inputs from user and making a csv
    n1 = int(input("Enter no. of elements: "))
    X = []
    print("enter the values:")
    for i in range(0, n1):
        a = float(input())
        X.append(a)

    dic = {'X': X}
    df = pd.DataFrame(dic)

    x̄ = sum(df['X']) / n1
    print("x̄ = ", x̄)  # mean printing

    df['(x-x̄)'] = df['X'] - x̄
    df['(x-x̄)²'] = df['(x-x̄)'] ** 2

    n2 = sum(df['(x-x̄)²'])
    print("\nΣ(x-x̄)² = ", n2)

    s = (1 / n1 * n2) ** (1 / 2)
    print("Sample Variance = ", s)

    t = (x̄ - μ) / (s / (n1 ** (1 / 2)))
    print("Calculated Value = ", t)

    if t < critical_value:
        print("Ho is Accepted\n")

    else:
        print("Ho is Rejected\n")

    print("Statistical Data Generated during the question\n", df)
    s = input("Save data to csv: Y/N? ")

    if s == 'Y':
        loc = input(
            "Enter the location where you want to save the file!\nExample: C:/Users/akshay/Desktop/\nLocation:  ")
        file = input("Give your file a name!\nExample: data.xlsx, stats.xlsx\n FileName: ")
        save = loc + file
        df.to_excel(save, index=False)
        #
        print("Thank you for using this Calculator!")
    else:
        print("Thanks!")


def T_Test_difference_2means():
    print("T - Test for difference of two means\n")
    level_of_significance = int(input("Enter the level of significance "))
    level_of_significance = level_of_significance / 100

    critical_value = st.t.ppf(1 - (level_of_significance / 2), df=int(input("Enter the value of df ")))
    print("Critical Value = ", critical_value)

    print("Test for difference of two means")
    print("Sample 1")
    n1 = int(input("Enter the value of n1 "))
    x̄1 = int(input("Enter the value of x̄1 "))
    s1 = int(input("Enter the value of s1 "))

    print("Sample 2")
    n2 = int(input("Enter the value of n2 "))
    x̄2 = int(input("Enter the value of x̄2 "))
    s2 = int(input("Enter the value of s2 "))

    (S) = 1 / (n1 + n2 - 2) * ((n1 * s1 ** 2) + (n2 * s2 ** 2))
    print(S)

    if S < critical_value:
        print("T calculated value is less than T Critical value. Therefore H0 is Accepted.")

    else:
        print("T Calculated value is greater than T Critical value. Therefore H0 is rejected")


def F_test():
    print('F_test\n')
    list1 = int(input("Enter no. of elements: "))
    X = []
    print("enter the values:")
    for i in range(0, list1):
        a = float(input())
        X.append(a)

    list2 = int(input("Enter no. of elements: "))
    Y = []
    print("enter the values:")
    for i in range(0, list2):
        b = float(input())
        Y.append(b)

    dic = {'X': X, 'Y': Y}
    data = pd.DataFrame(dic)

    n1 = len(data['X'])
    print("n1 : ", n1)
    x̄ = sum(data['X']) / n1
    print("x̄ : ", x̄)
    n2 = len(data['Y'])
    print("n2 : ", n2)
    Ȳ = sum(data['Y']) / n2
    print("Ȳ : ", Ȳ)
    data['X - x̄'] = data['X'] - x̄
    data['Y - Ȳ'] = data['Y'] - Ȳ
    # print(data)
    data['X - x̄²'] = data['X - x̄'] ** 2
    # print(data)
    sum_ = sum(data['X - x̄²'])
    print("sum_ : ", sum_)
    data['Y - Ȳ²'] = data['Y - Ȳ'] ** 2
    # print(data)
    sum_2 = sum(data['Y - Ȳ²'])
    print("sum_2 : ", sum_2)
    Standard_deviation_square_one = (1 / (n1 - 1)) * sum_
    print("Standard_deviation_square_one : ", Standard_deviation_square_one)
    Standard_deviation_square_two = (1 / (n2 - 1)) * sum_2
    print("Standard_deviation_square_two : ", Standard_deviation_square_two)
    F_test1 = Standard_deviation_square_one / Standard_deviation_square_two
    print("F - Test = ", F_test1)

    print("Statistical Data Generated during the question\n", data)
    s = input("Save data to csv: Y/N? ")

    if s == 'Y':
        loc = input(
            "Enter the location where you want to save the file!\nExample: C:/Users/akshay/Desktop/\nLocation:  ")
        file = input("Give your file a name!\nExample: data.xlsx, stats.xlsx\n FileName: ")
        save = loc + file
        data.to_excel(save, index=False)
        print("Thank you for using this Calculator!")

    # print("Thank you for using this Calculator!")
    else:
        print("Thanks!")


def Sample_Mean():
    print('Sample_Mean')
    σ = int(input("Enter the value of σ "))
    n = int(input("Enter the value of n "))

    Sample_Mean_x̄ = σ / (n ** (1 / 2))
    print("Sample mean = ", Sample_Mean_x̄)


def Sample_Standard_deviation():
    print('Sample_Standard_deviation\n')
    σ = int(input("Enter the value of σ "))
    n = int(input("Enter the value of n "))

    Sample_Standard_deviation_S = ((σ / 2 * n) ** (1 / 2))
    print(("Sample Standard Deviation = ", Sample_Standard_deviation_S))


def Sample_Variance():
    print('Sample_Variance')
    σ = int(input("Enter the value of σ "))
    n = int(input("Enter the value of n "))

    Sample_Variance_s2 = σ ** 2 * (2 / n ** (1 / 2))
    print("Sample Variance = ", Sample_Variance_s2)


def Sample_Proportion():
    print("Sample Proportion\n")
    level_of_significance = int(input("Enter the level of significance "))
    level_of_significance = level_of_significance / 100

    critical_value = st.norm.ppf(1 - (level_of_significance / 2))
    # print("Critical Value = ", critical_value)

    z1 = critical_value
    print("Z Critical Value", z1)

    n = int(input("Enter the value of n "))
    x = int(input("Enter the value of x "))
    p = (x / n)
    print("p", p)
    p0 = int(input("Enter the percentage of p0 "))
    print("p0", p0 / 100)
    Q = 1 - p0
    z2 = p - p0 / ((p * Q / n) ** (1 / 2))
    print("Z", z2)

    if z2 < z1:
        print("Z calculated value is less than Z Critical value. Therefore H0 is Accepted.")

    else:
        print("Z Calculated value is greater than Z Critical value. Therefore H0 is rejected")


def Sample_Populations_Means():
    print("Sample Populations Means\n")
    level_of_significance = int(input("Enter the level of significance "))
    level_of_significance = level_of_significance / 100

    critical_value = st.norm.ppf(1 - (level_of_significance / 2))
    # print("Critical Value = ", critical_value)

    z1 = critical_value
    print("Z Critical Value", z1)

    print("Country A")
    Mean_height_x̄1 = float(input("Enter the value of x̄1 "))
    Standard_Deviation_s1 = float(input("Enter the value of s1 "))
    Number_in_samples_n1 = int(input("Enter the value of n1 "))

    print("Country B")
    Mean_height_x̄2 = float(input("Enter the value of x̄2 "))
    Standard_Deviation_s2 = float(input("Enter the value of s2 "))
    Number_in_samples_n2 = int(input("Enter the value of n2 "))

    z2 = (Mean_height_x̄1 - Mean_height_x̄2) / (
            Standard_Deviation_s1 ** 2 / Number_in_samples_n1 + Standard_Deviation_s2 ** 2 / Number_in_samples_n2) ** (
                 1 / 2)
    print("Z = ", z2)

    if z2 < z1:
        print("Z calculated value is less than Z Critical value. Therefore H0 is Accepted.")

    else:
        print("Z Calculated value is greater than Z Critical value. Therefore H0 is rejected")


def Sample_Standard_Deviations():
    print('Sample_Standard_Deviations\n')
    level_of_significance = int(input("Enter the level of significance "))
    level_of_significance = level_of_significance / 100

    critical_value = st.norm.ppf(1 - (level_of_significance / 2))
    # print("Critical Value = ", critical_value)

    z1 = critical_value
    print("Z Critical Value", z1)

    print("Country A")
    Standard_Deviation_s1 = float(input("Enter the value of s1 "))
    Number_in_samples_n1 = int(input("Enter the value of n1 "))

    print("Country B")
    Standard_Deviation_s2 = float(input("Enter the value of s2 "))
    Number_in_samples_n2 = int(input("Enter the value of n2 "))

    z2 = (Standard_Deviation_s1 - Standard_Deviation_s2) / (
            (Standard_Deviation_s1 ** 2) / (2 * Number_in_samples_n1) + (Standard_Deviation_s2 ** 2) / (
            2 * Number_in_samples_n2)) ** (1 / 2)
    print("Z = ", z2)

    if z2 < z1:
        print("Z calculated value is less than Z Critical value. Therefore H0 is Accepted.")

    else:
        print("Z Calculated value is greater than Z Critical value. Therefore H0 is rejected")


def Sample_proportions():
    print("Sample proportions\n")
    n1 = int(input("Enter the value of n1 "))
    n2 = int(input("Enter the value of n2 "))
    p1 = int(input("Enter the percentage of p0 "))
    print("p1", p1 / 100)
    p2 = int(input("Enter the percentage of p0 "))
    print("p2", p2 / 100)
    Q1 = 1 - p1
    print("Q1", Q1)
    Q2 = 1 - p2
    print("Q2", Q2)

    Z = p1 - p2 / (p1 * Q1) / n1 + (p2 * Q2) / n2 ** (1 / 2)
    print("Z2", Z)


def Con_limits_for_normal_mean():
    print("Confidence limits for a normal mean\n")
    x̄ = float(input("Enter tha value of x ̄"))
    σ = int(input("Enter the value of σ "))
    n = int(input("Enter the value of n "))
    level_of_significance = int(input("Enter the level of significance "))
    level_of_significance = level_of_significance / 100
    critical_value = st.norm.ppf(1 - (level_of_significance / 2))
    print("Critical Value = ", critical_value)
    Z = critical_value
    print("For 95% confidence limits,  Zα/2 = ", critical_value)

    normal_mean = x̄ - Z * σ / (n ** (1 / 2))
    print(normal_mean)
    normal_mean2 = x̄ + Z * σ / (n ** (1 / 2))
    print(normal_mean2)
    print(normal_mean, ",", normal_mean2)


def UnknownVariance():
    print('UnknownVariance\n')
    level_of_significance = int(input("Enter the level of significance "))
    level_of_significance = level_of_significance / 100

    critical_value = st.t.ppf(1 - (level_of_significance / 2), df=int(input("Enter the value of df ")))
    print("Critical Value = ", critical_value)

    t = critical_value

    x̄ = float(input("Enter tha value of x ̄"))
    s = int(input("Enter the value of s "))
    n = int(input("Enter the value of n "))

    VUM = x̄ - t * s / (n ** (1 / 2))
    print(VUM)
    VUM2 = x̄ - t * s / (n ** (1 / 2))
    print(VUM2)
    print(VUM, ",", VUM2)


def Con_limits_for_std():
    print("Confidence limits for standard deviation")
    Std = float(input("Enter the value of Standard Deviation "))
    n = int(input("Enter the value of n "))
    level_of_significance = int(input("Enter the level of significance "))
    level_of_significance = level_of_significance / 100
    critical_value = st.norm.ppf(1 - (level_of_significance / 2))
    print("Critical Value = ", critical_value)
    Z = critical_value
    print("For 95% confidence limits,  Zα/2 = ", critical_value)

    Interval_Standard_Deviation = Std - Z * ((Std ** 2 / (2 * n)) ** (1 / 2))
    print(Interval_Standard_Deviation)

    Interval_Standard_Deviation2 = Std + Z * ((Std ** 2 / (2 * n)) ** (1 / 2))
    print(Interval_Standard_Deviation2)
    print(Interval_Standard_Deviation, ",", Interval_Standard_Deviation2)


def Diff_populations_means_Con_limits():
    level_of_significance = int(input("Enter the level of significance "))
    level_of_significance = level_of_significance / 100

    critical_value = st.norm.ppf(1 - (level_of_significance / 2))
    print("Critical Value = ", critical_value)
    Z = critical_value
    print("For 95% confidence limits,  Zα/2 = ", critical_value)

    print("Sample 1 ")
    n1 = int(input("Enter the value of n1 "))
    Mean_1 = int(input("Enter the value of Mean_1 "))
    Std_1 = float(input("Enter the value of Std_1 "))

    print("Sample 2 ")
    n2 = int(input("Enter the value of n2 "))
    Mean_2 = int(input("Enter the value of Mean_2 "))
    Std_2 = float(input("Enter the value of Std_2 "))

    print("Confidence limits for difference of population means ")
    Interval_Population_Mean = (Mean_1 - Mean_2) + Z * (Std_1 / n1 + Std_2 / n2 ** (1 / 2))
    print(Interval_Population_Mean)

    Interval_Population_Mean2 = (Mean_1 - Mean_2) - Z * (Std_1 / n1 + Std_2 / n2 ** (1 / 2))
    print(Interval_Population_Mean2)
    print(Interval_Population_Mean, ",", Interval_Population_Mean2)


def main():
    print('''^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\n
               Central tendency:
               \t1.	Mean, median, mode, Standard deviation and Variance
               Hypothesis testing:
               \t2.	t-test for single mean
               \t3.	t-test for difference of two means
               \t4.	F-test for equality of population variances
               \t5.	Sample Mean
               \t6.	Sample Standard Deviation
               \t7.	Sample Variance
               \t8.	Sample Proportion
               \t9.	Difference of two independent sample means
               \t10.	Difference of two independent sample standard deviations
               \t11.	Difference of two independent sample proportions
               Interval Estimation
               \t12.	Confidence interval for a normal mean
               \t13.	Confidence interval for a normal mean when the variance is unknown
               \t14.	Confidence limits for standard deviation
               \t15.	Confidence limits for difference of population means
               EXIT:
               \tAny Other Key To Close The Program!
           ''')
    a = int(input('Choose a number to perform the calculations!  -->  '))
    # print('\n', switch(a))
    while a != 0 and a < 16:
        if a == 1:
            Central_Tendency()
            main()
        elif a == 2:
            T_test_for_single_mean()
            main()
        elif a == 3:
            T_Test_difference_2means()
            main()
        elif a == 4:
            F_test()
            main()
        elif a == 5:
            Sample_Mean()
            main()
        elif a == 6:
            Sample_Standard_deviation()
            main()
        elif a == 7:
            Sample_Variance()
            main()
        elif a == 8:
            Sample_Proportion()
            main()
        elif a == 9:
            Sample_Populations_Means()
            main()
        elif a == 10:
            Sample_Standard_Deviations()
            main()
        elif a == 11:
            Sample_proportions()
            main()
        elif a == 12:
            Con_limits_for_normal_mean()
            main()
        elif a == 13:
            UnknownVariance()
            main()
        elif a == 14:
            Con_limits_for_std()
            main()
        elif a == 15:
            Diff_populations_means_Con_limits()
            main()
        else:
            print('Thank You! Have a Good Day!')
        break


if __name__ == "__main__":
    main()