import streamlit as st
from main import *

st.set_page_config(page_title="TENJIDAN", layout="wide")

with st.container(): 
    st.write("---")
    st.title("TENJIDAN")
    st.subheader("""Welcome to TENJIDAN - A school starboard page""")
    st.write("""Everyone has is privy to freedom of speech. Here, you can share your opinions and suggestions about the school
            and learning environment. Worry not, because all of the posts are anonymous ;-) . """)
    st.write("---")

col1, col2, col3=st.columns((1, 1, 7))
mode=1
with st.container(): 
    with col1: 
        if(st.button("Hot")): 
            mode=1
    with col2: 
        if(st.button("New")):
            mode=2   
    with col3: 
        if(st.button("Best")): 
            mode=3
    
col4, col5=st.columns((1, 1))
with st.container():         
        with col5: 
            st.subheader("CREATE A POST/SHARE YOUR OPINIONS")
            topic=st.text_input('Topic', 'Your Topic')
            opinion=st.text_input('What would you like to share?', 'Your opinions')
            if(st.button("Share")): 
                temp=mode
                mode=0
                mode=temp
                makePost([0, time.time()//86400, topic, opinion])
                
with col4: 
    if(mode==1): 
        change(mode)
        for i in range(len(hot)):
            with st.container(): 
                topic=getPost(i)[2]
                text=getPost(i)[3]
                st.write(topic + "------------Stars: " + str(hot[i][0]))
                st.write(text)            
                if(st.checkbox("Star",False,str(i)+str(mode))): 
                    updatePost(-1, i)
                else: 
                    updatePost(1, i)
    elif(mode==2): 
        change(mode)
        for i in range(len(hot)):
            with st.container(): 
                topic=getPost(i)[2]
                text=getPost(i)[3]
                st.write(topic + "------------Stars: " + str(hot[i][0]))
                st.write(text)
                if(st.checkbox("Star",False,str(i)+str(mode))): 
                    updatePost(-1, i)
                else: 
                    updatePost(1, i)
    elif(mode==3): 
        change(mode)
        for i in range(len(hot)):
            with st.container(): 
                topic=getPost(i)[2]
                text=getPost(i)[3]
                st.write(topic + "------------Stars: " + str(hot[i][0]))
                st.write(text)  
                if(st.checkbox("Star",False,str(i)+str(mode))): 
                    updatePost(-1, i)
                else: 
                    updatePost(1, i)

            