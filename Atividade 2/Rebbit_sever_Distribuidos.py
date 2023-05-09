# Dupla: Guilherme Lirioberto e Lucas Ribeiro Alvino

from gc import callbacks
import psutil
import pika
import winsound


class RabbitMQ:
    def __init__(self, host='localhost', queue='minha_fila'):
        self.host = host
        self.queue = queue
        self.connection = None
        self.channel = None

    def connect(self):
        # Cria uma conexão com o servidor RabbitMQ
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(self.host))
        # Cria um canal de comunicação com o servidor RabbitMQ
        self.channel = self.connection.channel()
        # Declara a fila de mensagens no RabbitMQ
        self.channel.queue_declare(queue=self.queue)

    def send_message(self, message):
        # Envia uma mensagem contendo uma tarefa a ser realizada para a fila
        self.channel.basic_publish(
            exchange='', routing_key=self.queue, body=message)

    def receive_message(self, callback):
        # Registra o consumidor para a fila
        self.channel.basic_consume(
            queue=self.queue, on_message_callback=callback, auto_ack=True)
        # Inicia o loop de espera por mensagens
        print('Aguardando tarefas...')
        self.channel.start_consuming()

    def close(self):
        # Fecha a conexão com o servidor RabbitMQ
     if self.connection:
            self.connection.close()
    def callback(ch, method, properties, body):
        print("Tarefa recebida: %r" % body)
    def get_cpu_temperature():
        temperature = psutil.sensors_temperatures().get('coretemp')[0].current
        return temperature
        print(get_cpu_temperature())     

    def check_temperature(temperature):
       if temperature > 50:
        print('Temperatura muito alta!.')
        winsound.Beep(1000, 1000)
       else:
        print('Temperatura normal.')

       temperature = psutil.sensors_temperatures().get('coretemp')[0].current
       check_temperature(temperature)

    # Realiza o processamento da tarefa aqui
if __name__ == '__main__':
    rabbitmq = RabbitMQ()
    rabbitmq.connect()
    rabbitmq.send_message('Minha tarefa')
    rabbitmq.receive_message(callbacks)
    rabbitmq.get_cpu_temperature()
    rabbitmq.check_temperature()
    rabbitmq.close()