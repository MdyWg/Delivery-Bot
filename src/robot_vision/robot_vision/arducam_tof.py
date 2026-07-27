import threading
import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, CameraInfo
import ArducamDepthCamera as ac


class ArducamToFNode(Node):
    def __init__(self):
        super().__init__('arducam_tof')

        self.depth_pub = self.create_publisher(Image, 'depth/image_raw', 10)
        self.info_pub  = self.create_publisher(CameraInfo, 'depth/camera_info', 10)

        self.cam = ac.ArducamCamera()

        ret = self.cam.open(ac.Connection.CSI, 0)
        if ret != 0:
            print("Failed to open camera. Error code:", ret)
            return

        ret = self.cam.start(ac.FrameType.DEPTH)
        if ret != 0:
            print("Failed to start camera. Error code:", ret)
            self.cam.close()
            return

        self.range  = self.cam.getControl(ac.Control.RANGE)
        self.info = self.cam.getCameraInfo()
        self.get_logger().info(f'Camera {self.info.width}x{self.info.height}')

        threading.Thread(target=self.cam_loop, daemon=True).start()

    def cam_loop(self):
        frame_count = 0
        while rclpy.ok():
            frame = self.cam.requestFrame(2000)
            if frame is not None and isinstance(frame, ac.DepthData):
                frame_count += 1
                if frame_count % 3 != 0:
                    self.cam.releaseFrame(frame)
                    continue
                depth_buf = frame.depth_data
                confidence_buf = frame.confidence_data

                depth_buf[confidence_buf < 30] = 0.0

                # SDK returns depth in mm — convert to metres for ROS
                depth_m = (depth_buf / 1000.0).astype(np.float32)

                stamp = self.get_clock().now().to_msg()

                depth_msg = Image()
                depth_msg.header.stamp = stamp
                depth_msg.header.frame_id  = 'camera_link'
                depth_msg.height = self.info.height
                depth_msg.width = self.info.width
                depth_msg.encoding = '32FC1'
                depth_msg.step = self.info.width * 4
                depth_msg.data = depth_m.tobytes()

                info_msg = CameraInfo()
                info_msg.header.stamp = stamp
                info_msg.header.frame_id = 'camera_link'
                info_msg.width = self.info.width
                info_msg.height = self.info.height
                # placeholder intrinsics — replace with calibrated values
                fx = cx = float(self.info.width) / 2.0
                fy = cy = float(self.info.height) / 2.0
                info_msg.k = [fx, 0.0, cx, 0.0, fy, cy, 0.0, 0.0, 1.0]
                info_msg.r = [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
                info_msg.p = [fx, 0.0, cx, 0.0, 0.0, fy, cy, 0.0, 0.0, 0.0, 1.0, 0.0]
                info_msg.distortion_model  = 'plumb_bob'
                info_msg.d = [0.0, 0.0, 0.0, 0.0, 0.0]
                self.depth_pub.publish(depth_msg)
                self.info_pub.publish(info_msg)
                self.cam.releaseFrame(frame)

    def destroy_node(self):
        self.cam.stop()
        self.cam.close()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = ArducamToFNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
