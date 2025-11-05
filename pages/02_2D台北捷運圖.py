import solara
import leafmap.maplibregl as leafmap

def create_map():
    """建立一個以台北為中心的捷運地圖"""
    
    m = leafmap.Map(
        style="dark-matter",  # 您可以改成 "streets" 或 "satellite"
        projection="mercator",  # 區域地圖使用 "mercator" 投影更合適
        height="750px",
        center=[121.56, 25.04],  # 台北市中心
        zoom=11,               # 縮放至城市等級
    )
    
    # 台北捷運路網的 GeoJSON 資料來源 (來自台灣政府開放資料)
    # 來源: https://github.com/datagovtw/tpe-mrt-lines
    geojson_url = "https://raw.githubusercontent.com/datagovtw/tpe-mrt-lines/master/tpe-mrt-lines.json"

    # 1. 定義 MapLibre 資料來源 (Source)
    # 我們給這個來源一個 ID，例如 'mrt-source'
    mrt_source = {
        "type": "geojson",
        "data": geojson_url
    }
    
    # 2. 定義 MapLibre 圖層 (Layer)
    # 這個圖層會使用上面的 'mrt-source'
    mrt_layer = {
        "id": "mrt-lines",        # 圖層的唯一 ID
        "source": "mrt-source",   # 告訴它要用哪個 source
        "type": "line",           # 向量類型
        "layout": {
            "line-join": "round",
            "line-cap": "round"
        },
        "paint": {
            # 這是關鍵：使用 "data-driven" 樣式
            # 從 GeoJSON 的 "Color" 屬性中取得顏色
            "line-color": ["get", "Color"],
            "line-width": 5  # 路線寬度
        }
    }

    # 3. 將 Source 和 Layer 加入地圖
    m.add_source("mrt-source", mrt_source)
    m.add_layer(mrt_layer)
    
    # 4. (可選) 加入工具提示，當滑鼠移上時顯示
    # "mrt-lines" 必須對應上面 layer 的 "id"
    # "Line_Name" 是 GeoJSON 屬性中的欄位
    m.add_tooltip("mrt-lines", ["Line_Name", "Line_ID"])

    return m

@solara.component
def Page():
    
    # (A) 設定瀏覽器分頁標題
    solara.Title("台北捷運路網圖")
    
    # (B) 這是「頁面上的可見標題」 
    solara.Markdown("## 台北捷運路網圖") 
    
    # (C) 建立並顯示地圖
    m = create_map()
    return m.to_solara()