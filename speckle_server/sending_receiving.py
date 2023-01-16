from specklepy.api.client import  SpeckleClient
from specklepy.api.credentials import get_account_from_token
from specklepy.objects import Base
from specklepy.objects.geometry import Point
from specklepy.transports.server import ServerTransport
from specklepy.api import operations
import websockets
import asyncio

client= SpeckleClient(host="speckle.xyz")


client.authenticate_with_token("a3d8170e6b12393d5dbd45b9480c71bd47185bf110")
stream=client.stream.search("Winter Garden")
new_stream_id= stream[0].id
# new_stream=client.stream.get(id=new_stream_id)

 

# class Block(Base):

#         length:float
#         width:float
#         height:float
#         origin:Point= None

#         def __init__(self,lenght=1.0,width=1.0,height=1.0,origin=Point(), **kwargs) -> None:

#             super().__init__(**kwargs)

#             self.add_detachable_attrs({"origin"})

#             self.length = lenght
#             self.width = width
#             self.height = height
#             self.origin = origin
    

# block = Block(lenght=2,height=4,width=10)



bubble_mesh= client.commit.list(new_stream_id)[0].referencedObject
print (bubble_mesh)

transport=ServerTransport(client=client,stream_id=new_stream_id)

hash= operations.receive(bubble_mesh,remote_transport=transport)
print (type(transport))

# hash_2= operations.send(bubble_mesh,remote_transport=transport)
# print(hash.id)
# commit_id= client.commit.create(
#     stream_id=new_stream_id,
#     object_id=hash,
#     message="first oject with speckle_py"
# )

#received_base = operations.receive(obj_id=hash, remote_transport=transport)