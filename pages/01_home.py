import solara

# 必須命名為 Page
@solara.component
def Page():
    solara.Title("首頁")  # 使用 solara.Title 來設定頁面標題
    solara.Markdown("這是我的首頁 ")