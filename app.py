import solara

# 1. 這是您的「佈局」 (Layout)
# 
# solara.AppLayout 會「自動」掃描 `pages` 資料夾
# 並將它們「呈現」在側邊欄中。
# 
@solara.component
def Layout(children):
    # solara.AppLayout 就是負責「呈現分頁」的元件
    return solara.AppLayout(children=children)


# 2. 這是您的「根頁面」 (Page at /)
# 
# 它的唯一工作就是將使用者導向至 `01_home.py` (也就是 /home)
#
@solara.component
def Page():
    # 獲取 Solara 的路由
    router = solara.use_router()

    # 定義一個「效果」(Effect)，這個效果只會在元件載入時執行一次
    def redirect_if_root():
        # 檢查當前路徑是否為根目錄 '/'
        if router.path == "/":
            # 立即將瀏覽器 URL 推送到 '/home'
            # '/home' 是 Solara 根據 'pages/01_home.py' 自動產生的路徑
            solara.routing.push("/home")

    # 註冊這個效果，[] 空列表意味著 "只執行一次"
    solara.use_effect(redirect_if_root, [])
    
    # 在重定向發生時，我們不需要顯示任何內容
    return solara.Div()