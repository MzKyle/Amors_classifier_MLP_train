# Copyright (c) 2023 ChenJun

import rosbag2_py
import cv2
import sys

from sensor_msgs.msg import Image
from cv_bridge import CvBridge

from rosbag2_py import deserialize_message


def get_rosbag_options(path, serialization_format='cdr'):
    storage_options = rosbag2_py.StorageOptions(uri=path, storage_id='sqlite3')

    converter_options = rosbag2_py.ConverterOptions(
        input_serialization_format=serialization_format,
        output_serialization_format=serialization_format)

    return storage_options, converter_options


def main():
    bag_path = sys.argv[1]
    storage_options, converter_options = get_rosbag_options(bag_path)

    reader = rosbag2_py.SequentialReader()
    reader.open(storage_options, converter_options)

    storage_filter = rosbag2_py.StorageFilter(
        topics=['/detector/number_img'])
    reader.set_filter(storage_filter)

    bridge = CvBridge()

    count = 0
    save_path = sys.argv[2]
    print("Saving images to %s" % save_path)
    while reader.has_next():
        (topic, data, t) = reader.read_next()
        msg = deserialize_message(data, Image)

        cv_img = bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough")

        cv2.imwrite(save_path + ("%06i.png" % count), cv_img)
        print("Writing image %i" % count)
        count += 1


if __name__ == '__main__':
    main()
