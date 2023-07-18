import copy
from random import randint
import random

distance=[0,7.1,12.736,15.35,6.069,7.554,6.323,7.439,8.863,7.689,8.04,4.446,12.137,16.758,7.322,8.848,8.558,12.206,7.521,10.165,
          10.539,5.745,8.914,7.129,7.661,7.352,6.732,6.713,7.364,6.089,7.737,5.202,5.15,7.045,7.792,2.904,8.672,16.347,8.702,7.307,8.70,
          6.655,6.783,6.779],
[7.476,0,6.009,4.422,0.959,0.782,7.37,0.726,9.504,4.044,4.395,3.88,5.41,5.83,1.671,2.601,5.224,6.425,4.275,3.219,2.9,3.612,2.003,1.474,0.902,
3.297,1.346,2.693,3.309,2.303,2.082,3.821,3.769,1.39,0.616,6.42,5.027,5.419,5.057,0.411,5.057,2.666,1.397,5.893],
[13.367,6.25,0,10.313,6.85,6.284,12.826,6.228,13.675,8.114,8.465,10.558,1.261,11.721,7.123,7.449,10.68,11.881,9.731,8.127,7.808,9.068,7.098,
6.93,6.404,8.753,8.024,8.149,8.765,7.759,7.538,10.499,10.447,6.846,5.995,12.311,9.097,11.31,9.127,6.144,9.127,8.122,8.075,12.823],
[7.378,3.024,8.827,0,2.153,3.926,22.589,3.87,11.715,3.63,3.981,5.291,8.228,3.302,4.088,5.603,7.645,8.636,6.696,6.672,6.353,6.033,5.005,3.895,
4.046,5.718,3.498,5.114,5.73,4.724,4.503,5.232,5.18,3.811,3.637,6.322,4.613,4.883,4.643,3.393,4.643,5.087,3.549,9.015],
[6.733,1.429,7.232,3.673,0,2.331,22.376,2.275,10.868,3.084,3.435,4.444,6.633,5.081,2.5,4.008,6.057,7.789,5.108,4.368,4.049,4.445,3.41,2.307,
2.451,4.13,1.91,3.526,4.142,3.136,2.915,4.385,4.333,2.223,2.042,5.677,4.067,4.67,4.097,1.798,4.097,3.499,1.961,6.726],
[8.211,0.712,6.097,5.135,1.672,0,7.029,0.114,8.374,4.757,5.108,4.002,5.498,6.543,1.01,2.093,4.883,6.084,3.934,2.874,2.555,3.271,1.495,1.133,0.29,
2.956,1.468,2.352,2.968,1.962,1.741,3.943,3.891,1.049,0.29,5.914,5.74,6.132,5.77,0.508,5.77,2.325,1.519,5.552],
[6.244,7.902,13.535,20.908,7.802,7.542,0,7.427,4.153,9.452,9.803,6.596,12.936,22.316,6.787,8.745,5.733,1.272,4.696,7.34,7.714,4.696,10.275,6.566,
7.282,5.43,6.819,5.664,5.442,5.84,6.81,5.191,5.139,6.482,8.142,7.178,10.435,21.905,10.465,7.657,10.465,5.753,7.133,2.318],
[8.155,0.726,6.125,5.172,1.709,0.114,6.914,0,8.259,4.794,5.145,3.946,5.526,6.58,0.895,2.208,4.768,5.969,3.819,2.759,2.44,3.156,1.61,1.018,0.234,
2.841,1.412,2.237,2.853,1.847,1.626,3.887,3.835,0.934,0.405,5.858,5.777,6.169,5.807,0.452,5.807,2.21,1.463,5.437],
[9.052,9.08,14.582,24.306,9.723,8.447,5.025,8.391,0,11.373,11.724,8.517,14.717,25.714,6.985,7.397,4.385,4.08,4.894,5.992,6.366,6.617,10.444,7.215,
8.209,5.628,8.74,6.754,5.64,6.93,7.008,7.112,7.06,7.256,8.49,9.099,12.356,25.303,12.386,9.11,12.386,5.951,9.054,4.239],
[9.757,4.37,7.062,5.388,3.52,5.272,11.689,5.216,13.823,1.86,0,7.399,6.463,3.327,5.455,6.949,9.012,10.744,8.063,7.323,7.004,7.4,6.351,5.262,5.392,
7.085,4.865,6.481,7.097,6.091,5.87,7.34,7.288,5.178,4.983,8.701,1.331,3.936,0.661,4.739,0.661,6.454,4.916,9.681],
[5.422,3.796,9.432,4.988,2.765,4.25,5.698,4.135,7.832,4.415,4.766,0,8.833,6.396,4.018,5.544,5.47,4.753,4.049,5.886,5.567,2.892,5.61,3.825,4.357,
3.543,3.428,2.668,3.555,2.495,2.847,1.349,1.297,3.741,4.488,3.125,5.398,5.985,5.428,4.003,5.428,2.61,3.479,5.132],
[12.768,5.651,1.261,9.714,6.251,5.685,12.227,5.629,12.413,7.515,7.866,9.959,0,11.122,6.524,6.187,9.887,11.282,9.132,6.865,6.546,8.469,6.501,6.331,
5.805,8.154,7.425,7.55,8.166,7.16,6.939,9.9,9.848,6.247,5.396,11.712,8.498,10.711,8.528,5.545,8.528,7.523,7.476,11.561],
[15.745,5.155,8.915,2.211,4.284,6.057,21.005,6.001,25.227,1.814,1.852,7.422,8.316,0,6.219,7.734,9.776,21.432,8.827,8.803,8.484,8.164,7.136,6.026,6.177,7.849,5.629,7.245,
7.861,6.855,6.634,7.363,7.311,5.942,5.768,8.453,3.184,1.092,2.514,5.524,2.514,7.218,5.68,21.602],
[7.985,1.74,7.125,6.522,3.059,1.004,6.942,0.889,7.512,6.144,6.495,3.616,6.526,7.93,0,1.9,4.312,5.997,3.363,2.012,1.693,2.764,2.137,0.689,0.812,
1.933,2.207,2.122,2.397,1.732,1.511,3.717,3.665,0.73,1.214,5.688,7.127,7.519,7.157,1.247,7.157,1.818,2.258,6.66],
[9.849,2.35,7.746,6.795,3.332,1.842,9.398,1.957,7.141,6.417,6.768,7.04,6.14,8.203,2.268,0,4.615,8.453,4.185,1.593,1.274,4.812,1.171,2.976,2.133,
3.836,4.506,4.195,3.301,3.805,3.584,6.981,6.929,2.892,1.76,8.793,7.4,7.792,7.43,2.351,7.43,4.147,4.557,6.289],
[7.636,5.366,10.868,9.917,6.454,4.733,5.524,4.677,3.267,8.677,9.028,5.821,9.486,11.325,4.288,3.683,0,4.579,1.971,2.278,2.652,3.463,5.213,4.097,
4.495,2.51,5.331,3.657,2.522,3.833,3.89,4.416,4.364,4.138,4.776,7.133,9.66,10.914,9.69,5.396,9.69,2.821,5.645,2.415],
[4.971,8.566,14.202,18.764,67.535,7.561,1.398,7.446,4.201,9.185,9.536,6.329,13.603,20.172,6.806,8.363,5.351,0,4.715,6.958,7.332,4.715,9.893,6.585,
7.301,5.449,3.838,5.683,5.461,5.859,6.829,4.924,4.872,6.501,8.161,5.445,10.168,19.761,10.198,7.676,10.198,5.772,7.152,2.366],
[6.886,3.581,8.966,7.452,4.978,2.845,5.843,2.73,6.705,6.879,7.23,4.023,8.367,8.86,2.09,3.157,2.492,4.898,0,2.099,2.473,1.665,4.392,2.32,2.585,
0.733,3.533,1.859,0.745,2.035,2.113,2.618,2.566,2.361,2.987,4.589,7.862,8.449,7.892,3.088,7.892,1.056,3.847,3.654],
[8.384,3.087,8.589,7.638,4.175,2.454,7.756,2.398,5.499,7.26,7.611,5.521,6.948,9.046,2.009,1.404,2.973,6.811,2.536,0,0.373,3.163,2.675,
2.789,2.216,2.187,4.077,3.357,1.652,3.533,3.119,4.116,4.064,2.83,2.497,6.087,8.243,8.635,8.273,3.117,8.273,2.498,4.128,4.647],
[8.758,2.768,8.27,7.319,3.856,2.135,8.13,2.079,5.873,6.941,7.292,5.895,6.629,8.727,1.69,1.359,3.347,7.185,2.91,0.373,0,3.537,2.356,2.47,1.897,
2.561,3.758,3.731,2.026,3.449,2.8,4.49,4.438,2.511,2.178,6.461,7.924,8.316,7.954,2.798,7.954,2.872,3.809,5.021],
[5.994,3.724,9.357,6.56,4.086,3.726,4.951,3.611,7.085,5.987,6.338,3.131,8.758,7.968,3.1,4.127,2.48,4.006,1.156,3.069,3.443,0,5.362,2.388,
3.833,1.606,2.641,0.967,1.618,1.143,2.414,1.726,1.674,2.304,3.964,3.697,6.97,7.557,7,3.479,7,0.909,2.955,3.221],
[9.095,1.596,6.992,6.041,2.578,1.088,9.674,1.203,7.417,5.663,6.014,6.286,6.393,7.449,1.329,0.854,4.891,8.729,4.424,1.917,1.598,3.917,0,1.908,
1.379,3.086,3.752,3.277,3.55,2.887,2.666,6.227,6.175,1.949,1.006,8.039,6.646,7.038,6.676,1.597,6.676,2.971,3.803,6.565],
[7.195,2.21,7.595,6.115,3.104,1.474,6.152,1.359,8.286,5.526,5.877,2.969,6.996,7.523,0.754,2.149,4.006,5.207,3.057,2.301,1.982,2.394,2.776,0,
1.451,2.079,1.659,1.475,2.091,1.085,0.864,2.927,2.875,0.083,1.765,4.898,6.509,7.112,6.539,1.717,6.539,1.448,1.973,4.675],
[8.331,0.902,6.301,5.348,1.885,0.29,7.149,0.234,8.147,4.97,5.321,4.122,5.702,6.756,1.117,1.852,5.003,6.204,4.054,2.647,2.328,3.391,1.917,1.253,
0,3.076,1.588,2.472,3.088,2.082,1.861,4.063,4.011,1.169,0.581,6.034,5.953,6.345,5.983,0.628,5.983,2.445,1.639,5.672],
[7.125,2.92,8.305,7.634,4.171,2.184,6.082,2.069,6.292,7.143,7.494,3.56,7.706,9.042,1.429,2.473,2.776,5.137,1.827,1.704,2.078,1.904,2.931,1.659,
1.924,0,3.276,1.5,0.084,1.676,1.452,2.857,2.805,1.7,2.326,4.828,8.126,8.631,8.156,2.427,8.156,1.187,3.59,4.431],
[6.742,1.756,7.841,4.455,1.444,2.21,6.823,2.095,8.957,3.866,4.217,2.533,7.242,5.863,1.978,3.504,5.028,5.878,4.079,3.846,3.527,3.416,4.289,1.785,
2.317,3.101,0,2.497,3.113,1.9,2.393,2.474,2.422,1.701,2.448,4.445,4.849,5.452,4.879,1.963,4.879,2.47,1.439,6.257],
[6.302,2.634,8.267,6.007,2.996,2.636,5.259,2.521,7.393,5.418,5.769,2.076,7.668,7.415,2.01,3.405,3.346,4.314,2.397,2.882,3.256,1.734,4.261,1.298,
2.743,1.419,1.551,0,1.431,0.192,1.324,2.034,1.982,1.214,2.874,4.005,6.401,7.004,6.431,2.389,6.431,0.788,1.865,4.693],
[7.59,2.932,8.317,7.646,4.183,2.196,6.547,2.081,6.207,7.155,7.506,3.572,7.718,9.054,1.441,2.677,2.691,5.602,1.742,1.619,1.993,2.369,2.943,1.671,
1.936,0.084,3.288,1.512,0,1.688,1.464,3.322,3.27,1.712,2.338,5.293,8.138,8.643,8.168,2.439,8.168,1.199,3.602,5.355],
[6.109,2.441,8.074,5.814,2.803,2.443,5.066,2.328,7.2,5.225,5.576,1.883,7.475,7.222,1.817,3.212,3.63,4.121,2.681,3.166,3.045,1.918,4.068,1.105,2.55,
1.703,1.358,1.099,1.715,0,1.131,1.841,1.789,1.021,2.681,3.812,6.208,6.811,6.238,2.196,6.238,1.072,1.672,4.5],
[6.793,3.271,8.904,6.644,3.633,3.369,5.75,3.254,7.884,6.055,6.406,2.713,8.305,8.052,2.614,3.778,3.184,4.805,2.235,2.72,3.094,1.572,5.013,1.935,
3.109,1.257,2.188,0.653,1.269,0.829,0,2.525,2.473,1.851,3.511,4.496,7.038,7.641,7.068,3.026,7.068,0.626,2.502,3.853],
[4.267,4.696,10.332,5.888,3.665,5.15,6.689,5.035,7.721,5.315,5.666,1.404,9.733,7.296,4.918,6.444,5.756,4.642,4.972,5.562,5.317,3.068,6.51,3.377,
5.257,4.099,4.328,3.224,4.111,3.051,3.403,0,1.204,3.293,5.388,1.97,6.298,6.885,6.328,4.903,6.328,3.166,4.379,5.021],
[4.319,4.748,10.384,5.94,3.717,5.202,6.741,5.087,7.773,5.367,5.718,1.456,9.785,7.348,4.97,6.496,5.808,4.694,5.024,5.614,5.369,3.12,6.562,3.429,
5.309,4.151,4.38,3.276,4.163,3.103,3.455,0.051,0,3.345,5.44,2.022,6.35,6.937,6.38,4.955,6.38,3.218,4.431,5.073],
[7.111,2.251,7.636,6.031,3.02,1.515,6.068,1.4,8.202,5.442,5.793,2.885,7.037,7.439,0.795,2.19,3.922,5.123,2.973,2.342,2.023,2.31,2.817,0.083,1.492,
1.995,1.575,1.391,2.007,1.001,0.78,2.843,2.791,0,1.806,4.814,6.425,7.028,6.455,1.758,6.455,1.364,1.889,4.591],
[8.485,0.838,6.142,5.431,1.968,0.37,7.4,0.485,8.129,5.053,5.404,4.373,5.543,6.839,1.224,2.011,5.603,6.455,4.305,2.629,2.31,3.642,1.413,1.504,0.661,
3.327,1.839,2.723,3.339,2.333,2.112,4.314,4.262,1.42,0,7.429,6.036,6.428,6.066,0.879,6.066,2.696,1.89,7.277],
[3.275,6.045,11.681,7.237,5.014,6.499,5.685,6.384,7.839,6.664,7.015,2.529,11.082,8.645,6.267,7.793,6.918,5.871,5.881,8.525,8.899,4.078,7.859,4.726,
6.606,5.685,5.677,5.046,5.697,5.222,4.752,2.1,2.048,4.642,6.737,0,7.647,8.234,7.677,6.252,7.677,4.988,5.728,5.139],
[9.061,3.236,5.928,5.988,2.565,4.138,10.581,4.082,12.715,2.278,2.629,6.291,5.329,4.086,4.347,5.815,7.904,9.636,6.955,6.215,5.896,6.292,5.217,4.154,
4.258,5.977,3.757,5.373,5.989,4.983,4.762,6.232,6.18,4.07,3.849,8.005,0,6.985,3.291,3.605,3.291,5.346,3.808,8.573],
[16.066,5.476,11.279,2.532,4.605,6.378,21.326,6.322,25.548,2.491,2.529,7.743,10.68,0.827,6.54,8.055,10.097,21.753,9.148,9.124,8.805,8.485,7.457,
6.347,6.498,8.17,5.95,7.566,8.182,7.176,6.955,7.684,7.632,6.263,6.089,8.774,3.861,0,3.191,5.845,3.191,7.539,6.001,21.923],
[9.93,4.543,7.235,4.544,3.693,5.445,23.338,5.389,13.996,2.033,1.033,7.572,6.636,2.483,5.628,7.122,9.185,10.917,8.236,7.496,7.177,7.573,6.524,5.435,
5.565,7.258,5.038,6.654,7.27,6.264,6.043,7.513,7.461,5.351,5.156,8.874,1.504,3.274,0,4.912,0,6.627,5.089,9.854],
[7.702,0.518,6.138,4.749,1.286,1.02,7.783,0.905,9.917,4.826,5.177,3.493,5.539,6.157,1.259,2.73,4.812,6.838,3.863,3.123,2.804,3.2,2.132,1.062,1.031,
2.885,0.959,2.281,2.897,1.891,1.67,3.434,3.382,0.978,0.745,5.405,5.809,5.746,5.839,0,5.839,2.254,1.01,5.481],
[9.93,4.543,7.235,4.544,3.693,5.445,23.338,5.389,13.996,2.033,1.033,7.572,6.636,2.483,5.628,7.122,9.185,10.917,8.236,7.496,7.177,7.573,6.524,5.435,
5.565,7.258,5.038,6.654,7.27,6.264,6.043,7.513,7.461,5.351,5.156,8.874,1.504,3.274,0,4.912,0,6.627,5.089,9.854],
[6.166,3.896,9.529,6.732,4.258,3.898,5.123,3.783,7.257,6.159,6.51,3.303,8.93,8.14,3.272,4.535,2.485,4.178,1.161,3.477,3.851,0.945,5.77,2.56,4.005,
2.014,2.813,1.139,2.026,1.315,2.586,1.898,1.846,2.476,4.136,3.869,7.142,7.729,7.172,3.651,7.172,0,3.127,3.226],
[7.394,1.734,7.367,5.107,2.096,1.736,6.6,1.621,8.734,4.518,4.869,3.185,6.768,6.515,1.416,3.03,4.454,5.655,3.505,2.963,2.644,2.842,3.361,0.704,
1.843,2.527,0.651,1.923,2.539,1.533,1.312,3.126,3.074,0.62,1.974,5.097,5.501,6.104,5.531,1.489,5.531,1.896,0,5.123],
[6.441,6.648,11.351,8.785,6.562,5.23,2.777,5.115,3.087,8.212,8.563,5.356,11.836,10.193,4.475,6.033,3.021,1.832,2.384,4.628,5.002,3.442,7.563,
4.705,6.845,3.118,5.565,4.244,3.13,4.42,4.498,3.951,3.899,4.746,7.126,5.938,9.195,9.782,9.225,5.473,9.225,3.441,5.879,0]

tempat=["DEPOT","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","AA",
"AB","AC","AD","AE","AF","AG","AH","AI","AJ","AK","AL","AM","AN","AO","AP","AQ"]
print(len(tempat))
tpt={}

def getcustomer(hari):
    daftarCustomer = []
    if (hari == 1):
        daftarCustomer.append(Customer("A", 30, 23))
        daftarCustomer.append(Customer("B", 7, 7))
        daftarCustomer.append(Customer("C", 7, 7))
        daftarCustomer.append(Customer("D", 8, 9))
        daftarCustomer.append(Customer("E", 6, 6))
        daftarCustomer.append(Customer("G", 26, 24))
        daftarCustomer.append(Customer("I", 6, 6))
        daftarCustomer.append(Customer("K", 24, 22))
        daftarCustomer.append(Customer("L", 5, 5))
        daftarCustomer.append(Customer("M", 3, 3))
        daftarCustomer.append(Customer("N", 30, 30))
        daftarCustomer.append(Customer("O", 6, 6))
        daftarCustomer.append(Customer("S", 12, 12))
        daftarCustomer.append(Customer("T", 10, 10))
        daftarCustomer.append(Customer("V", 4, 4))
        daftarCustomer.append(Customer("W", 4, 3))
        daftarCustomer.append(Customer("X", 5, 5))
        daftarCustomer.append(Customer("Y", 11, 12))
        daftarCustomer.append(Customer("Z", 10, 10))
        daftarCustomer.append(Customer("AA", 15, 15))
        daftarCustomer.append(Customer("AB", 4, 7))
        daftarCustomer.append(Customer("AC", 7, 9))
        daftarCustomer.append(Customer("AD", 28, 30))
        daftarCustomer.append(Customer("AE", 10, 10))
        daftarCustomer.append(Customer("AF", 20, 21))
        daftarCustomer.append(Customer("AH", 5, 5))
        daftarCustomer.append(Customer("AI", 5, 3))
        daftarCustomer.append(Customer("AK", 15, 16))
        daftarCustomer.append(Customer("AL", 18, 21))
        daftarCustomer.append(Customer("AP", 20, 19))
        daftarCustomer.append(Customer("AQ", 10, 9))
    elif (hari==2) :
        daftarCustomer.append(Customer("A", 16, 16))
        daftarCustomer.append(Customer("C", 8, 8))
        daftarCustomer.append(Customer("D", 8, 8))
        daftarCustomer.append(Customer("E", 35, 32))
        daftarCustomer.append(Customer("F", 35, 35))
        daftarCustomer.append(Customer("G", 46, 47))
        daftarCustomer.append(Customer("H", 25, 25))
        daftarCustomer.append(Customer("I", 5, 5))
        daftarCustomer.append(Customer("K", 13, 12))
        daftarCustomer.append(Customer("L", 8, 11))
        daftarCustomer.append(Customer("M", 7, 9))
        daftarCustomer.append(Customer("O", 21, 21))
        daftarCustomer.append(Customer("P", 9, 9))
        daftarCustomer.append(Customer("S", 12, 12))
        daftarCustomer.append(Customer("U", 22, 22))
        daftarCustomer.append(Customer("V", 12, 12))
        daftarCustomer.append(Customer("W", 10, 11))
        daftarCustomer.append(Customer("X", 10, 8))
        daftarCustomer.append(Customer("Y", 7, 7))
        daftarCustomer.append(Customer("AC", 5, 7))
        daftarCustomer.append(Customer("AD", 15, 8))
        daftarCustomer.append(Customer("AF", 5, 5))
        daftarCustomer.append(Customer("AG", 7, 7))
        daftarCustomer.append(Customer("AJ", 8, 7))
        daftarCustomer.append(Customer("AK", 5, 2))
        daftarCustomer.append(Customer("AL", 58, 56))
        daftarCustomer.append(Customer("AN", 14, 13))
        daftarCustomer.append(Customer("AO", 7, 7))
        daftarCustomer.append(Customer("AQ", 10, 8))
    elif (hari==3) :
        daftarCustomer.append(Customer("A", 58, 59))
        daftarCustomer.append(Customer("B", 6, 11))
        daftarCustomer.append(Customer("D", 32, 31))
        daftarCustomer.append(Customer("F", 6, 5))
        daftarCustomer.append(Customer("G", 40, 41))
        daftarCustomer.append(Customer("H", 4, 2))
        daftarCustomer.append(Customer("J", 5, 5))
        daftarCustomer.append(Customer("L", 25, 22))
        daftarCustomer.append(Customer("M", 9, 9))
        daftarCustomer.append(Customer("O", 4, 4))
        daftarCustomer.append(Customer("P", 10, 10))
        daftarCustomer.append(Customer("R", 5, 5))
        daftarCustomer.append(Customer("S", 7, 7))
        daftarCustomer.append(Customer("T", 5, 4))
        daftarCustomer.append(Customer("V", 6, 6))
        daftarCustomer.append(Customer("W", 9, 9))
        daftarCustomer.append(Customer("Y", 35, 32))
        daftarCustomer.append(Customer("Z", 16, 17))
        daftarCustomer.append(Customer("AB", 7, 7))
        daftarCustomer.append(Customer("AE", 47, 44))
        daftarCustomer.append(Customer("AF", 15, 15))
        daftarCustomer.append(Customer("AG", 10, 8))
        daftarCustomer.append(Customer("AI", 12, 12))
        daftarCustomer.append(Customer("AJ", 5, 5))
        daftarCustomer.append(Customer("AL", 38, 38))
        daftarCustomer.append(Customer("AM", 33, 33))
        daftarCustomer.append(Customer("AN", 10, 10))
        daftarCustomer.append(Customer("AO", 21, 20))
        daftarCustomer.append(Customer("AP", 16, 16))
    elif (hari==4) :
        daftarCustomer.append(Customer("A", 5, 1))
        daftarCustomer.append(Customer("B", 4, 4))
        daftarCustomer.append(Customer("C", 44, 51))
        daftarCustomer.append(Customer("D", 5, 5))
        daftarCustomer.append(Customer("E", 18, 18))
        daftarCustomer.append(Customer("G", 5, 3))
        daftarCustomer.append(Customer("H", 10, 10))
        daftarCustomer.append(Customer("I", 18, 18))
        daftarCustomer.append(Customer("K", 16, 15))
        daftarCustomer.append(Customer("M", 3, 0))
        daftarCustomer.append(Customer("N", 6, 6))
        daftarCustomer.append(Customer("Q", 5, 5))
        daftarCustomer.append(Customer("R", 12, 12))
        daftarCustomer.append(Customer("S", 28, 26))
        daftarCustomer.append(Customer("T", 12, 11))
        daftarCustomer.append(Customer("U", 37, 38))
        daftarCustomer.append(Customer("V", 23, 21))
        daftarCustomer.append(Customer("X", 6, 6))
        daftarCustomer.append(Customer("Y", 5, 5))
        daftarCustomer.append(Customer("AA", 18, 18))
        daftarCustomer.append(Customer("AC", 23, 23))
        daftarCustomer.append(Customer("AD", 19, 19))
        daftarCustomer.append(Customer("AG", 28, 27))
        daftarCustomer.append(Customer("AH", 34, 34))
        daftarCustomer.append(Customer("AI", 12, 10))
        daftarCustomer.append(Customer("AJ", 5, 8))
        daftarCustomer.append(Customer("AK", 25, 30))
        daftarCustomer.append(Customer("AL", 5, 5))
        daftarCustomer.append(Customer("AM", 13, 11))
        daftarCustomer.append(Customer("AN", 21, 21))
        daftarCustomer.append(Customer("AQ", 10, 10))
    elif (hari==5) :
        daftarCustomer.append(Customer("B", 21, 21))
        daftarCustomer.append(Customer("C", 8, 8))
        daftarCustomer.append(Customer("D", 13, 12))
        daftarCustomer.append(Customer("F", 39, 42))
        daftarCustomer.append(Customer("G", 61, 56))
        daftarCustomer.append(Customer("J", 19, 22))
        daftarCustomer.append(Customer("K", 11, 11))
        daftarCustomer.append(Customer("L", 47, 40))
        daftarCustomer.append(Customer("M", 6, 6))
        daftarCustomer.append(Customer("P", 41, 40))
        daftarCustomer.append(Customer("Q", 5, 5))
        daftarCustomer.append(Customer("R", 8, 9))
        daftarCustomer.append(Customer("S", 6, 7))
        daftarCustomer.append(Customer("T", 10, 10))
        daftarCustomer.append(Customer("V", 8, 8))
        daftarCustomer.append(Customer("W", 12, 12))
        daftarCustomer.append(Customer("X", 8, 8))
        daftarCustomer.append(Customer("Z", 22, 22))
        daftarCustomer.append(Customer("AA", 10, 13))
        daftarCustomer.append(Customer("AB", 30, 31))
        daftarCustomer.append(Customer("AC", 11, 11))
        daftarCustomer.append(Customer("AF", 5, 4))
        daftarCustomer.append(Customer("AG", 3, 1))
        daftarCustomer.append(Customer("AH", 3, 3))
        daftarCustomer.append(Customer("AI", 5, 2))
        daftarCustomer.append(Customer("AJ", 5, 5))
        daftarCustomer.append(Customer("AK", 10, 8))
        daftarCustomer.append(Customer("AL", 17, 15))
        daftarCustomer.append(Customer("AM", 10, 10))
        daftarCustomer.append(Customer("AN", 7, 10))
        daftarCustomer.append(Customer("AP", 31, 31))
    elif (hari==6) :
        daftarCustomer.append(Customer("A", 10, 10))
        daftarCustomer.append(Customer("B", 9, 9))
        daftarCustomer.append(Customer("C", 12, 12))
        daftarCustomer.append(Customer("D", 13, 13))
        daftarCustomer.append(Customer("E", 16, 16))
        daftarCustomer.append(Customer("G", 6, 6))
        daftarCustomer.append(Customer("H", 10, 10))
        daftarCustomer.append(Customer("I", 14, 14))
        daftarCustomer.append(Customer("J", 5, 12))
        daftarCustomer.append(Customer("L", 8, 8))
        daftarCustomer.append(Customer("M", 16, 16))
        daftarCustomer.append(Customer("N", 20, 18))
        daftarCustomer.append(Customer("O", 9, 9))
        daftarCustomer.append(Customer("P", 12, 11))
        daftarCustomer.append(Customer("R", 4, 4))
        daftarCustomer.append(Customer("S", 12, 12))
        daftarCustomer.append(Customer("U", 15, 15))
        daftarCustomer.append(Customer("V", 37, 35))
        daftarCustomer.append(Customer("W", 35, 30))
        daftarCustomer.append(Customer("X", 10, 10))
        daftarCustomer.append(Customer("Y", 21, 21))
        daftarCustomer.append(Customer("Z", 10, 14))
        daftarCustomer.append(Customer("AA", 3, 0))
        daftarCustomer.append(Customer("AB", 4, 1))
        daftarCustomer.append(Customer("AE", 7, 11))
        daftarCustomer.append(Customer("AI", 11, 12))
        daftarCustomer.append(Customer("AJ", 5, 7))
        daftarCustomer.append(Customer("AK", 13, 15))
        daftarCustomer.append(Customer("AM", 29, 27))
        daftarCustomer.append(Customer("AN", 7, 5))
        daftarCustomer.append(Customer("AO", 4, 8))
        daftarCustomer.append(Customer("AP", 5, 5))
        daftarCustomer.append(Customer("AQ", 14, 12))
    elif (hari==7) :
        daftarCustomer.append(Customer("A", 19, 21))
        daftarCustomer.append(Customer("B", 2, 2))
        daftarCustomer.append(Customer("C", 5, 5))
        daftarCustomer.append(Customer("D", 10, 9))
        daftarCustomer.append(Customer("E", 3, 3))
        daftarCustomer.append(Customer("G", 61, 66))
        daftarCustomer.append(Customer("J", 2, 2))
        daftarCustomer.append(Customer("L", 3, 3))
        daftarCustomer.append(Customer("M", 2, 2))
        daftarCustomer.append(Customer("N", 4, 4))
        daftarCustomer.append(Customer("R", 8, 8))
        daftarCustomer.append(Customer("S", 5, 5))
        daftarCustomer.append(Customer("U", 2, 2))
        daftarCustomer.append(Customer("V", 8, 8))
        daftarCustomer.append(Customer("W", 11, 11))
        daftarCustomer.append(Customer("Y", 8, 8))
        daftarCustomer.append(Customer("Z", 19, 19))
        daftarCustomer.append(Customer("AA", 6, 6))
        daftarCustomer.append(Customer("AB", 10, 10))
        daftarCustomer.append(Customer("AC", 59, 59))
        daftarCustomer.append(Customer("AD", 3, 3))
        daftarCustomer.append(Customer("AF", 4, 4))
        daftarCustomer.append(Customer("AG", 5, 5))
        daftarCustomer.append(Customer("AH", 10, 10))
        daftarCustomer.append(Customer("AI", 3, 3))
        daftarCustomer.append(Customer("AJ", 3, 3))
        daftarCustomer.append(Customer("AK", 17, 18))
        daftarCustomer.append(Customer("AL", 18, 18))
        daftarCustomer.append(Customer("AM", 62, 61))
        daftarCustomer.append(Customer("AN", 39, 40))
        daftarCustomer.append(Customer("AO", 30, 30))
    return daftarCustomer
def findpath(path):
    global tpt
    global tempat

    pathF=[]
    fromT="DEPOT"
    totalJarak=0
    pt=copy.copy(path)
    
    for i in range(len(path)):
        
        mjarak=1000
        mindex=0
        for j in range(len(pt)):
            idx=fromT+"_"+pt[j]
            jarakC=tpt[idx]
            if (jarakC<mjarak) :
                mjarak=jarakC
                mindex=j

        fromT = pt[mindex]
        pathF.append(pt[mindex])
        pt.pop(mindex)
        totalJarak=totalJarak+mjarak

    idx = fromT + "_DEPOT"
    jarakC = tpt[idx]
    totalJarak=totalJarak+jarakC;

    return [pathF,totalJarak];
   
class Customer:
    def __init__(self, kode, demand, pickup):
        self.kode=kode
        self.demand=demand
        self.pickup=pickup

totalTruk =3
kapasitasTruk =200

kecepatanTruk =40

waktuDelivery=1.48

waktuPickup=0.71

batasWaktu=480
daftarCustomer=getcustomer(1)
dictCustomer={}

daftarCandidat=[]

totalBerat=0
for content in daftarCustomer:
    totalBerat=totalBerat+content.demand

class Candidate:
    def __init__(self, daftarTruk, listTruk ):
        self.daftarTruk =daftarTruk 
        self.listTruk =listTruk 
        self.fitness=0
        self.prob=0
        self.muatanLebih=0

    def getfitness(self,printB=False):
        global batasWaktu
        global dictCustomer
        global tpt
        global waktuDelivery
        global waktuPickup

        self.muatanLebih=0
        waktuA=0

        fitnessValue=0
        avg=0
        sisaWaktuA=[]
        for i in range(len(self.daftarTruk)):
            trk=self.daftarTruk [i]
            daftarCustomer=trk.muatan
            daftarPath = trk.pathHuruf
            fromT="DEPOT"
            waktuA=0
            sisaWaktu = batasWaktu
            totalMuatan = 0
            totalMuatan2 = 0
            if (printB) :
                print("Truk "+(str(i+1)))
                print("Berangkat dari Depot")
            for j in range(len(daftarPath)):
        
                toT=daftarPath[j]
                idx = fromT + "_" + toT
                jrk=tpt[idx]

                menit=(jrk/kecepatanTruk )*60
                waktuA=waktuA+menit
                customerA=dictCustomer[toT]
                totalMuatan=totalMuatan+customerA.demand
                totalMuatan2=totalMuatan2+customerA.pickup
                if (printB) :
                    print("Sampai di "+toT+" menit ke "+str(waktuA))

                fromT=toT
        
                waktuB=customerA.demand*waktuDelivery
                waktuA=waktuA+waktuB
                if (printB) :
                    print("Selesai menurunkan muatan di " + toT + " menit ke " + str(waktuA))
                waktuB=customerA.pickup*waktuPickup
                waktuA=waktuA+waktuB

                if (printB) : print("Selesai menaikkan muatan di " + toT + ",dan berangkat di menit ke " + str(waktuA))
            
        toT="DEPOT"
        idx = fromT + "_" + toT
 
        jrk = tpt[idx]
    
        menit = (jrk / kecepatanTruk ) * 60
        waktuA = waktuA + menit
        if (printB) : 
            print("Kembali di depot menit ke "+str(waktuA))
        sisaWaktu=batasWaktu-waktuA
        sisaWaktuA.append(waktuA)
        sisaMuatan=kapasitasTruk -totalMuatan
        sisaMuatan2=kapasitasTruk -totalMuatan2
        avg=avg+waktuA
        if (printB):
            print("Sisa waktu "+str(sisaWaktu))
            print("Sisa muatan antar "+str(sisaMuatan))
            print("Sisa muatan pickup " + str(sisaMuatan2))
            print("_________________________________________________")
            
        if (sisaWaktu<0) :
            sisaWaktu=sisaWaktu*10
        if (sisaMuatan<0 or sisaMuatan2<0) :
            self.muatanLebih=1
        if (sisaMuatan < 0):
            sisaMuatan = sisaMuatan * 30
            
        fitnessValue=fitnessValue+(sisaWaktu+sisaMuatan)
        
    
def generateCandidate(listTruk ):
    global totalTruk 
    global daftarCustomer
 
    daftarTruk =[]
    for i in range(totalTruk ):
        daftarTruk.append(Truk (i))
        
    for i in range(len(listTruk )):
        daftarTruk [listTruk [i]].addCustomer(daftarCustomer[i])

    for i in range(len(daftarTruk )):hsl=findpath(daftarTruk [i].pathHuruf)
    daftarTruk [i].jarak=hsl[1]
    daftarTruk [i].path=hsl[0]

    cd=Candidate(daftarTruk,listTruk )
    cd.getfitness()
    return cd


def generateCandidateRandom():
    global totalTruk 
    global daftarCustomer
 
    listTruk =[]
    for i in range(len(daftarCustomer)):
        listTruk.append(randint(0,totalTruk -1))
    
    return generateCandidate(listTruk )

def sortCandidat():
    global daftarCandidat
    for i in range(len(daftarCandidat)) :
        for j in range(i+1,len(daftarCandidat)):
            if (daftarCandidat[i].fitness<daftarCandidat[j].fitness) :
                ti=daftarCandidat[i]
                daftarCandidat[i]=daftarCandidat[j]
                daftarCandidat[j]=ti
 
class Truk :
    def __init__(self,counter):
        self.path=[]
        self.muatan=[]
        self.pathHuruf=[]
        self.counter=counter
        self.jarak=0
        
    def addCustomer(self,customer):
        self.muatan.append(customer)
        self.pathHuruf.append(customer.kode)
        
for i in range(len(daftarCustomer)):
    dictCustomer[daftarCustomer[i].kode]=daftarCustomer[i]
    
for i in range(len(tempat)) :
    for j in range(len(tempat)) :
        ix=tempat[i]
        jx=tempat[j]
        idx=ix+"_"+jx
        idx2=ix+"_"+jx
        
        tpt[idx]=distance[i][j]
        tpt[idx2]=distance[j][i]
        
totalKandidat=50
totalLoop=100

while (len(daftarCandidat)<totalKandidat) :
    tc=generateCandidateRandom()
    if (tc.muatanLebih==0):
        daftarCandidat.append(tc)
        
for i2 in range(totalLoop):
    fmin=1000000
    imin=0
    
    for i in range(len(daftarCandidat)) :
        if (daftarCandidat[i].fitness<fmin) :
            imin=i
            fmin=daftarCandidat[i].fitnesssortCandidat()
    
    arrInduk=[]
    for i in range(len(daftarCandidat)):
        prop=daftarCandidat[i].fitness+(fmin*-1)+10
        for j in range(int(prop)) :arrInduk.append(i)
    idxAyah=random.randint(0, len(arrInduk)-1)
    idxIbu=random.randint(0, len(arrInduk)-1)
    iAyah=arrInduk[idxAyah]
    iIbu=arrInduk[idxIbu]
    candidate1=daftarCandidat[iAyah]
    candidate2=daftarCandidat[iIbu]
 
    pt=[]
    size2=(int)(round(len(candidate1.listTruk )/2))
    for i in range(size2):
        pt.append(candidate1.listTruk [i])
        
    for j in range(size2,len(candidate1.listTruk )):
        pt.append(candidate2.listTruk [j])
    
    child=generateCandidate(pt)
    if (child.fitness>fmin) :
        if (child.muatanLebih == 0):
            daftarCandidat[imin]=child
    
    mutation=random.randint(0, 100)
    if (mutation<=5) :
        childBaru=generateCandidateRandom()
        if (childBaru.fitness>fmin and childBaru.muatanLebih==0):
            daftarCandidat[imin]=childBaru

daftarCandidat[0].getfitness(True)