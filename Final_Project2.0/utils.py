from dataset import df
import pandas as pd
from app import n_samples

def select_balanced_samples(df, n_samples):
    samples_per_group = n_samples
    grouped = df.groupby('Tipo Titulo')
    balanced_samples = pd.DataFrame()
    for _, group in grouped:
        samples = group.sample(min(len(group), samples_per_group), random_state=1)
        balanced_samples = pd.concat([balanced_samples, samples], ignore_index=True)
    return balanced_samples

# Seleção de amostras equitativas antes de gerar gráficos
df_samples = select_balanced_samples(df, n_samples)
