from mechanicalsoup import StatefulBrowser
import browser_cookie3 as browsercookie

bro = StatefulBrowser()

# # Requests / browsercookie setup
cj = browsercookie.chrome()
# # Set cookiejar from argument vector.
bro.set_cookiejar(cj)

def wl():
	WL = bro.get('https://www.youtube.com/playlist?list=WL')

	# # YouTube
	links = WL.soup.find_all('tr', {'class': 'pl-video', 'data-title':True})
	no_video = ('[Deleted video]', '[Private video]')

	for link in links:
		path = link['data-title']
		img = 'No data' if path in no_video else link.find('img')['data-thumb']
		path = link.find('a')['href']
		yield (img, path)

if __name__ == '__main__':
	for i in wl():
		print(i)
		print()
