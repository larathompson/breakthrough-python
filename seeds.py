from datetime import datetime

#  can you add a new blog post to the list? 
#  can you update the content of the blog posts? 
#  can you add more fields to the blog posts? For example, you can add a field for the author of the blog post? Or how many views the blog post has?
blog_posts = [
    {
        "id": 1,
        "title": "My first blog post",
        "description": "Learning how to be a blogger",
        #  can you find different images and save them as svgs as we have done here? 
        "image": "static/images/train.svg",
        "content": "Welcome to our first blog post content.",
        "date_posted": datetime(2024, 11, 28)
    },
    {
        "id": 2,
        "title": "Learning how to code",
        "description": "This tells the journey of learning how to code",
        "image": "https://placehold.co/600x400",
        "content": "Learning to code is a journey. And an exciting one!",
        "date_posted": datetime(2024, 11, 29)
    }
]