# %%
import pandas as pd
from raptor.raptor import RetrievalAugmentation 

# %%
df = pd.read_excel('./data/한국보훈복지의료공단_보훈병원 질병 및 수술통계_통합.xlsx')
texts = df['상병명'].to_list()
texts

# %%
RA = RetrievalAugmentation()

for disease_name in texts:
    RA.add_documents(disease_name) # 함수 구현이 안되어 있음...

# %%


# %%
hospitals = ['광주병원', '대구병원', '대전병원', '부산병원', '중앙병원']
gukbi_columns = [f'{hospital}_국비' for hospital in hospitals]
df['국비_sum'] = df[gukbi_columns].sum(axis=1)
sabi_columns = [f'{hospital}_사비' for hospital in hospitals]
df['사비_sum'] = df[sabi_columns].sum(axis=1)
df


# %%
df['국비_비율'] = df['국비_sum'] / (df['국비_sum'] + df['사비_sum'] + 1e-6)

# %%
def iqr_outliers(group):
    group = group.copy()
    q1 = group['국비_비율'].quantile(0.25)
    q3 = group['국비_비율'].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return group[(group['국비_비율'] < lower) | (group['국비_비율'] > upper)]

