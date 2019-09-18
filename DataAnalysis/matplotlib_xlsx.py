import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import xlsxwriter
#图标样式 http://matplotlib.org/gallery.html
#python库 www.lfd.uci.edu/~gohlke/pythonlibs/
np.random.seed(0)
# example data
mu = 100  # mean of distribution
sigma = 15  # standard deviation of distribution
x = mu + sigma * np.random.randn(437)
num_bins = 50
fig, ax = plt.subplots()
# the histogram of the data
n, bins, patches = ax.hist(x, num_bins, normed=1)
# add a 'best fit' line
y = mlab.normpdf(bins, mu, sigma)
ax.plot(bins, y, '--')
ax.set_xlabel('Smarts')
ax.set_ylabel('Probability density')
ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')
# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
#保存图片
plt.savefig("myplot.png", dpi = 400,bbox_inches='tight')
#显示图片
#plt.show()
#导入EXCEL
book = xlsxwriter.Workbook('input.xlsx')
sheet = book.add_worksheet('demo')
sheet.insert_image('D4','myplot.png')
book.close()