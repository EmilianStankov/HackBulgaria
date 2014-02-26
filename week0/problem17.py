from math import floor

def slope_style_score(scores):
	sorted_scores = sorted(scores)
	del sorted_scores[0]
	del sorted_scores[len(sorted_scores) - 1]

	return floor((sorted_scores[0] + sorted_scores[1] + sorted_scores[2]) / (3 / 100)) / 100


def main():
	print(slope_style_score([94, 95, 95, 95, 90]))
	print(slope_style_score([60, 70, 80, 90, 100]))
	print(slope_style_score([96, 95.5, 93, 89, 92]))

main()