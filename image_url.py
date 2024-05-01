from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
from wordpress_xmlrpc.methods.media import UploadFile
from gemini.gemini import *

# WordPress site URL and credentials
wordpress_url = 'http://hecktobyte.pk/xmlrpc.php'
wordpress_username = 'rahim'
wordpress_password = 'kolachi123'

def upload_image(client, image_path):
    # Upload image to WordPress
    with open(image_path, 'rb') as img:
        data = {
            'name': 'image.jpg',
            'type': 'image/jpeg',  # Change the type accordingly
        }
        response = client.call(UploadFile(data, img))
        return response['id']

def blog_post(top, subt, p1, p2, p3, p4, p5, image_paths):
    print("uploading")
    # Create WordPress client
    client = Client(wordpress_url, wordpress_username, wordpress_password)

    # Upload images and get their attachment IDs
    image_ids = []
    for image_path in image_paths:
        image_id = upload_image(client, image_path)
        image_ids.append(image_id)

    # Create a new WordPress post
    post = WordPressPost()

    post.title = top
    post.content = f"""
    <p align="justify">{p1}</p>

    <h3>{subt[0]}</h3>
    <p align="justify">{p2}</p>

    <img src="{image_ids[0]}" alt="Image 1"/>

    <h3>{subt[1]}</h3>
    <p align="justify">{p3}</p>

    <img src="{image_ids[1]}" alt="Image 2"/>

    <h3>{subt[2]}</h3>
    <p align="justify">{p4}</p>

    <img src="{image_ids[2]}" alt="Image 3"/>

    <h3>{subt[3]}</h3>
    <p align="justify">{p5}</p>

    <img src="{image_ids[3]}" alt="Image 4"/>
    """
    post.post_status = 'publish'  # Change to 'draft' if you want to save as draft

    # Publish the post
    post_id = client.call(NewPost(post))
    print("Post created successfully!")
    print("New post ID:", post_id)

# Example usage:
blog_post("Title", ["SubTitle 1", "SubTitle 2", "SubTitle 3", "SubTitle 4"],
          "Paragraph 1", "Paragraph 2", "Paragraph 3", "Paragraph 4", "Paragraph 5",
          ["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpg"])
