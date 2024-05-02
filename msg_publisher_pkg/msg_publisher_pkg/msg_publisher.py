import rclpy
# import the ROS2 python libraries
from rclpy.node import Node
# import the Twist interface from the geometry_msgs package
from experiment_interfaces.msg import Num

class SimplePublisher(Node):

    def __init__(self):
        # Here you have the class constructor
        # call super() in the constructor to initialize the Node object
        # the parameter you pass is the node name
        super().__init__('simple_publisher')
        # create the publisher object
        # in this case, the publisher will publish on /cmd_vel Topic with a queue size of 10 messages.
        # use the Twist module for /cmd_vel Topic
        self.publisher_ = self.create_publisher(Num, 'topic', 10)
        timer_period = 1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Num()
        msg.num = self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%d"' % msg.num)
        self.i += 1
            
def main(args=None):
    # initialize the ROS communication
    rclpy.init(args=args)
    # declare the node constructor
    simple_publisher = SimplePublisher()
    # pause the program execution, waits for a request to kill the node (ctrl+c)
    rclpy.spin(simple_publisher)
    # Explicity destroys the node
    simple_publisher.destroy_node()
    # shutdown the ROS communication
    rclpy.shutdown()

if __name__ == '__main__':
    main()
