import solara

# 錯誤的 "from solara.template import AppLayout" 已經被移除

@solara.component
def Layout(children):
    # 直接使用 solara.AppLayout
    return solara.AppLayout(children=children)

# 注意：
# 在這個檔案中，我們不需要定義 Page 元件
# 因為 Solara 會自動使用這個 Layout 
# 來包裝 pages/ 資料夾中的 Page 元件