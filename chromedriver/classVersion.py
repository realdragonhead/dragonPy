import chromedriver_autoinstaller
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys

class driverManipulator():
	# Make new driver added options
	def __init__(self):
		# install chromedriver automatically
		chromedriver_autoinstaller.install()

		# Add driver options
		self.chrome_options = wd.ChromeOptions()
		self.chrome_options.add_argument("--incognito")
		self.chrome_options.add_argument("disable-gpu")
		# self.chrome_options.add_argument("headless")
		self.chrome_options.add_argument("lang=ko_KR")
		self.chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
		self.driver = wd.Chrome(options=self.chrome_options)

	# Load target page
	def pageLoader(self, waitTime, url):
		self.driver.implicitly_wait(waitTime)
		self.driver.get(url)

	# Execute script by driver
	def execScript(self, text):
		self.driver.execute_script(text)

	# Return output after execute
	def execScripto(self, text):
		return self.driver.execute_script(text)

	# Close driver
	def byTag(self, target):
		return self.driver.find_element_by_tag_name(target)

	def bySelectors(self, target):
		return self.driver.find_elements_by_css_selector(target)

	def byTags(self, target):
		return self.driver.find_elements_by_tag_name(target)
