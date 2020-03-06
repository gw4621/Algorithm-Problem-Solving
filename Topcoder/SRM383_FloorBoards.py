class FloorBoards:
	def layout(self, room):
		width = len(room[0])
		height = len(room)
		bought = [[False for _ in range(width)] for _ in range(height)]
		boards = 0
		for i in range(height):
			for j in range(width):
				if bought[i][j]:
					continue
				if room[i][j] == '-':
					bought[i][j] = True
					for k in range(j+1, width):
						if not bought[i][k] and room[i][k] == '-':
							bought[i][k] = True
						else:
							break
					boards += 1
				elif room[i][j] == '|':
					bought[i][j] = True
					for k in range(i+1, height):
						if not bought[k][j] and room[k][j] == '|':
							bought[k][j] = True
						else:
							break
					boards += 1
		return boards
fb = FloorBoards()
inpstr = input()
room = []
while inpstr != '':
	room.append(inpstr)
	inpstr = input()
print(fb.layout(room))
