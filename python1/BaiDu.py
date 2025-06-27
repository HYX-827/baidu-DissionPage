from DrissionPage import ChromiumPage, ChromiumOptions
import pandas as pd

def main():
    # 创建浏览器选项实例
    co = ChromiumOptions().set_browser_path(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
    co.headless(False)  # 设置有头模式，如果想要无头模式可以设置为True

    # 创建浏览器页面实例
    page = ChromiumPage(co)

    # 打开百度首页
    url = "https://www.baidu.com"
    page.get(url)

    # 输入搜索内容并提交搜索
    search_content = "Python"
    page.ele("css:#kw").input(search_content)
    page.ele("css:#su").click()

    # 等待搜索结果加载完成
    page.wait.load_start()  # 修正此处，使用 load_start 而不是 loadstart

    # 获取搜索结果中的标题和链接
    results = []
    for item in page.eles("css:#content_left .result"):
        title = item.ele("css:h3").text
        link = item.ele("css:a").attr("href")
        results.append({"标题": title, "链接": link})

    # 转换为DataFrame
    df = pd.DataFrame(results)

    # 保存为Excel文件
    excel_path = "baidu_search_results.xlsx"
    df.to_excel(excel_path, index=False)

    print(f"搜索结果已保存到 {excel_path}")

if __name__ == "__main__":
    main()
