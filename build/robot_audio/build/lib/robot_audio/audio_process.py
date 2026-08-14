import speech_recognition as sr
import rclpy
from rclpy.node import Node

class SpeechRecognition(Node):
    def __init__(self):
        super().__init__('speech_recognition')
        self.speech_sub = self.create_subscription(ByteMultiArray, 'microphone/speech_audio', self.speech_callback, 10)
        self.face_pub = self.create_publisher(String, 'speech/recognized_text', 10)
        self.r = sr.Recognizer()

    def speech_callback(self, msg):
        wav_bytes = bytes(msg.data)
        audio = sr.AudioData(wav_bytes)
        try:
            text = self.r.recognize_whisper(audio)
            self.get_logger().info(f"Recognized speech: {text}")
            self.face_pub.publish(String(data=text))
        except sr.UnknownValueError:
            self.get_logger().warn("Whisper could not understand audio")
        except sr.RequestError as e:
            self.get_logger().error(f"Whisper error: {e}")

def main(args=None):
    rclpy.init(args=args)
    speech_rec = SpeechRecognition()
    rclpy.spin(speech_rec)
    speech_rec.destroy_node()
    rclpy.shutdown()