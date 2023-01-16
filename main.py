#-----------------------------
#IMPORT LIBRARIES
#import streamlit
import websockets
import asyncio
from collections import deque
import streamlit as st
#specklepy libraries
from specklepy.api.client import  SpeckleClient
from specklepy.api.credentials import get_account_from_token
from specklepy.objects import Base
from specklepy.objects.geometry import Point
from specklepy.transports.server import ServerTransport
from specklepy.api import operations
#import pandas
import pandas as pd
# import plotly express
import plotly_express as px
import json
from client import listen

# -----------------------------------------------

#SERVER

#------------------------------------------------
st.set_page_config(
    page_title=" 🧼 Winter Garden Activity @ UMEA",
    page_icon="🧼",
    layout= "wide"
)
#------------------------------------------------

#CONTAINERS

header= st.container()
miro_slide  = st.container()
viewer = st.container()
viewer2=st.container()
report = st.empty()
graphs = st.container()

#------------------------------------------------

#HEADER
#Page Header

with header:
    st.title("Winter Garden Activity @ UMEA ❄")

# About info

with header.expander("About this app 🔽", expanded=True):

    st.markdown(

        """ The Winter Garden Project is a device for the collective practice and public engagement.
        """
        """ The object will investigate how urban winter gardens can have a regenerative social impact in Nordic, urban contexts, and how temporary structures can help us formulate new responsive, ecological environments."""
    )

#----------------------------------



# Collect Inputs

# async def render_points():
#         url="ws://winter-garden-server.glitch.me"
#         async with websockets.connect(url) as websocket:
#             await websocket.send("hello server")
#             while True:
#                 msg = await websocket.recv()
#                 #print((msg))
#                 return msg


# with miro_slide:

#     st.subheader("Winter Garden Slide Presentation")
    
#     miro_frame="https://miro.com/app/live-embed/uXjVPIM8c1s=/?moveToViewport=6988,3966,738,494&embedId=203702165751"
#     #st.subheader("Inputs")
#     st.components.v1.iframe(miro_frame,height=400)
#     #----------------
#     #<iframe width="768" height="432" src="https://miro.com/app/live-embed/uXjVPIM8c1s=/?moveToViewport=6988,3966,738,494&embedId=203702165751" frameborder="0" scrolling="no" allow="fullscreen; clipboard-read; clipboard-write" allowfullscreen></iframe>
#     #Columns for inputs
#     #serverCol,tokenCol = st.columns([1,3])

#     #----------------

#     #User input boxes

speckleServer= "speckle.xyz"#serverCol.text_input("Server URL", "speckle.xyz", help="Speckle server to connect.")

speckleToken="a3d8170e6b12393d5dbd45b9480c71bd47185bf110" #tokenCol.text_input("Speckle token","Please enter your token here", help="If you don't know how to get your token, take a look at this [link](<https://speckle.guide/dev/tokens.html>)👈")
    #----------------

    ###  interacting with speckle Server ###

    #CLIENT //

client= SpeckleClient(host=speckleServer)

#Get account from Token

account=get_account_from_token(speckleToken,speckleServer)

#Authenticate

client.authenticate_with_token(str(speckleToken))

# --------------- Object ---------------

#----------------

#Stream lists

streams=client.stream.list(stream_limit=10)
#print (streams)
#Get Stream Names

stream_id= [s.id for s in streams if s.name =="Winter Garden" ]

#sName=client.stream.search("Winter_Garden") #st.selectbox(label="Select your stream", options=streamNames,help="Select your Stream from the dromdown menu")

#Selected stream
#print (stream_id[0])
stream=client.stream.get(stream_id[0])

#Stream Branches
branches=client.branch.list(stream.id)
#print (stream_id)
#Stream Commits
commits= client.commit.list(stream_id[0],limit=100)
    #Embedded Iframe

def commit2viewer(stream,commit,height=400)-> str:

    embed_src="http://speckle.xyz/embed?stream="+str(stream.id)+"&commit="+str(commit.id)+"&autoload=true"
    #embed_src="https://speckle.xyz/embed?stream=8dd22c09e4&commit=f42a6e31b6"
    return st.components.v1.iframe(src=embed_src,height=height)
        
# with viewer:
#     st.subheader("Winter Garden Digital Twin")
#     commit2viewer(stream, commits[0])

def commit2viewer2(stream,commit,height=400)-> str:

    embed_src="http://speckle.xyz/embed?stream="+str(stream.id)+"&commit="+str(commit.id)+"&autoload=true"
    #embed_src="https://speckle.xyz/embed?stream=8dd22c09e4&commit=f42a6e31b6"
    return embed_src
with viewer2:

    miroCol, speckleCol = st.columns(2)
    miroCol.subheader("Winter Garden Slide show")
    miroCol._iframe("https://miro.com/app/live-embed/uXjVPIM8c1s=/?moveToViewport=6988,3966,738,494&embedId=203702165751",height=540)
    speckleCol.subheader("Winter garden Digital twin")
    speckleCol._iframe(commit2viewer2(stream,commits[0]),height=540)

    



    #VIEWER

async def render_points():
        url="ws://winter-garden-server.glitch.me"
        async with websockets.connect(url) as websocket:
            await websocket.send("hello server")
            while True:
                msg = await websocket.recv()
                with report:
                    st.text(msg)
                print(msg)
                # return msg

# asyncio.get_event_loop().run_until_complete(render_points())

# # async def listen():

# #     async with websockets.connect(url) as websocket:
# #         await websocket.send("hello server")
# #         while True:
# #             msg = await websocket.recv()
# #             mydic={"values": msg }
# #             print (msg)
# #             with open("incomming_0","w") as outfile:
# #                 json.dump(mydic,outfile)


# #asyncio.get_event_loop().run_until_complete(listen())
