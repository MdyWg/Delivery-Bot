import speech_recognition as sr
import rclpy
from rclpy.node import Node
from std_msgs.msg import ByteMultiArray, String

class SpeechRecognition(Node):
    def __init__(self):
        super().__init__('speech_recognition')
        self.speech_sub = self.create_subscription(ByteMultiArray, 'microphone/speech_audio', self.speech_callback, 10)
        self.speech_pub = self.create_publisher(String, 'speech/recognized_text', 10)
        self.r = sr.Recognizer()

    def speech_callback(self, msg):
        wav_bytes = b''.join(msg.data)
        audio = sr.AudioData(wav_bytes, sample_rate=16000, sample_width=2)
        try:
            result = self.r.recognize_whisper(audio, model="small", show_dict=True, load_options={"device": "cuda"})
            text = result['text']
            self.get_logger().info(f"Recognized speech: {text}")
            self.speech_pub.publish(String(data=text))
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