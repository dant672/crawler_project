#string search to get new url

def get_next_target (s):
	start_link = s.find('<a href=');
	#if you dont find a link return return None, 0
	if start_link = -1:
		return None, 0;
	start_quote = s.find('"', start_link);
	end_quote = s.find('"', start_quote);
	url = page[start_quote + 1, end_quote];

	return end_quote, url;

#the mission of get_all_links is to take a seed page, if the seed page has a link(as judged by get_next_target)
#it adds the link to a link array and moves the page forward which it than calls again as page in the while loop
#it ultimately returns all the links 

def get_all_links (page):
	links = [];
	while True:
		url, end_quote = get_next_target(page)
		if url:
			links.append(url);
			#move page along
			page = page[end_quote:];
		else:
			break;
		return links

#crawl_web makes 2 arrays, 1 of pages to crawl, one that you've already called as to not crawl again

def get_page(url):
	try:
		import urllib
		return urllib.urlopen(url).read()
	except:
		return;

def crawl_web (seed):
	tocrawl = [seed];
	crawled = [];
	index = {};
	graph = {};
	while tocrawl:
		# use pop to remove element from list and it assigns that element to the variable page
		page = tocrawl.pop();
		#ionly crawl the page if it has not been crawled
		if page not in crawled:
			content = get_page(page);
			#take the page and take the content of that page and add it to the index.
			add_page_to_index(index, page, content);
			#union procedure allows us to add new links from that new page to the crawl array
			union (tocrawl, get_all_links(content));
			#then add that page to the crawled list
			crawled.append(page);
		return index;


#add_to_index updates the index with a url's to keywords that already exist, or it adds a keyword and url if 
#it's a new keyword that doesn't exist in the index

def add_to_index(index, keyword, url):
	if keyword in index:
		index[keyword].append(url)
	else
	#not found, add new keyword to index
		index[keyword] = [url];
#look up searches the index for the keyword, if it finds something it returns a list of urls

def lookup(index, keyword):
	if keyword in index:
		return index[keyword];
	else:
		return None;

#modify the index to include the words on that page of the url. it calls add_to_index

def add_page_to_index(index, url, content):
	words = content.split();
	for word in words:
		add_to_index(index, word, url)

def test_hash_function (func, keys, size):
	results = [0] * size
	keys_used = []
	for w in keys:
		if w not in keys_used:
			hv = func(w, size)
			results[hv] = results[hv] + 1
			keys_used.append(w)
	return results

#ord is a built in function that inputs a letter and outputs a number
#chr is a built in function that inputs a number and outputs a character


#hash string takes a keyword and a number of buckets and maps the keyword to the position that it should be in the table
def hash_string(keyword, buckets):
	sum = 0;
	for e in keyword:
		sum = sum + ord(e);
	return sum % buckets;

#creates an empty table with that many buckets
def make_hashtable(nbuckets):
	list = [];
	i = 0;
	for unused in range(0, nbuckets):
		list.append([]);
	return list;

def hashtable_get_bucket(table, keyword):
	return table[hash_string(keyword, len(table)];

def hashtable_add(htable, key, value):
	bucket = hashtable_get_bucket(htable, key)
	bucket.append([key, value]);

def hashtable_lookup(htable, key):
	bucket = hashtable_get_bucket(htable, key);
	for entry in bucket:
		if entry[0] == key:
			return entry[1];
	return None;
def hashtable_update(htable, key, value):
	bucket = hashtable_get_bucket(htable, key);
	for entry in bucket:
		if entry[0] == key:
			entry[1] = value;
			return;
	bucket.append([key, value]);

def union (p, q):
	for e in p:
		if e not in q:
			q.append(e);
	return q;



#

def when_offered(courses, course):
	offered = []
	for hexamester in courses:
		if course in courses[hexamester]:
			offered.append(hexamester);
	return offered;

def involved(courses, person):
	output = {};
	for hexamester in courses:
		#go through each course
		for course in courses[hexamester]:
			#go through each key in the name value pair
			for key in courses[hexamester][course]:
				if courses[hexamester][course][key] == person:
					if hexamester in output:
						output[hexamester].append(course)
					else:
						#adding a value to the name value pair
						output[hexamester] = [course]
	return output;


def cached_execution(cache, proc, proc_input):
	if proc_input not in cache:
		cache[proc_input] = proc(proc_input)
	return cache[proc_input];

def is_palindrome(s):
	if s = '':
		return True;
	else:
			if s[0] == s[-1]:
				return is_palindrome(s[1:-1])
			else return False;


def fibonacci(n):
	current = 0;
	after = 1
	for i in range(0, n):
		current, after = after, current + after;
	return current;




			