#!/usr/bin/env python
import rospy

from std_msgs import Float64
from sensor_msgs import Imu
from tf_transformattions import euler_from_quarternion

class quarternion_2_euler:
    def __init__(self):
        rospy.init_node('quarternion_2_euler', anonymous=True)

        self.roll_pub = rospy.Publisher('/roll', Float64, queue_size=1)
        self.pitch_pub = rospy.Publisher('/pitch', Float64, queue_size=1)
        self.yaw_pub = rospy.Publisher('/yaw', Float64, queue_size=1)
        rospy.Subscriber('/imu/data_raw', Imu, self.convert_2_euler)

    def convert_2_euler(self, imu_msg):
        (roll, pitch, yaw) = euler_from_quarternion(imu_msg.orientation.x, imu_msg.orientation.y, \
                imu_msg.orientation.z, imu_msg.orientation.w)
        self.roll_pub.publish(roll)
        self.pitch_pub.publish(pitch)
        self.yaw_pub.publish(yaw)

if __name__ == '__main__':
    try:
        m_quarternion_2_euler = quarternion_2_euler()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
