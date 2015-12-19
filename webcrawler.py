#The page to be crawled
page =('<div id="top_bin"><div id="top_content" class="width960">' '<div class="udacity float-left"><a href="http://udacity.com">')

start_link = page.find('<a href="')
link_start = page.find('"', start_link + 8)
end = page.find('"', link_start+1)
url = page[link_start+1:end]
print url
