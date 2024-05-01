from gemini.gemini import *
import pandas as pd
from app import *
def subtopics():
    try:
        topics=pd.read_csv("ai_post.csv")
        for i,topic in enumerate(topics["Title"]):

            if topics.loc[i,"done"]=="yes":
                print("already created")
            else:
                subtopics=g_model(f"write 4 sub topics on main topic = {topic}. sub topic should be related with topic and must be technical. its technical subject. must be comma seperated. dont give numbering. just return topic names")
                print(subtopics)
                print("topic="+topic)
                subtitles_list = subtopics.split(',')
                top,subt,p1,p2,p3,p4,p5=text_writer(topic,subtitles_list)
                blog_post(top,subt,p1,p2,p3,p4,p5)
                

                topics.loc[i, 'done'] = 'Yes'
                topics.to_csv('ai_post.csv', index=False, encoding='utf-8')
                time.sleep(10*60)
    except:
         pass


def topic_develop():
    topics=g_model("write 100 topics on machine learning subjects. its technical subject related with understanding the concept of machine learning. must be comma seperated. dont give numbering. just return topic names")
    titles_list = topics.split(',')
    titles = pd.DataFrame(titles_list, columns=['Title'])
    titles['done'] = 'no'
    titles.to_csv('ai_post.csv', index=False, encoding='utf-8')

def text_writer(title,subtit):
        time.sleep(60)
        print("p1")
        subpra1=g_modelpr(f"Compose three professional paragraphs on the topic of {title}, maintaining a tone that is both approachable and sophisticated. Utilize simple language to ensure clarity and readability, akin to conversing with a friend. Strive for precision and coherence in your writing, capturing the essence of the subject matter effectively. must be seo optimized, add keywords.dont mention paragraph word")
        time.sleep(60)
        print("p2")
        subpra2=g_model(f"Compose three professional paragraphs on the topic of {subtit[0]}, maintaining a tone that is both approachable and sophisticated. Utilize simple language to ensure clarity and readability, akin to conversing with a friend. Strive for precision and coherence in your writing, capturing the essence of the subject matter effectively. must be seo optimized, add keywords.dont mention paragraph word")
        time.sleep(60)
        print("p3")
        subpra3=g_model(f"Compose three professional paragraphs on the topic of {subtit[1]}, maintaining a tone that is both approachable and sophisticated. Utilize simple language to ensure clarity and readability, akin to conversing with a friend. Strive for precision and coherence in your writing, capturing the essence of the subject matter effectively. must be seo optimized, add keywords.dont mention paragraph word")
        time.sleep(60)
        print("p4")
        subpra4=g_model(f"Compose three professional paragraphs on the topic of {subtit[2]}, maintaining a tone that is both approachable and sophisticated. Utilize simple language to ensure clarity and readability, akin to conversing with a friend. Strive for precision and coherence in your writing, capturing the essence of the subject matter effectively. must be seo optimized, add keywords.dont mention paragraph word")
        time.sleep(60)
        print("p5")
        subpra5=g_model(f"Compose three professional paragraphs on the topic of {subtit[3]}, maintaining a tone that is both approachable and sophisticated. Utilize simple language to ensure clarity and readability, akin to conversing with a friend. Strive for precision and coherence in your writing, capturing the essence of the subject matter effectively. must be seo optimized, add keywords. dont mention paragraph word")
        
        return title,subtit,subpra1,subpra2,subpra3,subpra4,subpra5


subtopics()