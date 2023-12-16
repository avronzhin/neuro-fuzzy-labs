import math

import numpy as np


# q - количество атрибутов
# c - количество кластеров
# m - значение фазификации
def fcm(data, q, c, m, n_max, eps):
    v_list = []
    for j in range(c):
        v_list.append(data[j])
    current_big_j = big_j(data, q, c, m, v_list)
    n = 1
    while True:
        new_v_list = []
        for j in range(c):
            v_j = []
            for l in range(q):
                v_j.append(v_l_j(data, q, c, m, v_list, j, l))
            new_v_list.append(v_j)
        v_list = new_v_list
        new_big_j = big_j(data, q, c, m, v_list)
        print(new_big_j)
        print(v_list)
        n = n + 1
        if n > n_max or abs(current_big_j - new_big_j) <= eps:
            break
        current_big_j = new_big_j
    print(n)
    result = []
    for i in range(len(data)):
        u_i = []
        for j in range(c):
            z_i = data[i]
            u_i_j = u(z_i, c, v_list, j, m, q)
            u_i.append(u_i_j)
        result.append(u_i)
    return result


def normalize(raw_data, q):
    data = []
    min_list = []
    max_list = []
    for l in range(q):
        min_list.append(min(np.array(raw_data)[:, l]))
        max_list.append(max(np.array(raw_data)[:, l]))
    for i in range(len(raw_data)):
        raw_z = raw_data[i]
        z = []
        for l in range(q):
            z_l = (raw_z[l] - min_list[l]) / (max_list[l] - min_list[l])
            z.append(z_l)
        data.append(z)
    return data


def v_l_j(data, q, c, m, v_list, j, l):
    acc = 0
    for i in range(len(data)):
        z_i = data[i]
        u_j_i = u(z_i, c, v_list, j, m, q)
        acc = acc + u_j_i ** m * z_i[l]
    acc2 = 0
    for i in range(len(data)):
        z_i = data[i]
        u_j_i = u(z_i, c, v_list, j, m, q)
        acc2 = acc2 + u_j_i ** m
    return acc / acc2


def big_j(data, q, c, m, v_list):
    acc = 0
    for j in range(c):
        for i in range(len(data)):
            z_i = data[i]
            u_j_i = u(z_i, c, v_list, j, m, q)
            v_j = v_list[j]
            acc = acc + u_j_i ** m * d(z_i, v_j, q) ** 2
    return acc


def u(z, c, v_list, j, m, q):
    acc = 0
    v_j = v_list[j]
    d_j = d(z, v_j, q)
    for t in range(c):
        v_t = v_list[t]
        d_t = d(z, v_t, q)
        acc = acc + (d_j / d_t) ** (2 / (m - 1))
    return 1 / acc


def d(z, v, q):
    acc = 0
    for l in range(q):
        acc = acc + ((z[l] - v[l]) ** 2)
    if acc == 0:
        return 0.01
    return math.sqrt(acc)


def sil(data, i, q, cluster_relation, c):
    a_i = a(data, i, q, cluster_relation)
    b_i = b(data, i, q, cluster_relation, c)
    return (b_i - a_i) / max([a_i, b_i])


def a(data, i, q, cluster_relation):
    acc = 0
    z_i = data[i]
    r = cluster_relation[i]
    cluster_size = 0
    for j in range(len(data)):
        p = cluster_relation[j]
        if r == p:
            z_j = data[j]
            acc = acc + d(z_i, z_j, q)
            cluster_size = cluster_size + 1
    return acc / cluster_size


def b(data, i, q, cluster_relation, c):
    z_i = data[i]
    r = cluster_relation[i]
    clusters_dist = []
    for p in range(c):
        if p == r:
            continue
        acc = 0
        cluster_size = 0
        for j in range(len(data)):
            if cluster_relation[j] == p:
                z_j = data[j]
                acc = acc + d(z_i, z_j, q)
                cluster_size = cluster_size + 1
        if cluster_size != 0:
            clusters_dist.append(acc / cluster_size)
    return min(clusters_dist)
