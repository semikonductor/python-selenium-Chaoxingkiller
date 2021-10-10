'''希望大家能自己先学习selenium知识和python基本语法，这样DIY起来更加方便'''
#copyright @GitHub semiconductor
from selenium import webdriver
import time
#启动浏览器驱动
driver = webdriver.Edge(R"C:edgedriver.exe")  # Edge浏览器驱动绝对地址，注意地址格式！！！！
！！
# 打开网页
driver.get("https://learning.xidian.edu.cn/portal")  # 打开学在西电
#最大化
driver.maximize_window()
#登录按钮
button_log_in = driver.find_element_by_class_name('denglu')
button_log_in.click()
#输入用户名和密码
account = driver.find_element_by_id('username')
account.send_keys('XXXXXXXXXX')#学号
password = driver.find_element_by_id('password')
password.send_keys('XXXXXXXXXX')#密码

tongyi_login = driver.find_element_by_id('login_submit')
tongyi_login.click()
#更改为自己网课的首页（从学在西电点进去）例如：http:/mooc2-ans.chaoxing.com/mycourse/stu?courseid=xxxx……
driver.get("XXXXXXXXXXXX")#输入网址



# 获取打开的多个窗口句柄，关闭学在西电
windows = driver.window_handles
driver.switch_to.window(windows[1])
driver.close()

#倒计时给予选择的时间，不够可以自行添加
time_left = 10
print('请在十秒内选择要播放的课程')
while time_left > 0:
    print('倒计时(s):', time_left)
    time.sleep(1)
    time_left = time_left - 1
#控制权到当前页面
windows = driver.window_handles
driver.switch_to.window(windows[-1])

while 1:
    #注意一下iframe
    iframe1 = driver.find_element_by_id('iframe')
    driver.switch_to.frame(iframe1)

    iframe2 = driver.find_element_by_xpath('//*[@id="ext-gen1043"]/div/div/p/div/iframe')
    driver.switch_to.frame(iframe2)
    #播放按钮
    player = driver.find_element_by_class_name('vjs-big-play-button')
    player.click()
    # 开始播放，获取播放的进度
    time.sleep(1)
    currentTime = driver.find_element_by_class_name('vjs-current-time-display')
    x = currentTime.text
    totalTime = driver.find_element_by_class_name('vjs-duration-display')
    y = totalTime.text
    #每隔十秒检查是否播放完成
    while x != y or x == '':#加入空字符串对付隐藏的进度条，奇技淫巧23333
        time.sleep(10)
        y = totalTime.text
        x = currentTime.text
    #跳出iframe
    driver.switch_to.default_content()
    #这里找到下一章按钮，连击两次（我课程的要求）
    nextChapter = driver.find_element_by_id('right')
    nextChapter.click()
    nextChapter.click()
    #歇会，要不然好多元素加载不出来
    time.sleep(5)
