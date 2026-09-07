import speech_recognition as sr
import whisper
import numpy as np
import rclpy
from rclpy.node import Node
from std_msgs.msg import ByteMultiArray, String

class SpeechRecognition(Node):
    def __init__(self):
        super().__init__('speech_recognition')
        self.speech_sub = self.create_subscription(ByteMultiArray, 'microphone/speech_audio', self.speech_callback, 10)
        self.speech_pub = self.create_publisher(String, 'speech/recognized_text', 10)
        self.r = sr.Recognizer()

        self.model = whisper.load_model("small.en", device="cuda")
        self.get_logger.info("whisper model loaded")

    def speech_callback(self, msg):
        wav_bytes = b''.join(msg.data)
        audio = sr.AudioData(wav_bytes, sample_rate=16000, sample_width=2)
        try:
            audio_np = np.frombuffer(audio.get_raw_data(convert_rate=16000, convert_width=2), np.int16).astype(np.float32) / 32768.0
            result = self.model.transcribe(audio_np, fp26=True)
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