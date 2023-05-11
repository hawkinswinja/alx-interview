#!/usr/bin/python3
"""rotate_2d_matrix module"""


def rotate_2d_matrix(matrix):
    """rotate matrix clockwise 90"""
    matrix[:] = matrix[::-1]
    for i in range(len(matrix)):
        for j in range(i):
            if i == j:
                continue
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
