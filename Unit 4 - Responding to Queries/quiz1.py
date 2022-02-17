# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

index = []

def add_to_index(index,keyword,url):
    keyword_list = []
    url_list = []
    
    if index:
        for k in index:
            if k[0] == keyword:
                k[1].append(url)
                return index
    if keyword_list not in index:
        index.append(keyword_list)
    if keyword not in keyword_list:
        keyword_list.append(keyword)
    if url_list not in keyword_list:
        keyword_list.append(url_list)
    if url not in url_list:
        url_list.append(url)





add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
print index
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']], 
#>>> ['computing', ['http://acm.org']]]
