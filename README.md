모션 인식 AI를 만들기 위해 AI를 처음부터 공부하기 위한 공간
===================================================

python 환경변수 설정
------------------
설정 > 시스템 > 고급 시스템 설정 > 고급 > 환경 변수 > PATH 클릭 > 편집
새로 만들기 클릭후 파이썬 설치 경로와 Scripts 경로 붙여넣기

 26.05.23 NumPy 시작
----------
pip install numpy

### 이미지 출력

- flags
    - cv2.IMREAD_UNCHANGED : 원본 사용
    - cv2.IMREAD_GRAYSCALE : 1 채널, 그레이스케일 적용
    - cv2.IMREAD_COLOR : 3 채널, BGR 이미지 사용
    - cv2.IMREAD_ANYDEPTH : 이미지에 따라 정밀도를 16/32비트 또는 8비트로 사용
    - cv2.IMREAD_ANYCOLOR : 가능한 3 채널, 색상 이미지로 사용
    - cv2.IMREAD_REDUCED_GRAYSCALE_2 : 1 채널, 1/2 크기, 그레이스케일 적용
    - cv2.IMREAD_REDUCED_GRAYSCALE_4 : 1 채널, 1/4 크기, 그레이스케일 적용
    - cv2.IMREAD_REDUCED_GRAYSCALE_8 : 1 채널, 1/8 크기, 그레이스케일 적용
    - cv2.IMREAD_REDUCED_COLOR_2 : 3 채널, 1/2 크기, BGR 이미지 사용
    - cv2.IMREAD_REDUCED_COLOR_4 : 3 채널, 1/4 크기, BGR 이미지 사용
    - cv2.IMREAD_REDUCED_COLOR_8 : 3 채널, 1/8 크기, BGR 이미지 사용

```
height, width, channel = image(변수).shape
print(height, width, channel)
```
위 코드처럼 이미지의 높이(height), 너비(width), 채널(channel)의 값을 확인할 수 있음

이미지의 속성은 크기, 정밀도, 채널을 주요한 속성으로 사용함
- 크기: 이미지의 **높이**와 **너비**를 의미함
- 정밀도: 이미지의 처리 결과의 **정밀성**을 의미함
- 채널: 이미지의 **색상 정보**를 의미함
- TIP: **유효 비트가 많을 수록 더 정밀함**
- TIP: 채널이 3일 경우는 **다색 이미지**, 채널이 1일 경우 **단색 이미지**

