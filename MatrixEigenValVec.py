import numpy as np
import scipy
from numpy.linalg import svd
from scipy import linalg
import matplotlib.pyplot as plt


# Eigenvalue -> np.linalg.eig(Matrix)
# Trace -> np.trace(Matrix)
# print(np.linalg.eig(a)[0])
# print(np.linalg.eigvals(a))
# rint(np.trace(a))
# print(np.linalg.det(a))
def null(matrix, eps=1e-15):
    u, s, vh = scipy.linalg.svd(matrix)
    null_mask = (s <= eps)
    null_space = np.compress(null_mask, vh, axis=0)
    return np.transpose(null_space)


def nullspace(A, atol=1e-13, rtol=0):
    """Compute an approximate basis for the nullspace of A.

    The algorithm used by this function is based on the singular value
    decomposition of `A`.

    Parameters
    ----------
    A : ndarray
        A should be at most 2-D.  A 1-D array with length k will be treated
        as a 2-D with shape (1, k)
    atol : float
        The absolute tolerance for a zero singular value.  Singular values
        smaller than `atol` are considered to be zero.
    rtol : float
        The relative tolerance.  Singular values less than rtol*smax are
        considered to be zero, where smax is the largest singular value.

    If both `atol` and `rtol` are positive, the combined tolerance is the
    maximum of the two; that is::
        tol = max(atol, rtol * smax)
    Singular values smaller than `tol` are considered to be zero.

    Return value
    ------------
    ns : ndarray
        If `A` is an array with shape (m, k), then `ns` will be an array
        with shape (k, n), where n is the estimated dimension of the
        nullspace of `A`.  The columns of `ns` are a basis for the
        nullspace; each element in numpy.dot(A, ns) will be approximately
        zero.
    """

    A = np.atleast_2d(A)
    u, s, vh = svd(A)
    tol = max(atol, rtol * s[0])
    nnz = (s >= tol).sum()
    ns = vh[nnz:].conj().T
    return ns


def predprey(N, delta):
    # Making N by N predator prey model
    A = np.zeros((N, N))    # Needs zero rows for finding nullspace
    for r in range(N):
        for c in range(N):
            if c == r:
                A[r][c] = - delta
            if r != c:
                A[r][c] = np.random.normal(0, 1)
    eigenvalues, eigenvectors = np.linalg.eig(A)
    eva_list = []
    eve_list = []
    for i in eigenvalues:
        eva_list.append(i.real)
    for i in range(len(eigenvectors)):
        eve_list.append(eigenvectors[:, i])
    return A, eva_list, eve_list


def plotmatrix(matrix, N, delta):
    plt.close()
    [m, n] = np.shape(matrix)
    plt.imshow(matrix, alpha=.8, cmap='YlOrBr_r')
    plt.colorbar()
    # for tick numbers and labels
    plt.xticks(np.arange(n))
    plt.yticks(np.arange(m))
    plt.xlabel('Columns')
    plt.ylabel('Rows')
    plt.title(f'Predator Prey Matrix - Delta:{delta}')
    # plt.savefig(f'HW4-{N}{delta}.png')
    # plt.show()


for ddelta in range(21, 41):
    N = 11
    delta = ddelta/10
    ppmatrix, evalues, evectors = predprey(N, delta)
    # print(evalues)
    plotmatrix(ppmatrix, N, delta)
    pcount = 0
    ncount = 0
    for j in evalues:
        if j > 0:
            pcount += 1
        if j < 0:
            ncount += 1
    if pcount > 0 and ncount > 0:
        state = 'Saddle'
    if pcount > 0 and ncount == 0:
        state = 'Unstable'
    if pcount == 0 and ncount > 0:
        state = 'Stable'
    print(state, 'Delta:', delta)
