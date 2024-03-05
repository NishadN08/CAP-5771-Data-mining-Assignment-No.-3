# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Agglomerative hierarchical clustering creates clusters step by step by merging or splitting based on distance metrics, while k-means assigns points to the nearest cluster center, which may bias findings if outliers exist."

    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "K-means is randomization in initial centroids, which produces various results. Agglomerative hierarchical clustering, on the other hand, is deterministic, giving the same outcome each time."

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "While K-means is the most efficient clustering algorithm available, it requires less memory and time than agglomerative hierarchical clustering. However, other algorithms exist as well, such as the leader algorithm."

    # type: bool (True/False)
    answers["(d)"] = False

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "Splitting results in two centroids for the same set, which reduces the sum of squared errors and reduces the distance between the closest centroids."

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "Since the cohesion of clusters is measured inversely by the sum of squared errors (SSE), cohesion increases as SSE reduces and vice versa."

    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "The measure of cluster separation for k-means is the sum of squares between (SB). Consequently, as SSB rises, separation rises as well, and vice versa"

    # type: bool (True/False)
    answers["(g)"] = False

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "Since k-means is independent of both cohesion and separation, increasing cohesion does not always result in increased separation."

    # type : bool(True/False)
    answers["(h)"] = True

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "As per k-means, the total sum of squares (TSS) is the sum of the SSE and the between SSB.TSS remains constant throughout the k-means clustering procedure as well."

    # type: bool (True/False)
    answers["(i)"] = True

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "The inverse measure of cluster cohesion is SSE, and the measure of cluster separation is SSB. Consequently, cohesiveness rises, SSE decreases, and separation (SSB) increases."

    return answers


# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "As shown in the figure, clusters are too far away from the centroid to draw points from others.."

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers[
        "(b) explain"] = "The clusters will contain points from both of the shaded zones because, as the picture illustrates, the shaded regions are close to one another."

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "Since the 12.5 centroid is far from every point, every other cluster will eventually become empty."

    return answers


# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = "(R^2)*4"

    # type: a string that evaluates to a float
    answers["(b) SSE"] = "4*((a*a) + (b*b) + (c*c))"

    # type: a string that evaluates to a float
    answers["(c) SSE"] = "4*((R^2) + ((R/2)^2))"

    return answers



# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 1

    # type: int
    answers["(a) Circle (b)"] = 1

    # type: int
    answers["(a) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Since A and B have the same distance and number of points (100 points), one centroid will be attracted towards A. The two centroids are now located on the right side of B (2/3rd section). Despite the centroid's initial absence, Circle C, which has 100,000 points more than Circle B and is positioned similarly, is guaranteed to keep a centroid because of its higher attraction. Due to their comparable pulls, each centroid in A and B should be attracted by an even distribution of points."

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 1

    # type: int
    answers["(b) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Because of the current points in A and the lack of a greater pull, the centroid will remain at A. One centroid from B will be drawn in by a stronger pull from C. As a result, all the three circles will have 1, 1, 1 centroids."

    # type: int
    answers["(c) Circle (a)"] = 0

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "The centroid in circle A will get the points from circles B and A because they are near to each other but far from circle C. Two centroids, each having 50,000 points, will split the points in C.   Since the number of points in A and B are equal, the centroid in A will shift between the two. The centroids in C will remain in C with half of the points even though they will drift slightly apart."

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = {'Group A', 'Group B'}

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Group A and B can be merged since the rightmost point of A and leftmost point of B has the smallest single link distance."

    # type: set
    answers["(b)"] = {'Group A', 'Group C'}

    # type: explanatory string (at least four words)
    answers[
        "(b) explain"] = ".Group A and C can be merged since the rightmost point of A and farthest point of C has the smallest complete link distance."

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = {'B', 'C', 'E', 'F', 'I', 'J', 'L', 'M'}

    # type: set
    answers["(a) boundary"] = {'D', 'G'}

    # type: set
    answers["(a) noise"] = {'A', 'H'}

    # type: set
    answers["(b) cluster 1"] = {'B','C','D','E','F','G'}

    # type: set
    answers["(b) cluster 2"] = {'I','J','L','M'}

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = {'I', 'G', 'J', 'E', 'M', 'B', 'L', 'F', 'D', 'C'}

    # type: set
    answers["(c)-a boundary"] = {'A', 'H'}

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = {'G', 'I', 'H', 'J', 'E', 'M', 'B', 'D', 'F', 'L', 'C'}

    # type: set
    answers["(c)-b cluster 2"] = {'A'}

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "Cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Cluster 4 has highest entropy due to more even distribution of categories."

    # type: string
    answers["(b)"] = "Cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Cluster 1's unequal distribution results in poor entropy. It is extremely homogeneous since the great majority of its data points belong to a single category."
    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Dataset Z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "Two diagonal entries are more blue and crisp than the other two, indicating that two clusters (B and C) have higher cohesion than the other two (A and D)."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "The first and third rows relate to clusters A and C. This is because the colors of the off-diagonal entries for these two rows differ, indicating the different distances between clusters A (or C) and all other clusters (i.e., A is closest to C (blue off-diagonal), followed by B (green off-diagonal), and is the furthest from D (yellow off-diagonal); similar explanation for C). Row two relates to cluster B. The distances to A and C are the same (green off-diagonal), whereas the red one is the furthest from A. Row 4 relates to Cluster D. The distances from A and C are identical (yellow off-diagonal), however the furthest distance from B is red off-diagonal."

    # type: string
    answers["(a) Matrix 2"] = "Dataset X"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "Two diagonal entries are more blue and crisp than the others, indicating that two clusters (B and C) have stronger cohesion than the other two (A and D)."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "1. Rows with less crisp diagonal entries (rows 1 and 4) have all  different colors, indicating that all other clusters have different  distances from these clusters (e.g: Cluster A is the nearest to B,  followed by C and then D, no 2 clusters have same distance to cluster A).  2. Rows with more crisp diagonal entries have 2 same colors (other than  the diagonal), indicating that it has same distance to 2 clusters,  and is the furthest from 1 cluster (e.g: B’s distance to A and C is  similar, but is the furtherst from D)."

    # type: string
    answers["(a) Matrix 3"] = "Dataset Y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "Two diagonal entries are more blue and crisp than the other two, indicating that clusters B and C have higher cohesiveness than clusters A and D."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "All rows include two identical and one different color off diagonal entries.  This suggests that each cluster has two additional clusters that are comparatively closer to it than the remaining one. For example, B is similarly close to A and C as it is to D."

    # type: string
    answers["(b) Row 1"] = "Cluster A"

    # type: string
    answers["(b) Row 2"] = "Cluster B"

    # type: string
    answers["(b) Row 3"] = "Cluster C"

    # type: string
    answers["(b) Row 4"] = "Cluster D"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = "Less crisp diagonal entry indicates a less coherent cluster.  Every off-diagonal entry has a distinct color, signifying that every other cluster is at a different distance from it (farthest from A, farthest from B, and nearest to C)."

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = "The cluster is cohesive because the diagonal entry is more distinct.  While the off-diagonal indicating distances with A is less precise, two other clusters (A and C) are closer to it than it is, and it is the furthest from one other cluster (D). Two thirds of the off-diagonal entries have the same color."

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = "It is dense due to its black color, however it is not closer to the first cluster."

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = "It's not dense and is far from the first clusters."

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ['Hierarchical', 'Partial', 'Overlapping']

    # type: list
    answers["(b)"] = ['Partitional', 'Exclusive', 'Complete']

    # type: list
    answers["(c)"] = ['Partitional', 'fuzzy', 'complete']

    # type: list
    answers["(d)"] = ['Hierarchical', 'overlapping', 'partial']

    # type: list
    answers["(e)"] = ['Partitional', 'Exclusive', 'Complete']

    # type: explanatory string (at least four words)
    answers[
        "(e) explain"] = "Every student in the class will earn a grade (complete), letter grades are discrete categories that do not overlap (exclusive), and each student receives only one grade per class (exclusive).."

    return answers



# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "No"

    # type: string
    answers["(a) Figure (b)"] = "Yes"

    ##type: explanatory string (at least four words)
    answers["(a) explain"] = "Only (b) will allow DBSCAN to function because only in (b) are the points in the mouth, nose, and eyes significantly closer together than they are apart, making it possible for DBSCAN to discern between them. Since the noise in (a) is significantly denser than the interest patterns, so DBSCAN will exclude the mouth, eyes, and nose."

    # type: string
    answers["(b) Figure (a)"] = "No"

    # type: string
    answers["(b) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "If the number of clusters is set to 4, K-means can be applied to (b), but it would also include the lower density points. K-means is ineffective for (a).S"

    # type: string
    answers["(c)"] = "Take the reciprocal of the density as the new density and apply DBSCAN."


    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
