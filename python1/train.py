from DrissionPage import ChromiumPage, ChromiumOptions
import time

def main():
    # 创建浏览器
    co = ChromiumOptions().set_browser_path(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
    co.headless(False)
    # 创建浏览器页面实例
    page = ChromiumPage(co)

    # 打开百度首页
    url = "https://www.baidu.com"
    page.get(url)

    # 等待页面完全加载
    time.sleep(3)

    # 获取页面内容
    page_content = page.html

    # 打印页面内容
    print(page_content)

    # 将页面内容保存到文件
    file_path = "baidu_homepage_content.txt"
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(page_content)

    print(f"页面内容已保存到 {file_path}")

if __name__ == "__main__":
    main()
