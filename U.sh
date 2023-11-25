#!/bin/bash
git add .
git commit -m " 💠 121 >> Practice07 Image-9 if DoesNotExist pk way_1
try:
    post = Post.objects.get(pk=pk)
except ObjectDoesNotExist:
    post = None
"
git push -u origin main 
