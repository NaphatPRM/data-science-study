import numpy as np
import random
import math


class Kmeans:
    def __init__(self, X, K, max_iters):
        # Data
        self.X = X
        # Number of clusters
        self.K = K
        # Number of maximum iterations
        self.max_iters = max_iters
        # Initialize centroids
        self.centroids = self.init_centroids()

    def init_centroids(self):
        """
        Selects k random rows from inputs and returns them as the chosen centroids.
        You should randomly choose these rows without replacement and only
        choose from the unique rows in the dataset. Hint: look at
        Python's random.sample function as well as np.unique
        :return: a Numpy array of k cluster centroids, one per row
        """
        # TODO
        new_X = np.unique(self.X, axis=0)
        row_random = random.sample(list(new_X), self.K)
        return np.asarray(row_random)

    def euclidean_dist(self, x, y):
        """
        Computes the Euclidean distance between two points, x and y

        :param x: the first data point, a Python numpy array
        :param y: the second data point, a Python numpy array
        :return: the Euclidean distance between x and y
        """
        # TODO
        return np.linalg.norm(x - y)

    def closest_centroids(self):
        """
        Computes the closest centroid for each data point in X, returning
        an array of centroid indices

        :return: an array of centroid indices
        """
        # TODO
        idx = np.zeros(self.X.shape[0])
        for i in range(self.X.shape[0]):
            distance_array = [self.euclidean_dist(self.X[i], j) for j in self.centroids]
            # argmin returns the indices of the minimum values along an axis,
            # replacing the need for a for-loop and if statement.
            min_dst = np.argmin(distance_array)
            idx[i] = min_dst
        return idx

    def compute_centroids(self, centroid_indices):
        """
        Computes the centroids for each cluster, or the average of all data points
        in the cluster. Update self.centroids.

        Check for convergence (new centroid coordinates match those of existing
        centroids) and return a Boolean whether k-means has converged

        :param centroid_indices: a Numpy array of centroid indices, one for each datapoint in X
        :return boolean: whether k-means has converged
        """
        # TODO
        new_centroid = np.zeros((self.K, self.X.shape[1]))
        for i in range(self.K):
            new_array = np.where(centroid_indices == i)
            needed_array = self.X[new_array[0], :]
            result = np.mean(needed_array, axis=0)
            new_centroid[i, :] = result

        if (new_centroid == self.centroids).all():
            return True
        else:
            self.centroids = new_centroid
            return False

    def run(self):
        """
        Run the k-means algorithm on dataset X with K clusters for max_iters.
        Make sure to call closest_centroids and compute_centroids! Stop early
        if algorithm has converged.
        :return: a tuple of (cluster centroids, indices for each data point)
        Note: cluster centroids and indices should both be numpy ndarrays
        """
        # TODO
        max_iter = self.max_iters
        list_indices = []
        for i in range(max_iter):
            list_indices = self.closest_centroids()
            converge = self.compute_centroids(list_indices)
            print(converge)
            if converge:
                break
        return self.centroids, list_indices

    def inertia(self, centroids, centroid_indices):
        """
        Returns the inertia of the clustering. Inertia is defined as the
        sum of the squared distances between each data point and the centroid of
        its assigned cluster.

        :param centroids - the coordinates that represent the center of the clusters
        :param centroid_indices - the index of the centroid that corresponding data point it closest to
        :return inertia as a float
        """
        # TODO
        total_distance = 0
        for i in range(self.X.shape[0]):
            distances = np.power(self.euclidean_dist(self.X[i], centroids[int(centroid_indices[i])]), 2)
            # argmin returns the indices of the minimum values along an axis,
            # replacing the need for a for-loop and if statement.
            total_distance = total_distance + distances

        print(total_distance)
        return np.power(total_distance, 0.5)
