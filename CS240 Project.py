import matplotlib.pyplot as plt
import statsmodels.formula.api as smf


from methods import *
import numpy as np


data = readData("teams.csv")
year = data[0]
wins = data[1]
loss = data[2]

print year
print wins
print loss

h2 = test_time_gpa((wins, loss))
year = np.array(year).astype(np.float)
print np.mean(wins)
print np.mean(loss)
print h2.TestStatistic((wins, loss))

print h2.PValue(iters=10000)

#
slope, intercept = np.polyfit(wins,loss,1)
print "slope: ", slope, "intercept: ", intercept
pointsLine = [intercept+slope*x for x in wins]
plt.figure()
plt.plot(wins,loss, "ro")
plt.plot(wins, pointsLine, "--")
plt.show()

residuals = [y- (slope*x + intercept) for x, y in zip(wins,loss)]
res_plt = sorted(zip(wins, residuals))
t2 = [x for x,y in res_plt]
r2 = [y for x,y in res_plt]
plt.figure()
plt.plot(t2, r2, 'ro-')
plt.show()

log_year = [np.log(x) for x in year]
slope_log, intercept_log = np.polyfit(year,log_year,1)
print "line fit for age and log(year)"
print "slope: ", slope_log, "intercept: ", intercept_log
pointsLineLog = [intercept_log+slope_log*x for x in year]
plt.figure()
plt.plot(year, log_year, "ro")
plt.plot(year, pointsLineLog, '--')
plt.show()

formula='year ~ year + wins + loss'
data_dict = {"gpa":loss, "age":year, "time":wins}
model = smf.poisson(formula, data=data_dict)
model = model.fit()


print "slope for wins and losses is: ", slope