from io import BytesIO

import numpy as np
import numpy.testing as nt

import harminv


class ReferenceData(object):
    # output generated from command line use of harminv
    # cat tests/input.dat | harminv -t 0.01 0.001-1
    cli_output = """frequency, decay constant, Q, amplitude, phase, error
    -0.506426, 3.072252e-03, 517.856, 0.507868, -0.200813, 2.128453e-04
    -0.301698, 6.482521e-04, 1462.11, 0.49748, -0.0520909, 7.269295e-05
    -0.104134, 9.490460e-04, 344.711, 0.481868, -0.129022, 1.780971e-04
    0.104119, 9.403484e-04, 347.851, 0.481781, 0.128571, 1.766600e-04
    0.301435, 6.051884e-04, 1564.78, 0.497346, 0.0438478, 6.678115e-05
    0.50092, 3.922559e-04, 4011.89, 0.499714, 0.0283455, 3.297469e-05
    1.10893, -2.500241e-01, -13.9339, 0.000228962, 1.03671, 6.522260e-04
    """

    refp = BytesIO(cli_output.encode())

    data = np.genfromtxt(refp, delimiter=',', names=True)

    def __getitem__(self, key):
        return self.data[key]


def create_signal():
    """Create the test signal.

    N.B the random component varies the results slightly. If you
    regenerate the test data then you will need to update
    ReferenceData.cli_output.
    """
    tau = 2 * np.pi
    dt = 0.01
    time = np.arange(1000) * dt
    noise = 0.1 * np.random.random(1000)
    signal = np.cos(tau * 0.1 * time) \
        + np.cos(tau * 0.3 * time) \
        + np.cos(tau * 0.5 * time)
    return noise + signal


def write_signal(signal):
    with open('tests/input.dat', 'w') as f:
        signal.tofile(f, sep=' ')


def read_signal():
    return np.fromfile('tests/input.dat', sep=' ')


def test_harminv():
    refdata = ReferenceData()
    signal = read_signal()
    harm = harminv.Harminv(signal=signal, fmin=0.001, fmax=1, nf=100, dt=0.01)

    nt.assert_allclose(harm.freq, refdata['frequency'], rtol=1e-5)
    nt.assert_allclose(harm.decay, refdata['decay_constant'], rtol=1e-4)
    nt.assert_allclose(harm.Q, refdata['Q'], rtol=1e-4)
    nt.assert_allclose(harm.amplitude, refdata['amplitude'], rtol=1e-4)
    nt.assert_allclose(harm.phase, refdata['phase'], rtol=1e-4)
    nt.assert_allclose(harm.error, refdata['error'], rtol=1e-4)

    for i in range(harm.freq.size):
        print("%g, %e, %g, %g, %g, %e" % (harm.freq[i],
                                          harm.decay[i],
                                          harm.Q[i],
                                          harm.amplitude[i],
                                          harm.phase[i],
                                          harm.error[i]))
