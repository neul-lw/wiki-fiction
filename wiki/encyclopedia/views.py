from django.shortcuts import render

from . import util
import markdown 


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
})


def title(request, page): 
    """ 
    Should retrieve the page title via util function 
    If content exists 
        returns 
        Page contents 
        title 

    if not 
        error 
    """
    if util.get_entry(page):
        md_to_html = markdown.markdown(util.get_entry(page))
        return render(request, "encyclopedia/page.html", { 
        "title": page,
        "content": md_to_html})
    return None # TODO: Should return page for error 
