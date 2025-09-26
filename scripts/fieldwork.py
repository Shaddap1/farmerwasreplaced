def is_even(n):
	return n % 2 == 0

def till_field(water = False):
	print("Tilling field")
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			till()
			if water == True:
				use_item(Items.Water)
			move(North)
		move(East)

def plant_crop(crop):
	if crop == "wood":
		plant(Entities.Tree)
	elif crop == "hay":
		return
	elif crop == "carrot": 
		plant(Entities.Carrot)
	elif crop == "pumpkin":
		plant(Entities.Pumpkin)
	elif crop == "sunflower":
		plant(Entities.Sunflower)
	elif crop == None:
		print("Enter Crop as Str")

def water(level = 0.50):
	if not get_entity_type() == None:
		while get_water() < level:
			use_item(Items.Water)

def grow_pumpkin(crop, quota):
	total_needed = assign_quota(crop, quota)
	print("Harvesting" + " " + str(quota) + " " + crop)
	while get_inv(crop) < total_needed:
		count = 0
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if get_entity_type() == None:
					if num_items(Items.Carrot) < 2:
						print("Not enough carrots to plant pumpkins")
						break
					plant(Entities.Pumpkin)
				move(North)
				if get_entity_type() == Entities.Pumpkin:
					count = count + 1
			move(East)
			if count == get_world_size() ** 2:
					harvest()

def plant_checkerboard(crop = None, level = 0):
	print("Checkerboard-planting" + " " + crop + ", water = " + str(level))
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if is_even(get_pos_x()):
				if is_even(get_pos_y()):
					plant_crop(crop)
					water(level)
			elif not is_even(get_pos_x()):
				if not is_even(get_pos_y()):
					plant_crop(crop)
					water(level)
			move(North)
		move(East)

def plant_field(crop = None, level = 0):
	print("Planting" + " " + crop + ", water = " + str(level))
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			harvest()
			if crop == "pumpkin" and num_items(Items.Carrot) < 2:
				print("Not enough carrots to plant pumpkins")
				return
			if crop == "carrot":
				if num_items(Items.Hay) < 7:
					print("Not enough hay to plant carrots")
					return
				if num_items(Items.Wood) < 7:
					print("Not enough wood to plant carrots")
					return
			plant_crop(crop)
			if not level == 0:
				water(level)
			move(North)
		move(East)

def get_inv(crop):
	if crop == "wood":
		return num_items(Items.Wood)
	elif crop == "hay":
		return num_items(Items.Hay)
	elif crop == "carrot": 
		return num_items(Items.Carrot)
	elif crop == "pumpkin":
		return num_items(Items.Pumpkin)
	elif crop == "sunflower":
		return num_items(Items.Power)
	elif crop == None:
		print("Enter Crop as Str")
		
def assign_quota(crop, quota):
	sum = get_inv(crop) + quota
	return sum
	

def farm_field(crop = None, level = 0, quota = 0):
	total_needed = assign_quota(crop, quota)
	print("Harvesting" + " " + str(quota) + " " + crop)
	while get_inv(crop) < total_needed:
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if can_harvest():
					harvest()
					plant_crop(crop)
					if not level == 0:
						water(level)
			move(North)
		move(East)
	
