import solara
import solara.lab

# 1. 這是您的「佈局」 (Layout)
# 它會套用到所有頁面，並負責顯示側邊欄
@solara.component
def Layout(children):
    return solara.AppLayout(children=children)


# 2. 這是您的「根頁面」 (Page at /)
# 我們用這個頁面來執行「重定向」
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
    # 返回一個空的 Div 即可
    return solara.Div()