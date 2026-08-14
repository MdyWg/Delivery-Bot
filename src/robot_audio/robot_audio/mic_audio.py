import os 
import time
import speech_recognition as sr
import rclpy
from rclpy.node import Node
from std_msgs.msg import ByteMultiArray

class MicrophoneNode(Node):
    def __init__(self):
        super().__init__('microphone_node')
        
        self.mic_pub = self.create_publisher(ByteMultiArray, 'microphone/speech_audio', 10)

        self.m = None
        self.r = sr.Recognizer()
        for i, microphone_name in enumerate(sr.Microphone.list_microphone_names()):
            print(i, microphone_name)
            if "Lavalier" in microphone_name:
                self.m = sr.Microphone(device_index=i)
                break

        if self.m is None:
            raise RuntimeError("Lavalier microphone not found.")

        with self.m as source:
            self.r.adjust_for_ambient_noise(source)

        self.stop_listening = self.r.listen_in_background(self.m, self.callback)

    def callback(self, recognizer, audio):
        raw_bytes = audio.get_raw_data(convert_rate=16000, convert_width=2)
        self.mic_pub.publish(ByteMultiArray(data=raw_bytes))


def main(args=None):
    rclpy.init(args=args)
    mic_pub = MicrophoneNode()
    rclpy.spin(mic_pub)
    mic_pub.destroy_node()
    rclpy.shutdown()


    