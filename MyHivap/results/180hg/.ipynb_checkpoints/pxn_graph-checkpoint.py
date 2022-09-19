import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

proj = '88Sr'
trg = '92Mo'
cn = '180Hg'
bf = 0.85
ch = 'pxn'

file_name10 = proj + '_' + trg + '_' + cn + '_' + ch + '_' + 'IFUS10' + '_' + 'barfac' + str(bf) + '.dat'
file_name0 = proj + '_' + trg + '_' + cn + '_' + ch + '_' + 'IFUS0' + '_' + 'barfac' + str(bf) + '.dat'

stano10 = open('hivaperg_180Hg_88Sr92Mo_F10_stano.dat', 'r')
stano0 = open('hivaperg_180Hg_88Sr92Mo_F0_stano.dat', 'r')

pxn_10 = open('data/' + file_name10, 'r')
pxn_0 = open('data/' + file_name0, 'r')

df_pxn10 = pd.read_csv('data/' + file_name10, sep='\t')
df_pxn0 = pd.read_csv('data/' + file_name0, sep='\t')

dfm10 = df_pxn10.melt(id_vars=['E_lab', 'E*/MeV'], var_name='isotope', value_name='CS')
dfm0 = df_pxn0.melt(id_vars=['E_lab', 'E*/MeV'], var_name='isotope', value_name='CS')

plt.figure(figsize=(9,6))
ax1 = sns.lineplot(x='E_lab', y='CS', hue='isotope', data=dfm10)
plt.semilogy()
plt.ylim(1e-2, 1e1)
# plt.xlim(right=50)
plt.ylabel('$\sigma$ [mb]')
plt.xlabel('$E_{proj}$ [MeV]')
plt.legend(loc='upper right')
ax2 = sns.lineplot(x='E_lab', y='CS', hue='isotope', data=dfm0, linestyle='dashed', legend=None)
plt.show()