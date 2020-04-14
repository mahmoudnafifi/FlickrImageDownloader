import flickrapi
import urllib.request
import os

keyword = 'sunset' #modify it with your new keyword(s)
key = 'here you will enter the key code generated in step 2, see the readme file for more details'
secret = 'here you will enter the secret code generated in step 2, see the readme file for more details'
if not os.path.isdir(keyword):
    os.mkdir(keyword)

# Flickr api access key 
flickr=flickrapi.FlickrAPI(key, secret, cache=True)

count = 0
photos = flickr.walk(text=keyword, # you can change these options, see more details from here: https://www.flickr.com/services/api/flickr.photos.search.html
                     tag_mode='all',
                     tags=keyword,
                     extras='url_sq',
                     per_page=4000,           
                     sort='relevance',
                     privacy_filter=1,
                     license=(3,4))

for photo in photos:
        try:
            url=photo.get('url_sq')
            urllib.request.urlretrieve(url, keyword + '\\' + str(count) +".jpg")
            count = count + 1
        except Exception as e:
            print('Error: Failed to download the image!')
