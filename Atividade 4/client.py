
import greete_pb2_grpc
import greete_pb2
import time
import grpc

def get_client_stream_requests():
    while True:
        name = input("Por favor insira um nome (ou nada para parar de conversar): ")

        if name == "":
            break

        hello_request = greete_pb2.HelloRequest(greeting = "Hello", name = name)
        yield hello_request
        time.sleep(1)

def run():
    with grpc.insecure_channel('localhost:5555') as channel:
        stub = greete_pb2_grpc.GreeterStub(channel)
        print("1. SayHello")  #diga olá
        print("2. ParrotSaysHello - Server Side Streaming") #stream do lado do servidor
        print("3. ChattyClientSaysHello - Client Side Streaming") #stream do lado do cliente
        print("4. InteractingHello - Both Streaming")# ambos transmitindo
        rpc_call = input("Qual rpc você gostaria de fazer?: ")

        if rpc_call == "1":
            hello_request = greete_pb2.HelloRequest(greeting = "hello", name = "Lucas")
            hello_reply = stub.SayHello(hello_request)
            print("SayHello Response Received:")
            print(hello_reply)
        elif rpc_call == "2":
            hello_request = greete_pb2.HelloRequest(greeting = "hello", name = "Lucas")
            hello_replies = stub.ParrotSaysHello(hello_request)

            for hello_reply in hello_replies:
                print("ParrotSaysHello Response Received:")
                print(hello_reply)
        elif rpc_call == "3":
            delayed_reply = stub.ChattyClientSaysHello(get_client_stream_requests())

            print("ChattyClientSaysHello Response Received:")
            print(delayed_reply)
        elif rpc_call == "4":
            responses = stub.InteractingHello(get_client_stream_requests())

            for response in responses:
                print("InteractingHello Response Received: ")
                print(response)

if __name__ == "__main__":
    run()
