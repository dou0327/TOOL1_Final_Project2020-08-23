import seaborn as sns
import matplotlib.pyplot as plt

# penguins dataset
df = sns.load_dataset("penguins")

# drop rows with nan value, and rearrange the index
df.dropna(axis=0, how='any', inplace=True)
df.reset_index(drop=True, inplace=True)

print(df.info())
print(df.head())
print(df.describe())

# classify columns
continuous_variables = df.dtypes[df.dtypes != 'object'].index.values
discrete_variables = df.dtypes[df.dtypes == 'object'].index.values

print('column possible values:')
col_values = {}
for col in discrete_variables:
    col_values[col] = df.groupby(col).all().index.values.tolist()
    print(col + ' ' * (14 - len(col)) + ': ', col_values[col])

# transfer str discrete columns to int columns
for col_name, col_value in col_values.items():
    class_mapping = {label: idx for idx, label in enumerate(col_value)}
    df[col_name + '_label'] = df[col_name].map(class_mapping)


# heatmap
sns.heatmap(df.corr(), vmin=-1, annot=True, cmap='coolwarm')
plt.show()
# The heatmap shows the strongest correlation between flipper_length_mm and body_mass_g,
# the weakest correlation between bill_depth_mm and flipper_length_mm.

# pairplot, by species
sns.pairplot(data=df, diag_kind='hist', hue='species')
plt.legend()
plt.show()
# The pairplot shows the correlation between any two characteristics in three species,
# and the difference between Gentoo and the other two species is the most obvious in
# flipper_length_mm and bill_depth_mm.

# pairplot, by island
sns.pairplot(data=df, diag_kind='hist', hue='island')
plt.show()
# The pairplot shows the correlation between any two characteristics in three island,
# and the difference between Biscoe and the other two islands is the most obvious in
# flipper_length_mm and bill_depth_mm.




# The distribution difference of different species on different characteristics
plt.figure()
plt.subplot(2, 2, 1)
sns.boxplot(x='species', y='bill_length_mm', saturation=0.5, palette='pastel', data=df)
plt.title('bill_length_mm')
plt.subplot(2, 2, 2)
sns.boxplot(x='species', y='bill_depth_mm', saturation=0.5, palette='pastel', data=df)
plt.title('bill_depth_mm')
plt.subplot(2, 2, 3)
sns.boxplot(x='species', y='flipper_length_mm', saturation=0.5, palette='pastel', data=df)
plt.title('flipper_length_mm')
plt.subplot(2, 2, 4)
sns.boxplot(x='species', y='body_mass_g', saturation=0.5, palette='pastel', data=df)
plt.title('body_mass_g')
plt.show()
# The boxplot shows the distribution interval of the characteristics of different species.
# and it is obvious that the body of Gentoo species is larger than other species

# The distribution difference of different island on different characteristics
plt.figure()
plt.subplot(2, 2, 1)
sns.boxplot(x='island', y='bill_length_mm', saturation=0.5, palette='pastel', data=df)
plt.title('bill_length_mm')
plt.subplot(2, 2, 2)
sns.boxplot(x='island', y='bill_depth_mm', saturation=0.5, palette='pastel', data=df)
plt.title('bill_depth_mm')
plt.subplot(2, 2, 3)
sns.boxplot(x='island', y='flipper_length_mm', saturation=0.5, palette='pastel', data=df)
plt.title('flipper_length_mm')
plt.subplot(2, 2, 4)
sns.boxplot(x='island', y='body_mass_g', saturation=0.5, palette='pastel', data=df)
plt.title('body_mass_g')
plt.show()
# The boxplot shows the distribution interval of the characteristics of different islands.
# and it is obvious that the bill of the penguin in Dream island is more widely distributed.

# a scattergram with the linear model
plt.figure()
plt.subplot(3, 1, 1)
g = sns.regplot(data=df, x='bill_length_mm', y='body_mass_g')
plt.subplot(3, 1, 2)
g = sns.regplot(data=df, x='bill_depth_mm', y='body_mass_g')
plt.subplot(3, 1, 3)
g = sns.regplot(data=df, x='flipper_length_mm', y='body_mass_g')
plt.show()

# The regplot shows a scattergram with the linear model, only shows a few of them, and we can
# get that the bigger their flippers are, the bigger they are.
