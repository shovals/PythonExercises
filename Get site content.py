from selenium import webdriver

# browser = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')  # Chrome driver
browser = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')  # Firefox driver
browser.get('https://www.google.co.il/search?source=hp&ei=0Xb4WYTsDsreUZDTqig&q=pycon&oq=pycon&gs_l=psy-ab.3..0l10.3502.4124.0.6011.6.5.0.0.0.0.141.470.0j4.4.0....0...1.1.64.psy-ab..2.4.469.0..35i39k1j0i67k1j0i131k1.0.k35lMsT7Bcc')  # Site location

# results = browser.find_elements_by_xpath('//div[@class="main-content"]')
# results = browser.find_elements_by_class_name('style-scope ytd-search')
results = browser.find_elements_by_id('search')
print(len(results))

for result in results:
    video = result.find_element_by_xpath('.//h3/a')
    title = video.get_attribute('text')
    url = video.get_attribute('href')
    print("{} ({})".format(title, url))
browser.quit()

