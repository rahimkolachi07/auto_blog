from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
from gemini.gemini import *
from image_upload import *

# WordPress site URL and credentials
wordpress_url = 'http://hecktobyte.pk/xmlrpc.php'
wordpress_username = 'rahim'
wordpress_password = 'kolachi123'



def blog_post(top,subt,p1,p2,p3,p4,p5):
    print("uploading")
    # Create WordPress client
    client = Client(wordpress_url, wordpress_username, wordpress_password)

    # Create a new WordPress post
    post = WordPressPost()

    post.title = top
    post.content = f"""
    <p align="justify">{p1}</p>

    <h3>{subt[0]}</h3>
    <p align="justify">{p2}</p>


    <h3>{subt[1]}</h3>
    <p align="justify">{p3}</p>


    <h3>{subt[2]}</h3>
    <p align="justify">{p4}</p>


    <h3>{subt[3]}</h3>
    <p align="justify">{p5}</p>


    """
    post.post_status = 'publish'  # Cshange to 'draft' if you want to save as draft
    #post.thumbnail = image_id


    # Publish the post
    post_id = client.call(NewPost(post))
    print("Post created successfully!")
    print("New post ID:", post_id)
