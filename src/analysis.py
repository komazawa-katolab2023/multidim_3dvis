# 必要なライブラリの読み込み
import pandas as pd
from sklearn.manifold import TSNE
import plotly.express as px
from plotly.offline import plot

# CSVファイルの読み込み
file_path = 'data/sample_data.csv'
df = pd.read_csv(file_path)
data_df = df.drop('Name', axis=1)

# t-SNEでの次元削減
tsne = TSNE(n_components=3, random_state=0)
reduced_data = tsne.fit_transform(data_df)

# 結果をDataFrameに変換
reduced_df = pd.DataFrame(reduced_data, columns=['Dimension 1', 'Dimension 2', 'Dimension 3'])
reduced_df['Name'] = df['Name']

# Plotlyでの可視化
fig = px.scatter_3d(reduced_df, x='Dimension 1', y='Dimension 2', z='Dimension 3', text='Name')
fig.update_traces(marker_size = 5)

# グラフをHTMLファイルとしてエクスポート
output_file = 'index.html'
plot(fig, filename=output_file)