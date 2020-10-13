from . import ActivationBaseClass
import numpy as np

from typing import Union


class SoftPlus(ActivationBaseClass):
    """ Soft+ function

    Class that holds the soft+ function and gradient as discussed in [1]_

    Parameters
    ----------
    beta : int or float, optional, default=1
           Positive non-zero value that controls the steepness of the Soft+ function.

    See also
    --------
    Identity, Sigmoid, Swish

    References
    ----------
    .. [1] Villmann, T., Ravichandran, J., Villmann, A., Nebel, D., & Kaden, M. (2019). "Activation
        Functions for Generalized Learning Vector Quantization - A Performance Comparison", 2019.
    """

    __slots__ = "beta"

    def __init__(self, beta: Union[int, float] = 1):
        if beta <= 0:
            raise ValueError(
                "The activation function {} expects beta > 0, but got beta = {}".format(
                    type(self).__name__, beta
                )
            )

        self.beta = beta

    def __call__(self, x: np.ndarray) -> np.ndarray:
        """ Implements the soft+ function:
            .. math::

                f(\\vec{x}) = \\ln(1 + e^{\\beta \\cdot \\vec{x}})

        Parameters
        ----------
        x : ndarray of any shape

        Returns
        -------
        ndarray of shape (x.shape)
            Elementwise evaluation of the soft+ function.
        """
        return np.log(1 + np.exp(self.beta * x))

    def gradient(self, x: np.ndarray) -> np.ndarray:
        """ Implements the sigmoid function's derivative:
            .. math::

                \\frac{\\partial f}{\\partial \\vec{x}} = \\frac{\\beta \\cdot e^{\\beta \\cdot \\vec{x}}}{1 + e^{\\beta \\cdot \\vec{x}}}

        Parameters
        ----------
        x : ndarray

        Returns
        -------
        ndarray of shape (x.shape)
            Elementwise evaluation of the soft+ function's gradient.
        """

        exp = np.exp(self.beta * x)
        return (self.beta * exp) / (1 + exp)
