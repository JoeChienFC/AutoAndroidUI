import os

from skimage.metrics import structural_similarity as ssim
import cv2
import numpy as np
import pytest


class ImageValidator:
    def __init__(self, threshold=100):
        self.threshold = threshold  # 相似度阈值，默认为90%

    def read_image(self, path):
        """读取图像并转换为灰度图"""
        image = cv2.imread(path)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray_image

    def compare_images(self, img1_path, img2_path):
        """比较两张图片的相似度并返回相似度百分比"""
        image1 = self.read_image(img1_path)
        image2 = self.read_image(img2_path)

        # 调整图像大小以进行比较
        if image1.shape != image2.shape:
            image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

        # 计算结构相似性指数（SSIM）
        similarity_index, _ = ssim(image1, image2, full=True)
        similarity_percentage = similarity_index * 100
        return similarity_percentage

    def validate(self, test_image_path):
        try:
            """验证传入的待测照片与参照照片的相似度"""
            # 确定基准图片的路径
            base_path = os.path.abspath(os.path.join(os.getcwd(), "../../data/ref_page"))
            # 获取参照图片的文件路径
            reference_image_path = os.path.join(base_path, os.path.basename(test_image_path))

            if not os.path.exists(reference_image_path):
                pytest.fail(f"Reference image not found: {reference_image_path}")

            # 比较两张图片
            similarity = self.compare_images(test_image_path, reference_image_path)

            if similarity < self.threshold:
                pytest.fail(f"Images are less than {self.threshold}% similar. Similarity: {similarity:.2f}%")
            else:
                print(f"Images are {similarity:.2f}% similar, validation passed.")

        finally:
            # 删除传入的待测图片，无论验证成功或失败
            self.delete_image(test_image_path)

    def delete_image(self, image_path):
        """删除指定路径的图片"""
        try:
            if os.path.exists(image_path):
                os.remove(image_path)
                print(f"Deleted image: {image_path}")
            else:
                print(f"Image not found, could not delete: {image_path}")
        except Exception as e:
            print(f"Error deleting image {image_path}: {e}")
