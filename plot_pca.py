import glob
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pca_file = glob.glob("**/plink_results_projected.sscore", recursive=True)[0]
panel_file = glob.glob("**/*.panel", recursive=True)[0]

pca = pd.read_table(pca_file, sep="\t")
ped = pd.read_table(panel_file, sep="\t")

pcaped = pd.merge(pca, ped, right_on="sample", left_on="IID", how="inner")

plt.figure(figsize=(10, 10))
sns.scatterplot(data=pcaped, x="PC1_AVG", y="PC2_AVG", hue="pop", s=50)
plt.savefig("pca_plot.png", dpi=150)