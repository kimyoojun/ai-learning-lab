import cv2

# 카메라 출력

# 카메라에서 정보를 받아오는 코드
capture = cv2.VideoCapture(0)   # cv2.VideoCapture(index) index는 카메라 번호 내장 카메라는 0 외장카메라는 1~n
# 카메라 속성 설정
# capture.set(propid, value)로 카메라의 속성(propid) 값(value)을 설정
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # 카메라 너비는 640
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # 카메라 높이는 480

# 반복문을 활용하여 카메라에서 프레임을 지속적으로 받아옴
while cv2.waitKey(33) < 0:  # cv2.waitKey는 지정된 시간 동안 키 입력이 있을때까지 프로그램 지연
                            # cv2.waitKey(delay) delay는 지연시간
                            # while cv2.waitKey(33) != ord('q'): 이런 식의 반복문이면 q키가 입력되면 반복문 종료
    ret, frame = capture.read() # 프레임 읽기 메서드 capture.read()를 이용하여 카메라의 상태 및 프레임을 받아옴
                                # ret은 카메라의 상태가 저장되면 카메라가 동작하면 True를 반환, 작동하지 않으면 False를 반환
                                # frame에는 현재시점의 프레임이 저장
    cv2.imshow("VideoFrame", frame) # 이미지 표시 함수 cv2.show 사용하여 특정 윈도우 창에 이미지를 띄움
                                    # cv2.imshow(winname, mat)으로 윈도우 창의 제목(winname) 이미지(mat)를 할당
                                    # winname은 문자열로 표시, 할당한 문자열이 변수와 비슷한 역할을함
                                    # 이 코드는 VideoFrame이라는 윈도우 창에 프레임이 표시됨

capture.release()   # 메모리 해제 메서드 capture.release()로 카메라 장치에서 받아온 메모리 해제
cv2.destroyAllWindows() # 윈도우 창 제거 함수 cv2.destroyAllWindows()를 이용하여 모든 윈도우 창을 닫음
                        # 특정 윈도우 창만 닫으려면 cv2.destroyAllWindows(winname) 형식으로 특정 윈도우 창만 닫음
