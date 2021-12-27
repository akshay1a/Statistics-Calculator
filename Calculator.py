import CalModule as m
# Program to run statistic calculator in minimum lines of code
while True:
    print('''\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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
    if a != 0 and a < 16:
        if a == 1:
            m.Central_Tendency()
        elif a == 2:
            m.T_test_for_single_mean()
        elif a == 3:
            m.T_Test_difference_2means()
        elif a == 4:
            m.F_test()
        elif a == 5:
            m.Sample_Mean()
        elif a == 6:
            m.Sample_Standard_deviation()
        elif a == 7:
            m.Sample_Variance()
        elif a == 8:
            m.Sample_Proportion()
        elif a == 9:
            m.Sample_Populations_Means()
        elif a == 10:
            m.Sample_Standard_Deviations()
        elif a == 11:
            m.Sample_proportions()
        elif a == 12:
            m.Con_limits_for_normal_mean()
        elif a == 13:
            m.UnknownVariance()
        elif a == 14:
            m.Con_limits_for_std()
        elif a == 15:
            m.Diff_populations_means_Con_limits()
    else:
        print('Thank You! Have a Good Day!')
        break