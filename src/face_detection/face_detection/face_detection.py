import cv2
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import os


class FaceDetector(Node):
    def __init__(self):
        super().__init__("face_detector_node")
        path = os.path.abspath('') + '/src/face_detection/face_detection/haar/haarcascade_frontalface_default.xml'
        self.face_cascade = cv2.CascadeClassifier(path)
        self.subscriber = self.create_subscription(Image, "camera/image_raw", self.callback, 10)


    def callback(self, msg):
        cv_image = CvBridge().imgmsg_to_cv2(msg, desired_encoding="bgr8")


        image_gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)       
            
            # scale_factor: Parameter specifying how much the image size is reduced at each image scale.
        scale_factor = 1.1
        # min_neighbours: Parameter specifying how many neighbors each candidate rectangle should have to retain it.
        min_neighbours = 5

        # Perform the faces detection
        faces = self.face_cascade.detectMultiScale(image_gray, scale_factor, min_neighbours)
        
        for (x,y,w,h) in faces:
            
            # Draw a rectangle at the detected location of the face
            cv2.rectangle(image_gray, (x,y), (x+w,y+h), (255, 255, 255) ,2)     


        # Show the frame
        cv2.imshow('frame', image_gray)
        
        c=cv2.waitKey(1)
        if c == 27:
            cv2.destroyAllWindows()
            #unsubscribe
            self.destroy_subscription(self.subscriber)
            


def main(args=None):
    try:
        rclpy.init(args=args)
        node = FaceDetector()
        rclpy.spin(node)
        rclpy.destroy_node(node)
        rclpy.shutdown()
    except KeyboardInterrupt:
        pass