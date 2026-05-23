import numpy as np

## array 만들기
# range_array = np.arange(10)
# print(range_array)

# a = np.array([1,2,3,4,5])
# print(a)

# a = [1,2,3,4,5]
# b = np.array(a)
# c = np.array([1,3,5])
# print(a)
# print(b)
# print(c)



## numpy 배열 복제
# a = np.array([1,2,3,4,5])
# b = a
# c = a.copy() # 원본값이 바뀌어도 copy로 복제한 데이터는 바뀌지 않는다

# b[0] = 99

# print(a)
# print(b)
# print(c)


## numpy 배열 호출
# a = [1,2,3,4,5]
# b = np.array(a)
# c = np.array([1,3,5,7])

# print(b[2])
# print(c[-1])
# print(c[0:3])



## numpy 배열 계산
# a = [1,2,3,4,5]
# b = np.array(a)
# c = np.array([1,3,5])

# print(a*2) # list는 * 기호 사용시 배열을 붙임
# print(b*2) # numpy는 수학적 기호를 사용하면 각각의 원소를 계산하여 반환함
# print(c+3)



## 1차원 배열 타입
# a = np.array([1,2,3], dtype = int)
# b = np.array([1.1, 2.2, 3.3], dtype=float)
# c = np.array([1,1,0], dtype=bool)

# print(a)
# print(b)
# print(c)



## 다차원 배열
# a = np.array([[1,2,3], [4,5,6], [7,8,9]])
# b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])

# print(a)
# print(b)
# print(a[0][1])
# print(b[0][1][1])



## 배열 속성 반환
# a = np.array([[1,2,3], [4,5,6], [7,8,9]])
# b = np.array([[[1,2], [3,4]], [[5,6], [7,8]], [[9,10], [11,12]]])

# print(a.ndim)
# print(a.shape)
# print(a.dtype)

# print(np.ndim(b))
# print(np.shape(b))



# # 모든 값이 1인 배열
# a = np.ones((2,2), dtype=int)
# b = [1, 2, 3, 4, 5]
# c = np.ones_like(b, dtype=int)

# print(a)
# print(b)
# print(c)



# # 모든 값이 0인 배열
# a = np.zeros((2,2), dtype=int)
# b = [1, 2, 3, 4, 5]
# c = np.zeros_like(b, dtype=int)

# print(a)
# print(b)
# print(c)



# # 모든 값이 초기화하지 않는 배열
# a = np.empty((2,2), dtype=int)
# b = [1, 2, 3, 4, 5]
# c = np.empty_like(b, dtype=int)

# print(a)
# print(b)
# print(c)



# # 대각의 값이 1인 배열(단위 행렬)
# a = np.identity(7, dtype=int)
# b = np.eye(7, 6, k=2, dtype=int) # numpy.eye(세로, 가로, k=시작 간격, dtype=타입)

# print(a)
# print(b)



# # 등간격
# a = np.arange(0, 10, step=5) # numpy.arange(start, end-1, step= 간격)
# b = np.arange(1, 10, step=5)
# c = np.arange(0, 10, step=1)

# print(a)
# print(b)
# print(c)

# a = np.linspace(0, 10, num=5, endpoint=True, retstep=True)
# b = np.linspace(1, 10, num=5, endpoint=True, retstep=False)
# c = np.linspace(0, 10, num=5, endpoint=False, retstep=False)

# print(a)
# print(b)
# print(c)

# a = np.logspace(0, 10, num=5, endpoint=True, base=10.0)
# b = np.logspace(1, 10, num=5, endpoint=True, base=5.0)
# c = np.logspace(0, 10, num=5, endpoint=False, base=1.0)

# print(a)
# print(b)
# print(c)



## array 연결 및 합치기
# x = np.array([[1,1], [2,2]])
# y = np.array([[5,6]])

# print(np.concatenate((x,y), axis=0))



# # 인덱싱과 슬라이싱
# data = np.array([1, 2, 3, 4, 5])
# print(data[1])
# print(data[0:2])



# # array와 행렬
# mat1 = np.array([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
# unit_matrix = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
# print(np.dot(mat1, unit_matrix))


# # axios를 이용한 체크
# print(mat1.max(axis=0)) # axis=0은 열(세로) axis=1은 행(가로)


# # 크기가 같은 행렬의 합
# data = np.array([[1, 2, 3], [3, 4, 5]])
# ones = np.array([[1, 1, 1], [1, 1, 1]])

# print(data + ones)


# # 크기가 다른 행렬의 합
# data = np.array([[1, 2], [3, 4], [5, 6]])
# ones_row = np.array([[1, 1]])

# print(data, "\n")
# print(data + ones_row)


# # 행렬의 곱
# mat1 = np.array([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
# unit_matrix = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

# print(mat1 @ unit_matrix)


# # 행렬의 크기 변경
# mat2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# mat2 = mat2.reshape((3, 3)) # 3행 3열로 변경

# print(mat2)





# 데이터 생성

# # 3열 5행 데이터가 1인 배열 생성
# print(np.ones((3, 5)))


# # 데이터가 0인 3열 5행 배열 생성
# print(np.zeros((3, 5)))


# # 데이터가 랜덤인 3열 2행 배열 생성
# print(np.random.random((3, 2)))



