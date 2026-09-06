import re
import rclpy
from rclpy.node import Node

class WordIntent(Node):
    def __init__(self):
        super().__init__('word_intent')
        self.speech_sub = self.create_subscription(String, 'speech/recognized_text', self.intent_callback, 10)
        self.intent_pub = self.create_publisher(String, 'speech/intent', 10)

    def intent_callback(self, msg):
        text = msg.data.lower()
        intent = self.determine_intent(text)
        self.get_logger().info(f"Determined intent: {intent}")
        self.intent_pub.publish(String(data=intent))

    def determine_intent(self, text):
        if "hello" in text or "hi" in text:
            return "greeting"
        elif "bye" in text or "goodbye" in text:
            return "farewell"
        elif "tired" in text or re.search(r"sleep\w+", text):
            return "tired"

def main(args=None):
    rclpy.init(args=args)
    word_intent = WordIntent()
    rclpy.spin(word_intent)
    word_intent.destroy_node()
    rclpy.shutdown()