#!/bin/bash
git add .
git commit -m " 💠 121 >> Practice05 Django Templates | commit = 5
context = {
    'page_name': 'About',
    'description': 'This part is about our team.'
}
return render(request, 'pages/about.html', context)
     "
git push -u origin main 
