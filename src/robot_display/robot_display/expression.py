import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Expression(Node):
    def __init__(self):
        super().__init__('expression')
        self.intent_sub = self.create_subscription(String, 'speech/intent', self.face_callback, 10)
        self.status = "idle"
    
    def face_callback(self, msg):
        intent = msg.data
        self.status = self.determine_status(intent)
    
    def determine_status(self, intent):
        if intent == "greeting":
            return "happy"
        elif intent == "farewell":
            return "sad"
        elif intent == "tired":
            return "tired"
        return "idle"

