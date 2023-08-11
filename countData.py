import os, sys



def countRecFiles(path):
	dirs = os.listdir( path )

	count = 0
	for item in dirs:
		itemPath = os.path.join(path, item)	

		if os.path.isdir(itemPath):
			count += countRecFiles(itemPath)
		elif os.path.isfile(itemPath):
			count +=1
		else:
			print("Unknown : " + path+item)

	return count


def count_dataset(data_path, dataset = "global"):
	originPath = os.path.join(data_path, dataset)
	dirs = os.listdir( originPath )
	#dirs = filter(os.path.isdir, os.listdir(path))

	countTotal = 0
	for item in dirs:
		itemPath = os.path.join(originPath, item)

		if os.path.isdir(itemPath):
			#print(typePath)
			countType = countRecFiles(itemPath)

			#print(item +"\t: \t"+ str(countType))
			#"Location: {0:20} Revision {1}".format(Location, Revision)

			print("{0:11} : {1}".format(item, str(countType)))
			countTotal += countType
		else:
			print("Not type : " + item)

	print("Total : "+ str(countTotal))
	return countTotal

def count_partition(data_path, data_sets, global_data_set):
	global_path = os.path.join(data_path, global_data_set)

	dirs = os.listdir( global_path )
	for label in dirs:
		count_set = [0 for k in range(len(data_sets))]

		for i in range(len(data_sets)):
			set_path = os.path.join(data_path, os.path.join(data_sets[i], label))

			if os.path.isdir(set_path):
				count_set[i] = countRecFiles(set_path)

		img_sum = sum(count_set)
		print()
		print(label +"("+str(img_sum)+")")
		print("*****")
		for i in range(len(data_sets)):
			perce =  str(round(count_set[i]/img_sum * 100,2))
			#print(data_sets[i] + " : " +  + "% (" + str(count_set[i]) + ")")
			print("{0:11} : {1:5}% ({2:1})".format(data_sets[i], perce, str(count_set[i])))



data_sets = ["train", "validation", "test"]

data_path = "./data/"



count_partition(data_path, data_sets, "global")
#count_dataset(data_path, dataset = "global")