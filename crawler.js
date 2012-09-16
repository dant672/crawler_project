function getNextTarget (s){
	var startLink = s.indexOf('<a href=');
		if (startLink == -1){
			return false, 0;
		}
	var startQuote = s.indexOf('"', startLink + 1);
	var endQuote = s.indexOf('"', startQuote + 1);
	url = s[startQuote + 1, endQuote];

	return end_quote, url;
};



//captures all the links on a page
function getAllLinks (page){
	var links = [];
	while (true){
		url, end_pos = getNextTarget (page);
		if(url != ''){
			links.push(url);
			page = page[end_pos];
		};
		else{
			break;
		}
	}
	return links;
}

//decides whether or not to crawl that page. seed == a site, say match.com. We check if match.com has been crawled. if not we add all the links
//on match.com, which we've extracted with the getAllLinks function and added them to tocrawl array. Then we through away the match.com page
//into the crawled array.
function crawlWeb (seed){
	var toCrawl = [seed];
	var crawled = [];
	while (toCrawl.length > 0){
		var page = toCrawl.pop();
		for(var i = 0; i < crawled.length; i++){
			if (page == crawled[i]){
				return crawled;
			}
			else{
				union(tocrawl, getAllLinks(page))
				crawled.push(page);

			}
		}

		

	}

};

function union (p, q){
	var match = false;
	for(var i = 0; i < p.length; i++){
		for(var j = 0; j < q.length; j++){
			if(p[i] == q[j]){
				match = true;
			}
		}
			if(match == false){
				q.push(p[i]);
			} 
	}
}

