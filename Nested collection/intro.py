social_media_posts=[
    [1,"good morning",500,600,"anu"],#0
    [2,"manifestation",750,800,"manu"],#1,2
    [3,"celebrity photoshoot",450,300,"arun"],#3
    [4,"wedding",560,400,"sabu"],#4
]
print(social_media_posts[1][2])
post_names=[lst[1]for lst in  social_media_posts]
print(post_names)
fb_views=[lst[2]for lst in social_media_posts]
print(fb_views)
insta_views=[lst[3]for lst in social_media_posts]
print(insta_views)
# display the name of post having fb count is 750
fb_views=[lst[1]for lst in social_media_posts if lst[2]==750]
print(fb_views)
#print the highest insta view 
#display the highest insta view id name
max_insta_view=max([lst[3]for lst in social_media_posts])
print(max_insta_view)
max_insta_view_id_name=[lst[4] for lst in social_media_posts if lst[3]==max_insta_view]
print(max_insta_view_id_name)
#display the less fb less_fb_likes and his id name
less_fb_likes=min([lst[2]for lst in social_media_posts])
less_fb_likes_idname=[lst[4]for lst in social_media_posts if lst[2]==less_fb_likes]
print(less_fb_likes)
print(less_fb_likes_idname)





