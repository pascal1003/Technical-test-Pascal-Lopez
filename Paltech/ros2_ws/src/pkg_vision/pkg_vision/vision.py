import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class VisionNode(Node):

    def __init__(self):
        super().__init__('vision')
        
        # Publisher al tópico "imagen"
        self.publisher_ = self.create_publisher(String, 'imagen', 10)

        # Timer de 1 segundo
        self.timer = self.create_timer(1.0, self.timer_callback)

        self.get_logger().info("Nodo vision iniciado y publicando en 'imagen'")

    def timer_callback(self):
        msg = String()
        msg.data = "hola"

        self.publisher_.publish(msg)
        
        # Imprimir
        self.get_logger().info(f"Publicado: {msg.data}")


def main(args=None):
    rclpy.init(args=args)
    node = VisionNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()