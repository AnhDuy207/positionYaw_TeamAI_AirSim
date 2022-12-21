import rospy

from geometry_msgs.msg import Point

points_pub = rospy.Publisher("optimization_point", Point, queue_size=10)
rospy.init_node('node_generate_points')
r = rospy.Rate(30) # 10-10hz   0.033 => 30Hz

point = Point()
x1 = 0
y1 = 0
z1 = 5

while not rospy.is_shutdown():
   point.x = x1
   point.y = y1
   point.z = z1
   if x1 < 10:
      x1 = x1 + 0.02
      y1 = y1 + 0.02
      print(point.x, point.y, point.z)
   points_pub.publish(point)
   r.sleep()   
