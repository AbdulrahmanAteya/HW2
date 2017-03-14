import nsfg
import thinkplot
import thinkstats2
pres = nsfg.ReadFemResp()

fmar1age = pres['fmar1age']
his1 = thinkstats2.Hist(pres.fmar1age)
hist1 = thinkstats2.Hist(his1)
pres.fmar1age.value_counts().sort_index()

thinkplot.Hist(hist1, color='Blue')
thinkplot.Show(xlabel="The age during the first marraige",ylabel = "The Frequency")

fmarno = pres['fmarno']
histo2 = thinkstats2.Hist(fmarno)
pres.fmarno.value_counts().sort_index()

totincr = pres['totincr']
histo3 = thinkstats2.Hist(totincr)
pres.totincr.value_counts().sort_index()

thinkplot.Hist(histo3, color='Blue',width=0.4,label="The total income")
thinkplot.Config(xlabel='The range', ylabel='The frequency')
thinkplot.Show()

neverMarried = pres[pres.fmarno == 0]
married = pres[pres.fmarno >= 1]

histo4 = thinkstats2.Hist(neverMarried.totincr, label="Who had never married")
histo5 = thinkstats2.Hist(married.totincr, label="The married")
thinkplot.Hist(histo4, align='right',width=0.4,color='Green')
thinkplot.Hist(histo5, align='left',width=0.4,color='Blue')
thinkplot.Show(xlabel='The time', ylabel='The amount',)

print 'Lowest value of those who have never got married of their income is %.2f' %neverMarried.totincr.min()

print 'Lowest value of those who have never got married of their total income is %.2f' %married.totincr.min()

print 'The highest value of who heve never got married of their total income is %.2f' %neverMarried.totincr.max()

print 'The highest value of married respondents of the total income is %.2f' %married.totincr.max()

print 'The Normal variation of those who have never got married of the total income is %.2f' %neverMarried.totincr.std()

print 'The Normal variation of married respondents of the total income is %.2f' %married.totincr.std()

print 'The varience of those who have never got married respondents of the total income is %.2f' %neverMarried.totincr.var()

print 'The varience of married respondents of total income is %.2f' %married.totincr.var()

print 'The avarage of never married respondents of total income is %.2f' %neverMarried.totincr.mean()

print 'The avarage of married respondents of total income is %.2f' %married.totincr.mean()