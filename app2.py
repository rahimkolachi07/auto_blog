from gemini.gemini import *
import pandas as pd
from app import *
import os
from image_gen import *

def text_writer(title,subtit):
        time.sleep(60)
        print("p1")
        subpra1=g_modelpr(f"Compose three professional paragraphs on the topic of {title}, maintaining a tone that is both approachable and sophisticated. Utilize simple language to ensure clarity and readability, akin to conversing with a friend. Strive for precision and coherence in your writing, capturing the essence of the subject matter effectively. must be seo optimized, add keywords.dont mention paragraph word")
        time.sleep(60)
        print("p2")
        subpra2=g_model(f"Compose three professional paragraphs on the topic of {subtit[0]}, maintaining a tone that is both approachable and sophisticated. Utilize simple language to ensure clarity and readability, akin to conversing with a friend. Strive for precision and coherence in your writing, capturing the essence of the subject matter effectively. must be seo optimized, add keywords.dont mention paragraph word,it will be great to give titles to those paragraphs")

        time.sleep(60)
        print("p3")
        subpra3=g_model(f"Compose three professional paragraphs on the topic of {subtit[1]}, maintaining a tone that is both approachable and sophisticated. Utilize simple language to ensure clarity and readability, akin to conversing with a friend. Strive for precision and coherence in your writing, capturing the essence of the subject matter effectively. must be seo optimized, add keywords.dont mention paragraph word,it will be great to give titles to those paragraphs")
        time.sleep(60)
        print("p4")
        subpra4=g_model(f"Compose three professional paragraphs on the topic of {subtit[2]}, maintaining a tone that is both approachable and sophisticated. Utilize simple language to ensure clarity and readability, akin to conversing with a friend. Strive for precision and coherence in your writing, capturing the essence of the subject matter effectively. must be seo optimized, add keywords.dont mention paragraph word,it will be great to give titles to those paragraphs")
        time.sleep(60)
        print("p5")
        subpra5=g_model(f"Compose three professional paragraphs on the topic of {subtit[3]}, maintaining a tone that is both approachable and sophisticated. Utilize simple language to ensure clarity and readability, akin to conversing with a friend. Strive for precision and coherence in your writing, capturing the essence of the subject matter effectively. must be seo optimized, add keywords. dont mention paragraph word,it will be great to give titles to those paragraphs")
        return title,subtit,subpra1,subpra2,subpra3,subpra4,subpra5
def noise(data):
    data=str(data).replace("*"," ")
    data=str(data).replace("#"," ")
    data=str(data).replace("-"," ")
    data=str(data).replace("["," ")
    data=str(data).replace("]"," ")
    return data


cat1=["generative AI","large languge model","huggingface","AI transformers", "Tensorflow","pytorch","sklearn","computer vision","natural language processing","ai arts","robotics","automation","website development","software development","app development","digital marketing",]
for i,cat in enumerate(cat1):         
    if os.path.exists("ai_post.csv"):
            topics=pd.read_csv("ai_post.csv")
    else:  
        topics=g_modelpr(f"write 200 topics on {cat} subjects. its technical subject related with understanding the concept of {cat}. must be comma seperated. dont give numbering. just return topic names")
        titles_list = topics.split(',')
        titles = pd.DataFrame(titles_list, columns=['Title'])
        titles.to_csv('ai_post.csv', index=False, encoding='utf-8')
        topics=pd.read_csv("ai_post.csv")

    for row_n in range(len(topics["Title"])):
        try:
            if topics["Title"][row_n]=="done":
                pass
            else:
                print(topics["Title"][row_n])
                topic_name=topics["Title"][row_n]
                subtopics=g_model(f"write 4 sub topics on main topic = {topic_name}. sub topic should be related with topic and must be technical. its technical subject. must be comma seperated. dont give numbering. just return topic names")
                subtitles_list = subtopics.split(',')
                image_gen("generate image with 4k quality. focused on the topic. catchy image on "+topic_name+" best impressive image on "+topic_name)
                time.sleep(60)
                #image_id=upload_image("image/feature_image.png")
                top,subt,p1,p2,p3,p4,p5=text_writer(topics["Title"][row_n],subtitles_list)
                top=noise(top)
                p1=noise(p1)
                p2=noise(p2)
                p3=noise(p3)
                p4=noise(p4)
                p5=noise(p5)
                blog_post(top,subt,p1,p2,p3,p4,p5)
                topics["Title"][row_n]="done"
                topics.to_csv("ai_post.csv",index=False)
        except Exception as e:
            print("error=",e)
    os.remove("ai_post.csv")



