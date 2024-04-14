# Function to create Linear Regression plot
def lin_regress_plot(x, y, x_label, y_label, line_x_cord, line_y_coord):
    ''' Function takes in two columns or series of data and performs a linear regression calculation.
    
    Args:
        x: DataFrame column for plotting along the x-axis,
        y: DataFrame column for plotting along the y-axis,
        x_label: scatter plot x label,
        y_label: scatter plot y label,
        line_x_cord: x coordinate for regression line equation placement,
        line_y_coord: y coordinate for regression line equation placement.
    
    Returns:
        - A scatter plot using the data from the two columns.
        - A regression line plot showing the linear relationship between two sets of data.
        - The line equation for the linear regression.
    
    '''
    
    from scipy.stats import linregress
    (slope, intercept, rvalue, pvalue, stderr) = linregress(x, y)
    regress_y = x * slope + intercept
    print(f'The r-value is: {rvalue}')
    line_equation = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
    plt.scatter(x,y)
    plt.plot(x,regress_y,"r", alpha=0.5)
    plt.annotate(line_equation,(line_x_cord,line_y_coord),fontsize=15,color="red")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()