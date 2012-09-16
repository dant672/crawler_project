page = " ";

start_link = page.find('<a href=');
start_quote = page.find('"', start_link);
end_quote = page.find("", start_quote + 1);
url = page[start_quote + 1 : end_quote];

print url;

page =  page [end_quote:];

def get_next_target (s):
	start_link = s.find('<a href=');
	if start_link = -1:
		return None, 0;
	start_quote = s.find('"', start_link);
	end_quote = s.find('"', start_quote + 1);
	url = s[start_quote + 1, end_quote];

	return end_point, url;

def get_all_links (page):
	links = []
	while True:
		url, end_pos = get_next_target(page);
		if url:
			links.append(url);
			page = page[end_pos:];
		else:
			break;

print_all_links(get_page('http://match.com'));



def factorial (n):
	if (n == 1):
		return 1;
	else:
		return n * factorial(n - 1);

def new_factorial (n):
	result = 1;
	while n >= 1:
		result = result * n;
		n = n - 1;
	return result;

/for key in array loops through each array

def measure_uppers(U):
	count = 0;
	for e in U:
		if e[0] == 'U':
			count += 1;
	return count;

def find_element (p, t):
	i = 0;
	while i < len(p):
		if p[i] == t:
			return i;
		i += 1;
		return -1;

def find_element_for (p,t):
	i = 0;
	for e in p:
		if e == t:
			return i;
			i += 1;
		else:
			return -1;
def find_element_index (p, t):
	if t in p:
		return p.index(t);
	else: 
		return -1;
def find_element_index_not (p,t):
	if t not in p:
		return -1;
	return p.index(t);

def union (p, q):
	for e in q:
		if e not in p:
			p.append(e);