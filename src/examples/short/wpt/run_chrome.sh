# This will run "headless" chrome and will enable to control it via
# port 9222 in a chrome protocol that tools like lighthouse or puppeteer

google-chrome \
	--headless\
	--disable-gpu\
	--remote-debugging-port=9222
