from selenium import webdriver

class infow():
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")
    def get_info(selfself,query):
        self.query=query
        self.driver.get(url="https://www.wikipedia.org/")

assit=infow()
assit.get_info("hello")