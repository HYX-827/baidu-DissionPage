from DrissionPage import ChromiumOptions, Chromium

co = ChromiumOptions()
co.use_system_user_path()  # 使用系统浏览器配置
browser = Chromium(co)
tab = browser.latest_tab