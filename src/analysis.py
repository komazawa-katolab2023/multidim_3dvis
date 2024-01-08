# 必要なライブラリの読み込み
import pandas as pd
from sklearn.manifold import TSNE
import plotly.express as px
from plotly.offline import plot

# CSVファイルの読み込み
file_path = 'data.csv'
df = pd.read_csv(file_path)

# t-SNEでの次元削減
tsne = TSNE(n_components=3, random_state=0)
reduced_data = tsne.fit_transform(df)

# 結果をDataFrameに変換
reduced_df = pd.DataFrame(reduced_data, columns=['Dimension 1', 'Dimension 2', 'Dimension 3'])

# Plotlyでの可視化
fig = px.scatter_3d(reduced_df, x='Dimension 1', y='Dimension 2', z='Dimension 3')

# グラフをHTMLファイルとしてエクスポート
output_file = 'index.html'
plot(fig, filename=output_file)