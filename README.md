# rm_classifier_training
RoboMaster 装甲板图案分类器训练相关代码


## 使用 CIFAR-100 作为负样本

下载地址：https://www.cs.toronto.edu/~kriz/cifar.html

下载解压后，使用 [process_cifra100.py](process_cifra100.py) 对其进行处理

## 装甲板图案数据采集

1. 启动相机节点与识别器
2. 将装甲板置于相机视野中，并拉远到期望的识别距离，检查识别器此时得到的角点是否准确
3. 改变装甲板姿态，若此时角点依然准确，录制该类别的 rosbag

    ```
    ros2 bag record /detector/number_img -o <output_path>
    ```

4. 从 bag 中提取出图片作为数据集

    ```
    python3 extract_bag.py <bag_path> <output_images_path>
    ```

5. 按照下列结构放置图片作为数据集

    ```
    datasets
    ├─1
    ├─2
    ├─3
    ├─4
    ├─5
    ├─6outpost
    ├─7guard
    ├─8base
    └─9negative
    ```

## 训练

运行 [mlp_training.py](mlp_training.py)
