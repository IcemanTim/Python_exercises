i = 0
array = []
while i < 10:
	while True:
		print("Введите очередное Ваше число")
		num = input()
		try:
			num = int(num)
			array.append(num)
			break
		except ValueError:
			print("Необходимо число!!!\n")
	i += 1

print("Отсортированный массив : ", sorted(array))
        