import os 
import time
import speech_recognition as sr
import rclpy
from rclpy.node import Node

class MicrophoneNode(Node):
    def __init__(self):
        super().__init__('microphone_node')
        
        self.mic_pub = self.create_publisher(ByteMultiArray, 'microphone/speech_audio', 10)

        m = None
        for i, microphone_name in enumerate(sr.Microphone.list_microphone_names()):
            print(i, microphone_name)
            if "Lavalier" in microphone_name:
                m = sr.Microphone(device_index=i)
                break

        if m is None:
            raise RuntimeError("Lavalier microphone not found.")

    def callback(recognizer, audio):
        raw_bytes = audio.get_raw_data()
        self.mic_pub.publish(ByteMultiArray(data=list(raw_bytes)))

    r = sr.Recognizer()
    with m as source:
        r.adjust_for_ambient_noise(source)

    stop_listening = r.listen_in_background(m, callback)

def main(args=None):
    rclpy.init(args=args)
    mic_pub = MicrophoneNode()
    rclpy.spin(mic_pub)
    mic_pub.destroy_node()
    rclpy.shutdown()


    