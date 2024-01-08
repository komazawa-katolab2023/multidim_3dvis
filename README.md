
# t-SNE 3D Visualization Project

このプロジェクトでは、多次元データをt-SNEを用いて3次元に変換し、その結果をPlotlyで可視化し、GitHub Pagesで公開する方法を紹介します。

## ステップバイステップガイド

1. **多次元データの準備**: CSVファイル形式でデータを用意します。

2. **Pythonでのデータの読み込みと前処理**: Pythonを使ってCSVデータを読み込み、必要に応じて前処理（欠損値の処理、正規化など）を行います。

3. **t-SNEを用いた次元削減**: Pythonのscikit-learnライブラリを用いて、t-SNEを実装し多次元データを3次元に変換します。

4. **Plotlyでの可視化**: 変換された3次元データをPlotlyを用いてグラフ化します。

5. **GitHub Pagesへの公開**: 可視化されたグラフをHTML形式でエクスポートし、GitHubにアップロードしてGitHub Pagesを介して公開します。

## 必要なライブラリ

- scikit-learn
- pandas
- plotly

これらのライブラリは以下のコマンドでインストールできます：

```bash
pip install scikit-learn pandas plotly
```

## 実装例

以下は、CSVデータを読み込み、t-SNEで3次元に変換し、Plotlyで可視化するための基本的なPythonコードの例です。

```python
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
output_file = 'tsne_visualization.html'
plot(fig, filename=output_file)
```

## 注意点

- Plotlyで作成されたHTMLファイルは、データを埋め込む形でエクスポートされます。そのため、元のCSVファイルを同時にGitHubレポジトリに配置する必要はありません。
- データの機密性や公開に関する注意が必要です。HTMLファイルにはデータが埋め込まれているため、機密性が高い情報は含めないでください。
- CSVファイルもレポジトリに含めることで、データの再利用性や透明性が向上します。
