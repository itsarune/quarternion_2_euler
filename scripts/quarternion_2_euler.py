#!/usr/bin/env python
import rospy

from std_msgs.msg import Float64
from sensor_msgs.msg import Imu
import tf

class quarternion_2_euler:
    def __init__(self):
        rospy.init_node('quarternion_2_euler', anonymous=True)

        roll_topic = rospy.get_param("~roll_topic", "/roll")
        pitch_topic = rospy.get_param("~pitch_topic", "/pitch")
        yaw_topic = rospy.get_param("~yaw_topic", "/yaw")
        imu_topic = rospy.get_param("~imu_topic", "/imu/data")

        self.roll_pub = rospy.Publisher(roll_topic, Float64, queue_size=1)
        self.pitch_pub = rospy.Publisher(pitch_topic, Float64, queue_size=1)
        self.yaw_pub = rospy.Publisher(yaw_topic, Float64, queue_size=1)
        rospy.Subscriber(imu_topic, Imu, self.convert_2_euler)

    def convert_2_euler(self, imu_msg):
        (roll, pitch, yaw) = tf.transformations.euler_from_quaternion([imu_msg.orientation.x, imu_msg.orientation.y, \
                imu_msg.orientation.z, imu_msg.orientation.w])
        self.roll_pub.publish(roll)
        self.pitch_pub.publish(pitch)
        self.yaw_pub.publish(yaw)

if __name__ == '__main__':
    try:
        m_quarternion_2_euler = quarternion_2_euler()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
