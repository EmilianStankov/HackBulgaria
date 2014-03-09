from math import floor

def slope_style_score(scores):
	sorted_scores = sorted(scores)
	del sorted_scores[0]
	del sorted_scores[len(sorted_scores) - 1]

	return floor((sorted_scores[0] + sorted_scores[1] + sorted_scores[2]) / (3 / 100)) / 100
