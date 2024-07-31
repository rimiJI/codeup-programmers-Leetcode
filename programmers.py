# 주어진 리스트
original_list = ["h", "i", "1", "2", "3", "9", "2"]

# 숫자만 골라내는 리스트 컴프리헨션
filtered_list = [int(item) for item in original_list if item.isdigit()]

# 결과 출력
print(filtered_list)