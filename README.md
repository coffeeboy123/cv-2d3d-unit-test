# 2D → 3D 변환 및 Unit Test 프로젝트

## 1. 프로젝트 개요

2D 이미지를 입력으로 받아 Depth Map을 생성하고, 이를 기반으로 3D 포인트 클라우드를 구성하였다.
또한 `pytest`를 활용하여 코드의 정상 동작을 검증하였다.

---

## 2. 사용 기술

* Python
* OpenCV
* NumPy
* pytest

---

## 3. 주요 기능

### Depth Map 생성

이미지를 grayscale로 변환 후 컬러맵을 적용하여 depth map 생성

```python
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
depth_map = cv2.applyColorMap(gray, cv2.COLORMAP_JET)
```

---

### 3D 포인트 클라우드 생성

픽셀 좌표 (X, Y)와 grayscale 값을 Z로 사용하여 3D 데이터 생성

```python
X, Y = np.meshgrid(np.arange(w), np.arange(h))
Z = gray.astype(np.float32)
points_3d = np.dstack((X, Y, Z))
```

---

## 4. 실행 방법

```bash
python src/depth_processing.py
```

결과:

* Depth Map 생성
* 3D 포인트 클라우드 생성
* outputs 폴더에 결과 저장

---

## 5. Unit Test

테스트 실행:

```bash
pytest -v test_3d_processing.py
```

결과:

* depth map 생성 검증
* 3D 포인트 생성 검증
* 예외 처리 검증

→ 모든 테스트 통과

---

## 6. 결론

2D 이미지 기반으로 Depth Map과 3D 데이터를 생성하고,
Unit Test를 통해 코드의 신뢰성을 검증하였다.

---

## PR Test
This update is added to demonstrate the pull request workflow.