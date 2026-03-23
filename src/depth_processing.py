import cv2
import numpy as np
import os


def generate_depth_map(image):
    if image is None:
        raise ValueError("입력된 이미지가 없습니다.")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    depth_map = cv2.applyColorMap(gray, cv2.COLORMAP_JET)
    return gray, depth_map


def generate_point_cloud(gray):
    if gray is None:
        raise ValueError("그레이스케일 이미지가 없습니다.")

    h, w = gray.shape[:2]
    X, Y = np.meshgrid(np.arange(w), np.arange(h))
    Z = gray.astype(np.float32)

    points_3d = np.dstack((X, Y, Z))
    return points_3d


def main():
    input_path = "images/sample.jpg"
    output_depth_path = "outputs/depth_map.jpg"
    output_gray_path = "outputs/gray.jpg"
    output_points_path = "outputs/points_3d.npy"

    image = cv2.imread(input_path)

    if image is None:
        raise ValueError(f"이미지를 불러올 수 없습니다: {input_path}")

    gray, depth_map = generate_depth_map(image)
    points_3d = generate_point_cloud(gray)

    os.makedirs("outputs", exist_ok=True)

    cv2.imwrite(output_gray_path, gray)
    cv2.imwrite(output_depth_path, depth_map)
    np.save(output_points_path, points_3d)

    print("Gray 이미지 저장 완료:", output_gray_path)
    print("Depth map 저장 완료:", output_depth_path)
    print("3D 포인트 클라우드 저장 완료:", output_points_path)
    print("3D 포인트 클라우드 shape:", points_3d.shape)
    print("예시 좌표 [0,0]:", points_3d[0, 0])

    cv2.imshow("Original Image", image)
    cv2.imshow("Depth Map", depth_map)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()