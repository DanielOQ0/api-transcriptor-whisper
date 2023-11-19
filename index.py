from threading import Thread
from concurrent import futures
from config import config
from src import init_app
from src.routes.TranscriptorRoutes import *
from src.protocode import audio_pb2_grpc 
from src.services.Greeter import Greeter
import grpc

configuration = config['development']
app = init_app(configuration)

def grpcserve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    audio_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("gRPC server started, listening on " + port)
    server.wait_for_termination()

if __name__ == '__main__':
    grpc_thread = Thread(target=grpcserve)
    grpc_thread.start()

    app.run(host='0.0.0.0', port=5001)
