import solara

# 確保元件名稱為 Page (P 大寫)
@solara.component
def Page():
    
    # 1. 設定瀏覽器分頁的標題
    solara.Title("首頁 | GIS 應用程式")

    # 2. 使用 solara.Markdown 撰寫您的介紹
    solara.Markdown(
        """
        ## 歡迎來到我的 GIS 應用程式
        
        這是一個使用 Solara 和 Hugging Face Spaces 部署的 Web App。
        
        ---
        
        ### 1105作業
            這是地理三洪子晴的Webmap app
        
        """
    )
   