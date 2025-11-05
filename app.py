import solara

# 匯入 Solara 的標準 App 佈局
# AppLayout 會自動處理側邊欄、標題等
from solara.template import AppLayout

# 'children' 參數是 Solara 自動傳入的
# 它代表了您當前頁面 (例如 01_home.py) 的所有內容
@solara.component
def Layout(children):
    return AppLayout(children=children)

# 注意：
# 在這個檔案中，我們不需要定義 Page 元件
# 因為 Solara 會自動使用這個 Layout 
# 來包裝 pages/ 資料夾中的 Page 元件