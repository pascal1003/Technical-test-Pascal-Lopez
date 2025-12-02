import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Receptor(Node):

    def __init__(self):
        super().__init__('receptor')
        self.subscription = self.create_subscription(
            String,
            'imagen',
            self.listener_callback,
            10
        )
        self.get_logger().info("Nodo receptor iniciado y escuchando 'imagen'")

    def listener_callback(self, msg):
        self.get_logger().info(f"Recibido: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = Receptor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()