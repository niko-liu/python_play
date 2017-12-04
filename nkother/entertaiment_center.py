# encoding: utf-8
'''
Created on 2017年11月15日

@author: niko
'''
import media
import turtle

toy_store = media.Movie("玩具总动员",
                        "故事是关于一个小孩和他的玩具",
                        "http://img0.imgtn.bdimg.com/it/u=4050486633,1921528843&fm=27&gp=0.jpg",
                        "http://v.youku.com/v_show/id_XMTYzODgwNzI4.html?spm=a2h0k.8191407.0.0&from=s1.8-3-1.1")

#print toy_store.storyline
#toy_store.show_trailer()

avandar = media.Movie("avandar",
                      "",
                      "https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=3406091069,767440882&fm=27&gp=0.jpg",
                      "http://v.youku.com/v_show/id_XMTg5MDk1NDA4.html?spm=a2h1n.8261147.around_2.5~5~5~5~A")

# movies=[toy_store, avandar]
# fresh_tomatoes.create_movie_tiles_content(movies)
# fresh_tomatoes.open_movies_page(movies)

print(turtle.Turtle.__doc__)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
