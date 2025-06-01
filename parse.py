import pdfplumber
import pandas as pd

pdf_path = "shoplist.pdf"  # PDFファイルのパス
csv_path = "output.csv"  # 書き出すCSVファイル名

from typing import List

tables: List[pd.DataFrame] = []

# PDFから表を抽出
with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages):
        table = page.extract_table()
        if table:
            df = pd.DataFrame(table[1:], columns=table[0])  # 1行目をヘッダーに
            tables.append(df)

# 複数ページの表を結合
if tables:
    final_df = pd.concat(tables, ignore_index=True)
    final_df.to_csv(csv_path, index=False)
    print(f"✅ CSV書き出し完了: {csv_path}")
else:
    print("⚠️ 表が見つかりませんでした。")
