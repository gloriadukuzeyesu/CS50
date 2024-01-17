from django.shortcuts import render
from django.shortcuts import redirect
from markdown2 import Markdown
from . import util
import random



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_wiki_entry(request, title):
    html_content = convert_mark_down_to_Html(title)
    if html_content is None:
        return render(request, "encyclopedia/pageNotFound.html", {
            "error_message" : "This entry does not exist!"
        })
    else:
        return render(request, "encyclopedia/entryTemplate.html", {
            "title" : title, 
            "content" : html_content
        })
    
    
def convert_mark_down_to_Html(title):
    content = util.get_entry(title)
    markdowner = Markdown()
    if content is None:
        return None
    else:
        return markdowner.convert(content)
    

# Search 

def search(request):
    if request.method == "POST":
        searched_encyclopedia_entry = request.POST['q'] #grab the data from the form using request.POST
        html_content = convert_mark_down_to_Html(searched_encyclopedia_entry)
        if html_content is not None:
              return render(request, "encyclopedia/entryTemplate.html", {
                "title" : searched_encyclopedia_entry, 
                "content" : html_content
            })
        else:
            entry_list = util.list_entries() # a list of all entries 
            recommended_entry = [] 
            for entry in entry_list:
                if searched_encyclopedia_entry.lower() in entry.lower():
                    recommended_entry.append(entry)
    
    return render(request, "encyclopedia/search.html", {
        "recommendations" : recommended_entry
    })  
    
def new_page(request):
    if request.method == "GET":
        #  # user should be able to create a new page 
        return render(request, "encyclopedia/new_page.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        # verify is the entry already exist. 
        existing_content = util.get_entry(title)
        if existing_content is not None:
            # already exists
            return render(request, "encyclopedia/pageNotFound.html", {
                "error_message" : "Entry Page already Exists"
            })
        else:
            util.save_entry(title, content) 
            html_content = convert_mark_down_to_Html(title)
            return render(request, "encyclopedia/entryTemplate.html", {
                "title" : title, 
                "content" : html_content
            })
            
def edit(request):
    if request.method == "POST":
        title = request.POST['existing_entry_title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title" : title, 
            "content" : content
        })
        
        
def save_edits(request):
    if request.method == "POST":
        title = request.POST['entry_title']
        content = request.POST['content']
        util.save_entry(title, content)
        html_content = convert_mark_down_to_Html(title)
        return render(request, "encyclopedia/entryTemplate.html", {
            "title" : title, 
            "content" : html_content
        })
        
        
def random_page(request):
    all_entries_page = util.list_entries()
    random_entry_page = random.choice(all_entries_page)
    html_content = convert_mark_down_to_Html(random_entry_page)
    return render(request, "encyclopedia/entryTemplate.html", {
        "title" : random_entry_page, 
        "content" : html_content
    })

                

    

        
        
            
                    
            
    
    
    
    


