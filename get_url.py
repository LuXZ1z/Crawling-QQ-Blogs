import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

qq = '123456'           # 键入你的QQ号

def save_blog_data(page_content):
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(page_content, "html.parser")

    # 找到所有包含博客ID的<a>标签
    blog_links = soup.find_all('a', {'rel': 'blog-detail-link'})

    # 提取博客ID并保存到一个列表中
    blog_ids = []
    for link in blog_links:
        blog_id = link['blogid']
        blog_ids.append(blog_id)

    print(blog_ids)

    # 提取数据并保存到CSV文件
    with open("qq_blog_link.csv", "a", encoding="utf-8") as csvfile:
        for x in blog_ids:
            csvfile.write(f"{x}\n")

class blog():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def get(self, qq):
        self.driver.get("https://user.qzone.qq.com/" + qq)
        self.driver.set_window_size(1106, 696)
        time.sleep(5)
        element = self.driver.find_element(By.LINK_TEXT, "返回个人中心")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".menu_item_2:nth-child(2) > a").click()
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        time.sleep(1)
        # 切换到iframe上下文
        iframe_element = self.driver.find_element(By.XPATH, "//iframe[@id='tblog']")
        self.driver.switch_to.frame(iframe_element)

        cnt = 1
        while(1):
            try:
                time.sleep(1)
                self.driver.find_element(By.LINK_TEXT, "下一页").click()

                page_content = self.driver.page_source
                print(cnt)
                # print(page_content)
                save_blog_data(page_content)
                cnt = cnt + 1
            except:
                print("Error, cnt is", cnt)

bl = blog()

bl.setup_method()
bl.get(qq)
