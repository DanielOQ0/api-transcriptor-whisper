from src.protocode import audio_pb2_grpc 
from src.services.Greeter import Greeter
from concurrent import futures
import grpc

port = "50051"
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
audio_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
server.add_insecure_port("[::]:" + port)
server.start()
print("gRPC server started, listening on " + port)
server.wait_for_termination()