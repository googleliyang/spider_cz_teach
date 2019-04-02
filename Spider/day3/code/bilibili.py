#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import time
from io import BytesIO


class Bilibili(object):

    def __init__(self):
        # 创建浏览器对象
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        # 保存登录url
        self.url = 'https://passport.bilibili.com/login'
        # 保存账号密码
        self.user = "13074125935"
        self.pwd = "!QAZ2wsx#EDC"

    def input_user_pwd(self):
        # 来到登录页面
        self.driver.get(self.url)

        # 输入账号密码
        el_user = self.driver.find_element_by_id('login-username')
        el_user.send_keys(self.user)

        el_pwd = self.driver.find_element_by_id('login-passwd')
        el_pwd.send_keys(self.pwd)

    def get_screenshot(self):
        """
        获取屏幕截图
        :return: 
        """
        # 截图
        screentshot = self.driver.get_screenshot_as_png()
        # 使用PIL将截图创建成图片对象，该对想可以获取图片的相关信息
        screentshot = Image.open(BytesIO(screentshot))

        return screentshot



    def get_position(self):
        """
        用于获取截取验证码时的四条边
        :return: 
        """

        # 定位锁按钮，模拟点击
        el_lock = self.driver.find_element_by_xpath('//div[@class="gt_ajax_tip gt_ready"]')
        el_lock.click()

        # 定位图片对象
        img = self.driver.find_element_by_xpath('//div[@class="gt_cut_fullbg gt_show"]')
        time.sleep(2)

        # 获取图片对象的坐标
        location = img.location
        print(location)

        # 获取图片对象的尺寸
        size = img.size
        print(size)

        # 计算图片的截取区域
        left, top, right, button = 2 * location["x"], 2 * location["y"], 2 * (location["x"] + size["width"]), 2 * (location["y"] + size["height"])

        # 返回
        return left, top, right, button

    def get_image(self):
        """
        获取两张验证码图片
        :return: 
        """

        # 获取验证码的位置
        position = self.get_position()

        # 屏幕截图
        screenshot1 = self.get_screenshot()

        # 抠出没有滑块和阴影的验证码图片
        captcha1 = screenshot1.crop(position)
        with open('captcha1.png','wb')as f:
            captcha1.save(f)

        # 点击验证码拖动按钮
        el_button = self.driver.find_element_by_xpath('//div[@class="gt_slider_knob gt_show"]')
        el_button.click()

        # 等待错误提示信息消失
        time.sleep(4)

        # 屏幕截图
        screenshot2 = self.get_screenshot()

        # 抠验证码图
        captcha2 = screenshot2.crop(position)
        with open('captcha2.png', 'wb')as f:
            captcha2.save(f)

        # 返回两个图片验证码对象
        return captcha1, captcha2

    def is_pixel_equal(self,image1, image2, x, y):
        """
        比较两个图片的相同一点的三原色相似度
        :param image1: 
        :param image2: 
        :param x: 
        :param y: 
        :return: 
        """

        pixel1 = image1.load()[x, y]
        pixel2 = image2.load()[x, y]
        # print(pixel1,pixel2)

        # 设定一个比较值
        threshold = 60

        # 比较
        if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(pixel1[2] - pixel2[2]) < threshold:
            return True
        else:
            return False

    def get_gap(self, image1, image2):
        """
        核对两个验证码的的相同位置的像素，找出像素偏差值大的位置，返回其x值，该值为验证码拖动的位移
        :param image1: 没有阴影的验证码图片对象
        :param image2: 有阴影的验证码图片对象
        :return: 比对之后的偏移值
        """

        left = 120

        # print(image1.size)
        # 遍历x轴的点到最后
        for i in range(left, image1.size[0]):
            for j in range(image1.size[1]):
                # 获取一个坐标点，然后在两张图上核对该坐标点的颜色差距，
                # 判断颜色差距是否过大，过大则该x值为偏移值，返回该值，否则继续
                if not self.is_pixel_equal(image1, image2, i, j):
                    left = i
                    return round(left/2 - 8)
        return left

    def get_track(self, offset):
        """
        通过偏移总量，模拟人类操作计算每次偏移量
        :param offset: 
        :return: 
        """
        # 存储步伐
        track = []
        # 当前位移
        current = 0
        # 中间点，用于切换加速度
        mid= offset * 3/5
        t = 0.3
        v = 0

        while current < offset:
            if current < round(mid):
                a = 2
            else:
                a = -3

            v0 = v
            v = v0 + a*t

            move = v0 * t + 1/2 * a * t * t
            current += move

            track.append(round(move))

        return track

    def operate_button(self, track):

        # 点击拖动按钮
        el_button = self.driver.find_element_by_xpath('//div[@class="gt_slider_knob gt_show"]')
        ActionChains(self.driver).click_and_hold(el_button).perform()

        ActionChains(self.driver).move_by_offset(xoffset=100, yoffset=0).perform()
        ActionChains(self.driver).move_by_offset(xoffset=-100, yoffset=0).perform()

        # 移动滑块
        for i in track:
            ActionChains(self.driver).move_by_offset(xoffset=i, yoffset=0).perform()

        # 松开按钮
        ActionChains(self.driver).release().perform()

    def do_captcha(self):
        """
            实现验证码的处理
        """
        print(1)
        # 获取验证码图片 & 有阴影拼图的验证码图片
        img1, img2 = self.get_image()
        print(2)
        # 比较两个验证码图片获取验证码滑块的偏移量
        offset = self.get_gap(img1, img2)
        print(offset)

        # 使用偏移值计算移动操作
        track = self.get_track(offset)

        # 操作滑块按钮，模拟拖动滑块做验证登录
        self.operate_button(track)

    def run(self):
        # 主逻辑

        # 来到登录页面&输入账号密码
        self.input_user_pwd()

        # 处理验证码
        self.do_captcha()

if __name__ == '__main__':
    bili = Bilibili()
    bili.run()
